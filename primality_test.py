import time
import sys

from rng.rng import \
    linear_congruential_generator, \
    lagged_fibonacci_generator, \
    seed_update
    
from primality_test.primality_testers import miller_rabin, fermat

def main(outfilepath):
    table = [[
        "bits",
        "lcg",
        "lfg"
    ]]

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
        # 4096,
    ]

    generators = [linear_congruential_generator, lagged_fibonacci_generator]

    runs = 1
    false_positives = []

    for nbl in number_bit_lengths:
        table_row = [str(nbl)]
        for generator in generators:
            quantity = runs
            times = []
            while quantity > 0:
                start = time.perf_counter_ns() / 1000
                while quantity > 0:
                    n = generator(nbl)
                    if (not miller_rabin(n, 1)):
                        continue
                    end = time.perf_counter_ns() / 1000
                    break
                
                if not any(fermat(n, 1), miller_rabin(n, 40)):
                    false_positives.append(n)
                    continue

                quantity -= 1
                times.append(end - start)
            table_row.append(f"{sum(times) / runs}")
        table.append(table_row)

    with open(outfilepath, "w") as file:
        file.write("\n".join([",".join(line) for line in table]))

if __name__ == "__main__":
    assert(len(sys.argv) == 2)
    main(sys.argv[1])
    