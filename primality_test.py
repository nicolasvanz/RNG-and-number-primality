from rng.rng import \
    linear_congruential_generator, \
    lagged_fibonacci_generator, \
    seed_update
    
from primality_test.primality_testers import miller_rabin, fermat

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

def search_for_false_positives():
    number_bit_lengths = [
        # 40,
        # 56,
        # 80,
        128,
        # 168,
        # 224,
        # 256,
        # 512,
        # 1024,
        # 2048,
        # 4096,
    ]
    for nbl in number_bit_lengths:
        while True:
            n = linear_congruential_generator(nbl)
            # n = lagged_fibonacci_generator(nbl)
            if (miller_rabin(n, 1)):
                if (fermat(n, 1)):
                    continue
                else:
                    print(f"{n} -> miller_rabin OK fermat X")
            else:
                if fermat(n, 1):
                    print(f"{n} -> miller_rabin X fermat OK")
        print(f"{nbl} -> {n}\n")

if __name__ == "__main__":
    search_for_false_positives()