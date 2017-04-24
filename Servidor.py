#!/usr/bin/env python
import socket

TCP_IP = "192.168.1.104"
TCP_PORT = 5000
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((TCP_IP, TCP_PORT))
server.listen(1)
socket_c, (host_c, addr_c) = server.accept()
i=0

while (1):
  if(i==0):
    ip=socket_c.recv(BUFFER_SIZE)
    print("IP del cliente es: "+ip.decode())
    nombre=socket_c.recv(BUFFER_SIZE)
    print("Nombre del cliente es: "+nombre.decode())
    i+=1
  print ("Enviar un mensaje al cliente: ")
  mensaje=input()
  socket_c.send(mensaje.encode())
  print ("Esperando respuesta...\n")
  respuesta= socket_c.recv(BUFFER_SIZE)
  if (respuesta.decode()=='over'): 
    break
  print ("Cliente: "+ respuesta.decode())
print ("\n...")
print ("\n  Desconectando...")
socket_c.close()
server.close()