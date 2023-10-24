#conexão de chat entre servidor e cliente, porém o servidor apenas recebe mensagens e o cliente apenas envia mensagens

#código do servidor

import socket      


s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM )


s.bind(("127.0.0.1",65001))
print("Servidor conectado, esperando mensagem do cliente")

#ao receber mensagem do cliente


while True:           #o servidor vai continuar sendo o receptor enquanto tivermos o while True
       print(s.recvfrom(1024))
