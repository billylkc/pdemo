import pandas as pd
import numpy as np


def main():
    print("Main")


def dev():
    print("dev")
    s = pd.Series(list('abca'))
    df = pd.get_dummies(s)
    print(df.head())
    print("some notes from A")
    print("some other notes from A")
    print("Print sth")
    print("Print sth more")
    print("Print sth more")


if __name__ == '__main__':
    # main()
    dev()
