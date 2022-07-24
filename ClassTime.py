import time

tiempo = 0

class TiempoA(object):
    
    def __init__(self, vtime):
        self.vtime = vtime
        print("Ingresa al Constructo con el valor: ", vtime)
 
    def GTime(self):
        
        if tiempo == self.vtime:
            print("Ingresa a GTime, Ingresa al IF y retorna 0: ", self.vtime)
            return 0
            
            
        elif tiempo == 0:
            print("Ingresa a GTime, Ingresa al Elif y retorna 1: ", tiempo)
            tiempo = self.vtime + 300
            return 1
            
        
        else:
            print("Ingresa a GTime, Ingresa al Else y restablece el tiempo: ", tiempo)
            tiempo = 0
            
    def ValidarT(self):
        
        if self.vtime >= tiempo:
            print("Ingresa a ValidarT, Verifica el tiempo guardado VS el actual: ", self.vtime, tiempo)
            return 1
            
        else:
            print("Ingresa a ValidarT, retorna 0")
            return 0
            