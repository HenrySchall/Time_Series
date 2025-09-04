import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy.stats as stats
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from matplotlib.pylab import rcParams
from statsmodels.tsa.seasonal import seasonal_decompose as decompose

# Configuração do padrão de medidas do plot dos gráficos para ficar visivelmente mais agradáveis
rcParams['figure.figsize'] = 15, 6

##################
### Introdução ###
##################

# Série Anual (1980 a 2020 = 41 anos)
np.random.seed(10) # definir ponto inicial para sempre gerar mesmos valores aleatórios
df_anual = np.random.normal(
    0, # média
    1, # desvio padrão
    41) # quantidade de valores
df_anual.shape
df_anual

# Série Mensal (1995-01 a 2000-12 = 72 meses)
#np.random.seed(10) # definir ponto inicial para sempre gerar mesmos valores aleatórios
#df_mensal = np.random.normal(
#    0, # média
#    1, # desvio padrão
#    72) #quantidade de valores
#df_mensal.shape
#df_mensal

# Transformando em Série
serie_anual = pd.Series(df_anual)
serie_anual.plot()
plt.show()

# Transformando em DataFrame
df_anual = pd.DataFrame(df_anual)
df_anual.columns = ['Valores']
df_anual

df_anual.describe()

# count = Número de observações no conjunto de dados
# mean = Número de observações no conjunto de dados
# std = O desvio padrão. Mede a dispersão dos dados em relação à média. Quanto maior, mais espalhados os valores estão
# min = O menor valor do conjunto de dados
# 25% = O primeiro quartil. 25% dos dados estão abaixo deste valor
# 50% = A mediana. 50% dos dados estão abaixo deste valor
# 75% = O terceiro quartil. 75% dos dados estão abaixo deste valor
# max = O maior valor do conjunto de dados

index_anual = pd.date_range(
    start="1980",
    periods = len(df_anual),    
    freq="AS") #A ou AS
index_anual

#index_mensal = pd.date_range(
#    start="1980-01",
#    end="2015-12",
#    freq = 'M') M ou MS
#index_mensal

serie_index = pd.Series(df_anual['Valores'].values, index = index_anual)
serie_index.plot()

### Customizando o gráfico ###
### Título
ax.set_title("Série Temporal Anual", color="white", fontsize=14)

### Fundo
ax.set_facecolor("black")             # fundo da área do gráfico
ax.figure.set_facecolor("black")      # fundo da figura

### Cor da linha
ax = serie_index.plot(color="cyan")   

### Eixos
ax.tick_params(colors="white") # Valores
ax.xaxis.label.set_color("white") # Eixo x
ax.yaxis.label.set_color("white") # Eixo y
for spine in ax.spines.values():
    spine.set_color("white") # Bordas

plt.show()

######################
### Autocorrelação ###
######################

np.random.seed(6)
dados1 = np.random.normal(0,1,72)
dados1

serie = pd.Series(dados1)
serie.plot()
plt.show()

## FAC ###
plot_acf(serie, lags=15)
plt.show()

## FACP ###
plot_pacf(serie, lags=30)
plt.show()

#########################
### Passeio Aleatório ###
#########################

from random import sample, random

# Série Passeio aleatório 1
# Criando dados
dados_alet = sample(range(100), k=41) # k -> valores retirados de 100
dados_alet

# Criando período
periodo = list(range(1980, 2021))
periodo

serie_alet = pd.Series(dados_alet, index = periodo)
serie_alet
serie_alet.plot()
plt.show()

## Série Passeio aleatório 2
# Criando dados
serie2 = list()
serie2.append(-1 if random() < 0.5 else 1)
for i in range(1, 1000):
    movimento = -1 if random() < 0.5 else 1
    valor = serie2[i-1] + movimento
    serie2.append(valor)

serie2 = pd.Series(serie2)
serie2.plot()
plt.show()

##############
### Testes ###
##############

### Testes de Normalidade ###
# - H0: resíduos normalmente distribuídos (p > 0.05)
# - H1: resíduos não são normalmente distribuídos (p <= 0.05)
stats.shapiro(serie1)

### Testes de Estacionaridade ###
# Teste pp (Philips-Perron)
# - H0 = é estacionária: p > 0.05
# - H1 = não é estacionária: p <= 0.05
pp_test = sm.phillips_perron(serie1)

