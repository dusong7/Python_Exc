以下是“心跳”程序的服务端（监听心跳）代码：

#!/usr/bin/python
#encoding:utf-8

'''
server
'''
import socket, sys, json
from thread import *
BUF_SIZE = 4096

HOST = socket.gethostname()
PORT = 7878
try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, e:
    print "Error creating socket: %s" %e
    sys.exit()
try:
    server.bind((HOST, PORT))
except socket.error:
    print "Bind failed!"
    sys.exit()
print "Socket bind complete"

server.listen(10)
print "Socket now listening"


def clientthread(coon):
    coon.send("Welcome to the server!")
    while True:
        try:
            data = coon.recv(BUF_SIZE)
            data_loaded = json.loads(data)
            print "ip: "+str(data_loaded['ip'])+" |status: "+data_loaded['status']+" |pid: "+str(data_loaded['pid'])
            # coon.sendall("hello, I love you!")    # set the client :setblock(0)is ok!
        except socket.error:
            print "One Client (IP: %s) Connected over!" % data_loaded['ip']
            break
    coon.close()


while True:
    coon, addr = server.accept()
    print "Connected with %s: %s " % (addr[0], str(addr[1]))
    start_new_thread(clientthread, (coon,))

server.close()
以下是心跳发起端代码：

#!/usr/bin/python
#encoding:utf-8

'''
client
'''

import socket, sys, os
import time, json

host = 'ZFQSH-L0686'  # maybe change
port = 7878
BUF_SIZE = 4096

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, e:
    print "Error creating socket: %s" % e
    sys.exit()

try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print "Hostname couldn't be resolved. Exciting"

    sys.exit()

try:
    client.connect((remote_ip, port))
    client.setblocking(0)   # set the socket is not blocking
    print "Socket connected to %s on ip %s" % (host, remote_ip)
except socket.gaierror, e:  #address related error
    print "connected to server error%s" % e
    sys.exit()


# beat_count = 0

#send heart_beat
while True:
    # beat_count += 1 #heart_beat time

    host_name = socket.gethostname()
    # data_to_server = "ip: "+str(socket.gethostbyname(host_name))+",    stats: alive,   "+"pid: "+str(os.getpid())
    data_to_server = {'ip': socket.gethostbyname(host_name), 'status': 'alive', 'pid': os.getpid()}
    data_dumped = json.dumps(data_to_server)
    try:
        client.sendall(data_dumped)
    except socket.error:
        print "Send failed!!"
        sys.exit()

    print 'I - ', os.getpid(), '- am alive.'
    time.sleep(50)
client.close()
