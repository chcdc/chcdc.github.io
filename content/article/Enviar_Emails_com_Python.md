---
title: Enviar emails com Python
date: 2018-02-09 02:10:18 -0200
comments: true
Category: Python
tags: emails, script
Status: published
Authors: Carlos Carvalho
---
Hoje me foi proposto um desafio, coletar logs de um servidor via Telegram e enviar por email.

Após algumas horas em pesquisa, cheguei ao seguinte script que vou ensinar mais abaixo, primeiramente vamos fazer
o script de envio de emails.

Antes de tudo, caso use GMail, você precisa permitir "aplicativos menos seguros" para executar seu script.

A versão do Python que iremos trabalhar é a **3.6**.

Vamos começar com um script simples,
existe uma biblioteca nativa em Python para enviar e-mails: smtplib. Não será necessário instalar bibliotecas externas!

Para enviar um email básico (sem linha de assunto), com um endereço do Gmail, o código é bastante simples:

```python3.6

0 import smtplib
1
2 s = smtplib.SMTP('smtp.gmail.com', 587)
3 s.starttls()
4 s.login("SEU EMAIL", "SUA SENHA")
5
6 msg = "MENSAGEM!"
7 s.sendmail("SEU EMAIL", "EMAIL DESTINO", msg)
8 s.quit()
```

Na linha 2, são os parâmetros para o servidor Gmail.
Primeiro, a localização do servidor (ou endereço IP), então a porta a ser usada.

Na linha 3, há uma função de segurança, necessária para se conectar ao servidor do Gmail.
Ele protegerá sua senha.

Não podemos esquecer o endereço de e-mail e senha na linha 4.

A variável ```msg``` conterá sua mensagem e a linha 7 irá enviá-la!

## Para um email mais elaborado

Aqui já estamos inserindo alguns dados, como assunto, rementente.

Para isso precisamos de mais modulos, já disponiveis na biblioteca basica do Python,
o **_email.mime.multipart_** e o **_email.mime.text_**

```python3.6
0
1  import smtplib
2  from email.mime.multipart import MIMEMultipart
3  from email.mime.text import MIMEText
4
5
6  fromaddr = "SEU ENDEREÇO"
7  toaddr = "ENDEREÇO DE DESTINO"
8  msg = MIMEMultipart()
9  msg['From'] = fromaddr
10 msg['To'] = toaddr
11 msg['Subject'] = "ASSUNTO"
12
13 body = "SUA MENSAGEM AQUI"
14 msg.attach(MIMEText(body, 'plain'))
15
16 server = smtplib.SMTP('smtp.gmail.com', 587)
17 server.starttls()
18 server.login(fromaddr, "SUA SENHA")
19 text = msg.as_string()
20 server.sendmail(fromaddr, toaddr, text)
21 server.quit()
```

Não esqueça de alterar as seguinte linhas:

- Linha 6 Com seu endereço de email
- Linha 7 O endereço de email de destino
- Linha 11 com o assunto
- Linha 13 com a mensagem a ser enviada
- Linha 18 com a senha do seu email


## Para enviar um email com anexo

Para enviarmos anexos, vamos a um código mais complicado. Percebi que todo mundo tem um método um pouco diferente pra fazer.
Fiz o codigo o mais simples possivel. Mas ainda vamos precisar de mais modulos.

Em resumo, o passo essencial é converter o arquivo em um Base64 antes de enviá-lo. Meu código funciona para arquivos de texto, arquivos pdf, imagens, arquivos de áudio e arquivos de vídeo!

```python3.6
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


fromaddr = "SEU EMAIL"
toaddr = "EMAIL DE DESTINO"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "ASSUNTO DO EMAIL"

body = "TEXTO A SER ENVIADO"

msg.attach(MIMEText(body, 'plain'))

filename = "NOME DO ARQUIVO OU EXTENSÃO"
attachment = open("CAMINHO DO ARQUIVO", "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "SUA SENHA")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
```

Esta feito o script de envio de emails.

Em breve publico o script de coleta de logs e do BOT para o telegram.


Simples Assim 😆



Fontes:

– https://docs.python.org/3/library/smtplib.html

– https://docs.python.org/3/library/email.mime.html

– https://docs.python.org/3/library/email-examples.html

– https://docs.python.org/3/library/email.html
