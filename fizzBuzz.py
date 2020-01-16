# fizzbuzzjazz
print("Enter a Number: ")
userNum = int(input())


def fizzBuzz(userNum):
    numList = []
    for n in range(1, userNum + 1):
        fizz = (n % 3 == 0)
        buzz = (n % 5 == 0)
        jazz = (n % 7 == 0)

        numString = ""

        if fizz:
            numString += 'Fizz'
        if buzz:
            numString += 'Buzz'
        if jazz:
            numString += 'Jazz'
        if not numString:
            numString = str(n)

        numList.append(numString)
    return print(" ".join(numList))


fizzBuzz(userNum)
