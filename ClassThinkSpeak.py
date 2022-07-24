import urequests
import json

class ThingSpeak(object):
    
    def __init__ (self):
        self.url = "https://api.thingspeak.com/update?api_key=xxxxxxxxxx"

    
    def enviarDatos(self,temp1,temp2,hum1,hum2,aire):
        self.temp1 = temp1
        self.temp2 = temp2
        self.hum1 = hum1
        self.hum2 = hum2
        self.aire = aire
        respuesta = urequests.get(self.url+"&field1="+str(self.temp1)+"&field2="+str(self.temp2)+"&field3="+str(self.hum1)+"&field4="+str(self.hum2)+"&field5="+str(self.aire))
        respuesta.close()