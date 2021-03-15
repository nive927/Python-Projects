# Higher order functions

def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 // n2


def calculator(n1, n2, func):
    return func(n1,n2)


print(calculator(10, 10, add))
print(calculator(10, 10, sub))
print(calculator(10, 10, mul))
print(calculator(10, 10, div))