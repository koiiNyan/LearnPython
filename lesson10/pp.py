import pandas as pd

data = pd.read_csv(
    open('stations.csv', 'r', encoding='cp1251'),
    sep=';'
)

print(data.head())