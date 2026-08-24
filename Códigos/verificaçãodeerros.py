import pandas as pd 
loc_arquivo = "dados/dados_brutos(RAW)/vendasficticias.csv" 
df = pd.read_csv(loc_arquivo)

print("Número de linhas e colunas, respectivamente:", df.shape)
print(df) 

print(f'quantidade de valores nulos: {df.isnull().sum()}')
print(f'percentual de valores nulos: {df.isnull().mean() * 100:.2f}%')
print(f'duplicados: {df.duplicated().sum()}')
print(df.dtypes)
print(df.info()) 


