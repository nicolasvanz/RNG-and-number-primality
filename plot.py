import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

import sys


def main(outfilepath):
    df = pd.read_csv(outfilepath)

    bits_list = df["bits"].to_list()
    lcg_list = df["lcg"].to_list()
    lfg_list = df["lfg"].to_list()

    plt.plot(np.arange(len(bits_list)), lcg_list, label = "linear congruential generator")
    plt.plot(np.arange(len(bits_list)), lfg_list, label = "lagged fibonacci generator")

    plt.grid()
    plt.xlabel("bits amount")
    plt.ylabel("microsseconds")
    plt.xticks(np.arange(len(bits_list)), bits_list)
    plt.yticks(lcg_list, lcg_list)
    plt.legend(loc="upper left")

    plt.show()

if __name__ == "__main__":
    main("results.csv")