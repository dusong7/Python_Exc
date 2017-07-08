##HeatBeat

#!/usr/bin/python
#encoding:utf-8

'''
client
'''

import socket, sys, os
import time, json
import logging  
import logging.handlers  
  
LOG_FILE = 'status.log'  
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5)
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'  
  
formatter = logging.Formatter(fmt)    
handler.setFormatter(formatter)       
  
logger = logging.getLogger('tst') 
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)  

host = '192.168.1.31'  # maybe change
port = 7878
BUF_SIZE = 4096

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, e:
    str = "Error creating socket: %s" % e
    logger.info(str)
    sys.exit()

try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    str = "Hostname couldn't be resolved. Exciting"
    logger.info(str)
    sys.exit()

try:
    client.connect((remote_ip, port))
    client.setblocking(0)   # set the socket is not blocking
    str = "Socket connected to %s on ip %s" % (host, remote_ip)
    logger.info(str)
except socket.gaierror, e:  #address related error
    str = "connected to server error%s" % e
    logger.info(str)
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
        str = "Send failed!!"
        logger.info(str)
        sys.exit()

    str = 'I - ', os.getpid(), '- am alive.'
    logger.info(str)
    time.sleep(10)
client.close()
