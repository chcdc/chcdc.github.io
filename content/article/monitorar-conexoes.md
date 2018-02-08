---
title: Monitorar conexoes
date: 2016-07-20 04:06:37 -0300
comments: true
Category: Network
Authors: Carlos Carvalho
Status: published
Summary: O tcpdump é um famoso sniffer para sistemas Linux. Muito util para analise  e solução de problemas da rede.
---

O tcpdump é um famoso sniffer para sistemas Linux. Muito util para analise  e solução de problemas da rede.

Sua documentação pode ser encontrada no site oficial.

[TCPDUMP][1]

A maioria das distribuições linux possuem binarios, caso não possua, sua instalação é bem simples.

```sh
	sudo apt-get install tcpdump
```

<!--more-->
Inicialmente não é necessario um parametro para sua execução, você apenas precisa executar como root, pois o tcpdump irá colocar sua placa de rede em modo promiscuo.

```sh
	tcpdump
```

Porém podemos utilizar diversos filtros por meio de parametros


Por padrão ele faz a captura da placa de rede ativa.Para selecionar a placa, devemos utilizar o parametro -i seguido da placa a ser monitorada

```sh
	tcpdump -i eth0
```

Podemos monitorar conexoes de origem utilizando o parametro _-src host_. Tudo que vier do nosso gateway (192.168.1.1) para o nosso computador ( 192.168.1.10 ), será monitorado com o seguinte comando

```sh
	tcpdump -i eth0 src 192.168.1.1
```

Se quisermos monitorar da forma inversa.Tudo que sair de nosso computador (192.168.1.10) para o nosso gateway, o comando será o seguinte

```sh
	tcpdump -i eth0 dst 192.168.1.1
```

Também é possivel especificar a porta de origem e destino com o comando _src port_ e _dst port_ . Um exemplo é monitorar a porta 443

```sh
	tcpdump -i eth0 dst port 443
```

Para que o tcpdump não converta os endereços e portas, devemos utilizar o parametro _-n_

```sh
	tcpdump -i eth0 -n host www.google.com.br
```


Podemos tambem utilizar operadores booleanos para um filtro mais refinado.

Por exemplo, capturar todos os pacotes da porta 80 e 443 da rede 192.168.1.0/16

```sh
	tcpdump -i eth0 -n net 192.168 and port 80 and port 443
```

Muitas opções podem ser obtidas com o tcpdump, essas são algumas opções basicas pra iniciar com sniffers.

[1]: http://www.tcpdump.org
