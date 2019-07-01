# script criado por Rafael Filgueiras
# Leia o README -> Importante 
# Acesse http://filgs.com.br/usando-o-zabbix-sender/ para ver cada detalhe da configuracao e caso queira pode baixar o app Portal Filgs pra ajudar :)

from pyzabbix import ZabbixMetric, ZabbixSender

valor = 1 + 6  # valor para teste

# Enviar a metrica para o zabbix trapper
packet = [
  ZabbixMetric('HOST_MONITORADO', 'KEY_DO_ITEM', valor),
]

result = ZabbixSender(zabbix_server='IP_DO_SERVIDOR_ZABBIX_OU_ZABBIX_PROXY', zabbix_port=10051, use_config=None, chunk_size=250, socket_wrapper=None, timeout=10).send(packet)
