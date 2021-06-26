---
title: VPN IPSec
date: 2018-09-15 01:59:44 -0300
comments: true
Category: Linux
Tags: IPSec, VPN
Status: published
Authors: Carlos Carvalho
---

É um conjunto de protocolos que oferece uma segurança no nivel de camada IP. Sendo assim opera pela camada de rede (camada 3) do modelo OSI e modelo TCP/IP.

O IPsec pode ser usado para proteger dados de rede, por exemplo, configurando circuitos usando o encapsulamento IPsec, no qual todos os dados enviados entre dois pontos de extremidade são criptografados, como em uma conexão VPN ( Rede Virtual Privada ); para criptografar dados da camada de aplicativo ; e para fornecer segurança aos roteadores que enviam dados de roteamento pela Internet pública. O IPsec também pode ser usado para fornecer autenticação sem criptografia, por exemplo, para autenticar os dados originados de um remetente conhecido.

O tráfego da Internet pode ser protegido de host para host sem o uso de IPsec, por exemplo, por criptografia na camada de aplicativo (Camada 7 do modelo OSI ) com HTTP Seguro (HTTPS) ou na camada de transporte (Camada 4 do modelo OSI) com o protocolo TLS ( Transport Layer Security ). No entanto, quando o tráfego usa criptografia ou autenticação nessas camadas superiores, os agentes de ameaça ainda podem interceptar informações de protocolo que podem expor dados que devem ser criptografados. 

 
Pode usar criptografia para fornecer segurança. O IPsec pode ser usado para a configuração de redes privadas virtuais (VPNs) de maneira segura.

<!--more-->
### Protocolos IPSec

O IPsec é definido para uso com as duas versões atuais do Internet Protocol, IPv4 e IPv6, sendo obrigatorio em IPv6. Os cabeçalhos do protocolo IPsec são incluídos no cabeçalho IP, onde aparecem como extensões de cabeçalho IP quando um sistema está usando IPsec.


 Os protocolos mais importantes considerados como parte do IPsec incluem:

- O Cabeçalho de Autenticação de IP (AH), especificado no [RFC 4302](https://tools.ietf.org/html/rfc4302), define um cabeçalho de pacote opcional a ser usado para garantir a integridade sem conexão e a autenticação de origem de dados para pacotes IP e para proteger contra replays.

- O IP Encapsulating Security Payload (ESP), especificado no [RFC 4303](https://www.ietf.org/rfc/rfc4303.txt), define um cabeçalho de pacote opcional que pode ser usado para fornecer confidencialidade através de criptografia do pacote, bem como proteção de integridade, autenticação de origem de dados, controle de acesso e proteção opcional contra replays ou análise de tráfego.

- O IKE (Internet Key Exchange), definido no [RFC 7296](https://tools.ietf.org/html/rfc7296), "IKEv2 (Internet Key Exchange Protocol Version 2)", é um protocolo definido para permitir que os hosts especifiquem quais serviços devem ser incorporados nos pacotes, algoritmos criptográficos que serão usados ​​para fornecer esses serviços e um mecanismo para compartilhar as chaves usadas com esses algoritmos criptográficos. 

### Fases IPSec 


O IPSec envolve muitas tecnologias de componentes e métodos de criptografia. No entanto, a operação do IPSec pode ser dividida em cinco etapas principais:

- **"Interesting traffic"** Inicia o processo IPSec. O tráfego é considerado interessante quando a política de segurança IPSec configurada nos pares IPSec inicia o processo IKE.

- **Fase IKE 1.**  O IKE autentica os pares IPSec e negocia os IKEs SA durante essa fase, configurando um canal seguro para negociar as SAs IPSec na fase 2.

- **Fase IKE 2.** IKE negocia os parâmetros IPSec SA e configura as SAs IPSec correspondentes nos pares.

- **Transferência de dados.** Os dados são transferidos entre os pares IPSec com base nos parâmetros IPSec e nas chaves armazenadas no banco de dados SA.

- **Terminação de túnel IPSec.** IPSec SAs terminam por exclusão ou por tempo limite.

### Implementando o IPsec

O suporte a IPsec foi geralmente incluído na maioria dos sistemas operacionais comuns (e outros) disponíveis desde o final dos anos 90, incluindo sistemas operacionais de desktop e servidor, bem como roteadores e outros dispositivos de segurança de rede.

Embora os sistemas mais antigos possam suportar alguma versão do IPsec, as empresas devem implantar o IPsec usando sistemas operacionais atualizados e atualizados em patches de segurança. Além disso, sistemas mais antigos que suportam versões mais antigas do IPsec e parecem ativar circuitos IPsec seguros podem, na verdade, não manter os dados seguros. 


Nos proximos posts vamos configurar e implementar uma VPN IPSec.



---
##### Fontes:

- [RFC 4302](https://tools.ietf.org/html/rfc4302)
- [RFC 4303](https://www.ietf.org/rfc/rfc4303.txt)
- [RFC 7296](https://tools.ietf.org/html/rfc7296)
- [Cisco Press](http://www.ciscopress.com/articles/article.asp?p=25474&seqNum=7)
