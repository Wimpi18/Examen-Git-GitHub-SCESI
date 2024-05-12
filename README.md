# Examen-Git-GitHub
## Sum function
I have two functions to sum many numbers.
```python
def sumTwoNumbers(num1, num2):
    return num1 + num2
```

The question is ...
> ***Is there a way to add multiple numbers in a single function?***

Te answer is yes
```python
def sumManyNumbers(numbersArray):
    res = 0
    for number in numbersArray:
        res = res + number
    return res
```

But the question is again ...
> ***It can improve?***

### This is my best sum function
```python
    def sum(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result
```

----------

# HELP
Mi función "sumManyNumbers" dejó de funcionar, no sé en que momento introduje el primer error. Por favor ayúdame a identificar el SHA del commit que introdujo el primer error.