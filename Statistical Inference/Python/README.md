## Introdução
- Download Python: https://www.python.org/downloads/
- Comunidade: https://www.python.org/community/forums/

> Python is a programming language created by Guido van Rossum, a Dutch programmer, in 1991. Guido van Rossum created the language with the goal of developing simple, intuitive and easy-to-learn programming, without sacrificing the ability to solve complex problems. The name "Python" was inspired by the British comedy group "Monty Python", of which van Rossum was a fan.

## R Language
- Download R: https://cran.r-project.org/bin/windows/base/
- Comunidade: https://rpubs.com/

> R is an open-source programming language for statistical computing, widely used in data analysis. The language was created by Ross Ihaka and Robert Gentleman at the University of Auckland, New Zealand, in the early 1990s. They were motivated by the desire to develop a programming language that was powerful for statistical analysis and at the same time accessible and flexible.

### Setting up R for use in Visual Studio Code

```
# Run in the R terminal
install.packages("languageserver")
install.packages("httpgd")
```

```

    "editor.suggest.showSnippets": false,
    "editor.quickSuggestions": {"comments": "on", "strings": "on","other": "on"}
# Preferences (Open User Settings (JSON)
"editor.quickSuggestions.other": false
r.lsp.diagnostics": false
"r.plot.useHttpgd": true
```

### Introdução 



#### Data Types

Qualitative (non-numeric attributes).
- Nominal: Denominations (colors, gender, race, titles, etc.)
- Ordinal: attributes that can be classified (e.g., ranking of most-watched movies, level of education, level of satisfaction, etc.).

Quantitative (numerical attributes).
- Discrete: finite or enumerable values ​​(number of people in a room, number of cars in a parking lot, etc.)
- Continuous: infinite possible values ​​in an interval (income, time, height, etc.).

#############################
### Tipo Básico do Objeto ###
#############################

# Graficamente
fig = px.pie(relacao, names="cs_sexo")
fig.show()

filmes.dtypes()

# int: Tipo inteiro da biblioteca NumPy. Esse tipo de dado não tem suporte a valores ausentes.
# int64: Numero nulo inteiros do Pandas.
# float64: Numero de ponto flutuante da biblioteca NumPy. Esse tipo de dado suporta valores ausentes.
# object: Com esse tipo de dados você trabalhar com sequencias de caracteres. Esses caracteres podem ser números ou letras.
# category: Tipo categórico da biblioteca Pandas.
# bool: Tipo booleano da biblioteca NumPy. Esse tipo de dado não suporta dados ausentes.
# boolean: Tipo booleano que suporta valor nulo.
# datetime64: Tipos data da biblioteca NumPy. Esse tipo aceita valores ausentes.

base_credit.head(10)
base_credit.tail(8)

##########################
### Visualizando Dados ###
##########################

base_credit = pd.read_csv("C:\Users\henri\OneDrive\Repositórios\Python\Datasets\credit_risk_dataset.csv")
base_credit

# default 
# 0 = paga por empréstimo
# 1 = não paga o empréstimo

base_credit.info()
base_credit.describe()
# count  
# mean -> média  
# std -> desvio padrão      
# min -> valor mínimo    
# 25% -> 1 quartil
# 50% -> 2 quartil/mediana
# 75% -> 3 quartil
# max -> valor máximo

# trazendo o cliente com a maior/menor renda
base_credit[base_credit['income'] >= 69995.685578]
base_credit[base_credit['income'] <= 20014.489471]

# visualizando dados default 
np.unique(base_credit['default'], return_counts=True)
# array [1717, 283]
# pagam o empréstimo -> 1717
# não pagam o empréstimo -> 283

sns.countplot(x = base_credit['default'])

# gráfico de correlção das variáveis
grafico = px.scatter_matrix(base_credit, dimensions=['age', 'income', 'loan'], color = 'default')
grafico.show()

#########################################
### Tratamento Valores Inconsistentes ###
#########################################

# quantidade de registros
base_credit.shape  

# idades menores que zero
base_credit.loc[base_credit['age'] < 0]
# observa-se 3 valores inconsistentes, então:
# 1) Apagar eles
# 2) Apagar a variável
# 3) Substituir pela média

