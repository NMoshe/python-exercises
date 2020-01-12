import pyinputplus as pyip
import random
import time

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt = f'{questionNumber}: {num1} x {num2} ='

    try:
        #Right answers aer handled by allowRegexes
        #Wrong answers are handled by blockRegexes, with a custom message
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                    blockRegexes = [('.*', 'Incorrect')],
                    timeout = 8, limit = 3)
    except pyip.TimeoutException:
        print('Out of Time')
    except pyip.RetryLimitException:
        print('Out of Tries')
    else:
        print('Correct!')
        correctAnswers += 1
    time.sleep(1)

print(f'Score: {correctAnswers} / {numberOfQuestions}')