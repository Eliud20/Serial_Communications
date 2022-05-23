#RX.- Recibe varios caracteres
import serial,time

ser = serial.Serial("COM2",9600)
time.sleep(1)

while ser.inWaiting() == 0:
    continue

numCar = ser.inWaiting()

print("Número de caractéres: ",numCar)

for elem in range(numCar):
    car = ser.read()
    car = str(car)[2:3]
    if car != "\\":
        print(car,end="")

ser.close()

print("\nFin del programa")