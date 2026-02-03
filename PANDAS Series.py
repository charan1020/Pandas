#pandas is a powerful data manipulation library in Python, widely used for data analysis and handling structured data.
import pandas as pd
#series is a one-dimensional array-like object that can hold various data types.
'''
data = [100, 102, 104]
series = pd.Series(data, index=['a', 'b', 'c'])
series.loc['c']=200
print(series.loc['c']) #loc is used to access a group of rows and columns by labels or a boolean array.

print(series.iloc[2]) #iloc is used for integer-location based indexing for selection by position.

data =[100,102,104,200,202]
series = pd.Series(data,index=['a','b','c','d','e'])
print(series[series>=200])
print(series[series<=200])
'''

calories={'day1':1420,'day2':1380,'day3':1390}
series=pd.Series(calories)
series.loc["day3"]=1500
print(series.loc["day3"])
print(series)
print(series[series>2000])