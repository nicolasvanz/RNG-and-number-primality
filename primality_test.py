from random import seed
from rng.rng import \
    linear_congruential_generator, \
    lagged_fibonacci_generator, \
    seed_update
    
from primality_test.miller_rabin import miller_rabin

def main():
    number_bit_lengths = [
        40,
        56,
        80,
        128,
        168,
        224,
        256,
        512,
        1024,
        2048,
        4096,
    ]
    for nbl in number_bit_lengths:
        while True:
            n = linear_congruential_generator(nbl)
            # n = lagged_fibonacci_generator(nbl)
            # seed_update()
            if (miller_rabin(n, 40)):
                break
        print(f"{nbl} -> {n}\n")


if __name__ == "__main__":
    main()