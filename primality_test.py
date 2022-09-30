import time
import sys

from rng.rng import \
    linear_congruential_generator, \
    lagged_fibonacci_generator, \
    seed_update
    
from primality_test.primality_testers import miller_rabin, fermat

def main(outpath_results, outfile_false_positives, outpath_primes):
    # output table
    table = [[
        "bits",
        "lcg",
        "lfg"
    ]]

    # target bits length for tests
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

    # target generators for tests
    generators = [linear_congruential_generator, lagged_fibonacci_generator]

    runs = 30
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
                
                # is n a false positive for a 1 trial
                # miller rabin primality test?
                if not any([fermat(n, 1), miller_rabin(n, 40)]):
                    false_positives.append(n)
                    continue

                quantity -= 1
                times.append(end - start)

                with open(outpath_primes, "a") as file:
                    file.write(f"{n}\n")

            # add average elapsed time to results table row
            table_row.append(f"{sum(times) / runs}")
        table.append(table_row)

    # save result
    with open(outpath_results, "w") as file:
        file.write("\n".join([",".join(line) for line in table]))
    
    with open(outfile_false_positives, "a") as file:
        file.write("\n".join(map(lambda x: str(x), false_positives)))

if __name__ == "__main__":
    assert(len(sys.argv) == 4)
    main(sys.argv[1], sys.argv[2], sys.argv[3])
    