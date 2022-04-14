"""
Desafio

Você trabalha em uma empresa de telecomunicação e tem clientes de vários
serviços diferentes, entre os principais: 'internet' e telefone.

O problema é que, analisando o histórico dos clientes dos últimos anos, você
percebeu que a empresa está com Churn de mais de 26% dos clientes.

Isso representa uma perda de milhões para a empresa.

O que a empresa precisa fazer para resolver isso?

"""
"""Passo 1 _ Importar a base de dados """
import pandas as pd

tabela = pd.read_csv('telecom_users.csv')


"""Passo 2 _ Visualizar a base de dados entendendo as informações"""
# Retirando uma coluna da tabela
# axis=0 -> Linha
# axis=1 -> Coluna
tabela = tabela.drop(['Unnamed: 0', 'IDCliente'], axis=1)
print(tabela)


"""Passo 3 _ Tratamento da Base de dados """
# Etapas:
# 1. — Analisar se a passe de dados está sendo lida na forma correta.

# Transformando a coluna "TotalGasto" em número
tabela['TotalGasto'] = pd.to_numeric(tabela['TotalGasto'], errors='coerce')

# 2. — Analisar se existe uma coluna completamente vazia.
# Deletando colunas vazias
tabela = tabela.dropna(how='all', axis=1)

# 3. — Analisar se existe alguma informação em alguma linha vazia.
# Deletando linhas vazias
tabela = tabela.dropna(how='any', axis=0)
print(tabela.info())

"""Passo 4 _ Analise inicial / Analise global"""
# Etapas:
# 1. — Analisar quantos clientes cancelaram
print(tabela['Churn'].value_counts())
# 2. — Analisar o percentual de cancelamento
print(tabela['Churn'].value_counts(normalize=True).map('{:.2%}'.format))

"""Passo 5 _ Analise detalhada (buscar causa ou solução)"""
import plotly.express as px

# Etapas:
# https://plotly.com/python/histograms/ <- Dados para editar o gráfico
# 1. — Criar gráfico
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color='Churn')
# 2. — Exibir o gráfico (Código funcionando no navegador Edge)
    grafico.show()

