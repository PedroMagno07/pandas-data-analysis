import pandas as pd
import matplotlib.pyplot as plt

#Importação dos Arquivos
df_vendas = pd.read_csv("data/raw/vendas.csv")
df_produto = pd.read_csv("data/raw/produtos.csv")

#Conversão de Tipos
df_vendas['data'] = pd.to_datetime(df_vendas['data'])
df_vendas["quantidade"] = pd.to_numeric(df_vendas["quantidade"], errors="coerce")
df_vendas["preco_unitario"] = pd.to_numeric(df_vendas["preco_unitario"], errors="coerce")

#Remoção de Duplicatas
df_vendas = df_vendas.drop_duplicates()

#Limpeza Seletiva
df_vendas = df_vendas.dropna(subset=['quantidade', 'preco_unitario'])

#Resetando o Index 
df_vendas = df_vendas.reset_index(drop=True)

#Criação da Coluna de Faturamento
df_vendas["faturamento"] = df_vendas["quantidade"] * df_vendas["preco_unitario"]

#Junção das Tabelas
df_final = pd.merge(df_vendas, df_produto, on='produto', how='left')

#Cálculo de Faturamento Total por Categoria
ftCategoria = df_final.groupby('categoria')['faturamento'].sum().sort_values(ascending=False)

#Verificação
print('-----------------Tabela Final-----------------\n')
print(f'{df_final}\n\n')
print('-----------------Faturamento Total por Categoria-----------------\n')
print(f'{ftCategoria}\n\n')

#---------------------------Criação do Gráfico---------------------------
ftCategoria.plot(kind='bar', color='purple', edgecolor='black')
#Título 
plt.title("Faturamento Total por Categoria")
#Legenda Eixo X
plt.xlabel('Categoria')
#Legenda Eixo Y
plt.ylabel('Faturamento (R$)')
#Rotação dos Nomes
plt.xticks(rotation=45)
#Ajuste Automático dos Textos
plt.tight_layout()
#---------------------------Salvando Imagem do Gráfico---------------------------
plt.savefig('data/figures/faturamento_categoria.png')
