import pandas as pd

# Criando os DataFrames a partir das tabelas fornecidas
vendas_data = {
    'NOME_SHOPPING': ['SHOPPING A', 'SHOPPING A', 'SHOPPING A', 'SHOPPING A', 'SHOPPING B', 'SHOPPING B', 'SHOPPING B', 'SHOPPING B',
                      'SHOPPING C', 'SHOPPING C', 'SHOPPING C', 'SHOPPING C', 'SHOPPING A', 'SHOPPING A', 'SHOPPING A', 'SHOPPING A',
                      'SHOPPING B', 'SHOPPING B', 'SHOPPING B', 'SHOPPING B', 'SHOPPING C', 'SHOPPING C', 'SHOPPING C', 'SHOPPING C'],
    'MES': ['JANEIRO', 'JANEIRO', 'JANEIRO', 'JANEIRO', 'JANEIRO', 'JANEIRO', 'JANEIRO', 'JANEIRO',
            'JANEIRO', 'JANEIRO', 'JANEIRO', 'JANEIRO', 'FEVEREIRO', 'FEVEREIRO', 'FEVEREIRO', 'FEVEREIRO',
            'FEVEREIRO', 'FEVEREIRO', 'FEVEREIRO', 'FEVEREIRO', 'FEVEREIRO', 'FEVEREIRO', 'FEVEREIRO', 'FEVEREIRO'],
    'CODIGO_LOJA': ['L001', 'L002', 'L003', 'L004', 'L001', 'L002', 'L003', 'L006', 'L001', 'L002', 'L003', 'L005', 
                    'L001', 'L002', 'L003', 'L004', 'L001', 'L002', 'L003', 'L006', 'L001', 'L002', 'L003', 'L005'],
    'FATURAMENTO_BRUTO': [15000, 22000, 18000, 13000, 14000, 23000, 17500, 14500, 16000, 26000, 15400, 12300,
                          15000, 16200, 14300, 12600, 15200, 17800, 15250, 13650, 18000, 16480, 16200, 17000]
}

# Criando o DataFrame de vendas
df_vendas = pd.DataFrame(vendas_data)

# Somando o faturamento bruto por mês
faturamento_janeiro = df_vendas[df_vendas['MES'] == 'JANEIRO']['FATURAMENTO_BRUTO'].sum()
faturamento_fevereiro = df_vendas[df_vendas['MES'] == 'FEVEREIRO']['FATURAMENTO_BRUTO'].sum()

# Calculando a variação percentual entre fevereiro e janeiro
variacao_percentual = ((faturamento_fevereiro - faturamento_janeiro) / faturamento_janeiro) * 100

# Agrupando as vendas por shopping para ver qual shopping puxa o resultado
faturamento_por_shopping = df_vendas.groupby(['NOME_SHOPPING', 'MES'])['FATURAMENTO_BRUTO'].sum().unstack()

# Calculando a variação por shopping
faturamento_por_shopping['VARIACAO_%'] = ((faturamento_por_shopping['FEVEREIRO'] - faturamento_por_shopping['JANEIRO']) / faturamento_por_shopping['JANEIRO']) * 100

print(faturamento_janeiro, faturamento_fevereiro, variacao_percentual, faturamento_por_shopping)
-------------------------------q2------------------------------------------------

# Tabela de lojas com suas categorias
lojas_data = {
    'CODIGO_LOJA': ['L001', 'L002', 'L003', 'L004', 'L001', 'L002', 'L003', 'L006', 'L001', 'L002', 'L003', 'L005'],
    'NOME_SHOPPING': ['SHOPPING A', 'SHOPPING A', 'SHOPPING A', 'SHOPPING A', 'SHOPPING B', 'SHOPPING B', 'SHOPPING B', 'SHOPPING B',
                      'SHOPPING C', 'SHOPPING C', 'SHOPPING C', 'SHOPPING C'],
    'NOME_LOJA': ['Loja 01', 'Loja 02', 'Loja 03', 'Loja 04', 'Loja 01', 'Loja 02', 'Loja 03', 'Loja 06',
                  'Loja 01', 'Loja 02', 'Loja 03', 'Loja 05'],
    'NOME_CATEGORIA': ['Vestuário', 'Alimentação', 'Calçado', 'Vestuário', 'Vestuário', 'Alimentação', 'Calçado', 'Calçado',
                       'Vestuário', 'Alimentação', 'Calçado', 'Vestuário']
}

