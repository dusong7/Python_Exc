在linux/unix平台下，可以使用ps -A找到进程：

import subprocess,signal

p = subprocess.Popen(['ps','-A'],stdout=subprocess.PIPE)
out,err = p.communicate()

这样ps -A命令的执行结果就输出到out中了，可以分析每一行获得要杀死的进程信息

for line in out.splitlines():
if 'processNameToKill' in line:
pid = int(line.split(None,1)[0])
os.kill(pid,signal.SIGKILL)

这里的os.kill(pid,signal.SIGKILL)和kill -9的效果是一样的，signal.SIGKILL的值是9
