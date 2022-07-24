from machine import Pin, I2C

# ---- Se requiere la Libreria SSD1306, para la importación ---- #

from ssd1306 import SSD1306_I2C
from utime import sleep

# ---- Configuracion de parametros del Oled ---- #

alto = 64
ancho = 128

# ---- Configuracion de Pines de transmision ---- #

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(ancho, alto, i2c)

# ---- Verificacion de Pantalla ---- #

oled.fill(0)
oled.text(str("Cargando"),35,20)
oled.text(str("Datos"),45,30)
oled.show()

# ---- Creación de la Clase ---- #

class Oled(object):
    
    # ---- Función de mapeo de Valores de temperatura y humedad ---- #
    
    def __init__(self,temp1, temp2, hum1, hum2):
        
        self.temp1 = temp1
        self.hum1 = hum1
        self.temp2 = temp2
        self.hum2 = hum2
        self.est = est
    
    # ---- Función Para imprimir los valores ---- #
    
    def ImpOled(self):
        
        # ---- Limpia la Pantalla ---- #
    
        oled.fill(0)
        
        sleep(300)
        
        # ---- Imprime los valores del primer sensor ---- #
    
        oled.text("Temp 1;", 0 , 0)
        oled.text(str(self.temp1), 60 ,0)
        oled.text("Hum 1:", 0, 15)
        oled.text(str(self.hum1), 60, 15)
        
        # ---- Imprime los valores del segundo sensor ---- #
        
        oled.text("Temp 2:", 0 , 35)
        oled.text(str(self.temp2), 60 ,35)
        oled.text("Hum 2:", 0,45)
        oled.text(str(self.hum2), 50,45)
        
        oled.show()
    
    def OffOled(self):
        
        if self.est == 1:
            
            oled.poweroff()
        
        else:
        
            oled.poweron()