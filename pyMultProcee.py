# import thread
# import time
#
# def print_time(threadName, delay):
#     count = 0;
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         print("%s %s"%(threadName, time.ctime(time.time())))
#
# try:
#     thread.start_new(print_time, ("Thread-1", 2, ))
#     thread.start_new(print_time, ("Thread-1", 2,))
# except:
#     print "Error : unable to start thread"
#
# while 1:
#     pass

from multiprocessing import Process

def run():
    while True:
        for i in range(10000):
            x  = i * i




if __name__ == '__main__':
    p = Process(target=run)
    p.start()
    p1 = Process(target=run)
    p1.start()
    p2 = Process(target=run)
    p2.start()
    p3 = Process(target=run)
    p3.start()
