#!/usr/bin/env python3
# Network Programming in Python: The Basics
# UDP-клиент и сервер на localhost

import argparse
import socket
import time
from datetime import datetime

MAX_BYTES = 65535


def server(port):
    """UDP-сервер: принимает сообщение и отвечает клиенту."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("127.0.0.1", port))
    print("Listening at {}".format(sock.getsockname()))

    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode("ascii")
        print("The client at {} says {!r}".format(address, text))

        time.sleep(500)

        text = "Your data was {} bytes long".format(len(data))
        data = text.encode("ascii")
        sock.sendto(data, address)


def client(port):
    """UDP-клиент: отправляет время и ждёт ответа."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = "The time is {}".format(datetime.now())
    data = text.encode("ascii")

    sock.sendto(data, ("127.0.0.1", port))
    print("The OS assigned me the address {}".format(sock.getsockname()))

    data, address = sock.recvfrom(MAX_BYTES)  # Осторожно! См. главу 2
    text = data.decode("ascii")
    print("The server {} replied {!r}".format(address, text))


if __name__ == "__main__":
    choices = {"client": client, "server": server}
    parser = argparse.ArgumentParser(description="Send and receive UDP locally")
    parser.add_argument("role", choices=choices, help="which role to play")
    parser.add_argument(
        "-p", metavar="PORT", type=int, default=1060, help="UDP port (default 1060)"
    )
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)
