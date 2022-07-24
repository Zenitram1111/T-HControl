import umail

class Email(object):
    
    def __init__(self):
        self.smtp = umail.SMTP('smtp.gmail.com', 587, ssl=False)
    
    def EnviarCor(self, temp1, temp2, hum1, hum2, aire):
        
        self.smtp.login('correo@correo.com', 'xxxxxxxxx')
        self.smtp.to('correo@correo.com')
        self.smtp.write("From:correo@correo.com\n")
        self.smtp.write("To:correo@correo.com \n")
        self.smtp.write("Subject: Alerta de Temperatura y Humedad - T&H Control \n\n")
        
        self.smtp.write("Mensaje de Alerta \n")
        self.smtp.write("La Temperatura Actual es: \n")
        self.smtp.write("Sensor #1: " + str(self.temp1) + " °C \n")
        self.smtp.write("Sensor #2: " + str(self.temp2) + " °C \n \n")
        self.smtp.write("La Humedad Actual es: \n")
        self.smtp.write("Sensor #1: " + str(self.hum1) + " % \n")
        self.smtp.write("Sensor #2: " + str(self.hum2) + " % \n \n")
        self.smtp.write("La Calidad del Aire Actual es: \n")
        self.smtp.write("Sensor #1: " + str(self.aire) + " % \n")
        
        smtp.send()
        smtp.quit()