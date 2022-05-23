# RX.- Recibe un sólo caracter
import serial
import time

try:
    ser = serial.Serial("COM2", 9600)
except:
    print("Error!")
    ser.close()

time.sleep(1)

while True:
    if ser.inWaiting() != 0:
        break

print(ser.read())

ser.close()

print("Fin del programa")
