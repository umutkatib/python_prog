import pandas as pd

veri = pd.read_csv("iris.data")

print(veri.head())

print(veri.columns)

print(veri[2:4])

veri = veri.sort_values(by="sepal_length")
print(veri.head())

toplam_veri = veri["sepal_length"].sum()
ortalama_veri = veri["sepal_length"].mean()
ortanca_veri = veri["sepal_length"].median()

print("sum:",toplam_veri,
      "\nMean:",ortalama_veri,
      "\nMEdian:",ortanca_veri)