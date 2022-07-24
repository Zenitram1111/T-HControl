from machine import Pin

class RGBLed(object):

## ---- Configuracion de Pines para Modulo RGB ---- ##

    def __init__(self):
        
        self.r = Pin(12, Pin.OUT)
        self.g = Pin(13, Pin.OUT)
        self.b = Pin(14, Pin.OUT)

## ---- Funcion de RGB ---- ##

    def ColorLed(self,R,G,B):
    
        self.r.value(R)
        self.g.value(G)
        self.b.value(B)