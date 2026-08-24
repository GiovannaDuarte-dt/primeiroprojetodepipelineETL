import pandas as pd 
df = pd.read_csv("dados/dados_brutos(RAW)/vendasficticias.csv")

print(df) 
df["date"] = pd.to_datetime(df["date"], format ='mixed', dayfirst=True, errors= "coerce") 
df["date"] = df["date"].dt.strftime("%Y-%m-%d") 

coluna_texto =["dealership", "brand", "model", "color", "city"] 
for column in coluna_texto:
    df[column] = df[column].astype("string").str.strip().str.title()

df = df.drop_duplicates(
    subset= ["date", "dealership", "brand", "model", "color", "price", "city"] 
)


df = df.dropna(subset=["date"]) # Para excluir linhas com datas de valor nulo por ser considerado inválido. 

df["price"] = pd.to_numeric(df["price"], errors = "coerce")

df["price"] = df["price"].fillna(
    df.groupby (
        ["dealership", "brand", "model", "color", "city"] 
    )["price"].transform("median") 
)

df["date"] = pd.to_datetime(df["date"], errors = "coerce")

print(f"nova quantidade de linhas e colunas respectivamente:{df.shape}")

print("\n", df)