import random
import time

horses = []
hurdle = []
stayCount = []

# List to keep track of whether each horse is alive
horseAlive = []

# List to keep track of dead horses
dead = []

# toggle for is they want the deaths of horses or not
deaths = False

def race(horses, hurdle, stayCount, horseAlive, deaths):
    # the game lasts until one horse reaches 10 hurdles (need to change so all horses need to reach 10 hurdles)
    # also want to add mutliple races, e.g short ditance, middle distance, marathon
    while 10 not in hurdle:

        # determines whether a horse jumps forward or falls back
        posOrNeg = random.randint(0, 1)
        nextHurdle = random.randint(0, len(horses)-1)
        if horseAlive[nextHurdle] == True:
            # time setting to gamify it more
            # add total race time
            # add each horse's time
            time.sleep(0.25)

            if posOrNeg == 1:
                hurdle[nextHurdle] += 1
                #resets death counter if deaths are on as not idle anymore
                if deaths == True:
                    stayCount[nextHurdle] = 0
                # prints the horse that has moved forward
                print(f"{horses[nextHurdle]} has jumped to {hurdle[nextHurdle]}!")
            else:
                secondChance = random.randint(0, 2)
                if secondChance == 0 or secondChance == 1:
                    # can't go back if already at hurdle 0
                    if hurdle[nextHurdle] > 0:
                        hurdle[nextHurdle] -= 1
                    else:
                        print(f"Horse {horses[nextHurdle]} is already at the start line and cannot fall back!")
                    #resets death counter if deaths are on as not idle anymore
                    if deaths == True:
                        stayCount[nextHurdle] = 0
                    # prints the horse that has moved back
                    print(f"{horses[nextHurdle]} has fallen back to {hurdle[nextHurdle]}!")
                else:
                    print(f"Horse {horses[nextHurdle]} has stayed in the same position {hurdle[nextHurdle]}!")
                    # increments the idle count for the horse if deaths are on
                    if deaths == True:
                        stayCount[nextHurdle] += 1
                    # check if the horse has been idle for 3 turns, if so it dies and doesn't move anymore
                    if stayCount[nextHurdle] >= 3:
                        horseAlive[nextHurdle] = False
                        print(f"Horse {horses[nextHurdle]} has died!")

    # insertion sort to list the order of winners
    horseRank = hurdle.copy()
    nameRank = horses.copy()

    for i in range(1, len(horses)):
        key = horseRank[i]
        keyTwo = nameRank[i]
        j = i - 1
        while j >= 0 and horseRank[j] < key:
            horseRank[j + 1] = horseRank[j]
            nameRank[j + 1] = nameRank[j]
            j -= 1
        horseRank[j + 1] = key
        nameRank[j + 1] = keyTwo


    return horses, hurdle, stayCount, horseAlive, horseRank, nameRank



numOfHorses = int(input("Enter the number of horses: "))
for i in range(numOfHorses):
    horse = input(f"Enter the name of horse {i + 1}: ")

    # sets up teh different arrays fo rthe horse names, the hurdle they are on, their idle count and whether they are alive
    horses.append(horse)
    hurdle.append(0)
    stayCount.append(0)
    horseAlive.append(True)

# asks the user if they want to see the deaths of horses
wantDeaths = str(input("Do you want to see the deaths of horses? (yes/no): ")).lower()
if wantDeaths == "yes":
    deaths = True
else:
    deaths = False

# prints the initial state of the horses, hurdles, stay count and whether they are alive
print(horses)
print(hurdle)
print(stayCount)
print(horseAlive)

horses, hurdle, stayCount, horseAlive, horseRank, nameRank= race(horses, hurdle, stayCount, horseAlive, deaths)

# prints the final state of the horses, hurdles, stay count and whether they are alive
print(horses)
print(hurdle)
print(stayCount)
print(horseAlive)

# prints the final results
for i in range(len(horseRank)):
    if horseAlive[i]:
        print(f"{nameRank[i]} has finished in position {i + 1} with a distance of {horseRank[i]} hurdles!")
    else:
        dead.append(nameRank[i])
for i in range(len(dead)):
    print(f"{dead[i]} didn't make it")
