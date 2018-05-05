# -*- coding: utf-8 -*-
#!/usr/bin/python

from flask import Flask, render_template                                        
from flask_socketio import SocketIO, emit                                       

app = Flask(__name__)                                                           
app.config['SECRET_KEY'] = 'secret!'                                            
socketio = SocketIO(app)                                                        


@socketio.on('connect')                                                         
def connect():                                                                  
    emit('message', {'hello': "Hello"},broadcast=True)                                         


@app.route('/')                                                                 
def index():                                                                    
    return render_template('socket.html')  

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)	


if __name__ == '__main__':                                                      
    socketio.run(app, debug=True)