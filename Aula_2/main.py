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
tabela = tabela.drop('Unnamed: 0', axis=1)
print(tabela)


"""Passo 3 _ Tratamento da Base de dados """
"""Passo 4 _ Analise inicial / Analise global"""
"""Passo 5 _ Analise detalhada (buscar causa ou solução)"""


