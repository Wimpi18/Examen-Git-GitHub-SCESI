def multiply(*numbers):
    result = 0
    for number in numbers:
        result *= number
    return result

def multiplyTwoNumbers(num1, num2):
    return num1 * num2

def multiplyManyNumbers(numbersArray):
    result = 1
    for number in numbersArray:
        result *= number
    return result