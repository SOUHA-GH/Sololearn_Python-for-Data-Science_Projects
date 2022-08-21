#The program calculates the deaths/cases ratio and add it as a column to the DataFrame with the name 'ratio'.
#Then finds the row that corresponds to the largest value and outputs it.
import pandas as pd

df = pd.read_csv("/usercode/files/ca-covid.csv")

df.drop('state', axis=1, inplace=True)
df.set_index('date', inplace=True)
df["ratio"] = df["deaths"] / df["cases"]
max_ratio = df.loc[df["ratio"] == df["ratio"].max()]
print(max_ratio)
