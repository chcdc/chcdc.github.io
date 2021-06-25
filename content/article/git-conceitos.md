---
title: Git Conceitos básicos e História
date: 2021-06-22 22:27:45 -0200
comments: true
Category: DevOps
tags: git
Status: published
Authors: Carlos Carvalho
---

Nesse post vamos falar um pouco sobre a história e os conceitos básicos do GIT.


<!-- PELICAN_END_SUMMARY -->

### Historia


O núcleo (kernel) do Linux é um projeto de código aberto com um escopo bastante grande.

Em 2002, o projeto do núcleo do Linux começou usar uma DVCS proprietária chamada BitKeeper.

Em 2005, a relação entre a comunidade que desenvolveu o núcleo do Linux e a empresa que desenvolveu BitKeeper quebrou em pedaços, e a ferramenta passou a ser paga.

Isto alertou a comunidade que desenvolvia o Linux (e especialmente Linus Torvalds, o criador do Linux) a desenvolver a sua própria ferramenta baseada em lições aprendidas ao usar o BitKeeper.

Algumas metas do novo sistema era os seguintes:

- Velocidade

- Projeto simples

- Forte suporte para desenvolvimento não-linear (milhares de ramos paralelos)

- Completamente distribuído

- Capaz de lidar com projetos grandes como o núcleo o Linux com eficiência (velocidade e tamanho dos dados)

Desde seu nascimento em 2005, Git evoluiu e amadureceu para ser fácil de usar e ainda reter essas qualidades iniciais.

Ele é incrivelmente rápido, é muito eficiente com projetos grandes, e ele tem um incrível sistema de ramos para desenvolvimento não linear

### Como Funciona
O Git considera que os dados são como uma imagem do sistema de arquivos.

Toda vez que você fizer um commit, ou salvar o estado de seu projeto no Git, ele basicamente tira uma foto de todos os seus arquivos e armazena uma referência para esse conjunto de arquivos.

Para ser eficiente, se os arquivos não foram alterados, o Git não armazena o arquivo novamente, apenas um link para o arquivo idêntico anterior já armazenado.
O Git trata seus dados mais como um fluxo do estado dos arquivos.


![git-snapshot](/images/snapshots-git.png)

### Principais Características

- As operações são locais
- Tem integridade checksum
- Geralmente só adiciona dados

### Os três estados

O git tem tres estados principais que seus arquivos podem estar:

- **Committed**: Os dados estão armazenados de forma segura em seu banco de dados local.

- **Modified**: Significa que o arquivo foi alterado, mas ainda não fez o commit no seu banco de dados.

- **Staged**: Significa que você marcou a versão atual de um arquivo modificado para fazer parte do seu próximo commit


### Workflow

O fluxo de trabalho podemos descrever da seguinte forma:

- Você modifica arquivos no seu diretório de trabalho
- Seleciona os arquivos, adicionando imagens deles à sua area de trabalho
- Você faz o commit, que leva os arquivos como eles estão na sua área de preparação e os armazena permanentemente no seu diretório Git.


![Workflow GIT](/images/workflow-git.png)


### Repositórios Locais

Seus repositórios locais consistem em três "árvores" mantidas pelo git

- **Working Directory** : Contém os arquivos vigentes
- **Index** : Funciona como uma área temporária (stage)
- **HEAD** : Aponta para o ultimo commit feito

![Workflow GIT Directories](/images/workflow-git-dir.png)


A partir de um estado "não gerenciado", os arquivos entram em um ciclo de alterações de estado a cada modificação e posterior consolidação.

![Workflow GIT States](/images/states-git.png)


Esses são os conceitos iniciais do GIT, nos próximos posts vamos executar a instalação e fazer alguns commits e alterações.




Simples Assim 😆

[Fonte](http://git-scm.com/book/pt-br)

