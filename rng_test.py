import time
import sys

from rng.rng import \
    lagged_fibonacci_generator, \
    linear_congruential_generator, \
    seed_update

def main(outfilepath):
    # output table title
    table = [[
        "bits",
        "lcg",
        "lfg"
    ]]

    # target generators for tests
    generators = [linear_congruential_generator, lagged_fibonacci_generator]

    # target bit lengths for tests
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
    
    runs = 1000

    for nbl in number_bit_lengths:
        table_row = [str(nbl)]
        for generator in generators:
            times = []
            for _ in range(runs):
                seed_update()
                start = time.perf_counter_ns() / 1000
                generator(nbl)
                end = time.perf_counter_ns() / 1000
                times.append(end - start)
            # add average elapsed time to output table row
            table_row.append(f"{sum(times) / runs}")
        table.append(table_row)

    # save results
    with open(outfilepath, "w") as file:
        file.write("\n".join([",".join(line) for line in table]))

if __name__ == "__main__":
    assert(len(sys.argv) == 2)
    main(sys.argv[1])

