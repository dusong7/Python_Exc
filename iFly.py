import serial

while True:
    t = serial.Serial('/dev/ttyUSB0', 115200, 8, parity=serial.PARITY_NONE, stopbits=1)

    while True:
        if t.read(6):
            print(t.read(17))
            # print(t.read(11))
            t.close()
            break;
