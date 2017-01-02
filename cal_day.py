
import time

def dateCal(n):
    print(n%60) #second
    print(n//60%60) #min
    print(((n//60//60)+8)%24) #hour
    print((n//60//60 + 8)//24) #day
    print((n//60//60 + 8)//24/365) #year add leap year
dateCal(time.time())
