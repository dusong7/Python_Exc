##HeatBeat

#!/usr/bin/python
#encoding:utf-8

'''
client
'''

import socket, sys, os
import time, json

host = '192.168.56.101'  # maybe change
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

def doConnect(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
        sock.setblocking(0)
    except:
        pass
    return sock


# while True:
#
#
#     try:
#         client.connect((remote_ip, port))
#         client.setblocking(0)   # set the socket is not blocking
#         print "Socket connected to %s on ip %s" % (host, remote_ip)
#         break;
#     except socket.gaierror, e:  #address related error
#         print "connected to server error%s" % e
#     time.sleep(1)
#
#     # sys.exit()


# beat_count = 0

#send heart_beat
while True:
    # beat_count += 1 #heart_beat time
    client = doConnect(host, port)

    host_name = socket.gethostname()
    # data_to_server = "ip: "+str(socket.gethostbyname(host_name))+",    stats: alive,   "+"pid: "+str(os.getpid())
    data_to_server = {'ip': socket.gethostbyname(host_name), 'status': 'alive', 'pid': os.getpid()}
    data_dumped = json.dumps(data_to_server)
    try:
        client.sendall(data_dumped)
    except socket.error:
        client = doConnect(host, port)
        print "Send failed!!"

        # sys.exit()

    print 'I - ', os.getpid(), '- am alive.'
    time.sleep(10)



client.close()
