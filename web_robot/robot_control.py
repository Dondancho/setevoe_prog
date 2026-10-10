from gevent import monkey
monkey.patch_all()

from flask import Flask, render_template
from flask_socketio import SocketIO
import socket
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'robot-secret'
socketio = SocketIO(app, cors_allowed_origins='*', async_mode='gevent')

ROBOT_IP = '127.0.0.1'
ROBOT_PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(0.3)

robot_state = {'x': 0.0, 'y': 0.0, 'connected': False}


@app.route('/')
def index():
    return render_template('index.html')


def send_command(cmd):
    try:
        sock.sendto(cmd.encode('ascii'), (ROBOT_IP, ROBOT_PORT))
        data, _ = sock.recvfrom(1024)
        return data.decode('ascii')
    except socket.timeout:
        return None


@socketio.on('command')
def handle_command(data):
    cmd = data.get('cmd')
    if cmd not in ('forward', 'back', 'left', 'right', 'stop'):
        return
    reply = send_command(cmd)
    if reply:
        try:
            parts = dict(p.split('=') for p in reply.split(','))
            robot_state['x'] = float(parts['x'])
            robot_state['y'] = float(parts['y'])
            robot_state['connected'] = True
        except (ValueError, KeyError):
            pass
        socketio.emit('state', robot_state)


def telemetry_loop():
    while True:
        reply = send_command('ping')
        if reply:
            try:
                parts = dict(p.split('=') for p in reply.split(','))
                robot_state['x'] = float(parts['x'])
                robot_state['y'] = float(parts['y'])
                robot_state['connected'] = True
            except (ValueError, KeyError):
                pass
        else:
            robot_state['connected'] = False
        socketio.emit('state', robot_state)
        time.sleep(0.2)


if __name__ == '__main__':
    socketio.start_background_task(telemetry_loop)
    socketio.run(app, host='0.0.0.0', port=5000, debug=False)