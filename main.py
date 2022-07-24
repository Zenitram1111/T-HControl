import gc
gc.collect()

from machine import Pin, PWM, ADC
from utime import sleep
from utelegram import *
from ClassOled import Oled
from ClassTempHum import TemperaturaHumedad
from ClassRGB import RGBLed
from ClassZumbador import Zumbador
from ClassWifi import ConnectionWifi
from ClassThinkSpeak import ThingSpeak
from ClassCorreo import Email
from ClassTime import TiempoA
import time

CTiempo = TiempoA()

## ---- Instanciamos las clases para la captura de Temperatura y Humedad ---- ##

sensorTH1 = TemperaturaHumedad(15)
sensorTH2 = TemperaturaHumedad(4)

## ---- Instanciamos las clases para la captura de Aire ---- ##

aire = ADC(Pin(34))

## ---- Instanciamos las clases para el envio de datos al DashBoard ---- ##

dash = ThingSpeak()

## ---- Instanciamos las clases para la Alerta Visual ---- ##

rgb = RGBLed()

## ---- Instanciamos las clases para la Alerta Sonora ---- ##

zumba = Zumbador()

## ---- Instanciamos la clase para la conexión Wifi ---- ##

wifi = ConnectionWifi("xxxxxx","xxxxxxxx*")

estado = wifi.conectaWifi()

sleep(1)

## ---- Validamos el Estado de Conexión Wifi ---- ##

if estado != "" or estado != None:
    print("Conexión activa con la siguiente Configuracion: ", wifi.ConfigWifi())
    
    sleep(1)
    
    ## ---- Instanciamos la clase para la conexión Wifi ---- ##
    
    bot = ubot('xxxxxxxxxxxxxxxx')
    
else:
    estado = "--"
    print("El estado de la Conexión es: ", estado)

    ## ---- Ejecutamos El Programa ---- ##


while True:
    
    ## ---- Iniciomos la ejecución del Programa ---- ##
    
    try:
        
        sleep(1)

        ## ---- Capturamos la temperatura de los dos Sensores DHT11 y los almacenamos en un Variable ---- ##
      
        temp1 = sensorTH1.Temperatura()
        temp2 = sensorTH2.Temperatura()
        
        ## ---- Capturamos la humedad de los dos Sensores DHT11 y los almacenamos en un Variable ---- ##

        hum1 = sensorTH1.Humedad()
        hum2 = sensorTH2.Humedad()
        
        ## ---- Capturamos los valores del sensor de Aire ---- ##
        
        vaire = aire.read()
        
        print(temp1,temp2,hum1,hum2,vaire)
        
        ## ---- Capturamos los Parametros del Chat de Telegram ---- ##
        
        valor = bot.read_once()
            
        ## ---- Verificamos si hay mensajes nuevos de Telegram ---- ##
        
        if valor != []:
            
            ## ---- Guardamos el ID del Chat ---- ##
        
            idChat = valor[-1]['message']['chat']['id']
        
            ## ---- Guardamos el ID del Mensaje ---- ##
        
            idMess = valor[-1]['message']['message_id']
            
            ## ---- Captura el Valor del Mensaje ---- ##
            
            text = valor[-1]['message']['text']
            
            print(text)
            
            if text == "1":
                bot.send(idChat,'Temperatura Actual: \n\n' +
                         'Sensor #1: ' + str(temp1) + ' Ce \n' +
                         'Sensor #2: ' + str(temp2) + ' Ce')
                print(text)
            elif text == "2":
                bot.send(idChat,'Humedad Actual: \n\n' +
                         'Sensor #1: ' + str(hum1) + ' % \n' +
                         'Sensor #2: ' + str(hum2) + ' %')
                print(text)
            elif text == "3":
                bot.send(idChat,'Calidad Actual: \n\n' +
                         'Sensor #1: ' + str(vaire) + ' %')
                print(text)
            elif text == "4":
                bot.send(idChat,'https://thingspeak.com/channels/1810365')
                print(text)
            elif text == "5":
                
                Email().EnviarCor(temp1,temp2,hum1,hum2,vaire)
                
                bot.send(idChat,'Correo Enviado')
                print(text)
            else:
                bot.send(idChat, 'Bienvenido(a) a T&H Control \n\n' +
                         'A continuacion, se indicara las opciones a elegir: \n' +
                         '\n 1. Temperatura Actual' +
                         '\n 2. Humedad Actua' +
                         '\n 3. Calidad de Aire' +
                         '\n 4. DashBoard' +
                         '\n 5. Envio de Correo (Alerta)')
                
        else:
            print("No hay mensajes nuevos")
        
        if ((temp1 >= 18 and temp1 <= 24 and temp2 >= 18 and temp2 <= 24) and (hum1 >= 40 and hum1 <= 80 and hum2 >= 40 and hum2 <= 80) and (vaire >= 0 and vaire <= 3500)):

        ## ---- Si esta todo en optimas condiciones, la alerta visual (led) queda activo de Color Verde ---- ##

            rgb.ColorLed(0,1,0)
              
        ## ---- Se imprime los resultados en alerta visual (Pantalla) e indicamos en su ultimo valor, el tiempo de refresco ---- ##
              
            Oled(temp1,temp2,hum1,hum2,1).ImpOled()
                         
        ## ---- Se envia informacion al Dashboard ---- ##
            
            dash.enviarDatos(temp1,temp2,hum1,hum2,vaire)
        
                     
        else:
              
            ## ---- Si se supera el humbral de condiciones optimas, se activa la alerta visual (Led) de Color Rojo ---- ##
     
            rgb.ColorLed(1,0,0)
            
            sleep(1)
             
             ## ---- Se imprime los resultados en alerta visual (Pantalla) ---- ##
             
            Oled(temp1,temp2,hum1,hum2,1).ImpOled()
            
     
             ## ---- Se envia informacion al Dashboard ---- ##
            
            dash.enviarDatos(temp1,temp2,hum1,hum2,vaire)
            
             ## ---- Se activa la alerta sonora (Zumbador), generando tres (3) sonidos intermitentes ---- ##
     
            zumba.Zum()
                        
            ## ---- Capturamos la segudos actuales de la hora ---- ##

            tiempo = time.mktime(time.localtime())
            
            print("Almacenamos el Tiempo Actual: ", tiempo)
            print("---------------------------------------")
            
            TiempoV = CTiempo.GTime(tiempo)
            print("Instancia la Clase y enviamos el tiempo, nos retorna: ", TiempoV)
            print("---------------------------------------")
            
            ## ---- Se activa la alerta via correo electronico ---- ##
            
            if TiempoV == 1:
                print("Al guardarlo retorna 1, envia correo")
                print("---------------------------------------")
                Email().EnviarCor(temp1,temp2,hum1,hum2,vaire)
                
            elif TiempoV == 0 or TiempoV == 2:
                print("Al guardarlo nuevamente, valida si ya existe, retorna 0 si ya existe")
                print("---------------------------------------")
                if CTiempo.ValidarT(tiempo) == 1:
                    print("Como ya existe, valida el tiempo si es igual o mayor y envia correo si se cumple")
                    print("---------------------------------------")
                    Email().EnviarCor(temp1,temp2,hum1,hum2,vaire)
                
    except:
        
        sleep(1)
            
        rgb.ColorLed(1,0,0)
        
        Oled("Calibrando","Calibrando","Sensores","Sensores",2).ImpOled()
        
        zumba.Zum()