# Renomendando saídas 
pp_test_output = {'Estatítica do teste': pp_test[0], 'p-value': pp_test[1], 'Número de lags': pp_test[2], 'Número de Observações': pp_test[3], 'Valores Críticos': pp_test[4]}
pp_test_output

### Teste Kwiatkowski-Phillips-Schmidt-Shin ###
# - H0 = é estacionária: teste estatístico < valor crítico
# - H1 = não é estacionária: teste estatístico >= valor crítico
kpss_test = sm.kpss(serie1)

kpss_test_output = {'Estatítica do teste': kpss_test[0], 'p-value': kpss_test[1], 'Número de lags': kpss_test[2], 'Valores Críticos': kpss_test[3]}
kpss_test_output

### Teste Dickey Fuller ###
# - H0 = é estacionária:  teste estatístico < valor crítico
# - H1 = não é estacionária: teste estatístico > valor crítico
df_test = sm.adfuller(serie1)

df_test_output = {'Estatítica do teste': df_test[0], 'p-value': df_test[1], 'Número de lags': df_test[2], 'Número de Observações': df_test[3], 'Valores Críticos': df_test[4]}
df_test_output

### Testes de Autocorrelação (Ljung-Box ) ###
# - H0: não autocorrelacionados (p > 0.05)
# - H1: são autocorrelacionados (p <= 0.05)
ljung_box_test = sm.stats.acorr_ljungbox(serie1, lags=[10], return_df=True)
ljung_box_test










# Selecionando o Período 
# data = np.array('2015-01', dtype = np.datetime64())
# data = data + np.arange(72)
# data = pd.DataFrame(data)
# data.columns = ['data']
# data

# Combinando valores
# serie2 = pd.concat([data, dados], axis=1)
# serie2

# serie2 = pd.Series(serie2['valores'].values, index = serie2['data'])
# serie2
# serie2.plot()
# plt.show()

# Criando dados aleatórios (Série Diária)
# np.random.seed(12)
# dados = np.random.normal(0,1,731)
# dados = pd.DataFrame(dados)
# dados.columns = ['valores']
# dados

# Selecionando o Período 
# data = pd.date_range('2019 Jan 1', periods = len(dados3), freq = 'D'
# data

# serie3 = pd.Series(dados['valores'].values, index = data)
# serie3.plot()
# plt.show()

# Tabela 
dados = pd.DataFrame(dados)
dados.columns = ['valores']
dados
dados.shape # verificando valores

# Gráfico 
serie = pd.Series(dados)
serie.plot()
plt.show()

# Selecionando o Período 
periodo = pd.date_range('2000', periods = len(dados), freq = 'Y')
periodo

serie1 = pd.Series(dados['valores'].values, index = periodo)
serie1.plot()
plt.show()

### Case Manchas Solares ###

manchas_solares = sm.datasets.sunspots.load_pandas().data
manchas_solares

serie_m = pd.Series(manchas_solares['SUNACTIVITY'].values, index = manchas_solares['YEAR'])
serie_m

serie_m.plot()

plot_acf(serie_m, lags=45)
plt.show()

plot_pacf(serie_m, lags=30)
plt.show()

####################
### Decomposição ###
####################

concentracao = sm.datasets.co2.load_pandas().data
concentracao

serie = pd.Series(concentracao['co2'].values, index = concentracao.index)
serie

serie.plot()
plt.show()

# Valores missing
concentracao.isnull().sum()
concentracao.dropna(inplace=True)

serie2 = pd.Series(concentracao['co2'].values, index = concentracao.index)
serie2.plot()
plt.show()

decomposicao = decompose(serie2, period=15)
decomposicao = decompose(serie2)

decomposicao.plot()
plt.show()

# Renomeando Labels
plt.subplot(411)
plt.plot(serie, label='Original')
plt.legend(loc='best')
plt.subplot(412)
plt.plot(decomposicao.trend, label='Tendência')
plt.legend(loc='best')
plt.subplot(413)
plt.plot(decomposicao.seasonal,label='Sazonalidade')
plt.legend(loc='best')
plt.subplot(414)
plt.plot(decomposicao.resid, label='Resíduos')
plt.legend(loc='best')
plt.tight_layout()
plt.show()

# Decomposição multiplicativa
decomp_mult = decompose(serie2,period=7,model='multiplicative')
decomp_mult.plot()

decomp_mult.plot()
plt.show()

####################################
### Tranformação e Diferenciação ###
####################################

##################
### Suavização ###
##################
