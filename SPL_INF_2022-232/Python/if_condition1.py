#Erstelle eine Zufallszahl zwischen 0 und 100
from random import randrange
i = randrange(100)

#Gib die Zufallszahl aus

print(i)


if i < 20:
	print("Mini")
elif 20 <= i <= 50:
	print("Medium")
elif i > 50:
	print("Large")
