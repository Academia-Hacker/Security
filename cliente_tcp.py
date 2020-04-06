
import socket

target_host = "localhost"
target_port = 9999

#cria um objeto socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#faz o cliente se conectar
client.connect((target_host, target_port))

#envia alguns dados
#client.send(b"GET /HTTP/1.1\r\nHost: google.com\r\n\r\n")
msg = 'Hello, World! Eu sou o cliente'
client.send(msg.encode())

#recebe alguns dados
response = client.recv(4096)

print(response)




