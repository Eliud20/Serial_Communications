import socket
import time as t
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("192.168.0.36", 2021))

while True:
    a = input("Teclea el mensaje: ")

    if a == "Adios":
        b = a.encode()
        s.send(b)
        break
    else:
        b = a.encode()
        s.send(b)
        mensaje = s.recv(64)
        print("Servidor: ", mensaje.decode())

print("Desconectando en 3...")
for i in range(2, 0, -1):
    print(i, "...")
    t.sleep(1)


print("Desconectado")
s.close()
print("Fin de programa")
