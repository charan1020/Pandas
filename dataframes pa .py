#data frames is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns) in pandas.

import pandas as pd
data={'Name':['Alice','Bob','Charlie','David'],
      'Age':[24,27,22,32],}
#df=pd.DataFrame(data)
df=pd.DataFrame(data, index=["emp1","emp2","emp3","emp4"])
''''
print(df)
print(df.loc["emp2"])
print(df.iloc[2])
'''
#Add a new column
df["job"]=["Engineer","Doctor","Artist","Lawyer"]
#print(df)

#add a new row
df_row=pd.DataFrame([{'Name':'Eve','Age':29,'job':'Scientist'},
                    {'Name':'joe','Age':30,'job':'Manager'}],
                    index=['emp5','emp6'])
df=pd.concat([df,df_row])
print(df)