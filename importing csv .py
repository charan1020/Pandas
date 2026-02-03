import pandas as pd
df=pd.read_csv('data.csv',index_col="id")
''''
#SELECTION BY COLUMN is accessing a single column
print(df["name"].to_string())
print(df.to_string())
print(df[["name","age","country"]].to_string())
print(df.loc[1].to_string())
print(df.iloc[0:11:2,0:3])
'''

''''
id=input("Enter the id:")
try:
    print(df.loc[int(id)])
except KeyError:
    print("ID not found")
except ValueError:
    print("Invalid ID")


#filtering is a keeping rows that meet a certain condition

age=df[df["age"]>30]
country=df[df["country"]=="India"]
print(country)

'''

#aggregation is performing a calculation on a set of values to return a single value often used with groupby() function
'''
print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.max(numeric_only=True))
print(df.min(numeric_only=True))
print(df.median(numeric_only=True))
print(df.std(numeric_only=True))
print(df.var(numeric_only=True))
print(df.count())
print(df.describe())
print(df["score"].mean())


group=df.groupby("country")
print(group["score"].mean())
print(group["score"].max())
print(group["score"].min())
print(group["score"].count())   
print(group["age"].mean())
print(group["age"].max())
print(group["age"].min())
print(group["age"].count()) 
'''
#data cleaning is handling missing or inconsistent data. 75% of work done with pandas is data cleaning
#1.Drop irrelevant columns
#df=df.drop(columns=["email"])
#2.Handle missing values
#df=df.dropna(subset=["email"])
#3.fix inconsistent data
df["country"]=df["country"].replace({"USA":"United States","UK":"United Kingdom"})
#4.standardize text
df["name"]=df["name"].str.upper()
#5.fix data types
df["score"]=df["score"].astype(float)
#6.remove duplicates
df=df.drop_duplicates()
#7.rename columns
df=df.rename(columns={"score":"exam_score"})
print(df.to_string())