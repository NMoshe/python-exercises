# fizzbuzz using hash


def fizzBuzz(n):
    answer = []
    fizz = {3: 'Fizz', 5: 'Buzz'}

    for i in range(1, n + 1):
        strAnswer = ''
        for key in fizz:
            if i % key == 0:
                strAnswer += fizz[key]
        if not strAnswer:
            strAnswer += str(i)
        answer.append(strAnswer)
    return print(','.join(answer))


fizzBuzz(42)
