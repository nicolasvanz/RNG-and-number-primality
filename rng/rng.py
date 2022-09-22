from rng.randomseed import randint

def seed_update():
    global seed
    seed_digit_range = 256
    seed = randint(10 ** (seed_digit_range - 1), 10 ** seed_digit_range - 1)

def bit_truncate(n, bits):
    length = n.bit_length()
    if length > bits:
        return int(bin(n)[2:-(n.bit_length() - bits)], 2)
    elif length == bits:
        return n
    raise Exception("Expected longer number when truncating bits")

def lagged_fibonacci_generator(bits, j = 128, k = 159):
    global seed

    lfg_sequence = [int(digit) for digit in str(seed)]
    
    n = lfg_sequence[-j] + lfg_sequence[-k]
    lfg_sequence.append(n)

    while n.bit_length() < bits:
        sequence_next = lfg_sequence[-j] + lfg_sequence[-k]
        n = int(str(n) + str(sequence_next))
        lfg_sequence.append(sequence_next)

    return bit_truncate(n, bits)

def linear_congruential_generator(
    bits,
    mod = 2**32,
    a = 16843009,
    c = 826366247
):
    global seed

    x = (seed * a + c) % mod
    n = x

    while (n.bit_length() < bits):
        x = (x * a + c) % mod
        n = int(str(n) + str(x))

    return bit_truncate(n, bits)
