from socket import *

host = "localhost"
port = 5678
buf = 4096
addr = (host, port)
UDPSOCK = socket(AF_INET, SOCK_DGRAM)
def_msg = "---Enter your message---"
print '\n', def_msg
while 1:
  data = raw_input('>>  ')
  if not data:
    break
  else:
    if(UDPSOCK.sendto(data, addr)):
      print 
