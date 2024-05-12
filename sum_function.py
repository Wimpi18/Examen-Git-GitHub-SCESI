def sumTwoNumbers(num1, num2):
    return num1 + num2

def sumThreeNumbers(num1, num2, num3):
    return num1 + num2 + num3

def sumManyNumbers(a):
    x = 0
    for n in a:
        x = x + n
    return x

print(sumManyNumbers([1, 2, 3, 4]))