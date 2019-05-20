---
title: Ansible
date: 2018-02-06 01:30:45 -0200
comments: true
Category: DevOps
tags: ansible, automacao
Status: draft
Authors: Carlos Carvalho
---

[Ansible](ansible.com) é uma ferramenta Open Source em Python para automatizar ações em maquinas.

Ele pode configurar sistemas, implantar software e orquestrar tarefas de TI mais avançadas, como implementações contínuas ou atualizações de rotação de tempo de inatividade zero.

O principal objetivo é sua simplicidade e facilidade de uso.

Não vamos entrar em detalhes sobre sua instalação, que pode ser efetuada apenas com **apt-get install** ou **yum install**

Vamos simular uma estrutura onde com Squid, Sarg e Iptables
Usaremos as boas praticas descritas na Documentação Oficial

Vamos ao projeto

---
#### Projeto Hero

Vamos fazer apenas as configurações iniciais.

Após a instalação do *Ansible* os arquivos iniciais são:

```python
- hosts
- ansible.cfg
```
Inicialmente não vamos alterar o arquivo ***ansible.cfg***

##### Hosts
O arquivo hosts é onde estará todos os hosts a serem configurados pelo Ansible

```python
# This is the default ansible 'hosts' file.

[frw-hero-01]
10.138.10.1

[frw-hero-02]
10.158.10.1
```

É basicamente isso que precisamos no arquivo hosts.

Vamos trabalhar com a seguinte estrutura
```python
/etc/ansible/
  projeto_Hero.yml        # Nosso playbook principal
  host_vars/              # Diretorio onde sera as variaveis de cada Host
    frw-hero-01
    frw-hero-02

  roles/                  # Diretorio das regras e tarefas
    common/               # Aqui sera um diretorio comum de regras
      tasks/              # Diretorio de tarefas
        main.yml          #  Playbook onde serão chamadas todas as tarefas
        templates/        #  <-- arquivos para uso com o recurso de modelo
          squid.conf.j2   #  <------- Arquivo no modelo .j2 (Jinja)
        files/            #
          bloqueios.txt   #  <-- arquivos para uso com o recurso de cópia
        vars/             #
          main.yml        #  <-- variaveis associadas para essas regras
```

Pode parecer complicado, mas se torna organizado quando se tem um parque consideravelmente grande.


