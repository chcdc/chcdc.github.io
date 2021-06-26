---
title: Registro de acesso
date: 2016-01-05 01:59:44 -0300
comments: true
Category: Shell Script
Tags: sysadmin
Status: published
Authors: Carlos Carvalho
---

Tenho um notebook que fica grande parte do tempo no meu quarto, então quando não estou em casa, fica liberado para alguem usar.

Mas aí pensei, como saber em tempo real quem acessou minha maquina? A solução é simples!

<!--more-->
Criei um script pra cada vez que houver logon no sistema tira uma foto e envia ao meu Email!

O script é bem simples:

[gist:id=129b0f739b27db186eb7]

Os comandos se resumem no seguinte:

<b>`now=date +%Y%m%d-%H%M%S`</b> Variavel que recebe a data atual do sistema.
<br>`fswebcam` - Software que permite tirar fotos a partir do terminal
    <br> - `-F` Define o numero de Frames para captar
    <br> - `-r` Define a resolução da captura
    <br> - `--jpeg 100 ` Formato e qualidade da saida
    <br> - `-D 1 ` Tempo de delay para a captura
    <br> - `$now.jpeg` Arquivo que será salvo

<b>`sendemail` </b> - Software de envio de emails
    <br>  - `-f` [FROM] Email do remetente
    <br>  - `-t` [TO] Email de destino
    <br>  - `-u` [Subject] Assunto
    <br>  - `-m` [Message] Mensagem do email
    <br>  - `-s` [SMTP] Servidor de Saida SMTP
    <br>  - `-xu` [Username] Conta de email que sera utilizada para envio
    <br>  - `-xp` [ Password] Senha
    <br>  - `-a` [FILE] Anexo do Email

Simples assim :)
