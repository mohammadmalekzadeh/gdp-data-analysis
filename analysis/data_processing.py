# import library
import pandas as pd
import numpy as np

# read dataset
df = pd.read_csv("../dataset/Global GDP Explorer 2025 (World Bank  UN Data)_raw.csv")
print(df)

# columns cleaning
df["GDP (nominal, 2023)"] = df["GDP (nominal, 2023)"].apply(lambda x : int("".join(str(x).split("$")[1].split(","))))
df["GDP (abbrev.)"] = df["GDP (abbrev.)"].apply(lambda x : str(x).split(" ")[1].capitalize())
df["GDP Growth"] = df["GDP Growth"].apply(lambda x : round(float(str(x).split("%")[0])/100, 3))
df["GDP per capita"] = df["GDP per capita"].apply(lambda x : int("".join(str(x).split("$")[1].split(","))))
df["Share of World GDP"] = df["Share of World GDP"].apply(lambda x : round(float(str(x).split("%")[0])/100, 2))

# columns typing
df["Country"] = df["Country"].astype("string")
df["GDP (nominal, 2023)"] = df["GDP (nominal, 2023)"].astype("int")
df["GDP (abbrev.)"] = df["GDP (abbrev.)"].astype("string")
df["GDP Growth"] = df["GDP Growth"].astype("float")
df["Population 2023"] = df["Population 2023"].astype("int")
df["Share of World GDP"] = df["Share of World GDP"].astype("float")

# show result and datasets describe
print(df)
print(df.describe())
print(df.info())

# save processed dataset
df.to_csv("../dataset/gdp_data_processed.csv", index= False)
