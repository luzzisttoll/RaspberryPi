from random import randrange

sum = 0
while True:
    randInt = randrange(10, 30)
    if randInt == 15 or randInt == 25:
        break
    sum += randInt
print(randInt)
print(sum)