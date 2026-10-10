import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 9999))
print('Robot emulator listening on port 9999...')

x, y = 0.0, 0.0
STEP = 0.5

while True:
    data, addr = sock.recvfrom(1024)
    cmd = data.decode('ascii')

    if cmd == 'forward':
        y += STEP
    elif cmd == 'back':
        y -= STEP
    elif cmd == 'left':
        x -= STEP
    elif cmd == 'right':
        x += STEP
    elif cmd == 'stop':
        pass

    print(f'[{cmd}] -> position: x={x:.1f}, y={y:.1f}')

    reply = f'x={x:.1f},y={y:.1f}'
    sock.sendto(reply.encode('ascii'), addr)