import signal
import subprocess
import os

p = subprocess.Popen(['ps','-A'],stdout=subprocess.PIPE)
out,err = p.communicate()

curPPid = os.getppid() #parent pid

for line in out.splitlines():
    if 'bash' in line:
        pid = int(line.split(None,1)[0])
	if(pid != curPPid):
        	os.kill(pid,signal.SIGKILL)

os.system("gnome-terminal -e ./fifo")
os.kill(curPPid,signal.SIGKILL)
