port1=5555
ipa = socket.gethostbyname(socket.gethostname())
cilent1 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
cilent1.sendto("I am  cilent sending to server  using udp ".encode(),(ipa,port1))
data ,addr = cilent1.recvfrom(1024)
print(data.decode())
