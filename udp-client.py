import socket
client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

msg = "Hello UDP Server"
client_socket.sendto(msg.encode("utf-8"),('127.0.0.1',5000))
data,addr = client_socket.recvfrom(4096)
print("Server says")
print(str(data))
client_socket.close()

