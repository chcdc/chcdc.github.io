---
title: Copiando arquivos por extensão usando Python
date: 2017-01-25 11:45:45 -0200
comments: true
Category: Python
tags: regex
Status: published
Authors: Carlos Carvalho
---

Recentemente fiz download de milhares de arquivos em pdf (não foi pirataria ok?!)  e precisava organizar eles em uma pasta especifica.

Pesquisei diversas formas de fazer isso, poderia fazer facilmente em **Shell Script** mas como estou aprendendo **Python** aceitei o desafio.

Bom vamos ao código.

<!--more-->


```python
#!/usr/bin/env Python3.5
# -*- coding: utf-8 -*-
# Carlos Carvalho
# 21/01/2017
# Copiar/mover arquivos por extensão
# Copiar os arquivos em pdf do diretorio /mnt/DOCS/
# para o diretorio /mnt/DOCS/pdf

import os,shutil,re

#Regex para identificar os arquivos em pdf
filePattern = re.compile(r"""^(.*?)(.pdf)$""",re.VERBOSE)

# Percorre o diretorio com um loop
for amerFilename in os.listdir('/mnt/DOCS'):
    mo = filePattern.search(amerFilename)

    # Ignora os arquivos que não são pdf
    if mo == None:
        continue

    # Obtem as diferentes partes do nome do arquivo
    beforePart = mo.group(1)
    findPart = mo.group(2)


    # Obtem os paths absolutos do arquivo
    absWorkingDir = os.path.abspath('/mnt/DOCS')
    PathFileEnd = os.path.abspath('/mnt/DOCS/pdf')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    PathFileEnd = os.path.join(absWorkingDir,PathFileEnd)

    # Move os arquivos
    print('Moving %s to %s .. ' % (amerFilename, PathFileEnd))
shutil.move(amerFilename,PathFileEnd)


```
