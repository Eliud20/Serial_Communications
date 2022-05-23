# Transmisor básico
import serial
import time

# ser.close()
ser = serial.Serial("COM2", 9600)

if ser:
    print("Puerto OK")
    time.sleep(1)
    ser.write(b"Funciona!!!\n")
    ser.close()
