# check runtime of function

import time

number = 100000


def calculate():
    start = 1
    for i in range(1, number):
        start = start * i
    return start


startTime = time.ctime()
calc = calculate()
endTime = time.ctime()

print(f'The result is {len(str(calc))} digits long')
print(f'The calculation started at {startTime}')
print(f'The calculation ended at {endTime}')
