# librerias necesarias

import RPi.GPIO as GPIO
import time
from gpiozero import CPUTemperature

#Variables
PinVentilador = 21

# Configuraciones
GPIO.setmode(GPIO.BCM)#Defino el tipo de conexion
GPIO.setup(PinVentilador,GPIO.OUT)# Se trata de una salida
pwm = GPIO.PWM(PinVentilador, 20) # Pin del Ventilador y frecuencia del PWM en HZ
cpu = CPUTemperature() # Saber la temperatura que tiene el procesador

#Arranque
dc = 0;
pwm.start(dc)#Comienzo con una porcentaje, en este caso 0%

try:
    while True:# Loop until Ctl C is pressed to stop.
        if cpu.temperature > 57: #Si supera 57 grados
            dc = dc + 10
            if dc > 100: # No dejo que la señal esceda de 100 %
                dc = 100
            pwm.ChangeDutyCycle(dc) # Asigno el porcentaje
        elif cpu.temperature < 54: # Si se reduce menos de 54
            dc = dc -10
            if dc< 0: # No dejo que la señal decaiga de 0 %
                dc = 0
            pwm.ChangeDutyCycle(0) # Asigno el porcentaje
        time.sleep(1)
except KeyboardInterrupt:

pwm.stop()                         # stop PWM
GPIO.cleanup()                     # resets GPIO ports used back to input mode
        