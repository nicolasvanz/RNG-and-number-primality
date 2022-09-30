import random


# returns if n is a probable prime or not based on miller rabin primality test
# the bigger the parameters trials is, the more precise is the answer
def miller_rabin(n, trials):
    # basic test: n should be odd
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(trials):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            return False
    return True


# returns if n is a probable prime or not based on fermat primality test
# the bigger the parameters trials is, the more precise is the answer
def fermat(n, trials):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for _ in range(trials):
        if pow(random.randint(1, n-1), n-1, n) != 1:
            return False
    return True