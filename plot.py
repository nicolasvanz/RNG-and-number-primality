import sys

import matplotlib.pyplot as plt

import numpy as np
import pandas as pd


def main(infilepath, outfilepath, time_factor, title):
    # read data
    df = pd.read_csv(infilepath)

    # get data sets
    bits_list = df["bits"].to_list()
    lcg_list = (df["lcg"]/time_factor).to_list()
    lfg_list = (df["lfg"]/time_factor).to_list()
    difference = df["lfg"] / df["lcg"]
    difference = difference.to_list()

    npa = np.arange(len(bits_list))

    # creating subplots
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    # plot lines
    lns1 = ax1.plot(npa, lcg_list, label = "Linear Congruential Generator")
    lns2 = ax1.plot(npa, lfg_list, label = "Lagged Fibonacci Generator")
    lns3 = ax2.plot(npa, difference, label = "LFG / LCG", color = "r")

    # group subplots legends
    lns = lns1 + lns2 + lns3
    labs = [l.get_label() for l in lns]
    plt.legend(lns, labs, loc='center left', bbox_to_anchor=(0, -0.25))

    time_factor_to_ylabel = {
        1 : "microsseconds",
        1000 : "millisseconds",
        1000000 : "seconds",
    }

    # plot styles
    ax1.grid()
    ax1.set_xlabel("bits amount")
    ax1.set_ylabel(time_factor_to_ylabel[time_factor])
    ax2.set_ylabel("LFG / LCG", color = "r")
    ax2.tick_params(axis="y", colors="red")
    plt.xticks(np.arange(len(bits_list)), bits_list)
    
    # write exact y value on difference plotted line
    for index in range(len(npa)):
        plt.text(npa[index], difference[index], "%.1f" % (difference[index]))

    plt.title(f"{title}: LCG vs LFG")

    # save plot
    plt.savefig(outfilepath, bbox_inches = "tight")

if __name__ == "__main__":
    assert(len(sys.argv) == 5)
    # input file, output file, time factor and title
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4])