# 1) Apagar eles
base_credit_1 = base_credit.drop(base_credit[base_credit['age'] < 0].index)
base_credit_1

base_credit_1.loc[base_credit['age'] < 0]

# 2) Apagar a variável (coluna)
base_credit_2 = base_credit.drop('age', axis = 1)
base_credit_2

# 3) Substituir pela média
base_credit.mean()
base_credit['age'].mean()
base_credit.loc[base_credit['age'] < 0, 'age'] = 40.92
base_credit.loc[base_credit['age'] < 0]

####################################
### Tratamento Valores Faltantes ###
####################################

# Verificando valores nulos
base_credit.isnull().sum() # quantidade de valores NaN
base_credit.loc[pd.isnull(base_credit['age'])] # quais são os clientes com NaN

# Eliminando valores nulos
base_credit= base_credit.dropna(inplace=True)  
base_credit.isnull().sum()  

# Preenchendo valores nulos com a média
base_credit['age'].fillna(base_credit['age'].mean(), inplace = True)

base_credit.loc[[29]]
base_credit.loc[[31]]
base_credit.loc[[32]]

# Exportar como CSV
base_credit.to_csv('credit_risk_dataset.csv')

#########################################
### Divisão entre previsores e classe ###
#########################################

base_credit

# Criando um vetor com as variáveis explicativas
X_credit = base_credit.iloc[:, 1:4].values
X_credit

# Criando um vetor com a variável dependente
y_credit = base_credit.iloc[:, 4].values
y_credit

# Visualizando dados
X_credit[:,0].min() 
X_credit[:,1].min() 
X_credit[:,2].min()

# Realizando normalização/padronização
scaler_credit = StandardScaler()
X_credit = scaler_credit.fit_transform(X_credit)

X_credit[:,0].min() 
X_credit[:,1].min() 
X_credit[:,2].min()

######################################################
### LabelEncoder (transformar string para numeric) ###
######################################################

base_credit = pd.read_csv("C:/Users/henri/OneDrive/Repositórios/Python/Introdução/Datasets/credit_risk_dataset.csv")
base_credit

label_encoder_teste = LabelEncoder()
X_census[:,1]
teste = label_encoder_teste.fit_transform(X_census[:,1])
teste

label_encoder_workclass = LabelEncoder()
X_census[:,1] = label_encoder_workclass.fit_transform(X_census[:,1])

####################################################
### OneHotEncoder (criação de variáveis dummies) ###
####################################################

onehotencoder_census = ColumnTransformer(transformers=[('OneHot', OneHotEncoder(), [1,3,5,6,7,8,9,13])], remainder='passthrough')
X_census = onehotencoder_census.fit_transform(X_census).toarray()
X_census
X_census.shape

# Limpando colunas não necessárias
dataset.drop(labels=['RL Vale'], axis=1, inplace=True)
dataset.drop(labels=['RL Itau'], axis=1, inplace=True)
dataset.drop(labels=['RL Wege'], axis=1, inplace=True)
dataset.drop(labels=['RS Vale'], axis=1, inplace=True)
dataset.drop(labels=['RS Itau'], axis=1, inplace=True)
dataset.drop(labels=['RS Wege'], axis=1, inplace=True)

dataset
dataset.describe()


# Resertar indice 
dados2 = dados2.reset_index(drop=True) # drop é para excluir o índice anterior
dados2

######################
### Treino e Teste ###
######################

X_credit_treinamento, X_credit_teste, y_credit_treinamento, y_credit_teste = train_test_split(X_credit, y_credit, test_size = 0.25, random_state = 0)

X_credit_treinamento.shape
y_credit_treinamento.shape

X_credit_teste.shape
y_credit_teste.shape

import pickle #salvar em disco

with open('credit.pkl', mode = 'wb') as f:
  pickle.dump([X_credit_treinamento, y_credit_treinamento, X_credit_teste, y_credit_teste], f)
  
with open('census.pkl', mode = 'wb') as f:
  pickle.dump([X_census_treinamento, y_census_treinamento, X_census_teste, y_census_teste], f)

####################
### Naïve Baynes ###
####################