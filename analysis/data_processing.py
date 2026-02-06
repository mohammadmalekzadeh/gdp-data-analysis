# import library
import numpy as np
import pandas as pd
import math

# read raw dataset and create processed dataset
data = pd.read_csv("../dataset/Global GDP Explorer 2025 (World Bank  UN Data)_raw.csv")
df = pd.DataFrame()
data.head()

# data processing
df["Country"] = data["Country"]
df["GDP Value (log)"] = data["GDP (nominal, 2023)"].apply(lambda x : round(math.log(int("".join(str(x).split("$")[1].split(",")))), 4))
df["GDP Abbrev"] = data["GDP (abbrev.)"].apply(lambda x : str(x).split()[1].capitalize())
df["GDP Growth (%)"] = data["GDP Growth"].apply(lambda x : float("".join(str(x).split("%")[0])))
df["Population (log)"] = data["Population 2023"].apply(lambda x : round(math.log(int(x)), 4))
df["GDP Per Capita"] = data["GDP per capita"].apply(lambda x : (int("".join(str(x).split("$")[1].split(",")))))
df["Share of World GDP (%)"] = data["Share of World GDP"].apply(lambda x : float("".join(str(x).split("%")[0])))

# save processed dataset
df.to_csv("../dataset/gdp_processed_data.csv", index= False)