def div_by_primes_under_no_lambda(n):
    def checker(x):
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
div_by_primes_under_no_lambda(5)(1)