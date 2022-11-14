from tkinter import E
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)

pin = [3, 5, 7]
i = 0

while True:
    input("Press enter")
    GPIO.output(3, False)
    GPIO.output(5, False)
    GPIO.output(7, False)
    GPIO.output(pin[i], True)
    i+=1
    if i > 2:
        i = 0