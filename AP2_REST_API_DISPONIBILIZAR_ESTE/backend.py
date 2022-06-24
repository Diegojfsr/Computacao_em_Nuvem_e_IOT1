from flask import Flask, jsonify, make_response, render_template  
from os import environ
from flask_cors import CORS
from flask_socketio import SocketIO
import RPi.GPIO as GPIO, time, json
app = Flask(__name__)
app.config['DEBUG'] = True
socketio = SocketIO(app)
CORS(app)

## Para procurar um valor no dicionário, basta 
## usar PINOS[int], onde int é um número do pino.
## Ex.: print(PINOS[16]) retorna False
PINOS = {16: False, 
        17: False,
        22: False,
        23: False,
        24: False,
        25: False}
        

def setup():
    global PINOS
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for pino in PINOS:
        GPIO.setup(pino, GPIO.OUT)

## NÃO ALTERE essa função
@app.route('/', methods=['GET'])
def index():
    return render_template('index_api_client.html') 


## formato de retorno:
##  {'status':'pino ligado'} - Código 200
## {'status':'pino desligado'} - Código 200
## {'status':'pino inexistente'} - Código 404
@app.route('/altera/<int:pino>/', methods=['PUT'])
def altera_pino(pino):
    global PINOS
   
## formato de retorno:
##  {'status':'ativado'} - Código 200
## {'status':'pino inexistente'} - Código 404
## Use time.sleep(int), onde int é o tempo (em segundos) para controlar o tempo
## em que o dispositivo ficará ligado e depois desligue

@app.route('/pino/liga/<int:pino>/', methods=['GET'])
def pino_liga(pino):
    global PINOS
   
## formato de retorno: exatamente o mesmo formato da variável PINOS
@app.route('/pino/status/', methods=['GET'])
def pinos_status():
    global PINOS


if __name__ == '__main__':
    setup()
    socketio.run(app, host='0.0.0.0', port='5000', debug=(not environ.get('ENV') == 'PRODUCTION'))