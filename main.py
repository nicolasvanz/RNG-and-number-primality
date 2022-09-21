import sys

from rng.rng import \
    lagged_fibonacci_generator, \
    linear_congruential_generator, \
    seed_update    


def main(algorithm, bits):
    seed_update()
    print(algorithm(bits))

if __name__ == "__main__":
    algorithms =  {
        1 : lagged_fibonacci_generator,
        2 : linear_congruential_generator
    }

    if len(sys.argv) != 3:
        print("incorrect usage. Usage: python3 main.py <algorithm> <bits>")
        print("where <algorithm> is the desired generator " \
            "and <bits> is the desired random number bit length\n")
        
        print("<algorithm>:")
        for key, value in algorithms.items():
            print(f"{key} - {value.__name__}")
        
        exit(1)

    try:
        algorithm, bits = map(int, (sys.argv[1], sys.argv[2]))
    except ValueError:
        print("all arguments must be integers")
        exit(1)

    main(algorithms[algorithm], bits)
    