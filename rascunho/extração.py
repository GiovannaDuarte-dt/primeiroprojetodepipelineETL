import pandas as pd 
loc_arquivo = "Dados/dados_brutos(RAW)/vendasficticias.csv" 
df = pd.read_csv(loc_arquivo) 
print("Dados carregados com sucesso!")
print(f'Linhas:{df.shape[0]}') 
print(f'Colunas:{df.shape[1]}')
print ('\nTabela de dados:') 
print(df) 


