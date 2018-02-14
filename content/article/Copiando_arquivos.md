---
title: Copiando arquivos com Python
date: 2018-02-14 10:55:25 -0200
comments: true
Category: Python
tags: script
Status: published
Authors: Carlos Carvalho
---

Nesse [post](chcdc.com.br/posts/enviar-emails-com-python) ensinei a criar um script basico para o envio de emails usando python.

Vamos agora aprender a coletar os logs (ou arquivos que voce desejar) para anexar ao script de envio de emails.

Lembrando que a versão do Python que iremos trabalhar é a **3.6**.

Antes de tudo vamos instalar o modulo [Paramiko](http://docs.paramiko.org/en/2.4/)

```sh
$ pip3.6 install paramiko
```

Vamos inserir os modulos
```python3.6

import shutil
import paramiko
```

Começamos importando os modulos necessarios para acessar e copiar os arquivos.
Os modulos que vamos utilizar são [Paramiko](http://docs.paramiko.org/en/2.4/) e o [shutil](https://docs.python.org/3.6/library/shutil.html).

Esse ultimo não será necessario a instalação pois é um dos modulos padrões do Python

Inicialmente vamos abrir a conexão com servidor, passando por parametros as informações do host

Podemos ver que usamos a porta padrão, porem não esqueça de alterar caso seja diferente.
```python3.6

import shutil
import paramiko

def copyFile(HostIp):
    # Abre a conexão
    s = paramiko.SSHClient()
    # Insere a chave do servidor remoto como confiavel
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Carrega as chaves já inseridas
    s.load_system_host_keys()
    # Efetua a conexão pela porta 22 com o usuario USER
    s.connect(HostIp, port = 22, username = "USER")
```

Agora vamos setar as variáveis, inserindo quais arquivos copiar

```python3.6
    # Nome do arquivo a ser copiado
    files = ['NAME OF FILE']
    # Caminho do arquivo, podemos setar diversos locais
    remote_images_path = '/path/remote/of/file/'
    # Caminho onde sera salvo o arquivo
    local_path = '/path/local/of/destiny/'
```

Vamos precisar de um ```for``` para copiar os arquivo(s)

```python3.6
    # Abre a conexâo ftp
    sftp = s.open_sftp()
    for file in files:
        # Aqui setamos o caminho e o arquivo a ser copiado
        file_remote = remote_images_path + file
        # Aqui setamos o caminho local
        file_local = local_path + file

        # Exibe o caminho remoto sendo copiado para o caminho local
        print(file_remote + ' >>>'  + file_local)
        # Efetua a copia
        sftp.get(file_remote, file_local)

        # Fecha as conexões
        sftp.close()
        s.close()
```


###### O script final ficará dessa forma

```python3.6

import shutil
import paramiko

def copyFile(HostIp):
    # Abre a conexão
    s = paramiko.SSHClient()
    # Insere a chave do servidor remoto como confiavel
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Carrega as chaves já inseridas
    s.load_system_host_keys()
    # Efetua a conexão pela porta 22 com o usuario USER
    s.connect(HostIp, port = 22, username = "USER")

    # Nome do arquivo a ser copiado
    files = ['NAME OF FILE']
    # Caminho do arquivo, podemos setar diversos locais
    remote_images_path = '/path/remote/of/file/'
    # Caminho onde sera salvo o arquivo
    local_path = '/path/local/of/destiny/'

    # Abre a conexão ftp
    sftp = s.open_sftp()
    for file in files:
        # Aqui setamos o caminho e o arquivo a ser copiado
        file_remote = remote_images_path + file
        # Aqui setamos o caminho local
        file_local = local_path + file

        # Exibe o caminho remoto sendo copiado para o caminho local
        print(file_remote + ' >>>'  + file_local)
        # Efetua a copia
        sftp.get(file_remote, file_local)

        # Fecha as conexões
        sftp.close()
        s.close()
```



Simples Assim 😆


Qualquer duvida ou algo pra complementar deixe seu comentario.

Fontes:

– http://docs.paramiko.org/en/2.4/

– https://docs.python.org/3.6/library/shutil.html
