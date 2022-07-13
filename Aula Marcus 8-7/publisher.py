from paho.mqtt import client as mqtt_client
from random import randint
from time import sleep
import sys, logging, signal
import json

# Inicializa Logging
logging.basicConfig(level=logging.WARNING)  # configuração global de logging
logger = logging.getLogger("main")  
logger.setLevel(logging.INFO) 

##Alguns brokers públicos: mqtt.eclipseprojects.io, broker.hivemq.com
#broker = 'localhost'
broker = 'broker.hivemq.com'
porta = 1883
##topico='/iot/cpu-utilization/'
topico='buzzer'
id_cliente = f'python-mqtt-{randint(0, 1000)}'
cliente = mqtt_client.Client(id_cliente)

def publish():
    global cliente, topico
    
    try:
        #while True:
            #criar o dicionario
            #Ex: obj={'nome':'xpto', 'sobrenome': 'jose das couve'}
            #Gerar un json:
            #json.dumps(obj)
            
            msg= {'nome':'Diego', 'tempo':25} ##msg é o dicionario
            json_string = json.dumps(msg)   ##json_string e uma variavel qualquer que recebe o dicionario
            result = cliente.publish(topico, json_string)   ##result e uma variavel qualquer que recebe o cliente.publish(topico, json_string)

            ###Essa parte fica de fora...
            #msg= psutil.cpu_percent(interval=3) #recebe a procentagem de utilização da CPU
            #resultado: [0, 1]

            status = result[0]
            if status == 0:
                print(f"Enviando `{msg}` ao tópico `{topico}` - Mensagens enviadas: {count_msg}")
                count_msg +=1
            else:
                print(f"Falha ao enviar mensagem ao tópico {topico}") 
    except KeyboardInterrupt:
        print('Você presionou Control + C. Desligando, aguarde..')
        cliente.disconnect() #  Desconecta de forma 'graciosa' do Broker      
        exit(0) 


def mqtt_init():
    """Conecta ao broker MQTT"""
    global cliente, broker, porta     
    try:
        cliente.connect(broker, porta)
        publish() 
    except:
        sys.exit(f"Erro ao conectar ao broker {broker}, porta {porta}")    


if __name__ == "__main__":
    mqtt_init()