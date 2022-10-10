sum = 500
while True:
    print("Bitte geben Sie ein: \n 1. Einzahlen \n 2. Abheben \n 3. Kontostand \n 4. Beenden")
    eingabe = int(input())
    if eingabe == 1:
        print("Geben Sie die Summe ein, die Sie einzahlen möchten")
        inputEinzahlen = int(input())
        sum += inputEinzahlen
    elif eingabe == 2:
        print("Was für eine Summe möchten Sie auszahlen?")
        inputAuszahlen = int(input())
        if sum - inputAuszahlen < 0:
            print("Sie haben nicht genug Geld auf Ihrem Konto für die Auszahlung")
        else:
            sum -= inputAuszahlen
    elif eingabe == 3:
        print(sum)
    elif eingabe == 4:
        break
    else:
        print("Ihre Eingabe ist ungültig")

        