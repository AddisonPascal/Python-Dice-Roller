## Version 1.0.4
## By Addison Djatschenko

##########################################################

## Allows random numbers to be used in the file
import random
## Allows time in between rolls
import time
## User inputs
times = int( input('Amount of rolls: '))
while(True):
    sides = int( input('Amount of sides: '))
    if(sides > 3):
        break
    else:
        print("The dice needs to have at least four faces")
wait = float( input('Seconds in between each roll: '))
## Sets the dice rolls so far to zero
timesSoFar = int( 0)
## Runs until timesSoFar equals times
while timesSoFar != times:
    ## Displays current dice roll
    print (random.randint(1, sides))
    ## Increments timesSoFar
    timesSoFar = timesSoFar+1
    ## Waits for wait seconds
    time.sleep(wait)
while timesSoFar == timesSoFar:
    ## Stops program without exiting
    time.sleep(1)
