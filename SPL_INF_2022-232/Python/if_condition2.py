#Erstelle zwei Zufallszahl zwischen 0 und 100
from random import randrange
x = randrange(100)
y = randrange(100)
#Gib die Zufallszahl aus

print(x, y)

if x < y and x < 50:
	print("Zahl1 ist kleiner als Zahl2 und Mini")
if x < 30 or y < 30:
	print("Eine der beiden ist kleiner als 30")
if  x < 50 and y != 50:
	print("Erste Zahl klein, zweite kein 50iger")
