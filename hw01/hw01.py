""" Homework 1: Control """

# Q1
from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = a-b
    else:
        f = a+b
    return f

# Q2
def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    s = min(a,b,c)
    answer = a*a + b*b + c*c - s*s
    return answer

# Q3
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    i= 1
    factor = 0
    while (i != n):
        if n%i == 0:
            factor = i
        i += 1
    return factor
                
            

# Q4
def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> result = with_if_statement()
    2
    >>> print(result)
    None
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    """
    >>> result = with_if_function()
    1
    2
    >>> print(result)
    None
    """
    return if_function(c(), t(), f())

def c():
    return None
    "*** YOUR CODE HERE ***"

def t():
    
    print(1)
    return None
    "*** YOUR CODE HERE ***"

def f():
    print(2)
    return None
    "*** YOUR CODE HERE ***"
    print(with_if_statement())

# Q5
def hailstone(n):
    i=0
  

    int(n)
    print(n)
    while (n != 1):
        if (n%2 == 0):
            n = n/2
            n = int(n)
            print(n)
            i += 1
        elif (n%2 == 1):
            n = 3*n +1
            n = int(n)
            print(n)
            i += 1
    i += 1
    return i
