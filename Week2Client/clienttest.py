import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.0.130', 8080))
client.send("I am CLIENT\n".encode())
from_server = client.recv(4096).decode()
while(1):
    client.send("I am CLIENT\n".encode())
client.close()
print(from_server)
