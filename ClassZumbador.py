from machine import Pin, PWM
from utime import sleep

class Zumbador(object):
    
    def __init__(self):
    
## ---- Configuracion de Pines para Zumbador ---- ##

        self.zum = PWM(Pin(5), freq=1047)
        self.zum.duty(0)

## ---- Funcion de Alerta Sonora ---- ##

    def Zum(self):
        
        self.zum.duty(512)
        sleep(0.5)
        self.zum.duty(0)
        sleep(0.5)
        self.zum.duty(512)
        sleep(0.5)
        self.zum.duty(0)
        sleep(0.5)
        self.zum.duty(512)
        sleep(0.5)
        self.zum.duty(0)
        sleep(0.5)
