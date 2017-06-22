import os
import shutil
import time
num = 0

while True:

    global num
    num = num + 1
    # print time.asctime()
    dirOri = "bkp_" + str(time.asctime())
    dirTemp = dirOri.replace(" ","_")
    dirName = dirTemp.replace(":", "_")
    print dirName
    os.mkdir("E:\\SwUpdatesBkp\\"+dirName)
    shutil.copy("E:\TSS\\trunk\PluginsWPF\SwUpdates\SwUpdates\HomePage.xaml", "E:\\SwUpdatesBkp\\"+dirName)
    time.sleep(5)

# print (1e99)
