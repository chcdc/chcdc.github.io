---
title: Migrando repositorios do SVN para o GIT
date: 2019-12-14 19:12:45 -0300
comments: true
Category: Sysadmin
tags: svn, git
Status: published
Authors: Carlos Carvalho
---

Nesse post vou mostrar como migrar projetos do svn para o git.

Vou partir do principio que já entende como o [Subversion](https://subversion.apache.org/) e o [Git](https://git-scm.com/) se comportam.

Para tudo ocorrer como esperado, o nosso ambiente precisa estar seguinte forma:

* Cliente svn instalado
* Cliente git mais recente instalado
* Pacote git-svn
* PATH configurado que inclua o cliente git,svn e git-svn
<!--more-->

Primeiramente vamos obter os autores do repositorio svn
```bash
$ cd ~/
$ svn log --no-auth-cache -q http://svn.yourcompany/svn/repos/sample-repo/ \ 
| awk -F '|' '/^r/ {sub("^ ", "", $2);
        sub(" $", "", $2); print $2" = "$2" <"$2">"}' \
| sort -u >authors-transform.txt
```


Agora vamos 'clonar' localmente o nosso repositorio, esse processo pode demorar horas dependendo do tamanho do repositorio. Aqui o --stdlayout indica que o repositório segue o modelo tradicional, com pastas trunk, tags e branches.
```bash
$ cd ~/
$ git svn --username <usuario> --password <password> \
  clone http://svn.yourcompany/svn/repos/sample-repo/ \
  --no-metadata -A authors-transform.txt --stdlayout
```

Após finalizar, vamos criar um repositorio git do tipo bare e vamos indicar que o branch atual é o trunk
```bash
$ mkdir -p ~/sample-repo.git
$ cd ~/sample-repo.git
$ git init --bare
$ git symbolic-ref HEAD refs/heads/trunk
```

Agora temos um clone completo do repositório svn no diretório sample-repo, e um repositório git bare em sample-repo.git Vamos fazer um push do repositório svn clonado para o repositório git local. Configuramos tambem para que o push seja dos branches refs/remotes e dos refs/heads.
```bash
$ cd ~/sample-repo
$ git remote add bare ~/sample-repo.git
$ git config remote.bare.push 'refs/remotes/*:refs/heads/*'
$ git push bare
```

No final do passo anterior, o repositório svn será copiado para o git, mas precisaremos acertar algumas convenções git. Vamos renomear Trunk para *Master
```bash
$ cd ~/sample-repo.git
$ git branch -m trunk master
```

Precisaremos fazer uma limpeza de branches no git.
```bash
$ cd ~/sample-repo.git
$ git for-each-ref --format='%(refname)' refs/heads/origin/tags |
  cut -d / -f 5 |
  while read ref
    do
      echo $ref
      echo ""
      git tag "$ref" "origin/tags/$ref";
      git branch -D "origin/tags/$ref";
    done
```

E pra finalizar, vamos fazer o push para o servidor git da empresa
```bash
$ cd ~/sample-repo.git
$ git remote add origin https://username:password@gitserver/repo-sample
$ git push -u origin --all
$ git push -u origin --tags
```

Para facilitar o processo, criei um script para executar com maior facilidade.

Ele se encontra abaixo e no meu [Github](https://github.com/chcdc/svntogit/blob/master/run-import.sh)

Bons commits!! :)

```bash
#!/bin/bash 

if [[ -z "$1" || -z "$2" ]] ;then
    echo "Argument Null. Exiting"
    exit 1
else
    if [[ $1 != http?(s)://svn/* || $2 != git@git* ]]; then
        echo -e "Invalid URL. Exiting"
        echo -e "How to insert parameters:\n${0##*/} SVN GIT"
        exit 1
    else
        SVN=$1
        REPO_GIT=$2
    fi
fi

alias svn="svn --non-interactive --trust-server-cert"
PROJECT=${SVN##*/}

function create_dirs(){
    echo ""
    echo "Creating Directories $PROJECT"
    echo "---------------------------------------------"
    if [ -d ~/$PROJECT.git ]; then
        echo -e "Removing old directories | $PROJECT.git"
        rm -rf ~/$PROJECT.git
    fi
    if [ -d ~/repo-$PROJECT ]; then
        echo -e "Removing old directories  | repo-$PROJECT"
        rm -rf ~/repo-$PROJECT
    fi
    mkdir -p ~/repo-$PROJECT
    mkdir -p ~/$PROJECT.git
    if [ $? -eq 0 ]; then
        echo "Directories created"
        clone_repo_svn
    fi
}

function clone_repo_svn(){
    cd ~/repo-$PROJECT
    echo ""
    echo "Cloning repositories SVN - $SVN"
    echo "---------------------------------------------"
    svn log --no-auth-cache -q $SVN \ 
        | awk -F '|' '/^r/ {sub("^ ", "", $2); \
                sub(" $", "", $2); print $2" = "$2" <"$2">"}' \
        | sort -u >authors-transform.txt
    echo ""
    time git svn clone $SVN --no-metadata -A authors-transform.txt --stdlayout 
    if [ $? -eq 1 ]; then
        echo -e "Error cloning repositories\n"
        exit 1
    else
        git_config
    fi
}


function git_config(){
    echo ""
    echo "Convert to GIT - $PROJECT"
    echo "---------------------------------------------"
    cd ~/$PROJECT.git
    git init --bare
    git symbolic-ref HEAD refs/heads/trunk
    cd ~/repo-$PROJECT/$PROJECT
    git remote add bare ~/$PROJECT.git/
    git config remote.bare.push 'refs/remotes/*:refs/heads/*'
    git push bare
    cd ~/$PROJECT.git/
    git branch -m origin/trunk master
    git for-each-ref --format='%(refname)' refs/heads/origin/tags | 
    cut -d / -f 5 |
    while read ref
    do
      echo $ref
      echo ""
      git tag "$ref" "origin/tags/$ref";
      git branch -D "origin/tags/$ref";
    done
    git_pull
}

function git_pull(){
    echo ""
    echo "Push GIT - $REPO_GIT"
    echo "---------------------------------------------"
    cd ~/$PROJECT.git
    git remote add origin $REPO_GIT
    git push -u origin --all
    git push -u origin --tags
}

function main(){
    create_dirs
}

main
```
