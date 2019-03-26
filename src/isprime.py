# 1. Take goal number through command line arguments
# 2. Create a list of integers between 2 and the goal number
# 3. Create a variable to maintain current index in the list
# 4. Get first integer in the list
# 5. Remove all integers in the list that are multiples of that integer
# 6. Increment index by 1
# 7. Make sure that current index exists in list
# 8. Rerun 5-7 until the index does not exist in the list

import sys


# cachedDictionaries = {}
# cachedPrimes = []

# with open('cachedDictionaries') as f:
#     cachedDictionaries = f.read()

# with open('cachedPrimes') as f:
#     cachedResults = f.read()


# def genNumbers(maxNum, minNum):
#     return [i for i in range(minNum, maxNum+1)]


# def genValues(maxNum):
#     return [False for i in range(0, maxNum)]


# def genDict(maxNum, minNum):
#     numbers = genNumbers(maxNum, minNum)
#     values = genValues(maxNum)
#     output = dict(zip(numbers, values))
#     print(output)
#     return [i for i in range(minNum, maxNum+1)]

def genList(maxNum, minNum):
    return [i for i in range(minNum, maxNum+1)]


def isPrime(prime, numToTest):
    return(numToTest % prime == 0)


def checkNumber(prime, inputList):
    workingList = inputList.copy()
    for item, index in enumerate(workingList):
        if isPrime(prime, item):
            workingList.remove(item)
    return [workingList, False]


def controller(prime, inputList, complete=False):
    print(prime)
    if not complete:
        print(*checkNumber(prime, inputList))
        controller(inputList[prime+1], *checkNumber(prime, inputList))
    if complete:
        return inputList


def sieve(maxNum, minNum=2):
    numbers = genList(maxNum, minNum)
    primes = controller(minNum, numbers)
    print(primes)
    # print(numbers)


sieve(10)
