# ACENDER LEDS AZUL E VERMELHO COM RASPBERRY PI 3 E PYTHON
# Na aula de hoje vamos aprender como acender leds utilizando um RASPBERRY PI 3 e a linguagem de progração PYTHON 3


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwranings(False)

Led_Azul = 23
Led_Vermelho = 16

GPIO.setup(Led_Azul,GPIO.OUT)
GPIO.setup(Led_Vermelho,GPIO.OUT)

try:
    while True:
        print("LED AZUL")
        GPIO.Output(Led_Azul,True)
        GPIO.Output(Led_Vermelho,False)
        time.sleep(2)
        print("LED VERMELHO")
        GPIO.Output(Led_Azul,False)
        GPIO.Output(Led_Vermelho,True)
        time.sleep(2)
        print("LED AZUL E VERMELHO LIGADO")
        GPIO.Output(Led_Azul,True)
        GPIO.Output(Led_Vermelho,True)
        time.sleep(2)
        print("LED AZUL E VERMELHO DESLIGADO")
        GPIO.Output(Led_Azul,False)
        GPIO.Output(Led_Vermelho,False)
        time.sleep(2)
except KeyboardInterrupt:
    print("DESLIGANDO...")
    GPIO.cleanup()