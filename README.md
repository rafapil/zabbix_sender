# zabbix_sender
Pequeno Script para usar o Zabbix Sender, muito fácil de usar :)

Primeiro temos que criar um host no Zabbix (Não é necessário configurações especiais)

O próximo passo é criar um item conforme as imagens abaixo:


Clique em create item


Para as configurações:

Name: Coloque o nome do item que vai monitorar, aqui estou usando Trapper Item

Type: Zabbix trapper

Key: Coloque um identificador de fácil compreensão sem espaços (essa informação será usada mais tarde no python, anote!), no meu caso usei: sendertrap.

Perfeito já temos tudo o que precisamos, agora vamos ao nosso grande pequeno script.

Aqui vou utilizar o VSCode mas pode usar a IDE que achar melhor 🙂

Primeiramente vamos instalar os módulos necessários com o comando: 
pip install py-zabbix

Agora importe o modulo da seguinte forma:
from pyzabbix import ZabbixMetric, ZabbixSender

Para enviar a métrica faça isso: 

packet = [ ZabbixMetric(‘NOME_DO_HOST_CRIADO’, ‘sendertrap’, valor),]

Aqui você pode observar que passei uma variável “valor”, isso porque não vou passar o dado fixo, claro se quiser fazer isso basta trocar a variável pelo valor de sua preferencia.

Por fim vamos encaminhar os dados para o Zabbix: 
result = ZabbixSender(zabbix_server=’192.168.120.96′, zabbix_port=10051, use_config=None, chunk_size=250, socket_wrapper=None, timeout=10).send(packet) 

Observe que não existe segredos aqui passamos o endereço do Server Zabbix ou Zabbix Proxy (no meu caso é um Zabbix Proxy, que é a melhor opção sempre).

O Script inteiro fica dessa forma: 


Link GitHub
Se prestar atenção vai observar que tem uma adição que entrega o valor 8 (1+8) para a variável “valor”, vou fazer algumas execuções com valores maiores e menores para ver o resultado.




