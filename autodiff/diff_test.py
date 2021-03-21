import numpy as np
from diff_object import DiffObject


def poly1(x):
    return x - 2


def poly2(x):
    return -x ** 2


def poly3(x):
    return 2 * x ** 2 + 3 * x


def poly4(x):
    return 3 * x ** 4 - 3 * x ** 2 + x - 2


def quotient1(x):
    return 1 / x


def quotient2(x):
    return (x ** 2 + 1) / (x - 1)


def irrational1(x):
    return x ** 0.5


def irrational2(x):
    return 1 / (x ** 2 - 1) ** (1 / 3)


def mySin(x):
    return x - x ** 3 / 6 + x ** 5 / 120


def myCos(x):
    return 1 - x ** 2 / 2 + x ** 4 / 24

def myTan(x):
    return mySin(x) / myCos(x)

def exp(x):
    return np.e ** x

def sigmoid(x):
    return 1 / (1 + np.e ** (-x))

x = DiffObject(2)

print(poly1(x))
print(poly2(x))
print(poly3(x))
print(poly4(x))
print(quotient1(x))
print(quotient2(x))
print(irrational1(x))
print(irrational2(x))

y = DiffObject(0.1)

print(mySin(y))
print(myCos(y))
print(myTan(y))

print(exp(x))
print(sigmoid(x))

def complicated1(x):
    return (-x ** 2 + 1) * mySin(x)

def complicated2(x):
    return exp(x) * myCos(x)

print(complicated1(y))
print(complicated2(y))

# Compositions

print(exp(myCos(y)))
print(mySin(myCos(y)))
