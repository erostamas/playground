import pandas

dataframe = pandas.read_csv('data.csv')
print(dataframe)

print(dataframe.columns)
print(dataframe['NUMBER'])


s = pandas.Series([10, 20, 30], index=['a', 'b', 'c'])
p = pandas.Series([10, 20, 30])
print(s)
print(p)