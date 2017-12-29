import pandas as pd

def main():
    data = pd.read_csv('./data/gplus_combined.txt', sep=" ", header=None)
    data = data.drop_duplicates(keep='first')
    data.to_csv('./data/ego-Gplus.txt', sep=" ", header=None, index=False)

if __name__ == "__main__":
    main()