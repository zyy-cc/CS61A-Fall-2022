# generator function uses yield instead of return, return a iterator
def plus_minus(x):
    """Yield x and -x.

    >>> t = plus_minus(3)
    >>> next(t)
    3
    >>> next(t)
    -3
    >>> list(plus_minus(5))
    [5, -5]
    >>> list(map(abs, plus_minus(7)))
    [7, 7]
    """
    yield x
    yield -x



def evens(start, end):
    """A generator function that returns even numbers.

    >>> list(evens(2, 10))
    [2, 4, 6, 8]
    >>> list(evens(1, 10))
    [2, 4, 6, 8]
    """
    even = start + (start % 2)
    while even < end:
        yield even
        even += 2


# generator can yield from iterators
# yield from statement yields all values
# from an iterator or iterable
def a_then_b(a, b):
    # for x in a:
    #     yield x
    """The elements of a followed by those of b.

    >>> list(a_then_b_for([3, 4], [5, 6]))
    [3, 4, 5, 6]
    """
    yield from a
    yield from b


def countdown(k):
    """Count down to zero.

    >>> list(countdown(5))
    [5, 4, 3, 2, 1]
    """
    if k > 0:
        yield k
        # for x in countdown(k - 1):
        #     yield x
        yield from countdown(k - 1)
    else:
        yield "Blast off"


def prefixes(s):
    """Yield all prefixes of s.

    >>> list(prefixes('both'))
    ['b', 'bo', 'bot', 'both']
    """
    if s:
        yield from prefixes(s[:-1])
        yield s


def substrings(s):
    """Yield all substrings of s.

    >>> list(substrings('tops'))
    ['t', 'to', 'top', 'tops', 'o', 'op', 'ops', 'p', 'ps', 's']
    """
    if s:
        yield from prefixes(s)
        yield from substrings(s[1:])


def count_partitions(n, m):
    """
    Count partitions
    >>> count_partitions(6,4)
    9
    """
    if n < 0 or m == 0:
        return 0
    else:
        exact_match = 0
        if n == m:
            exact_match = 1
        with_m = count_partitions(n - m, m)
        without_m = count_partitions(n, m - 1)
        return exact_match + with_m + without_m


def list_partitions(n, m):
    """
    List partitions
    >>> for p in list_partitions(6, 4): print(p)
    [2, 4]
    [1, 1, 4]
    [3, 3]
    [1, 2, 3]
    [1, 1, 1, 3]
    [2, 2, 2]
    [1, 1, 2, 2]
    [1, 1, 1, 1, 2]
    [1, 1, 1, 1, 1, 1]

    """
    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [[m]]
        with_m = [p + [m] for p in list_partitions(n - m, m)]
        without_m = list_partitions(n, m - 1)
        return exact_match + with_m + without_m


def partitions(n, m):
    """List partitions.

    >>> for p in partitions(6, 4): print(p)
    2 + 4
    1 + 1 + 4
    3 + 3
    1 + 2 + 3
    1 + 1 + 1 + 3
    2 + 2 + 2
    1 + 1 + 2 + 2
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 1 + 1 + 1
    """
    if n <= 0:
        return []
    elif m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [str(m)]
        with_m = [p + ' + ' + str(m) for p in partitions(n - m, m)]
        without_m = partitions(n, m - 1)
        return exact_match + with_m + without_m

def partitions(n, m):
    """List partitions.

    >>> for p in partitions(6, 4): print(p)
    2 + 4
    1 + 1 + 4
    3 + 3
    1 + 2 + 3
    1 + 1 + 1 + 3
    2 + 2 + 2
    1 + 1 + 2 + 2
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 1 + 1 + 1
    """
    if n > 0 and m > 0:
        if n == m:
            yield str(m)
        for p in partitions(n-m, m):
            yield p + ' + ' + str(m)
        yield from partitions(n, m - 1)



