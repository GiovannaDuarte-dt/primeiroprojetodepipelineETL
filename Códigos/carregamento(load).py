import os
import pandas as pd
from sqlalchemy import create_engine, text

# Credenciais
DB_USER = "postgres"
DB_PASSWORD = "Gi08162403+"
DB_NAME = "bancodedadosvendas"
DB_HOST = "localhost"
DB_PORT = "5432"

LINK_DATABASE = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
arq_dadosT = "Dados/Dados_tratados(REFINED)/dados_tratados.csv"

def carregar_dados():
    # 1. Verifica se o arquivo existe
    if not os.path.exists(arq_dadosT):
        print(f"❌ ERRO: O arquivo '{arq_dadosT}' não foi encontrado.")
        return

    engine = create_engine(LINK_DATABASE)

    try:
        # 2. Cria o schema no PostgreSQL caso não exista
        with engine.begin() as conn:
            conn.execute(text("CREATE SCHEMA IF NOT EXISTS schemx_vendas;"))
        print(" Schema 'schemx_vendas' verificado/criado.")

        # 3. Lê o CSV com os dados tratados
        df = pd.read_csv(arq_dadosT)
        print(f" CSV lido com sucesso! Total de linhas a enviar: {len(df)}")

        # 4. Envia para o PostgreSQL (criando a tabela se não existir)
        df.to_sql(
            name="vendas_ficticias_table",
            con=engine,
            schema="schemx_vendas",
            if_exists="replace",  # Cria/sobrescreve a tabela do zero de forma limpa
            index=False
        )
        print("SUCESSO! Todos os dados foram gravados no PostgreSQL!")

    except Exception as e:
        print("OCORREU UM ERRO NA CARGA:")
        print(e)

if __name__ == "__main__":
    carregar_dados()
