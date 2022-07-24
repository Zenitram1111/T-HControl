import network, time, urequests

class ConnectionWifi(object):
    
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
        

    def conectaWifi (self):
        
        estadoCon = ""
        
        global miRed
        miRed = network.WLAN(network.STA_IF)
        
        if not miRed.isconnected():              #Si no está conectado…
          miRed.active(True)                   #activa la interface
          miRed.connect(self.ssid, self.password)         #Intenta conectar con la red
          
          timeout = time.time ()
          estadoCon = "La conexión a la Red: " + self.ssid + " fue establecida correctamente."
          
          while not miRed.isconnected():           #Mientras no se conecte..
              if (time.ticks_diff (time.time (), timeout) > 10):
                  estadoCon = "Error en la Conexión, verifique los datos ingresados"
                  return estadoCon
        else:
            estadoCon = "La red " + self.ssid + " ya se encuentra conectada"
            return estadoCon

    def ConfigWifi(self):
        self.red = miRed.ifconfig()
        
        return self.red
        
