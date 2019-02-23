import random

why = 'asdfghj'

def generateRandomArray():
    arrSize = int(input('Введите число '))
    arr = []

    for i in range(arrSize):
        arr.append(random.randint(-100, 100))

    print(arr)
