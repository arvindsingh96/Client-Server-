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


#USING UDP FOR CONNECTION
port1 =5555
ipa = socket.gethostbyname(socket.gethostname())
server1 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server1.bind((ipa,port1))
while True:
    data, addr = server1.recvfrom(1024)
    print(data.decode())
    server1.sendto("hello i am server sending this to cilent using  udp ".encode(),addr)