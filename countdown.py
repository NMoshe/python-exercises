# countdown script

import time
import subprocess

print('How long should the countdown be?\nEnter the length in seconds:')
timeLeft = int(input())
while timeLeft > 0:
    print(str(timeLeft))
    time.sleep(1)
    timeLeft = timeLeft - 1

subprocess.Popen(['start', 'coin.wav'], shell=True)
