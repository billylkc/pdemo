import pandas as pd


def main():
    print("Main")


def dev():
    print("dev")
    s = pd.Series(list('abca'))
    df = pd.get_dummies(s)
    print(df.head())
    print("some notes from A")
    print("some other notes from A")


if __name__ == '__main__':
    # main()
    dev()
