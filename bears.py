# int -> boolean
""" A True return value means that it is possible to win
    the bear game by starting with n bears. A False return value means
    that it is not possible to win the bear game by starting with n
    bears."""
def bears(n):
    if n == 42:
        return True
    elif n < 42:
        return False
    else:
        passing = False
        if n % 2 == 0:  # minus n/2
            passing = bears(n // 2)
            if passing:
                return True
        if (n % 3 == 0 or n % 4 == 0) and (n % 10 != 0 and (n // 10) % 10 != 0):  # minus (last 2 digits multiplied)
            ones = n % 10
            tens = (n // 10) % 10
            passing = bears(n - (tens * ones))
            if passing:
                return True
        if n % 5 == 0:  # minus 42
            passing = bears(n - 42)
            if passing:
                return True
        return passing
