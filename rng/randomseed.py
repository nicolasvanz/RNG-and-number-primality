import struct
import time


# returns k random bits using a relative drift of two clocks .
# it does not produce "good" random bits, but we are suposed to use that
# only when creating the first seed
def getrandbits(k):
    result = 0
    for _ in range(k):
        time.sleep(0)
        result <<= 1
        result |= struct.pack('!f', time.process_time())[-1] & 1
    return result

# returns random integer in range [a, b]
def randint(a, b):
    return a + randbelow(b - a + 1)

# returns a random integer in the range [0,n)
def randbelow(n):
    if n <= 0:
       raise ValueError
    k = n.bit_length()
    r = getrandbits(k)
    while r >= n:
        r = getrandbits(k)
    return r