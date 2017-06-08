import serial

while True:
    t = serial.Serial('/dev/ttyUSB0', 115200, 8, parity=serial.PARITY_NONE, stopbits=1)

    while True:
        if t.read(8):
            print(t.read(8))
            print(t.read(8))
            t.close()
            break;
