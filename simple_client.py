import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = b"Hello, UDP!"
sock.sendto(msg, ("127.0.0.1", 1060))
print("Отправил:", msg.decode())

sock.close()
