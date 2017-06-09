import serial
import pyaudio
import time
import pygame
file= "iflytek01.wav"
pygame.mixer.init()
print("播放音乐1")
track = pygame.mixer.music.load(file)

#also can run
# import pygame
# import sys

# pygame.init()
# pygame.mixer.music.load("call.pcm")
# pygame.mixer.music.play()
# # pygame.event.wait()
# time.sleep(2)

pygame.mixer.music.play()
time.sleep(2)
pygame.mixer.music.stop()

##sudo apt-get install python-pyaudio python3-pyaudio
while True:
    t = serial.Serial('/dev/ttyUSB0', 115200, 8, parity=serial.PARITY_NONE, stopbits=1)

    while True:
        if t.read(6):  ##\n\r
            print(t.read(17))##weak up. angle
            # print(t.read(11))
            t.close()
            break;
