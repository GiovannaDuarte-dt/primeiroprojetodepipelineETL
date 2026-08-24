import os
import pandas as pd 

df = pd.read_csv("Dados/dados_brutos(RAW)/vendasficticias.csv")
os.makedirs("Dados/preparação", exist_ok=True)
os.makedirs("Dados/Tratados", exist_ok=True)

df.to_csv("Dados/preparação/dados_preparados.csv", index=False)
df.to_csv("Dados/Tratados/dados_tratados.csv", index=False)

