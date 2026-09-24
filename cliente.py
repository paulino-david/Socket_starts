import socket

# sistema,nada,[IP_Ethernet,IP_Wifi]=socket.gethostbyname_ex(socket.gethostname())
IP_Servidor="192.168.1.189"
puerto=8000

#Crear el socket / la conexion del servidor
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.connect((IP_Servidor,puerto))

server.send("Hola mundo".encode("utf-8"))
print(server.recv(1024).decode('utf-8'))


#Public IP address: myip.is
