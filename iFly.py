import serial
import pyaudio
##sudo apt-get install python-pyaudio python3-pyaudio
while True:
    t = serial.Serial('/dev/ttyUSB0', 115200, 8, parity=serial.PARITY_NONE, stopbits=1)

    while True:
        if t.read(6):  ##\n\r
            print(t.read(17))##weak up. angle
            # print(t.read(11))
            t.close()
            break;
