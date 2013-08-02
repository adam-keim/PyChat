from serverapi.py import *

CONNECTION_LIST = [] #array to store connections
RECV_BUFFER = 8129
PORT = 5006

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# this has no effect, why ?
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("0.0.0.0", PORT)) #bund localhost to port?
server_socket.listen(10) # listen on socket when there are less than 10 messages in the queue(to prevent spam)
CONNECTION_LIST.append(server_socket) #add server socket to connection list
print "Chat server started on port " + str(PORT)
while True:
	#get socket list
	read_sockets,write_sockets,error_sockets = select.select(CONNECTION_LIST,[],[])
	for sock in read_sockets:
		if sock == server_socket:
			sockfd, addr = server_socket.accept