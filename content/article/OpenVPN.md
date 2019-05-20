---
title: OpenVPN
date: 2019-05-18 14:29:17 -0200
comments: true
Category: Network, Linux
Tags: sysadmin,VPN
Status: published
Authors: Carlos Carvalho
---

OpenVPN é uma aplicação VPN de código aberto que permite criar e participar de uma rede privada de forma segura através da Internet pública.

Vamos instalar e configurar o OpenVPN em um servidor CentOS 7.

Levando em consideração que o servidor Linux baseado na distribuição CentOS 7 esteja devidamente instalado e com a rede configurada, vamos iniciar a instalação.


<!--more-->
### Configurando o sistema
Desabilite o SELinux


```console
# sed -i 's/^SELINUX=.*/SELINUX=disabled/g' /etc/sysconfig/selinux && cat /etc/sysconfig/selinux 

```

Desabilite o firewalld
```console
# systemctl stop firewalld
# systemctl disable firewalld
```

Após as alterações reinicie o sistema para aplicar a configuração

Ajuste o kernel para habilitar o modo de roteamento:

```console
# echo net.ipv4.ip_forward = 1 >> /etc/sysctl.conf
# sysctl -p
```

Atualize o sistema operacional

```console
# yum upgrade -y
```

### Instalando OpenVPN

O repositório Extra Packages for Enterprise Linux (EPEL) é um repositório adicional gerenciado pelo Projeto Fedora contendo pacotes não padrão, mas populares. O OpenVPN não está disponível nos repositórios padrão do CentOS, mas está disponível no EPEL, então instale o EPEL:

```console
# yum install epel-release -y && yum update -y
```

Próximo passo é instalar os pacotes necessários

```console
# yum install openvpn vim -y
```


Usando o curl, faça o download do Easy RSA. 
Recomendo o uso do easy-rsa-2, pois há mais documentação disponível para esta versão. 

```console
# curl -L https://github.com/OpenVPN/easy-rsa-old/archive/2.3.3.tar.gz -o /tmp/easyrsa.tar.gz
```

Extraia o pacote e crie o diretório em /etc/openvpn/

```console
# tar xfz /tmp/easyrsa.tar.gz
# sudo mkdir /etc/openvpn/easy-rsa 
# sudo mkdir /etc/openvpn/keys
```


Copie a estrutura do diretório easy-rsa para o diretório /etc/openvpn/easy-rsa para facilitar a administração:

```console
# sudo cp -rfv easy-rsa-old-2.3.3/easy-rsa/2.0/* /etc/openvpn/easy-rsa/
```

Altere o diretório para um usuário não root

```console
# chown "user" /etc/openvpn/easy-rsa/
```

Depois que esses programas forem instalados e tiverem sido movidos para os locais corretos em seu sistema, a próxima etapa é personalizar a configuração do lado do servidor do OpenVPN.


### Configurando OpenVPN



Temos muitas formas de configurar o OpenVPN, neste documento vamos fazer a forma mais comum de conexão.

Crie o arquivo de configuração

```console
# vim /etc/openvpn/server.conf
```



Vamos a Configuração

```console
# IP do servidor VPN
local xxx.xxx.xxx.xxx

# Porta Utilizada
port 1194

# Protocolo de Conexão e porta utilizada
proto udp 
dev tun0 

# Permite que o túnel continue aberto mesmo que o endereço IP da outra máquina mude
float

## Localização das Chaves e certificados
ca /etc/openvpn/keys/ca.crt 
cert /etc/openvpn/keys/server.crt
key /etc/openvpn/keys/server.key  # This file should be kept secret
dh /etc/openvpn/keys/dh2048.pem

# Configura o OpenVPN para funcionar como uma 
# sub-rede e informa à máquina cliente qual endereço utilizar
topology subnet

# Configuração do endereço do servidor
server 10.1.1.0 255.255.255.0 

#Configuração para manter os endereços estáticos dos clientes, 
# caso o OpenVPN reinicie, 
# poderá ser atribuído aos clientes de reconexão o mesmo endereço IP
ifconfig-pool-persist ipp.txt

# Informa a configuração de cada cliente
client-config-dir /etc/openvpn/ccd/

# Configuração para setar o DNS dos clientes, no exemplo abaixo estamos utilizando o opendns.com
push "dhcp-option DNS 208.67.222.222"
push "dhcp-option DNS 208.67.220.220"

# Envia um “ping” de um lado para o outro, 
# de modo que cada lado saiba quando o outro lado ficou inativo.
# Ping a cada 10 segundos, declara como inativo se nenhum ping for recebido 
# durante um tempo de 120 segundos
keepalive 10 120


# Chave de segurança Cipher. Deve conter no arquivo cliente e servidor.
cipher AES-256-CBC

# Compactação 
comp-lzo

# Quantidade maxima de clientes 
max-clients 10

# Opções Persistentes
persist-key
persist-tun

# Arquivo de status curto, exibindo as conexões atuais, truncadas e reescrito a cada minuto
status /var/log/openvpn-status.log

# Log OpenVPN
log-append  /var/log/openvpn.log
verb 3

# Notificar o cliente que quando o servidor for reiniciado pode reconectar-se automaticamente.
explicit-exit-notify 1
```

