import pandas as pd


df = pd.read_csv("songs.csv", index_col = "track")

print(df.loc["Respect", "released"])
