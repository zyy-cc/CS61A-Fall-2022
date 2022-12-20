from operator import add, mul

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1


def accumulate(merger, start, n, term):
    if n== 0:
        return start
    else:
        before,current = start,0
        for k in range(1, n + 1):
            current = merger(before, term(k))
            before = current
        return current
print(accumulate(add, 11, 0, identity))
