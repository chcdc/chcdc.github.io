---
title: Gerando senhas seguras utilizando python
date: 2018-01-09 19:48:25 -0300
comments: true
Category: Python
Status: published
Authors: Carlos Carvalho
---


Nesse [post](http://chcdc.com.br/posts/gerando-senhas-seguras) ensinei a usar o pwgen para criar senhas, porém ele não tem me suprido pois necessito de senhas especificas.

Preciso enviar senhas de comprimento oito e apenas numeros e letras minusculas.

Resolvi criar então um script em Python para gerar essas senhas.

Vamos começar por partes

<!--more--> 

Primeiro vamos definir o executavel e importar os modulos **random** e **string** 
```python
#!/usr/local/bin/python3.6
import random
import string
```

Vamos criar uma função para gerar os numeros randomicos.

Atribuiremos a variavel **char** os caracteres minusculos e digitos numericos
```python
def randompassword(number):
    chars = random.sample(string.ascii_lowercase + string.digits, number)
    passw = ''.join(map(str, chars))
    return passw
```

Perguntaremos a quantidade de senhas necessarias e o comprimento, as respostas serão
armazenadas nas variaveis **amount** e **number** respectivamente.
```python
amount = int(input("Quantas senhas:\n"))
number = int(input("Qual o comprimento da senha?\n"))
```

Agora para cada quantidade declarada na variavel **amount** vamos imprimir uma
senha gerada randomicamente.
```python
for i in range(amount):
    print(f"Senha: {i} - {randompassword(number)} ")
```

O codigo final ficará dessa forma:
```python
#!/usr/local/bin/python3.6
import random
import string

def randompassword(number):
    chars = random.sample(string.ascii_lowercase + string.digits, number)
    passw = ''.join(map(str, chars))
    return passw

amount = int(input("Quantas senhas:\n"))
number = int(input("Qual o comprimento da senha?\n"))
for i in range(amount):
    print(f"   Senha: {i} - {randompassword(number)} ")
```

Algo simples, mas pode ser implementado em outros codigos, e claro pode ser melhorado.

Esse script encontra-se no meu [Github](https://github.com/chcdc/scripts/blob/master/Python/generate_pass.py)

Simples Assim 😃


