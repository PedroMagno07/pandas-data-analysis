import pandas as pd

df_vendas = pd.read_csv("data/raw/vendas.csv")

#Conversão de tipos
df_vendas["quantidade"] = pd.to_numeric(df_vendas["quantidade"], errors="coerce")
df_vendas["preco_unitario"] = pd.to_numeric(df_vendas["preco_unitario"], errors="coerce")

#Preenchendo valores vazios com 0
df_vendas = df_vendas.fillna({"quantidade": 0,
                "preco_unitario": 0})

#Criação da Coluna
df_vendas["faturamento"] = df_vendas["quantidade"] * df_vendas["preco_unitario"]

#Calculo de faturamento total por produto
ft = df_vendas.groupby('produto')['faturamento'].sum().sort_values(ascending=False)
print(ft)

#Filtrando apenas vendas de santos
vendas_santos = df_vendas[df_vendas['cidade'] == 'Santos']

print(vendas_santos)

