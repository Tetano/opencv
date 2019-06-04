import socket
import sys
import os

print("Testando apradigma requisição resposta")

def request_replay():
    #host = sys.arg[1]
    host = "www.google.com"
    porta = 88
    # cria um objeto socket
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # faz o cliente se conectar
    client.connect((host,porta))
    #envia alguns ados
    get_http = 'GET / HTTP/1.1\r\nHost: ' + host + '\r\n\r\r'
    client.send(get_http.encode())
    # Recebe alguns dados
    response = client.recv(4096)
    print(response + "-")

request_replay()