### Gerando Chaves e certificados Servidor

Começaremos nosso processo de geração de chaves e certificados criando um diretório no qual o Easy RSA armazenará todas as chaves e certificados gerados:


```console
# mkdir /etc/openvpn/easy-rsa/keys
```

Vamos editar as variáveis padrões que ficam no arquivo **vars** em **/etc/openvpn/easy-rsa/** :

Vá até o final do arquivo e altere os valores abaixo

KEY_NAME: O nome do servidor, o mesmo utilizado para a criação das chaves "server.key" e "server.crt"<br />
export KEY_COUNTRY="BR"<br />
export KEY_PROVINCE="PR"<br />
export KEY_CITY="Maringa"<br />
export KEY_ORG="Empresa"<br />
export KEY_EMAIL="vpn@company.com.br"<br />
export KEY_CN=openvpn<br />
export KEY_NAME="server"<br />
export KEY_OU="Infraestrutura"<br />

Salve e feche o arquivo

Para começar a gerar as chaves e os certificados, vá para o diretório easy-rsa e carregue as variáveis declaradas no arquivo vars na memória:

```console
# cd /etc/openvpn/easy-rsa
# source ./vars
```

Execute o script clean-all do Easy RSA para remover todas as chaves e certificados já existentes na pasta e gerar a autoridade de certificação:

**LEMBRE-SE: esse comando remove todas as chaves e certificados já criados. Não o execute em produção**

```console
# ./clean-all
```

Este script gera um arquivo chamado ca.key. Essa é a chave privada usada para assinar seu servidor e os certificados dos clientes. Se estiver perdido, você não poderá mais confiar em nenhum certificado dessa autoridade de certificação e, se alguém conseguir acessar esse arquivo, poderá assinar novos certificados e acessar sua VPN sem o seu conhecimento. 
Por esse motivo, o OpenVPN recomenda armazenar o ca.key em um local que possa estar offline o máximo possível e só deve ser ativado ao criar novos certificados.

Em seguida, construa a autoridade de certificação com o script build-ca. Você será solicitado a inserir valores para os campos de certificado, mas se você definir as variáveis no arquivo vars anteriormente, todas as suas opções já estarão definidas como padrões. Você pode pressionar ENTER para aceitar os padrões de cada um:


```console
# ./build-ca
```


Gere a chave de criptografia estática com o seguinte comando:
```console
# openvpn --genkey --secret /etc/openvpn/keys/vpn_server.tlsauth
```

Em seguida, crie uma chave e um certificado para o servidor usando o script build-key-server:
```console
# ./build-key-server server
```

Assim como na criação da autoridade de certificação, você verá os valores que definiu como padrão para poder pressionar ENTER nesses prompts. Além disso, você será solicitado a inserir uma senha de desafio e um nome de empresa opcional. Se você digitar uma senha de desafio, você será solicitado a se conectar à VPN do seu cliente. Se você não quiser definir uma senha de desafio, deixe esta linha em branco e pressione ENTER. No final, insira Y para confirmar as alterações.

A última parte da criação das chaves e dos certificados do servidor está gerando um arquivo de troca de chaves Diffie-Hellman. Use o script build-dh para fazer isso. Isso pode levar alguns minutos para ser concluído
```console
# ./build-dh
```

Quando o servidor terminar de gerar o arquivo de troca de chaves, copie as chaves do servidor e os certificados do diretório keys no diretório openvpn:

```console
# cd /etc/openvpn/easy-rsa/keys/
# sudo cp dh2048.pem ca.crt server.crt server.key /etc/openvpn/keys
``` 


### Gerando Chaves e certificados Cliente

Cada cliente também precisará de um certificado para que o servidor OpenVPN possa autenticá-lo. Essas chaves e certificados serão criados no servidor e você terá que copiá-los para seus clientes. É aconselhável gerar chaves e certificados separados para cada cliente que você pretende conectar à sua VPN.

Crie um certificado de cliente teste. Não crie um certificado para ser utilizado futuramente, pois o mesmo será utilizado para criar o arquivo de revogação de certificados e será invalidado logo em seguida. Preste atenção em alterar o endereço de email para cada certificado novo:

```console
# cd /etc/openvpn/easy-rsa/
# ./build-key cert-test
```

Revogue o certificado teste, criado anteriormente, para gerar o arquivo crl.pem, que será responsável por controlar os certificados revogados.

```console
# ./revoke-full cert-teste
```

Sempre que um certificado for revogado, o arquivo crl.pem deverá ser copiado para a raiz do servidor OpenVPN para que o mesmo possa ser lido:

```console
# cp /etc/openvpn/rsa/keys/crl.pem /etc/openvpn
```

Agora vamos criar o certificado, como vamos apenas criar esse, vamos nomeá-lo de client , mas você pode alterar isso para um nome mais descritivo se quiser:
```console
$ cd /etc/openvpn/easy-rsa/
$ ./build-key client
```

Copie o arquivo de configuração do OpenSSL com versão, openssl-1.0.0.cnf, para um nome sem versão, openssl.cnf. Não fazer isso pode resultar em um erro em que o OpenSSL não consegue carregar a configuração porque não pode detectar sua versão

```console
# cp /etc/openvpn/easy-rsa/openssl-1.0.0.cnf /etc/openvpn/easy-rsa/openssl.cnf
```


### Iniciando OpenVPN

Vamos configurar o OpenVPN para iniciar na inicialização. Para fazer isso, ative o servidor OpenVPN adicionando-o ao systemctl

```console
# sudo systemctl -f enable openvpn@server.service
```

Inicie o serviço
```console
# sudo systemctl start openvpn@server.service
```
Verifique se não houve erros durante a inicialização do serviço. Caso tenha erros, verifique o arquivo de log /var/log/openvpn.log



### Criando rotas estaticas

Vamos criar para cada cliente uma configuração de rede individual

```console
# mkdir /etc/openvpn/ccd
```

Dentro do diretório, crie um arquivo com o nome exatamente igual ao que foi gerado o certificado, no nosso caso é client
```console
# touch /etc/openvpn/ccd/client
```

Vamos inserir as informações necessárias.

[Optional]
Caso deseja que cada cliente tenha um endereço setado manualmente, insira no inicio do arquivo

```console
ifconfig-push 10.1.1.1 255.255.255.0 
```
[/optional]

Insira as rotas da rede local e a rede openvpn, caso deseja que ele acesse a mesma

```console
push "route 10.1.1.0 255.255.255.0"
push "route 10.42.12.0 255.255.254.0"
```

Insira as rotas desejadas, sempre comentando o destino 
```console
# Algum lugar do mundo
push "route 200.200.200.1 255.255.255.0"
```



### Configurando o Firewall

Para que o servidor faça os redirecionamentos necessários e aceite conexões precisamos setar isso no iptables

Execute os seguintes comandos

```console
# echo 1 > /proc/sys/net/ipv4/ip_forward
# iptables -P FORWARD ACCEPT
# iptables -A INPUT -i tun+ -j ACCEPT
# iptables -A FORWARD -i tun+ -j ACCEPT
# iptables -t nat -A POSTROUTING -o ens32 -j MASQUERADE
# iptables -A FORWARD -i tun0 -o tun0 -j ACCEPT
# iptables -A FORWARD -i tun0 -o ens32 -j ACCEPT
# iptables -A FORWARD -i ens32 -o tun0 -j ACCEPT
# iptables -A INPUT -p tcp --dport 1194 -j ACCEPT
# iptables -A INPUT -p udp --dport 1194 -j ACCEPT
# iptables -I INPUT -i tun+ -j ACCEPT
# iptables -I OUTPUT -o tun+ -j ACCEPT
# iptables -I FORWARD -i tun+ -j ACCEPT
# iptables -I FORWARD -o tun+ -j ACCEPT
```

### Configurando o Cliente

Os certificados e chave que serão inseridos no final do arquivo se encontram em /etc/openvpn/easy-rsa/keys/
Sendo eles
	* ca - ca.crt 
	* cert - client.crt
	* key - client.key

Crie o arquivo client.ovpn com as seguintes configurações

```console
client
pull
dev tun
proto udp
remote <ip external> 1194 udp
user nobody
group nogroup
comp-lzo
verb 3
resolv-retry infinite
persist-key
persist-tun
mute-replay-warnings
auth-nocache
float

# Ciphers
remote-cert-tls server
tls-version-min 1.2
tls-cipher TLS-DHE-RSA-WITH-AES-256-GCM-SHA384
cipher AES-256-CBC

# Client Keys
<ca>
-----BEGIN CERTIFICATE-----
-----END CERTIFICATE-----
</ca>
<cert>
-----BEGIN CERTIFICATE-----
-----END CERTIFICATE-----
</cert>
<key>
-----BEGIN RSA PRIVATE KEY-----
-----END RSA PRIVATE KEY-----
</key>
```


Copie o arquivo para sua máquina local, pode utilizar sftp ou scp. 

Após seguir esses passos, sua vpn deverá estar já criada e acessível. Realize os testes de acesso, sempre verificando os logs.



Simples Assim 😆
