from rng.randomseed import randint

# updates global seed, which is used in lfg and lcg
def seed_update():
    global seed, seed_digit_range
    # seed range. Note that the range should be at least 160 to support current
    # parameters at lfg.
    seed_digit_range = 256
    # generates a randon number of seed_digit_range length based on the
    # relative drift of two clocks.
    seed = randint(10 ** (seed_digit_range - 1), 10 ** seed_digit_range - 1)

# returns "bits" most significant bits from the given number
def bit_truncate(n, bits):
    length = n.bit_length()
    if length > bits:
        return int(bin(n)[2:-(n.bit_length() - bits)], 2)
    elif length == bits:
        return n
    raise Exception("Expected longer number when truncating bits")

def lagged_fibonacci_generator(bits, j = 128, k = 159):
    global seed, seed_digit_range

    # initial values
    lfg_sequence = [int(digit) for digit in str(seed)]
    
    # first random number
    n = lfg_sequence[-j] + lfg_sequence[-k]
    first = n
    lfg_sequence.append(n)

    # concatenates more random numbers to the sequence
    # until reach desired bit length
    while n.bit_length() < bits:
        sequence_next = lfg_sequence[-j] + lfg_sequence[-k]
        n = int(str(n) + str(sequence_next))
        lfg_sequence.append(sequence_next)

    # update seed
    seed = int(str(seed)[1:] + str(first))

    return bit_truncate(n, bits)

def linear_congruential_generator(
    bits,
    mod = 2**32,
    a = 16843009,
    c = 826366247
):
    global seed

    # first random number
    x = (seed * a + c) % mod
    n = x
    first = int(str(x)[0])

    # concatenates more random numbers to the sequence
    # until reach desired bit length
    while (n.bit_length() < bits):
        x = (x * a + c) % mod
        n = int(str(n) + str(x))

    # update seed
    seed = int(str(seed)[1:] + str(first))
    
    return bit_truncate(n, bits)

if __name__ == "__main__":
    pass
else:
    # we should declare a seed when importing this file
    seed_update()