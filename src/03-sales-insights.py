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

#Resetando o Index 
df = df.reset_index(drop=True)

#Criação da Coluna de Faturamento
df["faturamento"] = df["quantidade"] * df["preco_unitario"]

#Faturamento Total por Mês
ftm = df.groupby(df['data'].dt.to_period('M'))['faturamento'].sum()

#Ticket Médio por Cidade
tck = df.groupby('cidade')['faturamento'].mean().sort_values(ascending=False)

#Análise de Volume de Venda
#Filtrar quais vendas tiveram a quantidade maior que 2
avv = df[df["quantidade"] > 2]

print("--------------------Ticket Médio por Cidade--------------------\n")
print(f'{tck}\n\n')
print("--------------------Faturamento Total por Mês--------------------\n")
print(f'{ftm}\n\n')
print("--------------------Análise de Volume de Venda--------------------\n")
print(f'{avv}\n\n')