---
title: "Criando um Bot do Telegram"
date: 2016-09-18 20:14:12 -0300
comments: true
Category: Python
tags: Telegram, bot
Authors: Carlos Carvalho
---



Sim, resolvi me aventurar no desenvolvimento de um bot utilizando a [API do Telegram](https://core.telegram.org/bots/api).

Irei contar a minha saga da criação desse bot nesse maravilhoso [Telegram](https://telegram.org).

Pra fazer um bot novo, é muito simples.

<!--more-->

Irei partir do principio que você já tenha o Telegram instalado em seu smartphone e/ou computador  e que saiba o basico dele.


<!--![BotFather](../images/Bot.png)-->


  - Adicione o @BotFather
   - Escreva: /newbot
   - Ele pedirá um nome para o seu bot. Escreva o nome finalizado com _bot
   - Se o nome estiver disponível,o bot será criado e você receberá um token de acesso.

   Para testar seu bot acesse o seguinte link<br>
   https://api.telegram.org/bot[token]/getUpdates</br>

   Deverá receber a seguinte resposta:<br>
   `{"ok":true,"result":[{}]"`


Simples assim.
