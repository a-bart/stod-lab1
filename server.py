import socket, sys

socket.setdefaulttimeout(150)
host = ''
port = 50005
socksize = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
print("Server started on port: %s" % port)
counter = 0

while True:
    print("Now listening...\n")
    conn, addr = s.accept()
    print 'New connection from %s:%d' % (addr[0], addr[1])
    print 'Count', counter
    counter += 1
    data = conn.recv(socksize)
    if not data:
        break
    elif data == 'killsrv':
        conn.close()
        sys.exit()
    else:
        print(data)
