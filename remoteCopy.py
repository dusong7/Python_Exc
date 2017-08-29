import socket
import platform
import os

ip_prefix = "172.30.52"
listTargetMachine = []

def get_os():
    ##get os type
    os = platform.system()
    if os == "Windows":
        return "n"
    else:
        return "c"

def ping_ip(ip_str):
    cmd = ["ping", "-{op}".format(op=get_os()),
           "1", ip_str]
    output = os.popen(" ".join(cmd)).readlines()

    flag = False
    for line in list(output):
        if not line:
            continue
        if str(line).upper().find("TTL") >= 0:
            flag = True
            break
    if flag:
        ##can conneted
        ##
        print "%s can connected"%ip_str
        listTargetMachine.append(ip_str)
        return True
    else:
        return False


if __name__ == "__main__":

    for i in range(1, 256):
        ip = '%s.%s' % (ip_prefix, i)
        # if ping
        #     portOn = test_port(ip, 5555);
        #     if portOn:
        #         print ip + " got valid port"_ip(ip):
        ping_ip(ip)
        
##File remote addr copy        
result = shutil.copytree("//172.30.52.75/Utility/Multimedia/TruRecorder/Document","E://Downloads//Test")
print result


import socket

localIP = socket.gethostbyname(socket.gethostname())
print "local ip:%s " % localIP

ipList = socket.gethostbyname_ex(socket.gethostname())
for i in ipList:
    if i != localIP:
        print "external IP:%s" % i
      
    
 # -*- coding: utf-8 -*-
   #!/usr/bin/python
   #Filename:copyfile.py
   import os,shutil
   def mycopy(srcpath,dstpath):
       if not os.path.exists(srcpath):
           print "srcpath not exist!"
       if not os.path.exists(dstpath):
           print "dstpath not exist!"
      for root,dirs,files in os.walk(srcpath,True):
          for eachfile in files:
              shutil.copy(os.path.join(root,eachfile),dstpath)
  srcpath='e:\\pic'
  dstpath='f:\\pictotal'
  mycopy(srcpath,dstpath)

import shutil
import os
import socket
# shutil.copy("\\172.30.52.75\Utility\Multimedia\TruRecorder\Document","")
# shutil.copytree("E://Fold_Bkp","E://Downloads//Test")
# target_files = r'\\172.30.52.75\Utility\Multimedia\TruRecorder\Document\TruRecorder-Design_spec_addmore.pptx'
# shutil.copy("target_files","E://Downloads//Test")
#
# result = shutil.copytree("//172.30.52.75/Utility/Multimedia/TruRecorder/Document","E://Downloads//Test")
# print result


listContentRemote = os.listdir("//172.30.52.75/Utility/Multimedia/TruRecorder/Document")
for i in listContentRemote:
    print i
# import socket
#
# localIP = socket.gethostbyname(socket.gethostname())
# print "local ip:%s " % localIP
#
# ipList = socket.gethostbyname_ex(socket.gethostname())
# for i in ipList:
#     if i != localIP:
#         print "external IP:%s" % i
