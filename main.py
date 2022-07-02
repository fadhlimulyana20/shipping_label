import pandas as pd

df = pd.read_excel('data.xlsx')
df_new = df[['NAMA', 'ALAMAT', 'NOMER WA']]
df_new.dropna(subset = ["NAMA"], inplace=True)
print(df_new.head())