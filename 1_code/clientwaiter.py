# -*- coding: utf-8 -*-
#!/usr/bin/python
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

async_mode = None

#initialization
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,async_mode=async_mode)
#ends 

@socketio.on('my event')                          # Decorator to catch an event called "my event": sends "I'm connected"
def test_message(message):                        # test_message() is the event callback function.
    emit('my response', {'data': 'got it!'})      # Trigger a new event called "my response" 
                                                  # that can be caught by another callback later in the program.
 

@app.route('/')
def clientwaiter():
    return render_template('clientwaiter.html',async_mode=socketio.async_mode)

	

if __name__ == '__main__':
    socketio.run(app,debug=True)