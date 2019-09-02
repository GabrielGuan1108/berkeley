def make_counter():
    """Return a counter function.

    >>> c = make_counter()
    >>> c('a')
    1
    >>> c('a')
    2
    >>> c('b')
    1
    >>> c('a')
    3
    >>> c2 = make_counter()
    >>> c2('b')
    1
    >>> c2('b')
    2
    >>> c('b') + c2('b')
    5
    """
    xxx = {}
    def counter(a):
        if a not in xxx:
            xxx[a] = 0

        xxx[a] += 1
        return xxx[a]
    return counter


    "*** YOUR CODE HERE ***"

def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    """
    xxx = 0
    yyy = 1
    count = 0
    def fib():
        nonlocal xxx, yyy, count
        if count == 0:
            count += 1
            return 0
        if count ==1:
            count += 1
            return 1

        xxx = xxx + yyy
        xxx, yyy = yyy, xxx
        return yyy
    return fib
    "*** YOUR CODE HERE ***"

def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    balance, p = balance, password
    attempts = []
    count = 0
    def withdraw(amount, password):
        nonlocal balance, p, attempts, count
        if count < 3:

            if password == p:
                if amount > balance:
                    return 'Insufficient funds'
                balance = balance - amount
                return balance
            else:
                attempts += [password]
                count += 1

                return 'Incorrect password'
        else:
            a = "Your account is locked. Attempts: " + str(attempts)
            return a
    return withdraw


    "*** YOUR CODE HERE ***"

def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    s = withdraw(0, old_password)
    if type(s) == str:
        return s
    else:


        def new_withdraw(amount, password):

            if password == new_password:
                return withdraw(amount, old_password)
            else:
                return withdraw(amount, password)
        return new_withdraw

    "*** YOUR CODE HERE ***"

def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(tree(2, [tree(4, [tree(6)])]))
    [2, 4, 6]
    """
    b = branches(t)
    if b == []:
        return [t[0]]
    list = []
    def helper(p):
        nonlocal list
        if is_leaf(p):
            #print(p, 'is leaf', p)
            list.append(p[0])
            return 1
        else:
            bp = branches(p)
            #print('bp: ',bp)
            #print(p)
            list.append(p[0])
            #print(p, 'is branch', p)
            for i in bp:
                #print(i)
                #print('list:', list)
                helper(i)
            return list
    return helper(t)

    "*** YOUR CODE HERE ***"

class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.current_year.

    >>> mint = Mint()
    >>> mint.year
    2017
    >>> dime = mint.create(Dime)
    >>> dime.year
    2017
    >>> Mint.current_year = 2100  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2017
    >>> nickel.worth()  # 5 cents + (85 - 50 years)
    38
    >>> mint.update()   # The mint's year is updated to 2100
    >>> Mint.current_year = 2175     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (160 - 50 years)
    118
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (160 - 50 years)
    128

    """
    current_year = 2017

    def __init__(self):
        self.update()

    def create(self, kind):
        return kind(self.year)


        #p_y = Mint.current_year - self.year
        #if p_y > 50:
        #    self.worth = kind.worth(self) + p_y
        #else:
        #    self.worth = kind.worth(self)

        "*** YOUR CODE HERE ***"

    def update(self):
        #print('update')
        self.year = Mint.current_year
        "*** YOUR CODE HERE ***"

class Coin:
    def __init__(self, year):
        self.year = year
        self.worth = self.worth()

    def worth(self):
        p_y = Mint.current_year - self.year - 50
        print(p_y)
        if p_y > 0:
            #print(Nickel.cents + p_y)
            return self.cents + p_y
            
        else:
            #print(2)
            return self.cents



        "*** YOUR CODE HERE ***"

class Nickel(Coin):
    cents = 5
    


class Dime(Coin):
    cents = 10
    

## Tree ADT ##

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])
