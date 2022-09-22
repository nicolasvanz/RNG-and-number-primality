import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

import sys


def main(outfilepath):
    df = pd.read_csv(outfilepath)

    bits_list = df["bits"].to_list()
    lcg_list = df["lcg"].to_list()
    lfg_list = df["lfg"].to_list()
    difference = df["lfg"] / df["lcg"]
    difference = difference.to_list()

    npa = np.arange(len(bits_list))

    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    lns1 = ax1.plot(npa, lcg_list, label = "Linear Congruential Generator")
    lns2 = ax1.plot(npa, lfg_list, label = "Lagged Fibonacci Generator")
    lns3 = ax2.plot(npa, difference, label = "LFG / LCG", color = "r")
    lns = lns1 + lns2 + lns3
    labs = [l.get_label() for l in lns]
    plt.legend(lns, labs, loc="upper center")

    # plt.grid()
    ax1.grid()
    ax1.set_xlabel("bits amount")
    ax1.set_ylabel("microsseconds")
    ax2.set_ylabel("LFG / LCG", color = "r")
    # ax2.set_yticks(difference, difference)
    ax2.tick_params(axis="y", colors="red")
    plt.xticks(np.arange(len(bits_list)), bits_list)
    
    for index in range(len(npa)):
        plt.text(npa[index], difference[index], "%.1f" % (difference[index]))

    plt.title("LCG vs LFG")

    plt.show()

if __name__ == "__main__":
    main("results.csv")