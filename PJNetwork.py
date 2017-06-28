##TCP-server
from socket import *
import time

server = socket(AF_INET, SOCK_STREAM)

server.bind(('127.0.0.1', 8080))
server.listen(5)
print("starting")
while True:
    con, addr = server.accept()
    print(con)

    print('client addr', addr)
    print('ready to read msg')
    while True:
        client_msg = con.recv(1024)
        if len(client_msg) == 0:
            break
        print('client msg: %s'%client_msg)
        con.send(client_msg.upper())
    con.close()
server.close()


##TCP-client
from socket import *
import time


for i in range(1000):
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(('127.0.0.1', 8080))

# str2 = (b'Rain', b'is' ,b'falling', b'all', b'around', b'It' ,b'falls', b'on', b'field' b'and', b'tree')
    client.send('world'.encode('utf-8'))

    back_msg = client.recv(1024)
    print(back_msg)
    time.sleep(1)
    client.close()
    
    
##UDP-server

from socket import *
import time

server = socket(AF_INET, SOCK_STREAM)

server.bind(('127.0.0.1', 8080))
server.listen(5)
print("starting")
while True:
    con, addr = server.accept()
    print(con)

    print('client addr', addr)
    print('ready to read msg')
    client_msg = con.recv(1024)
    print('client msg: %s'%client_msg)
    con.send(client_msg.upper())
    con.close()

server.close()

##UDP-Client

from socket import *
import time


for i in range(1000):
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(('127.0.0.1', 8080))

# str2 = (b'Rain', b'is' ,b'falling', b'all', b'around', b'It' ,b'falls', b'on', b'field' b'and', b'tree')
    client.send('hello'.encode('utf-8'))

    back_msg = client.recv(1024)
    print(back_msg)
    time.sleep(1)
    client.close()
