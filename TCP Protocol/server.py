import socket 
port = 5050
ip = socket.gethostbyname(socket.gethostname())#it will get my ip address  
server= socket.socket(socket.AF_INET ,socket.SOCK_STREAM)
#AP_INET it tell to commuciate on ipv4 addre , SOCK_STREAM means use tcp model for commuction
server.bind((ip,port))
server.listen(5)
print(f"server listening on {ip}:{port}")
while True:
    client, addr =server.accept()
    print(f"connection established with {addr}")
    print(client.recv(1024).decode())
    client.send("Hello from server".encode())
    client.close()
