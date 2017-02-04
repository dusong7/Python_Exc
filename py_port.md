Python的串口网上有很多例子，这里了只是把认为好的整理到一起。
首先，应该安装serial模块，还能开始后续的操作。我用的python2.6，serial模块可以在这里下载安装serial模块下载

1,字符串的发送接收
短接串口的2、3脚，创建一个文本，如：
[python] view plain copy
import serial  
  
t = serial.Serial('com12',9600)  
n = t.write('you are my world')  
print t.portstr  
print n  
str = t.read(n)  
print str  

或者你可以稍微添加几句，变成你任意输入后打印出你的键入信息。
[python] view plain copy
import serial  
  
t = serial.Serial('com12',9600)  
print t.portstr  
strInput = raw_input('enter some words:')  
n = t.write(strInput)  
print n  
str = t.read(n)  
print str  

其中，read(value)方法的参数value为需要读取的字符长度。 如果想要全部读取，提供两个方法：
1）inWaiting：：监测接收字符。 inWaitting返回接收字符串的长度值，然后把这个值赋给read做参数。
2）readall（）：：读取全部字符。
===================================================================================================================================

2,十六进制显示
十六进制显示的实质是把接收到的字符诸葛转换成其对应的ASCII码，然后将ASCII码值再转换成十六进制数显示出来，这样就可以显示特殊字符了。
在这里定义了一个函数，如hexShow(argv)，代码如下：
[python] view plain copy
import serial  
  
def hexShow(argv):  
    result = ''  
    hLen = len(argv)  
    for i in xrange(hLen):  
        hvol = ord(argv[i])  
        hhex = '%02x'%hvol  
        result += hhex+' '  
    print 'hexShow:',result  
  
t = serial.Serial('com12',9600)  
print t.portstr  
strInput = raw_input('enter some words:')  
n = t.write(strInput)  
print n  
str = t.read(n)  
print str  
hexShow(str)  

===================================================================================================================================

3,十六进制发送
十六进制发送实质是发送十六进制格式的字符串，如'\xaa'，'\x0b'。重点在于怎么样把一个字符串转换成十六进制的格式，有两个误区：
1）'\x'+'aa'是不可以，涉及到转义符反斜杠
2）'\\x'+'aa'和r'\x'+'aa'也不可以，这样的打印结果虽然是\xaa，但赋给变量的值却是'\\xaa'

 这里用到decode函数，
[python] view plain copy
list='aabbccddee'  
hexer=list.decode("hex")  
print  hexer  

需要注意一点，如果字符串list的长度为奇数，则decode会报错，可以按照实际情况，用字符串的切片操作，在字符串的开头或结尾加一个'0'
 
假如在串口助手以十六进制发送字符串"abc"，那么你在python中则这样操作“self.l_serial.write(”\x61\x62\x63") ”
当然，还有另外一个方法：
[python] view plain copy
strSerial = "abc"  
strHex = binascii.b2a_hex(strSerial)  
#print strHex  
strhex = strHex.decode("hex")  
#print strhex  
self.l_serial.write(strhex);  
同样可以达到相同目的。
那么，串口方面的就整理完了。
源代码

额外一个小知识：
索引：也称作是下标操作，那么python就会为你抓取序列中对应位置的项目。它是从0开始计数，那么str[0]即为第一个项目， str[3]为第四个。（str只是一个参考序列）。当然呢，python有点不同是它可以是负数，位置就是从序列尾开始计算的。str[-1]表示序列的最后一个元素，而str[-2]为倒数第二个。
切片操作：顾名思义，就是可以连续一整块，把什么切成几段，但那一段是连续的。它是序列名后跟一个方括号，方括号有一对可选的数字，并用冒号分割。数是可选的，但冒号是必须的。例如str[1:3]返回从位置1开始，包括位置2，但是不包括位置3，返回的是一个含有两个项目的切片。类似，str[：]返回整个序列的拷贝。同样，它也是可以用负数的。
