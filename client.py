import socket
port = 5050
ip = socket.gethostbyname(socket.gethostname())
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((ip,port))
client.send("hello from clinet. i am speaking to to server ".encode())
print(client.recv(1024).decode())
client.close()


# USING UDP FOR CONNECTION
port1=5555
ipa = socket.gethostbyname(socket.gethostname())
cilent1 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
cilent1.sendto("I am  cilent sending to server  using udp ".encode(),(ipa,port1))
data ,addr = cilent1.recvfrom(1024)
print(data.decode())