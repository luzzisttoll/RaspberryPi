import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
while True:
    userInput = int(input("Geben Sie 1(grün), 2(gelb), 3(rot) ein für Licht und 4 für alle aus \n"))
    if userInput == 1:
        GPIO.output(3,True)

    elif userInput == 2:
        GPIO.output(5,True)
    
    elif userInput == 3:
        GPIO.output(7,True)

    elif userInput == 4:
        GPIO.output(3,False)
        GPIO.output(5,False)
        GPIO.output(7,False)
    else:
        print("Geben Sie e oder a ein")
        
