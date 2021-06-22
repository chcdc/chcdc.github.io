---
title: Ansible
date: 2021-06-21 22:27:45 -0200
comments: true
Category: DevOps
tags: ansible, automacao
Status: draft
Authors: Carlos Carvalho
---


[Ansible](ansible.com) é uma ferramenta Open Source em Python para automatizar ações em maquinas.

Ele pode configurar sistemas, implantar software e orquestrar tarefas de TI mais avançadas, como implementações contínuas ou atualizações de rotação de tempo de inatividade zero.

O principal objetivo é sua simplicidade e facilidade de uso.
<!--more-->

Sua instalação pode ser feita com a ferramenta ```pip``` utilizando o seguinte comando:

```console
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$ python get-pip.py --user
$ python -m pip install --user ansible
```

Vamos implementar um servidor OpenVPN com criação automatica de usuarios

Usaremos as boas praticas descritas na Documentação Oficial


Vamos ao projeto

#### Projeto OpenVPN

Vamos fazer apenas as configurações iniciais.

Após a instalação do *Ansible* os arquivos iniciais são:

```console
$ tree /etc/ansible
- hosts
- ansible.cfg
```
Inicialmente não vamos alterar o arquivo ***ansible.cfg***

#### Hosts
O arquivo hosts é onde estará todos os hosts a serem configurados pelo Ansible

```txt
# This is the default ansible 'hosts' file.

[vpn-server]
10.138.10.1
```

É basicamente isso que precisamos no arquivo hosts.

Primeiro, vamos criar o arquivo de configuração que atualiza o server e insere as regras iptables. 

Será o __prepare_system.yml__ , vamos criar inicialmente sem as variaveis, para podermos entender melhor o contexto.


Vamos criar o diretorio local para importação da configuração .ovpn
```yaml
---
- name: Create a directory
  become: False
  file:
    path: "/etc/ansible/vpn-config"
    state: directory
  delegate_to: localhost
```

Os proximos passos, são atualizar os pacotes já instalados e instalar o pacote openvpn
```yaml
- name: Update all packages to their latest version
  apt:
    name: "*"
    state: latest
    autoclean: yes
    update_cache: yes
    force_apt_get: yes
    install_recommends: yes

- name: Install Applications
  package:
    name: "openvpn"
    state: present
```

E por ultimo, vamos configurar o nosso firewall e o sistema para fazer os redirecionamentos necessarios.
```yaml
- name: Configuration IP forwarding
  sysctl:
    name: net.ipv4.ip_forward
    value: '1'
    state: present
    reload: yes

## Configure firewall
- name: Accept FORWARD
  iptables:
    table: filter
    chain: FORWARD
    policy: ACCEPT

- name: Accept INPUT and FORWARD from tun+
  iptables:
    action: append
    table: filter
    chain: "{{ item }}"
    in_interface: tun+
    jump: ACCEPT
  loop:
    - 'INPUT'
    - 'FORWARD'

- name: Masquerade POSTROUTING
  iptables:
    action: append
    table: nat
    chain: POSTROUTING
    out_interface: "{{ ansible_default_ipv4.interface }}"
    jump: MASQUERADE

- name: FORWARD tun+ to tun+ and {{ ansible_default_ipv4.interface }}
  iptables:
    action: append
    table: filter
    chain: FORWARD
    in_interface: tun+
    out_interface: "{{ item }}"
    jump: ACCEPT
  loop:
    - tun+
    - "{{ ansible_default_ipv4.interface }}"

- name: FORWARD {{ ansible_default_ipv4.interface }} to tun+
  iptables:
    action: append
    table: filter
    chain: FORWARD
    in_interface: "{{ ansible_default_ipv4.interface }}"
    out_interface: tun+
    jump: ACCEPT

- name: Accept INPUT from port 1190
  iptables:
    action: append
    protocol: "{{ item }}"
    table: filter
    chain: INPUT
    jump: ACCEPT
    destination_port: "1190"
  loop:
    - tcp
    - udp

- name: FORWARD and OUTPUT tun+
  iptables:
    action: append
    table: filter
    chain: "{{ item}}"
    out_interface: tun+
    jump: ACCEPT
  loop:
    - FORWARD
    - OUTPUT  
```

