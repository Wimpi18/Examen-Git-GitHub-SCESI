def sumTwoNumbers(num1, num2):
    return num1 + num2

def sumThreeNumbers(num1, num2, num3):
    return num1 + num2 + num3

def sumManyNumbers(a):
    res = 0
    for n in a:
        res = res + n
    return res

print(sumManyNumbers([1, 2, 3, 4]))