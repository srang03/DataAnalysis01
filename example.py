import pandas as pd


iris = pd.read_csv('./iris.csv')
# print(iris)
# print(type(iris))
print(iris.shape)
print(iris.describe())
print(iris.tail(10))