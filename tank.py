import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

GPIO.setup(25,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

GPIO.setup(11,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)

def moveforward(distance):
    move2(distance / 28,23,17,1)

def movebackward(duration):
    move2(duration / 28,22,27,0.95)

def turnleft(degrees):
    move(degrees / 180 * 1,27,23)
 
def turnright(degrees):
    move(degrees / 180 * 1,17,22)

def motor1forward(distance):
    motor(distance / 100,25)

def motor2forward(distance):
    motor(distance / 100,10)

def motor1backward(distance):
    motor(distance / 100,24)

def motor2backward(distance):
    motor(distance / 100,11)

def move(duration,pin1,pin2):
    GPIO.output(pin1,GPIO.HIGH)
    GPIO.output(pin2,GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(pin1,GPIO.LOW)
    GPIO.output(pin2,GPIO.LOW)

def move2(duration,pin1,pin2,ratio):
    GPIO.output(pin1,GPIO.HIGH)
    timesofar=0
    while timesofar < duration:
        GPIO.output(pin2,GPIO.HIGH)
        time.sleep(ratio*0.1)
        GPIO.output(pin2,GPIO.LOW)
        time.sleep(0.1-ratio*0.1)
        timesofar=timesofar+0.1
    GPIO.output(pin1,GPIO.LOW)

def motor(duration,pin):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(pin,GPIO.LOW)
    
    










