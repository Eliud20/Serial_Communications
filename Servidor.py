import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.0.36", 2021))
s.listen(5)

(sc, addrC) = s.accept()
print("IP del cliente: ", addrC)

while True:
    mensaje = sc.recv(64)
    print("Cliente: ", mensaje.decode())

    if(mensaje.decode() == 'Adios'):
        men = "Mensaje Recibido, Adios"
        sc.send(men.encode())
        break
    else:
        men = input("Teclee un mensaje: ")
        sc.send(men.encode())

print("Desconectado")
sc.close()
s.close()
print("Fin de programa")
