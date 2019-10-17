import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('172.20.10.3', 8080))
client.send("I am CLIENT\n".encode())
from_server = client.recv(4096).decode()
client.close()
print(from_server)
