#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd

def analisar_dados(arquivo):
    # Carrega o arquivo em um DataFrame do pandas
    df = pd.read_excel(arquivo)

    # Verifica a quantidade de valores duplicados nas colunas item e model
    qtd_duplicados = df[['item_id', 'model_id']].duplicated().sum()
    st.write(f'Quantidade de valores duplicados nas colunas "item" e "model": {qtd_duplicados}')

    # Verifica a quantidade de valores vazios, zerados e não inteiros na coluna estoque
    qtd_vazios = df['promo_stock'].isna().sum()
    qtd_zerados = (df['promo_stock'] == 0).sum()
    qtd_nao_inteiros = (~df['promo_stock'].astype(str).str.isdigit()).sum()
    st.write(f'Quantidade de valores vazios na coluna "estoque": {qtd_vazios}')
    st.write(f'Quantidade de valores zerados na coluna "estoque": {qtd_zerados}')
    st.write(f'Quantidade de valores não inteiros na coluna "estoque": {qtd_nao_inteiros}')


# In[2]:


# Cria um componente para upload de arquivo
arquivo = st.file_uploader('Selecione o arquivo .xlsx', type='xlsx')

# Verifica se um arquivo foi carregado e, se sim, executa a análise de dados
if arquivo is not None:
    analisar_dados(arquivo)

