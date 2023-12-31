"""
TÍTULO
Análise de Dados em um Radar de Velocidade

Autor: Natália Ferreira
User Github: Natferrx
Data de Criação: 30/08/2023

OBJETIVO
O objetivo é demonstrar como usar o Python e a biblioteca Pandas para extrair, transformar e
analisar dados.

CONTEXTO
Este código faz a leitura de dados fictícios de carros que passam por um radar de velocidade realiza análises simples
para calcular a velocidade média, identificar carros acima do limite de velocidade e contar carros abaixo
do limite.

ENTRADAS
O arquivo CSV contém as seguintes colunas:
- "Placa do Carro": Placa fictícia no formato AAA-1111.
- "Velocidade": Velocidade do carro em km/h.
- "Data": Data de passagem do carro pela estrada.

ETAPAS E RESULTADOS
O código realiza as seguintes etapas:
1. Lê os dados do arquivo CSV.
2. Calcula a velocidade média de todos os carros.
3. Conta e identifica carros acima do limite de velocidade (80 km/h).
4. Imprime os resultados das análises.

Observação: Certifique-se de ter o arquivo chamado dados_carros.csv no mesmo diretório do script com os dados apropriados.

"""

# Importa a biblioteca Pandas para trabalhar com dados tabulares
import pandas as pd

# PASSO 1 - EXTRAÇÃO

# Lê o arquivo CSV usando Pandas e coloca os dados em um DataFrame (tabela).
df = pd.read_csv('dados_carros.csv')

# PASSO 2 - TRANSFORMAÇÃO

# Calcula a velocidade média
velocidade_media = df['Velocidade'].mean()

# Define as variáveis iniciais para a velocidade dos carros e o valor limite da velocidade do radar
carros_acima_limite = 0
carros_abaixo_limite = 0
limite_radar = 80

# Verifica se cada carro está acima ou abaixo do limite
for velocidade in df['Velocidade']: #A função For faz um looping na coluna Velocidade
    if velocidade > limite_radar: #Se a velocidade estiver acima do limite acrescenta +1 valor na variável carros_acima_velocidade
        carros_acima_limite += 1
    else:
        carros_abaixo_limite += 1 #Se a velocidade estiver abaixo do limite acrescenta +1 valor na variável carros_abaixo_velocidade

# PASSO 3 - CARREGAMENTO

# Imprime resultados de forma organizada
print(f"Velocidade média: {velocidade_media:.2f} km/h")
print(f"Total de carros: {num_rows}")
print(f"Qtd. Carros acima do limite: {carros_acima_limite}")
print(f"Qtd. Carros abaixo do limite: {carros_abaixo_limite}")