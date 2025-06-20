port1 =5555
ipa = socket.gethostbyname(socket.gethostname())
server1 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server1.bind((ipa,port1))
while True:
    data, addr = server1.recvfrom(1024)
    print(data.decode())
    server1.sendto("hello i am server sending this to cilent using  udp ".encode(),addr)
