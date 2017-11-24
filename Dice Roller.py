import random
import time
times = int( input('Amount of rolls: '))
sides = int( input('Amount of sides: '))
wait = float( input('Seconds in between each roll: '))
timesSoFar = int( 0)
while timesSoFar != times:
    print (random.randint(1, sides))
    timesSoFar = timesSoFar+1
    time.sleep(wait)
