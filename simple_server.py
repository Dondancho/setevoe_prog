import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(('127.0.0.1', 1060))

print("Жду сообщение...")

data, addr = sock.recvfrom(1024)
print(f"Пришло от {addr}: {data.decode()}")

sock.close()
