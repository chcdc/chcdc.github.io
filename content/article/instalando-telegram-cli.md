---
title: Instalando Telegram-Cli
date: 2016-04-22 20:43:33 -0300
comments: true
Category: Telegram
Status: published
Authors: Carlos Carvalho
---

Telegram-CLI é um cliente do Telegram baseado na linguagem lua, ele é executado a partir do terminal.

<!--more-->

Instale as dependencias

```
apt-get install libreadline-dev libconfig-dev libssl-dev
 lua5.2 liblua5.2-dev libevent-dev libjansson-dev libpython-dev
 make git-core
```


Navege até o diretorio de instalacao

```
cd /opt/
```

Faça o clone do repositorio
```
git clone --recursive https://github.com/vysheng/tg.git && cd tg
```

Compile
```
./configure
make
```
Pronto, o proximo passo é a configuração do Telegram

Acesse a pasta do executavel

```
cd /opt/tg/bin
```
Execute o Telegram-Cli com o seguinte comando:

```
/opt/tg/bin/telegram-cli -W -k tg-server.pub
```

Na primeira execução será solicitado o numero de telefone e o codigo que será enviado por sms

```
Telegram-cli version 1.2.0, Copyright (C) 2013-2015 Vitaly Valtman
Telegram-cli comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions; type `show_license' for details.
Telegram-cli uses libtgl version 1.2.0
I: config dir=[~/.telegram-cli]
[~/.telegram-cli] created
[~/.telegram-cli/downloads] created
phone number: +554499999999 <--colocar aqui seu número de telefone
code ('call' for phone call): 12345 <-- colocar aqui o código que
                            o próprio Telegram enviará por SMS
```

Pronto! Está configurado!

Para enviar mensagens basta executar:
```
/opt/tg/bin/telegram-cli -W -k tg-server.pub
```



###Configurar para envio de notificações via sistema
---
Após o telegram-cli estar instalado e configurado, crie o seguinte arquivo
```
sudo vim /etc/profile.d/TelNotdata.sh
```

Acrescente o conteudo

```
#!/bin/bash
export TelNotIP=$(hostname -I|sed 's/[ ]*$//')
export TelNotPort="8080"
export TempFileDir="/var/tmp/"
export TelegramHomePath="/opt/tg/"
export TelegramScriptPath=$TelegramHomePath"scripts/user/"
export TelegramGenericPath=$TelegramHomePath"scripts/generic/"
export TelegramScript=$TelegramGenericPath"telegram.sh"
export TelegramCli=$TelegramHomePath"bin/telegram-cli"
export TelegramLog=$TempFileDir"tg.log"
export ReceiveLua=$TelegramGenericPath"receive.lua"
export TelegramTo="PrimeiroNome_SegundoNome"
export EmailTo="seu@email.com"
```

Torne ele executavel
```
sudo chmod +x /etc/profile.d/TelNotdata.sh
```
De um start no Daemon do Telegram-CLI
```
/opt/tg/bin/telegram-cli -vvvvRC -k tg-server.pub -W -dL tg.log -P 1234 &
```

Verifique se esta rodando
```
ps -ef | grep telegram
```

A saida é algo parecido com isso
```
root 1736  978  0 01:53 pts/0  00:00:01 bin/telegram-cli -vvvvRC -k tg-server.pub -W -dL tg.log -P 1234
```

Para enviar mensagens é simples!
```
echo "msg Firstname_Surname Test123" | nc 127.0.0.1 1234
echo "send_text Firstname_Surname  switch_icons.txt" | nc 127.0.0.1 1234
echo "send_photo Firstname_Surname  logo.png" | nc 127.0.0.1 1234
```


Dessa forma, voce pode criar scripts para enviar mensagens automaticas, 
inclusive quando ocorrer algo no servidor
