# Sum digits
def split(n):
    return n // 10, n % 10


def sum_digits(n):
    """Return the sum of the digits of positive integer n.

        >>> sum_digits(9)
        9
        >>> sum_digits(18117)
        18
        >>> sum_digits(9437184)
        36
        >>> sum_digits(11408855402054064613470328848384)
        126
    """
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return last + sum_digits(all_but_last)


# Iteration vs recursion
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def fact_iter(n):
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1
    return total


# Luhn algorithm
def luhn_sum(n):
    """Return the digit sum of n computed by the Luhn algorithm.

        >>> luhn_sum(2)
        2
        >>> luhn_sum(12)
        4
        >>> luhn_sum(42)
        10
        >>> luhn_sum(138743)
        30
        >>> luhn_sum(5105105105105100) # example Mastercard
        20
        >>> luhn_sum(4012888888881881) # example Visa
        90
        >>> luhn_sum(79927398713) # from Wikipedia
        70
        """
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return last + luhn_double_sum(all_but_last)


def luhn_double_sum(n):
    all_but_last, last = split(n)
    luhn_number = sum_digits(2 * last)
    if n < 10:
        return luhn_number
    else:
        return luhn_number + luhn_sum(all_but_last)


