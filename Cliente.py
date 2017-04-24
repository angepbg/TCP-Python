#!/usr/bin/env python
import socket
#Se importa la libreria socket que permitirá realizar una comunicación TCP o UDP
#Para este ejemplo usaremos una transmisión TCP
TCP_IP = '192.168.1.104' 
TCP_PORT = 5000
BUFFER_SIZE = 1024
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Se crea un socket indicando en el constructor:
# -socket.AF_INET que permite la comunicación utilizando protocolos de Internet como TCP o UDP
# -socket.SOCK_STREAM es una de clasificación de flujo, se usa dependiendo si el servicio utiliza TCP, de lo contrario
# se utilizaría socket.SOCK_DGRAM

client.connect((TCP_IP, TCP_PORT))
#Se establece la conexión con el servidor, la función connect() lleva como argumento:
# Una tupla con host y puerto

i=0
while(1):
    if (i==0):
        print("Enviando mi nombre e IP... ")
        nombre= socket.gethostname() #Se obtiene el nombre de nuestro host
        ip=socket.gethostbyname(nombre) #Se obtiene la IP apartir del nombre de nuestro host
        client.send(ip.encode()) #Envia la IP con la funcion send() al servidor, tomando como argumento una cadena codificada
        print("Dirección enviada")
        client.send(nombre.encode()) #Envia el nombre al servidor
        print("Nombre enviado")
        i+=1
    print ("Esperando respuesta...\n")
    respuesta = client.recv(BUFFER_SIZE) #Recibe una respuesta del servidor, la función recv() toma como parámetro el N° máximo de bytes a aceptar
    print ("Servidor: ", respuesta.decode()) #Muestra la respuesta en la consola usando la función decode() que decodifica la cadena enviada
    print ("Envia un mensaje al cliente: ")
    mensaje=input()
    client.send(mensaje.encode())
    if (mensaje=='over'):
        break
#
print ("\n ...")
print ("\n  Desconectando...")
client.close() #Cierra la conexión 
