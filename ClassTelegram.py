from machine import Pin
from utelegram import Bot
from ClassTempHum import TemperaturaHumedad

class Telegram(object):
    
    def __init__(self):
        self.bot = Bot('xxxxxxxxxxxxxxxx')
        self.sensorTH1 = TemperaturaHumedad(15)
        self.sensorTH2 = TemperaturaHumedad(4)
        self.bombillo  = Pin(2, Pin.OUT)

        @bot.add_message_handler("Hola")
        def help(update):
        update.reply('''¡Bienvenido(a) a T&H Control!
                     \n A continuacion indicamos el Menu Principal
                     \n Elije una opción:
                     
                     Temperatura : 1
                     Humedad: 2
                     Calidad de Aire: 3
                     Dashboard: 4
                     
                     \n Quedamos atentos a tu solicitud ''')

        @bot.add_message_handler("1")
        def help(update):

        self.bombillo.value(1)
        
        temp1 = sensorTH1.Temperatura()
        temp2 = sensorTH2.Temperatura()

        update.reply('La Temperatura Actual del Sensor #1 es de: ' + str(temp1) + '°C \n La Temperatura Actual del Sensor #2 es de: ' + str(temp2) + '°C')

        bot.start_loop()