# Criando o DataFrame de lojas e categorias
df_lojas = pd.DataFrame(lojas_data)

# Mesclando as vendas com as categorias de lojas
df_vendas_categorias = pd.merge(df_vendas, df_lojas, on=['CODIGO_LOJA', 'NOME_SHOPPING'])

# Agrupando o faturamento por categoria e mês
faturamento_por_categoria = df_vendas_categorias.groupby(['NOME_CATEGORIA', 'MES'])['FATURAMENTO_BRUTO'].sum().unstack()

# Calculando a variação percentual por categoria
faturamento_por_categoria['VARIACAO_%'] = ((faturamento_por_categoria['FEVEREIRO'] - faturamento_por_categoria['JANEIRO']) / faturamento_por_categoria['JANEIRO']) * 100

print(faturamento_por_categoria)

----------------------------------------q3----------------------------------------------------

# Agrupando as vendas por loja, shopping e mês
faturamento_por_loja = df_vendas.groupby(['CODIGO_LOJA', 'NOME_SHOPPING', 'MES'])['FATURAMENTO_BRUTO'].sum().unstack()

# Calculando a variação percentual por loja
faturamento_por_loja['VARIACAO_%'] = ((faturamento_por_loja['FEVEREIRO'] - faturamento_por_loja['JANEIRO']) / faturamento_por_loja['JANEIRO']) * 100

# Separando lojas com crescimento e lojas com queda
lojas_crescimento = faturamento_por_loja[faturamento_por_loja['VARIACAO_%'] > 0]
lojas_queda = faturamento_por_loja[faturamento_por_loja['VARIACAO_%'] < 0]

print(lojas_crescimento, lojas_queda)

-------------------------------------q4----------------------
import pandas as pd

same_store_lojas = df_vendas[df_vendas['CODIGO_LOJA'].isin(['L001', 'L002', 'L003'])]

# Agrupando as vendas por shopping e mês
same_store_vendas = same_store_lojas.groupby(['NOME_SHOPPING', 'MES'])['FATURAMENTO_BRUTO'].sum().unstack()

# Calculando a variação percentual
same_store_vendas['VARIACAO_%'] = ((same_store_vendas['FEVEREIRO'] - same_store_vendas['JANEIRO']) / same_store_vendas['JANEIRO']) * 100

# Exibindo os resultados
print(same_store_vendas[['VARIACAO_%']])

----------------------------------------------q5------------------------

data_abl = {
    'CODIGO_LOJA': ['L001', 'L002', 'L003', 'L004', 'L001', 'L002', 'L003', 'L006', 'L001', 'L002', 'L003', 'L005'],
    'NOME_SHOPPING': ['SHOPPING A', 'SHOPPING A', 'SHOPPING A', 'SHOPPING A', 
                     'SHOPPING B', 'SHOPPING B', 'SHOPPING B', 'SHOPPING B', 
                     'SHOPPING C', 'SHOPPING C', 'SHOPPING C', 'SHOPPING C'],
    'ABL': [202.8, 301.5, 80.0, 205.0, 
            250.3, 310.2, 75.0, 99.5, 
            206.0, 289.0, 79.0, 101.0]
}

df_abl = pd.DataFrame(data_abl)
# Mesclando dados de vendas com a tabela ABL
df_vendas_abl = pd.merge(df_vendas, df_abl, on=['CODIGO_LOJA', 'NOME_SHOPPING'])

# Calculando vendas por m²
df_vendas_abl['VENDAS_POR_M2'] = df_vendas_abl['FATURAMENTO_BRUTO'] / df_vendas_abl['ABL']

# Agrupando a média de vendas por m²
media_vendas_por_m2 = df_vendas_abl.groupby('NOME_SHOPPING')['VENDAS_POR_M2'].mean()
print(media_vendas_por_m2)



-----------------------------------------------------------------