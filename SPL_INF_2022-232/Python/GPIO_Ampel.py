import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
i = 0
while True:
    i+=1
    GPIO.output(3,False)
    GPIO.output(5,False)
    GPIO.output(7,False)
    if i == 1:
        GPIO.output(3,True)

    elif i == 2:
        GPIO.output(5,True)
    
    elif i == 3:
        GPIO.output(7,True)
    if i > 2:
        i = 0