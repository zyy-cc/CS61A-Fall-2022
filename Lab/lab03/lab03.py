def remove(n,digit):
    """
    >>>remove(231,3)
    21
    >>>remove(243132,2)
    remove(243132,2)
    """
    kept,digits = 0,0
    while n > 0:
        n,last=n//10,n%10
        if last != digit:
            kept += last * (10 ** digits)
            digits = digits + 1
    return kept

# decorator
def trace1(fn):
    """Returns a version of fn that first print before it is called.
        fn-a function of 1 argument
    """
    def traced(x):
        print ("calling",fn,"on argument",x)
        return fn(x)
    return traced

@trace1
def square(x):
    return x*x
# This is identical to
square = trace1(square)


from operator import add, mul

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1


def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False

    """
    "*** YOUR CODE HERE ***"
    if x <= 0:
        return False
    else:
        while x//10 > 0:
            curr_last, next_last = x % 10, (x//10) % 10
            if next_last > curr_last:
                return False
            else:
                x = x // 10
        return True


def get_k_run_starter(n, k):
    """Returns the 0th digit of the kth increasing run within n.
    >>> get_k_run_starter(123444345, 0) # example from description
    3
    >>> get_k_run_starter(123444345, 1)
    4
    >>> get_k_run_starter(123444345, 2)
    4
    >>> get_k_run_starter(123444345, 3)
    1
    >>> get_k_run_starter(123412341234, 1)
    1
    >>> get_k_run_starter(1234234534564567, 0)
    4
    >>> get_k_run_starter(1234234534564567, 1)
    3
    >>> get_k_run_starter(1234234534564567, 2)
    2
    """
    # i = 0
    # store = []
    # while i <= k:
    #     stop = False
    #     while not stop and n >0:
    #         curr_last, next_last = n % 10, (n // 10) % 10
    #         if next_last >= curr_last:
    #             stop = True
    #         if i == k:
    #             store.append(curr_last)
    #         n = n // 10
    #     i = i + 1
    # return store[-1]
    i = 0
    final = None
    while i <= k:
        while n > 10 and n % 10 > (n//10) % 10:
            n = n // 10
        final = n % 10
        i = i + 1
        n = n // 10
    return final


def make_repeater(func, n):
    """Return the function that computes the nth application of func.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    5
    """
    "*** YOUR CODE HERE ***"
    def repeat_func(x):
        if n == 0:
            return x
        elif n == 1:
            return func(x)
        else:
            i, new_func = 1, func
            while i < n:
                new_func = composer(func, new_func)
                i += 1
            return new_func(x)
    return repeat_func



def composer(func1, func2):
    """Return a function f, such that f(x) = func1(func2(x))."""
    def f(x):
        return func1(func2(x))
    return f


def apply_twice(func):
    """ Return a function that applies func twice.

    func -- a function that takes one argument

    >>> apply_twice(square)(2)
    16
    """
    "*** YOUR CODE HERE ***"
    return make_repeater(func, 2)


def div_by_primes_under(n):
    """return a function(k),
    if k is divided by n prime, return True
    else return False"""
    """
    >>> div_by_primes_under(10)(11)
    False
    >>> div_by_primes_under(10)(121)
    False
    >>> div_by_primes_under(10)(12)
    True
    >>> div_by_primes_under(5)(1)
    False
    """
    checker = lambda x: False # n < 2 return False
    i = 2
    while i <= n:
        # If i is not divided by the previous prime number, we can update the checker function
        if not checker(i):
            # Either x is divided by i or by the previous prime number, it returns True
            checker = (lambda f,i : lambda x: x % i == 0 or f(x))(checker,i)
        i = i + 1
    return checker


def div_by_primes_under_no_lambda(n):
    """
    >>> div_by_primes_under_no_lambda(10)(11)
    False
    >>> div_by_primes_under_no_lambda(10)(121)
    False
    """
    # def checker(k):
    #     i = 2
    #     while i <= n:
    #         if k % i == 0:
    #             return True
    #         i = i + 1
    #     return False
    # return checker
    def checker(k):
        return False
    i = 2
    while i <= n:
        if not checker(i):
            def outer(f,i):
                def inner(k):
                    return k % i == 0 or f(k)
                return inner
            checker = outer(checker,i)
        i += 1
    return checker


def zero(f):
    return lambda x: x


def successor(n):
    return lambda f: lambda x: f(n(f)(x))


def one(f):
    """Church numeral 1: same as successor(zero)"""
    "*** YOUR CODE HERE ***"
    return lambda x:f(x)


def two(f):
    """Church numeral 2: same as successor(successor(zero))"""
    "*** YOUR CODE HERE ***"
    return lambda x:f(f(x))


three = successor(two)


def church_to_int(n):
    """Convert the Church numeral n to a Python integer.

    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    >>> church_to_int(three)
    3
    """
    "*** YOUR CODE HERE ***"
    return n(lambda x:x+1)(0)



def add_church(m, n):
    """Return the Church numeral for m + n, for Church numerals m and n.

    >>> church_to_int(add_church(two, three))
    5
    """
    "*** YOUR CODE HERE ***"
    return lambda f:lambda x: m(f)(n(f)(x))



def mul_church(m, n):
    """Return the Church numeral for m * n, for Church numerals m and n.

    >>> four = successor(three)
    >>> church_to_int(mul_church(two, three))
    6
    >>> church_to_int(mul_church(three, four))
    12
    """
    "*** YOUR CODE HERE ***"
    return lambda f: lambda x: m(n(f))(x)


def pow_church(m, n):
    """Return the Church numeral m ** n, for Church numerals m and n.

    >>> church_to_int(pow_church(two, three))
    8
    >>> church_to_int(pow_church(three, two))
    9
    """
    "*** YOUR CODE HERE ***"
    return n(m)
