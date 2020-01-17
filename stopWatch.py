# stopwatch program

import time

# display instructions
print('Press ENTER to begin the stopwatch.\nPress ENTER again to pause the stopwatch\nPress CTRL-C to quit.')
input()
print('Started')
startTime = time.time()
lastTime = startTime
lapNumber = 1

# Track lap times
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print(f'Lap #{lapNumber}: {totalTime}({lapTime})', end='')
        lapNumber += 1
        lastTime = time.time()  # reset last lap
except KeyboardInterrupt:
    print('\nDone.')
