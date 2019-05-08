---
title: Dicas IPTables
date: 2018-12-16 19:00:45 -0200
comments: true
Category: Linux
tags: Network, Sysadmin
Status: published
Authors: Carlos Carvalho
---


Existem 3 tabelas gerenciáveis no IPTables:

* FILTER - esta é a tabela padrão, responsável pela filtragens de pacotes. Possui três cadeias de conjuntos de regras:
    + INPUT - pacotes destinados a sockets locais
    + FORWARD - pacotes encaminhados (roteados) através do firewall
    + OUTPUT - pacotes gerados localmente
* NAT - é uma tabela que é consultada quando um pacote tenta criar uma nova conexão. Pode alterar características de origem ou de destino de um pacote. Possui três cadeias de conjuntos de regras:
    + PREROUTING - utilizado para alterar um pacote, logo que é recebido
    + POSTROUTING - usado para alterar pacotes quando eles estão prestes a sair
    + OUTPUT - usado para alterar pacotes gerados localmente
* MANGLE - esta tabela é usada para alteração de pacotes. Até o kernel versão 2.4 esta tabela tinha apenas 2 cadeias, mas eles são agora 5:
    + PREROUTING - para alterar as conexões de entrada
    + OUTPUT - para alterar pacotes gerados localmente
    + INPUT - para pacotes de entrada
    + POSTROUTING - para alterar pacotes quando eles estão prestes a sair
    + FORWARD - pacotes encaminhados (roteados) através do firewall


**1 - Exibir todas as regras disponíveis**

```iptables -L -n -v```

Se preferir, verificar apenas uma tabela em específico (no caso a tabela nat):

```iptables -t nat -L -n -v```

Ou através de linhas numeradas:

```iptables -n -L -v --line-numbers```

**2 - Bloquear endereço IP específico entrante na rede**

Para adicionar regra:

```iptables -A INPUT -s xxx.xxx.xxx.xxx -j DROP```

Para removê-la:

```iptables -D INPUT -s xxx.xxx.xxx.xxx -j DROP```

**3 - Bloquear porta específica**

Sainte:

```iptables -A OUTPUT -p tcp --dport xxx -j DROP```

Entrante:

```iptables -A INPUT -p tcp --dport xxx -j ACCEPT```

Ou múltiplas portas:

```iptables -A INPUT  -p tcp -m multiport --dports 22,80,443 -j ACCEPT```
```iptables -A OUTPUT -p tcp -m multiport --sports 22,80,443 -j ACCEPT```

**4 - Permitir rede específica acessar determinada porta:**

```iptables -A OUTPUT -p tcp -d 192.168.100.0/24 --dport  -j ACCEPT```

**5 - Bloquear Network Flood sobre o servidor web que esteja escutando na porta 80**

Aceitando de 100 a 200 conexões por minuto (ajuste da maneira que achar melhor):

```iptables -A INPUT -p tcp --dport  -m limit --limit 100/minute --limit-burst  -j ACCEPT```

**6 - Manter registros de Log’s de pacotes bloqueados:**

```iptables -A INPUT -i eth0 -j LOG --log-prefix "Quantidade pacotes bloqueados:"```

```iptables -A INPUT -p tcp -dport  -j LOG -log-prefix “Serviço: ftp”```

Os log’s são salvos em /var/log/messages. Onde você poderá filtrar usando comando grep:

```grep "Quantidade pacotes bloqueados:" /var/log/messages```

**7 -Limitar o número de conexões simultâneas oriundas de determinado IP:**

```iptables -A INPUT -p tcp --syn --dport  -m connlimit --connlimit-above  -j REJECT```

Onde, essa regra permitirá 3 conexões simultâneas advindas de um mesmo endereço IP na porta 22 (SSH).

**8 - Permitir conexões já estabelecidas:**

```iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT```

**9 - Bloquear Ping Requests:**

```iptables -A INPUT -p icmp -icmp-type echo-request -j DROP```

**10 - Bloquear por endereço MAC:**

```iptables -A INPUT -m mac --mac-source 00:00:00:00:00:00 -j DROP```


Simples assim! 😆


