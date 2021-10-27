import pandas as pd
if __name__ == '__main__':

    csv = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",
                      names=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species'])
    print(csv.head())
    print(csv.nunique())






