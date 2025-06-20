import socket
port = 5050
ip = socket.gethostbyname(socket.gethostname())
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((ip,port))
client.send("hello from clinet. i am speaking to to server ".encode())
print(client.recv(1024).decode())
client.close()
