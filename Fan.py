# librerias necesarias

import RPi.GPIO as GPIO
import time
from gpiozero import CPUTemperature

#Variables
PinVentilador = 21

# Configuraciones
GPIO.setmode(GPIO.BCM)
GPIO.setup(PinVentilador,GPIO.OUT)
pwm = GPIO.PWM(PinVentilador, 20) # Pin del Ventilador y frecuencia del PWM en HZ
cpu = CPUTemperature()

#Arranque
dc = 0;
pwm.start(dc)

try:
    while True:# Loop until Ctl C is pressed to stop.
        cpu.temperature
        print(cpu.temperature)
        if cpu.temperature > 57: #Si supera 57 grados
            dc = dc + 10
            if dc > 100:
                dc = 100
            pwm.ChangeDutyCycle(dc)
        elif cpu.temperature < 54: # Si se reduce menos de 54
            dc = dc -10
            if dc< 0:
                dc = 0
            pwm.ChangeDutyCycle(0)
        
        time.sleep(1)
except KeyboardInterrupt:
  print("Ctl C pressed - ending program")

pwm.stop()                         # stop PWM
GPIO.cleanup()                     # resets GPIO ports used back to input mode
        