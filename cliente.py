import socket
import os
from dotenv import load_dotenv
load_dotenv()

sistema,nada,[IP_Ethernet,IP_Wifi]=socket.gethostbyname_ex(socket.gethostname())

IP_Servidor=os.getenv("IP_Wifi")
puerto=os.getenv("Port")

#Crear el socket / la conexion del servidor
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.connect((IP_Servidor,int(puerto)))
 
server.send("Hola mundo soy {}".format("el sistema "+sistema if sistema!=socket.gethostname() else "mi propio sistema y me estoy cominicando conmigo mismo").encode("utf-8"))
print(server.recv(1024).decode('utf-8'))


#Public IP address: myip.is
