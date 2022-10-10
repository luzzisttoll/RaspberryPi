from random import randrange

wuerfelanzahl = 1
sumUser = 0
sumComputer = 0
print("Hier spielen Sie ein Würfelspiel gegen den Computer. Sie müssen 6 mal würfeln und wenn die Augensumme höher ist, als die vom Computer, haben Sie gewonnen.")
while wuerfelanzahl <= 6:
    wuerfelanzahl += 1
    print("Drücken Sie zum Würfeln die 1")
    userInput = int(input())
    if userInput == 1:
        randomUser = randrange(1, 7)
        sumUser += randomUser
        randomComputer = randrange(1, 7)
        sumComputer += randomComputer
    else:
        print("Bitte geben Sie die 1 ein")
    
if sumUser < sumComputer:
    print("Der Computer hat gewonnen!! Der Punktestand des Computers lautet ", sumComputer, "und ihrer lautet ", sumUser)
elif sumUser > sumComputer:
    print("Sie haben gewonnen!! Ihr Punktestand lautet ", sumUser, " und der des Computers lautet", sumComputer)
else:
    print("Sie haben gleich viel Punkte wie der Computer. Unentschieden!! Eure Punktestände lauten ", sumUser)
        
    



