

import socket, string, select, sys
HOST, PORT = '', 5007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
s.bind((HOST, PORT))
s.listen(1)
try:
    f = open('log.txt', 'a')
    print 'logfile detected'
    f.close()
except:
    print "Will not use logfile"
socknames = {}
def write(message):
    
    global f
    try:
        f = open('log.txt', 'a')
        f.write(message)
        f.close()
    except: pass
def broadcast(message, sender):
    write(message)
    for sock in socknames.keys():
        if sock is not sender:
            sock.send(message)

while 1:
    nums = [s.fileno()]
    for sock in socknames.keys():
        nums.append(sock.fileno())
    rd, wr, ex = select.select(nums, [], [], None)

    for n in rd:
        if n == s.fileno():
            sock, addr = s.accept()
            socknames[sock] = None
            sock.send("Hello!  Please enter your name.\n")

        else:
            for sock in socknames.keys():
                if sock.fileno() == n: break
            name = socknames[sock]

            text = sock.makefile().readline()

            if not text:
                broadcast("%s has left.\n" % name, sock)
                sock.close()
                del socknames[sock]

            elif name is None:
                name = string.strip(text)
                socknames[sock] = name
                sock.send("Thanks!  Welcome to the conversation.\n")
                broadcast("%s has arrived.\n" % name, sock)

            else:
                if text == '/killserver':
                    sys.exit(0)
                broadcast("%s> %s\n" % (name, text), sock)

