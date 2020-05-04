from flask import Flask, render_template
from video import startVideo
import tank

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alex')
def alex():
    return render_template('alex.html')

@app.route('/forward/<int:distance>')
def forward(distance):
    tank.moveforward(distance)
    return ''

@app.route('/backward/<int:distance>')
def backward(distance):
    tank.movebackward(distance)
    return ''

@app.route('/left/<int:angle>')
def left(angle):
    tank.turnleft(angle)
    return ''

@app.route('/right/<int:angle>')
def right(angle):
    tank.turnright(angle)
    return ''

@app.route('/m1up/<int:distance>')
def m1up(distance):
    tank.motor1forward(distance)
    return ''

@app.route('/m1down/<int:distance>')
def m1down(distance):
    tank.motor1backward(distance)
    return ''

#startVideo()
