# Python - Grafico da População do Brasil por região
# Instalado a biblioteca
# para ler arquivos antigos excel xls - pip install xlrd
# para graficos - pip install matplotlib
import pandas as pd

# Lendo a planilha e ignorando a primeira linha com skiprows=1
df = pd.read_excel(f'[CAMINHO DO ARQUIVO]/Brasil_População_01072024.xls', skiprows=1)

df.head()
df.columns

# Carrega o df_lista_regiao
regiao = ['Norte','Nordeste','Centro-Oeste','Sudeste','Sul']
df_lista_regiao = df[df['BRASIL E UNIDADES DA FEDERAÇÃO'].isin(regiao)]
print(df_lista_regiao)

# Grafico de barras
import matplotlib.pyplot as plt

eixo_x = df_lista_regiao['BRASIL E UNIDADES DA FEDERAÇÃO']
eixo_y = df_lista_regiao['POPULAÇÃO ESTIMADA']
plt.bar(eixo_x, eixo_y, color='blue')
plt.title('Brasil - População por Região\nFonte: IBGE - Data de Referência 01/07/2024')
plt.xlabel('')
plt.ylabel('POPULAÇÃO ESTIMADA\nMilhão habitantes')
# colocando os valores nas colunas
for i, valor in enumerate(eixo_y):
    plt.text(i, valor + 5, f'{valor / 1000000:.3f} MM', ha='center')
# remove a linha com o valor 1e7 que aparece no alto a esquerda do grafico no eixo y
plt.ticklabel_format(style='plain', axis='y')
plt.show()

# Grafico de pizza
plt.pie(df_lista_regiao['POPULAÇÃO ESTIMADA'], labels=df_lista_regiao['BRASIL E UNIDADES DA FEDERAÇÃO'], autopct='%1.1f%%', startangle=90)
plt.title('Brasil - População por Região\nFonte: IBGE - Data de Referência 01/07/2024') # Adiciona um título
plt.show() # Exibe o gráfico
