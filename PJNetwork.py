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

udp_s = socket(AF_INET, SOCK_DGRAM)
udp_s.bind(('127.0.0.1', 9000))

listClient=[]
while True:
    msg, addr = udp_s.recvfrom(1024)
    print(msg, addr)
    if len(msg)==0:
        listClient.append(addr)
        # if(len(listClient) >0):
        #     addr != listClient[0]
        #     listClient.append(addr)
        # else:
        #     listClient.append(addr)

        if listClient.__len__() == 2:
            break

# print(type(listClient[0]))

while True:
    msg, addr = udp_s.recvfrom(1024)
    print(msg, addr)
    print(len(msg))

    if addr == listClient[0]:
        udp_s.sendto(msg.upper(),listClient[1])
    if addr == listClient[1]:
        udp_s.sendto(msg.upper(),listClient[0])
##UDP-Client

 from socket import *
import time
import _thread
import threading


udp_c = socket(AF_INET, SOCK_DGRAM)

# udp_c.sendto("".encode('utf-8'),('127.0.0.1', 9000))

def heart():
    while True:
        udp_c.sendto("".encode('utf-8'), ('127.0.0.1', 9000))

        time.sleep(2)


t = threading.Thread(target=heart)
# t.start()



while True:
    msg = input('>>: ').strip()
    if not msg:
        continue
    udp_c.sendto(msg.encode('utf-8'),('127.0.0.1', 9000))
    back_msg, addr = udp_c.recvfrom(1024)

    print(back_msg.decode('utf-8'), addr)
