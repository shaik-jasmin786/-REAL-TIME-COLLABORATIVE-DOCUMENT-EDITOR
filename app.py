from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('text_change')
def handle_text_change(data):
    emit('update_text', data, broadcast=True, include_self=False)

if __name__ == '__main__':
    socketio.run(app, debug=True)