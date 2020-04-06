
import socket
import threading

bind_ip = "localhost"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print('[*] Listening  on {}: {}'.format(bind_ip, bind_port))

def handle_client(client_socket):

	# exibe o que o cliente enviar
	request = client_socket.recv(1024)

	print('[*] Received: {}'.format(request))

	# envia um pacote de volta
	msg = 'Mensagem destinada ao cliente'
	client_socket.send(msg.encode())	

	client_socket.close()

while True:
	client, addr = server.accept()

	print('[*] Accepted connection from: {}: {}'.format(addr[0], addr[1]))

	# coloca nossa thread de clientes em ação para tratar dados de entrada
	client_handler = threading.Thread(target= handle_client, args= (client, ))
	#client_handler = client_thread(client)
	client_handler.start()



