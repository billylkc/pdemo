import pandas as pd


def main():
    print("Main")


def dev():
    print("dev")
    s = pd.Series(list('abca'))
    df = pd.get_dummies(s)
    print(df.head())


if __name__ == '__main__':
    # main()
    dev()
