#codigo do cliente


import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:       #com while True, cliente pode continuar a mandar mensagem
       ip = input("Informe o endereço IP: ")
       porta = input("Informe o número de porta: ")
       mensagem = input("Escreva a mensagem a ser enviada ao servidor: ")
       envio = s.sendto(mensagem.encode(),('127.0.0.1', 65001)) 
       if envio:
          print("Mensagem enviada")
