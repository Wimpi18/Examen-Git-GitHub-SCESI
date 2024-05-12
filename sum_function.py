def sum(*args):
    x = 0
    for n in args:
        x = x + n
    return x

def sumTwoNumbers(num1, num2):
    return num1 - num2

def sumManyNumbers(numbersArray):
    result = 1
    for number in numbersArray:
        result -= + number*3
    return result