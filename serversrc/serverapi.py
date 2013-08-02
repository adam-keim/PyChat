import socket, select

def broadcast_data(sock, message):
	for socket in CONNECTION_LIST: #run once per connected socket
		if socket != server_socket and socket != sock: # if the connected socket is not the server socket and is not the sending socket
			try:
				socket.send(message) #try to send message
			except: #if failed
				socket.close()
				CONNECTION_LIST.remove(socket)