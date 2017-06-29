用Python写的一个多线程TCP通信实例，实现了JSON数据的传输。
闲言少述，直接上代码
​
一、客户端
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#

import socket
import threading
import SocketServer
import json

def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))

    try:
        print "Send: {}".format(message)
        sock.sendall(message)
        response = sock.recv(1024)
        jresp = json.loads(response)
        print "Recv: ",jresp

    finally:
        sock.close()

if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 50001
    msg1 = [{'src':"zj", 'dst':"zjdst"}]
    msg2 = [{'src':"ln", 'dst':"lndst"}]
    msg3 = [{'src':"xj", 'dst':"xjdst"}]
​
    jmsg1 = json.dumps(msg1)
    jmsg2 = json.dumps(msg2)
    jmsg3 = json.dumps(msg3)

    client(HOST, PORT, jmsg1)
    client(HOST, PORT, jmsg2)
    client(HOST, PORT, jmsg3)

二、服务端
#!/usr/bin/env python
# -*- coding:utf-8 -*-
#

import socket
import threading
import SocketServer
import json, types,string
import os, time
  
class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        jdata = json.loads(data)
        print "Receive data from '%r'"% (data)
        print "Receive jdata from '%r'"% (jdata)
        rec_src = jdata[0]['src']
        rec_dst = jdata[0]['dst']

        cur_thread = threading.current_thread()
        response = [{'thread':cur_thread.name,'src':rec_src,'dst':rec_dst}]

        jresp = json.dumps(response)
        self.request.sendall(jresp)
        rec_cmd = "proccess "+rec_src+" -o "+rec_dst
        print "CMD '%r'" % (rec_cmd)
        os.system(rec_cmd)
           
class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 50001
    
    SocketServer.TCPServer.allow_reuse_address = True
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
​
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print "Server loop running in thread:", server_thread.name
    print " .... waiting for connection"

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
