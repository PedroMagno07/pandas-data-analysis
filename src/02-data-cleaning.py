import pandas as pd

df = pd.read_csv("data/vendas.csv")

#Conversão de Tipos
df['data'] = pd.to_datetime(df['data'])
df["quantidade"] = pd.to_numeric(df["quantidade"], errors="coerce")
df["preco_unitario"] = pd.to_numeric(df["preco_unitario"], errors="coerce")

#Remoção de Duplicatas
df = df.drop_duplicates()

#Limpeza Seletiva
df = df.dropna(subset=['quantidade', 'preco_unitario'])
df = df.reset_index(drop=True)

#Verificação
print("-------------------Resumo Técnico-------------------\n")
print(df.info())
print("-------------------Tabela Limpa-------------------\n")
print(df.to_string())