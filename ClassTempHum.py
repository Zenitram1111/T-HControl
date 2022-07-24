from machine import Pin
from dht import DHT11

## ---- Funcion de Temperatura ---- ##

class TemperaturaHumedad(object):

    def __init__(self, pin):
        self.pin = pin
        
    def Temperatura(self):
        
        sensorDHT11 = DHT11(Pin(self.pin))
        
        sensorDHT11.measure()
        
        temp = sensorDHT11.temperature()
    
        return temp

## ---- Funcion de Humedad ---- ##

    def Humedad(self):
        
        sensorDHT11 = DHT11(Pin(self.pin))
        
        sensorDHT11.measure()
        
        hum = sensorDHT11.humidity()
    
        return hum    