import pandas as pd

def main():
    data = pd.read_csv('ego-Gplus-original.txt', sep=" ", header=None)
    # data = pd.read_csv('new.txt', sep=" ", header=None)
    data = data.drop_duplicates(keep='first')
    data.to_csv('ego-Gplus.txt', sep=" ", header=None, index=False)

if __name__ == "__main__":
    main()