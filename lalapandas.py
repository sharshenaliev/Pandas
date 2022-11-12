import pandas as pd

df = pd.read_csv("getkeys.csv")

df1=df.sort_values(by=['sotok','summa','keys'],ascending=False)
#df.sort_values(by=['sotok'])

#print(df.columns)
print(df1)
df1.to_csv("sorted.csv", sep=';')
