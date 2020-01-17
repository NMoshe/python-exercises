# countdown script

import time
import subprocess
import sys

print('How long should the countdown be?\nEnter the length in seconds:')
try:
    timeLeft = int(input())
except ValueError:
    print('Please enter a valid number.')
    sys.exit()
while timeLeft > 0:
    print(str(timeLeft))
    time.sleep(1)
    timeLeft = timeLeft - 1

subprocess.Popen(['start', 'coin.wav'], shell=True)
