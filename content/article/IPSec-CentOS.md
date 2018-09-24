---
title: IPSec StrongSwan
date: 2018-09-18 20:45:15 -0200
comments: true
Category: Linux
Tags: IPSec, VPN
Status: published
Authors: Carlos Carvalho
---

Conforme mostrei nesse [post](https://blog.chcdc.com.br/posts/vpn-ipsec/) vamos agora configurar uma VPN IPSec.

Vamos utilizar o [StrongSwan](https://www.strongswan.org/) para configurarmos a VPN IPSec. 

Os peers serão configurados em dois ambientes distintos, Digital Ocean e AWS.

<!--more-->
A instalação será feita na distribuição CentOS 7.5.1804x64.

Para o ambiente amazon foi utilizado a instância Amazon Linux 2 AMI 

A VPN Site to Site precisa ser configurada dos dois lados, por isso, vamos configurar primeiro o servidor da esquerda (left) que será a Digital Ocean.

- Desabilitar SeLinux
```bash
[root@ipsec-server ~]# sed -i 's/^SELINUX=.*/SELINUX=disabled/g' /etc/sysconfig/selinux && cat /etc/sysconfig/selinux
```
- Atualizar o Sistema
```bash
[root@ipsec-server ~]# yum -y update
```
- Reiniciar para aplicar as alterações
```bash
[root@ipsec-server ~]# reboot
```

- Instale os pacotes necessários
```bash
[root@ipsec-server ~]#  yum install -y vim epel-release
```

- Para a instalação do lado amazon, vamos utilizar os repositórios Amazon
```bash
[root@peer-aws  ~]# amazon-linux-extras install epel -y
```

- Nesse caso, foi utilizado a última versão do pacote StrongSwan. Versão 5.6.3
```bash
[root@ipsec-server ~]# yum install strongswan -y
```

- Arquivo de configuração lado esquerdo (left)
```bash
[root@ipsec-server ~]# vim /etc/strongswan/ipsec.conf
```

```
config setup
	charondebug="all"
	uniqueids=yes
	strictcrlpolicy=no

conn %default
	ikelifetime=60m
	mobike=yes
	ike=aes128-sha1-modp1536,3des-sha1-modp3072!
	esp=aes128-sha1-modp1536,3des-sha1-modp3072!

# Nome a ser utilizado para a conexao 
conn left

	left=xxx.xx.xxx.xxx
	leftsubnet=10.46.0.0/16
	leftid=xxx.xx.xxx.xx
	leftfirewall=yes

	# Outra Ponta
	right=xx.xx.xxx.xxx	
	rightsubnet=172.31.13.0/20
	rightid=xx.xx.xx.xxx

	# Fechar a VPN automaticamente
	auto=start
	# Ativar o Tunel , necessario quando existe NAT
	type=tunnel
	# Compressao
	compress=yes
```

- Gerando a chave secret para usar em ambos os lados
Existem N formas de gerar uma chave/password, nesse caso vamos utilizar o seguinte comando:

```bash
[root@ipsec-server  ~]# date +%s | sha256sum | base64 | head -c 32 ; echo
```

O resultado apresentado foi:

**YmYyMzhiY2EwZWZjOGIzNzJiYjhkODRj**

- Vamos editar o arquivo secrets
```bash
[root@ipsec-server  ~]# vim /etc/strongswan/ipsec.secrets
```
```bash
# ipsec.secrets - strongSwan IPsec secrets file
#
# <IP lado direito> : <Criptografia Usada> “<Chave>”
xxx.xx.xx.xxx : PSK "YmYyMzhiY2EwZWZjOGIzNzJiYjhkODRj"
```


- Setando strongswan para iniciar com o sistema / Iniciar strongswan
```bash
[root@ipsec-server  ~]# systemctl enable strongswan
```


- Após a configuração do left vamos iniciar o strongswan e partir para configurar o right.
```bash
[root@ipsec-server  ~]# systemctl start strongswan
```

### Configurando lado direito (right)

Vamos partir do princípio que os passos 1 ao 4 já foram executados. Vamos configurar o nosso lado direito que no nosso caso é a AWS

- Arquivo de configuração do lado direito (right)

```bash
[root@aws-peer  ~]# vim /etc/strongswan/ipsec.conf
```

- No caso da Amazon, temos que configurar o endereço left com o IP da rede local, e o leftid com o IP externo

```bash
config setup
        charondebug="all"
        uniqueids=yes
        strictcrlpolicy=no

# Preferencias padroes para todas as conexoes
conn %default
        ikelifetime=60m
        mobike=yes
        ike=aes128-sha1-modp1536,3des-sha1-modp3072!
        esp=aes128-sha1-modp1536,3des-sha1-modp3072!

conn right
    left=xxx.xx.xx.xxx
    leftsubnet=172.31.13.0/20
    leftid=xxx.xxx.xx.xx
    leftfirewall=yes
    
    right=xx.xx.xxx.xxx
    rightsubnet=10.46.0.0/16
    rightid=xx.xx.xxx.xxx
    auto=start
    type=tunnel
```

- Vamos configurar o secret

```bash
[root@aws-peer  ~]# vim /etc/strongswan/ipsec.secrets
```

- Vamos inserir a mesma chave setada no left

```bash
# ipsec.secrets - strongSwan IPsec secrets file
#
# <IP lado direito> : <Criptografia Usada> “<Chave>”
xxx.xx.xxx.xxx : PSK "YmYyMzhiY2EwZWZjOGIzNzJiYjhkODRj"
```
- Setando para iniciar com o sistema / iniciando o serviço
```bash
[root@aws-peer  ~]# systemctl enable strongswan
[root@aws-peer  ~]# systemctl start strongswan
```

- Verificando conexões


 Lado Digital Ocean
```bash
[root@ipsec-server  ~]# strongswan status left

Security Associations (3 up, 0 connecting):
         left[6]: ESTABLISHED 2 minutes ago, xx.xx.xxx.xxx[xx.xx.xxx.xxx]...xx.xxx.xxx.xxx[xx.xx.xxx.xxx]
         left{5}:  INSTALLED, TUNNEL, reqid 4, ESP in UDP SPIs: ca942554_i ce718f43_o
         left{5}:   10.46.0.0/16 === 172.31.0.0/20
```

Lado AWS

```bash
[root@aws-peer  ~]# strongswan status right

Security Associations (1 up, 0 connecting):
right[1]: ESTABLISHED 3 minutes ago, xxx.xx.xx.xxx[xx.xxx.xxx.xxx]...xxx.xx.xx.xxx[xxx.xx.xx.xxx]
right{1}:  INSTALLED, TUNNEL, reqid 1, ESP in UDP SPIs: ce718f43_i ca942554_o
right{1}:   172.31.0.0/20 === 10.46.0.0/16
```




Simples Assim :)
