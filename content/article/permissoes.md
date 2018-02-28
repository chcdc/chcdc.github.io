---
title: Permissoes no Linux
date: 2018-02-27 09:23:45 -0200
comments: true
Category: Linux
tags: Sysadmin
Status: published
Authors: Carlos Carvalho
---

As permissões são usadas para definir quem pode acessar determinados arquivos ou diretórios, assim mantendo segurança e organização em seu sistema e sua rede. 

Quando, em um sistema (li)Unix digitamos o comando ```ls -l``` temos a seguinte visualização:

![ls -l](/images/ls_l.png)

Vemos o primeiro item em cada linha é a forma utilizada para mostrar as permissoes do arquivo.
O Linux trata todos os diretórios como arquivos também, portanto, as permissões se aplicam de igual forma para ambos.

O primeiro caractere aparece para indicar o tipo de arquivo:

d => diretório  
b => arquivo de bloco  
c => arquivo especial de caractere  
p => canal  
s => socket  
- => arquivo "normal"  

As permissões vão definidas assim:

* (r) Leitura
* (w) Escrita
* (x) Execução

Como as permissões são divididas em 3, irá aparecer assim: 

(rwx)(rwx)(rwx) 

Tipo de permissão Octal:  
4 - Indica permissão de leitura;  
2 - Permissão de escrita;  
1 - Indica permissão de execução;  
0 - Indica sem permissões.  


Então a liberações podem ser definidas somando as permissões em octal, fazendo da seguinte forma:  
 4 + 2 + 1 = 7 (permissão de rwx - Leitura, escrita e execução)  
 4 + 2 = 6     (permissão rw - Leitura e escrita)  
 4 =           (permissão r - Apenas Leitura)  


|     Usuário     |      Grupo      | Outros usuários (não donos) |
|:---------------:|:---------------:|:---------------------------:|
|        0        |        0        |              0              |
| Leitura=negada  | Leitura=negada  | Leitura=negada              |
| Escrita=negada  | Escrita=negada  | Escrita=negada              |
| Execução=negada | Execução=negada | Execução=negada             |


Simples Assim 😃
