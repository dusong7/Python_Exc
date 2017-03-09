import os
import shutil
import sys
import time
num = 0
while True:


    # print(time.clock())
    time.sleep(1)
    num += 1
    print(num)
    if num == 60:
        shutil.copy('C:\\Users\Admin\Documents\Visual Studio 2015\Projects\ConsoleDS_\\testDss\\testDss.cpp', 'F:\\')
        num = 0
        os.system('cls')
