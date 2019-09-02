"""Optional questions for Lab 1"""

# While Loops

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 0)
    1
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    """
    "*** YOUR CODE HERE ***"
    if (k!=0):
        
        i = 1
        a = n
        
    else:
        
        return 1
    while(i<k):
        
        n = n*(a-i)
        i += 1
        
    return n
        
        

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    if (n<10):
        return False
    else:
        i = 1
        eight = 0
        while (1==1):
            a = 10**i
            if (n >= a):
                b = int((n%(10**i))/(10**(i-1))) #把每一位上的数取出来
                n = n - n%(10**i)
                    
                
            elif(n <= a):
                b = i-1
                a = 10**b
              
                s = (n/a)*10
                
                
                if (n/a == 8):
                    eight += 1
                break
            if (b==8):
                eight += 1
                i += 1
               
            else:
                eight = 0
                i += 1
            if (eight == 2):
                break
            
                    
        if (eight == 2):
            return True
        else:
            return False


