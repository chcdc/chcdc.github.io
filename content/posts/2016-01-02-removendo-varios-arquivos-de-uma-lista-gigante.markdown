---
title: "Removendo vários arquivos de uma lista gigante"
date: 2016-01-02 23:39:17 -0200
comments: true
Category: Linux
Tags: sysadmin
Authors: Carlos Carvalho
---
Por experiência própria, vez por outra preciso apagar vários arquivos gigantescos (geralmente logs) de uma única vez e a seguinte mensagem é gerada:

/bin/rm Argument list too long (Lista de argumento muito longa)

E daí, o que fazer?

<!--more-->
Basta entrar no diretório onde encontram-se os arquivos e executar algumas das alternativas de comando.

Para apagar todos os arquivos que contenham "2015" em seu nome:
```sh
    $ for a in *2015*; do rm $a; done
```


Para apagar todos os arquivos que possuam a extensão .log:
```sh
    $ for a in *.log; do rm $a; done
```

Bem simples! :)
