import time

from rng.rng import \
    lagged_fibonacci_generator, \
    linear_congruential_generator, \
    seed_update

def main():
    table = [[
        "bits",
        "lcg",
        "lfg"
    ]]

    generators = [linear_congruential_generator, lagged_fibonacci_generator]
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
    
    runs = 100

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
            table_row.append(f"{sum(times) / runs}")
        table.append(table_row)

    with open("results.csv", "w") as file:
        file.write("\n".join([",".join(line) for line in table]))

if __name__ == "__main__":
    main()

