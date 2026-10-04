import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto("FAKE".encode("ascii"), ("127.0.0.1", 65525))
