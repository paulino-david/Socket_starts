import socket

#La definicion de como y para que sera el sevidor
#AF_INET: Para decir que es para internet
#SOCK_STREAM: Para decir que la comunicacion sera de protocolo TCP de transporte
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Para crear un nuevo socket; para crear conecciones

# Para obtener los datos de red del dispositivo; nombre, IP de cable ethernet y la IP Wifi que viene dentro de una tupla
nombreSistema,nada,[IP_Ethernet,IP_Wifi]=socket.gethostbyname_ex(socket.gethostname())
#Para definir el puerto del socket
port=8000

server.bind((IP_Wifi,port))

# Para indicar cuantas conexiones permite (limite maximo)
server.listen(5)

#Es para activar la conexion del servidor definitivamente hasta que sea false
while True:
    comunication_socket,IP_cliente=server.accept()
    print("Conected to {}".format(IP_cliente))
    mensaje_from_client=comunication_socket.recv(1024).decode("utf-8")
    print("Message from client {}".format(mensaje_from_client))
    comunication_socket.send("Got your connection".encode("utf-8"))
    comunication_socket.close()
    print("Connection with {} ended!".format(IP_cliente))

    

