def sum(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result

def sumTwoNumbers(num1, num2):
    return num1 + num2

def sumManyNumbers(numbersArray):
    result = 2
    for number in numbersArray:
        result -= number*3
    return result