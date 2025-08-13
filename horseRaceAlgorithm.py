import random
import time

horses = []
hurdle = []

def race(horses, hurdle):
    negCount = 0
    while 10 not in hurdle:
        # if negative 3 times in a row the next horse will die
        if negCount == 3:
            pass
        # determines whether a horse jumps forward or falls back
        posOrNeg = random.randint(0, 1)
        if posOrNeg == 1:
            nextHurdle = random.randint(0, len(horses)-1)
            hurdle[nextHurdle] += 1
            print(f"{horses[nextHurdle]} has jumped to {hurdle[nextHurdle]}!")
        else:
            negCount += 1

            secondChance = random.randint(0, 2)
            if secondChance == 0 or secondChance == 1:
                nextHurdle = random.randint(0, len(horses)-1)
                hurdle[nextHurdle] -= 1
                print(f"{horses[nextHurdle]} has fallen back to {hurdle[nextHurdle]}!")
    
    winner = None
    for i in range(0, len(horses)):
        if hurdle[i] == 10:
            winner = horses[i]
    
    print(horses)
    print(hurdle)

    return winner



numOfHorses = int(input("Enter the number of horses: "))
for i in range(numOfHorses):
    horse = input(f"Enter the name of horse {i + 1}: ")
    horses.append(horse)
    hurdle.append(0)

print(horses)
print(hurdle)

print(race(horses, hurdle))

