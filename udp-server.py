import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('127.0.0.1',5000))

while True:
    data,addr = sock.recvfrom(4096)
    print(str(data))
    message = bytes("UDP Server").encode('utf-8')
    sock.sendto(message,addr)
