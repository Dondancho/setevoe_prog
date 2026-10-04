from flask import Flask, render_template
import socket

app = Flask(__name__)

ROBOT_IP = '127.0.0.1'
ROBOT_PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cmd/<command>')
def cmd(command):
    if command not in ('forward', 'back', 'left', 'right', 'stop'):
        return 'Unknown command'

    sock.sendto(command.encode('ascii'), (ROBOT_IP, ROBOT_PORT))

    # Ждём ответ от робота
    sock.settimeout(0.5)
    try:
        data, _ = sock.recvfrom(1024)
        return data.decode('ascii')
    except socket.timeout:
        return 'No reply from robot'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)