---
title: Git Comandos Básicos
date: 2021-06-22 22:27:45 -0300
comments: true
Category: DevOps
tags: git
Status: published
Authors: Carlos Carvalho
---

Seguindo a sequencia, nesse post vamos iniciar o git com os comandos básicos.

Os conceitos eu abordei [aqui](/posts/git-conceitos-e-historia/#os-tres-estados)

Para esse Post, vamos utilizar um sistema baseado em Linux, porém os comandos são similares para sistemas Windows e MacOS.

<!--more-->
[TOC]


### Instalação

Em sua grande maioria de sistemas linux pode ser obtido da seguinte forma:

Debian like
```console
sudo apt install git
```

RedHat Like
```console
sudo yum install git
```

Para windows pode ser obtido [aqui](https://git-scm.com/download/win)

### Configuração Básica

Para utilizar o git em sua maquina, precisamos primeiro configurar o autor. Pelo motivo de que todos os *commits* devem ser identificados.

O arquivo `/etc/gitconfig` contém valores de configuração para todos usuários do sistema e todos os seus repositórios.
Se você passar a opção --system para git config, ele lerá e escreverá a partir deste arquivo especificamente.


O arquivo `~/.gitconfig` é específico para seu usuário.
Você pode fazer o Git ler e escrever a partir deste arquivo passando a opção --global.

Em sistemas Windows, Git procura pelo arquivo `.gitconfig` no diretório `$HOME`.
Isto significa um dos diretórios a seguir: `C:\Documents` e `Settings\$USER`, para a maioria dos usuários.


#### Configurando nome e email

Podemos definir seu nome e email para serem adicionados como autor nos *commits*.

A configuração global no sistema é feita utilizando o seguinte comando:
```console
$ git config --global user.name "Carlos Carvalho"
$ git config --global user.email carlos@chcdc.com.br
```

Não se esqueça de alterar as informações, não quero ser dono dos seus *commits*

#### Configurando preferencias
Vamos definir o editor *vim* como padrão

```console
$ git config --global core.editor vim
```

Configurar o Prompt colorido:

```console
$ git config --global color.ui true
```

Essas configurações já são suficientes para continuarmos, caso queira ver todas as configurações, basta rodar o comando:

```console
$ git config --list
```

Para listar uma configuração específica, por exemplo o user.name:

```console	
$ git config user.name
```

### Criando um projeto git

Para iniciar um repositório basta executar `git init`

Lembrando que é necessário estar no diretório do projeto em que se deseja utilizar o GIT

```console
$ cd projeto
$ git init
Initialized empty Git repository in projeto/.git/
```



Vamos criar o arquivo `README.md`, ele é um arquivo de apresentação. Ele inicialmente será a nossa base

Use o editor de texto de sua preferência, aqui usarei vim

```console
$ vim README.md
$ cat README.md
Iniciando um repositorio
```

Vamos dar um `git status`:

```console
$ git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md

nothing added to commit but untracked files present (use "git add" to track)
```

Como podemos ver arquivo esta `Untracked`, para adicionar ele vamos executar o `git add`

```console
$ git add README.md
```

Se rodarmos o `git status` novamente, veremos que agora o arquivo README.md esta pronto para *commit*
```console
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md
```

Agora vamos executar o commit, para isso vamos usar o comando `git commit -m ` . O parâmetro `m` indica qual a mensagem que deseja passar no *commit*
```console
$ git commit -m "Adicionando meu README.md"
[master (root-commit) ef567d0] Adicionando meu README.md
 1 file changed, 2 insertions(+)
 create mode 100644 README.md
```

Pronto, fizemos o nosso primeiro *commit*!!

Podemos ver nossas alterações utilizando o `git log`.
Onde temos o hash do commit, o author do commit e a data em que o commit foi realizado. (Talvez meu commit seja do futuro!)

```console
$ git log
commit ef567d0a3cef19e36ee75fd9251ebfb929a10b46 (HEAD -> master)
Author: Carlos Carvalho <carlos@chcdc.com.br>
Date:   Tue Jan 18 21:22:23 2061 -0300

    Adicionando meu README.md
```


O proximo comando é o `git diff`.
Então vamos fazer uma alteração no `README.md`. 
Faça a edição no seu editor favorito.

Ao executar o `git diff` temos a seguinte saida:
```console
$ git diff
diff --git a/README.md b/README.md
index abb520e..f603704 100644
--- a/README.md
+++ b/README.md
@@ -1,2 +1,2 @@
-Iniciando um repositório
+### Novo Projeto de colonização lunar
```
Nesse exemplo, removemos o texto **Iniciando um repositório** e inserimos o texto **Novo Projeto de colonização lunar**

Como podemos ver, ele mostrou, utilizando o simbolo *+*, o que adicionamos e utilizando o simbolo *-*, o que removemos.

O `git diff` nos permite ver qualquer alteração antes de fazer o *commit*, ele se torna um dos comandos mais importantes no workflow, sempre utilize ele pois assim pode revisar o que esta enviando.

**Lembrando que o `git diff` deve ser executado antes de adicionarmos o arquivo em staging**

Vamos adicionar o arquivo e fazer o commit dessas mudanças
```console
$ git add README.md
$ git commit -m "Novo projeto lunar"
[master 014982d] Novo projeto lunar
 1 file changed, 1 insertion(+), 1 deletion(-)
```

Como resultado ele nos mostrou que houve:

- 1 arquivo alterado (README.md)
- 1 inserção (### Novo Projeto de colonização lunar)
- 1 remoção (Iniciando um repositório)


Então nesse post vimos como criar um repositório local , inserir arquivos, ver alterações, adicionar e fazer o commit dos arquivos.

Com esses comandos já podemos trabalhar com o básico do git.

Simples Assim 😆

[Fonte](http://git-scm.com/book/pt-br)

