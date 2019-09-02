"""Lab 1: Expressions and Control Structures"""

# Q3
def both_positive(x, y):
    """Returns True if both x and y are positive.

    >>> both_positive(-1, 1)
    False
    >>> both_positive(1, 1)
    True
    """
    if ((x >0) and (y >0)):
        return True
    else:
        return False

# Q4
def sum_digits(n):
    if (n<10):
        return n
    else:
        i = 1
        b = 0
        while (1==1):
            a = 10**i
            c = 10**(i-1)
            if (n >= a):
                b = b + (n%(10**i))/(10**(i-1))
                b = int(b)
                n = n - n%(10**i)
                i += 1
            elif(n < a):
                a = a/10
                b = b + n/a
                b = int(b)
                break
    b = int(b)
    return b

                
            
            
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    "*** YOUR CODE HERE ***"
