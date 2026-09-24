import socket
from dotenv import load_dotenv,set_key

load_dotenv()

#La definicion de como y para que sera el sevidor
#AF_INET: Para decir que es para internet
#SOCK_STREAM: Para decir que la comunicacion sera de protocolo TCP de transporte
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Para crear un nuevo socket; en este caso es un socket de tipo TCP/IP para internet

# Para obtener los datos de red del sistema; nombre, IP de cable ethernet y la IP Wifi que viene dentro de una tupla
nombreSistema,nada,[IP_Ethernet,IP_Wifi]=socket.gethostbyname_ex(socket.gethostname())
#Para definir el puerto del socket
port=8000

#Para definir/asignar la IP del servidor y el puerto del socket; 
server.bind((IP_Wifi,port))

#Para guardar la IP y el puerto en el archivo .env
set_key(".env","IP_Wifi",IP_Wifi)
set_key(".env","Port",str(port))

# Para indicar cuantas conexiones permite (limite maximo)
server.listen(5)

#Es para activar la conexion del servidor definitivamente hasta que sea false
while True:
    #Para aceptar la conexion del cliente y guardar el socket de comunicacion y la IP del cliente
    comunication_socket,IP_cliente=server.accept()
    print("Conected to {}".format(IP_cliente))

# Para recibir el mensaje del cliente y decodificarlo a UTF-8 porque el servidor no actua como cliente y no puede recibir bytes, sino que recibe un mensaje en texto plano
# Y porque wl servidor no puede actuar sin que el cliente le envie un mensaje, por eso se hace un recv() para recibir el mensaje del cliente
    mensaje_from_client=comunication_socket.recv(1024).decode("utf-8")
    print("Message from client {}".format(mensaje_from_client))

#Para responderle al cliente con un mensaje de texto plano codificado a UTF-8 porque el cliente no actua como servidor y no puede recibir un mensaje en texto plano, sino que recibe bytes
    comunication_socket.send("Got your connection".encode("utf-8"))
#Para cerrar la conexion del socket de comunicacion con el cliente y que el servidor pueda seguir escuchando a otros clientes
    comunication_socket.close()
    print("Connection with {} ended!".format(IP_cliente))

    

