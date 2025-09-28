########################
### Install Packages ###
########################

packages <- c("magrittr","httpgd","mFilter","BCDating","rio","timetk","pdftools","textdata","tm",
"tidytext","dplyr","tidyverse","tidyr","ggplot2","readr","readxl","forecast","zoo","lubridate",
"ipeadatar","sidrar","GetBCBData","PNADcIBGE","survey","dygraphs","tseries","quantmod",
"Quandl","discreteRV","aTSA","fGarch","fUnitRoots","vars","MTS","seasonal","stats","nortest",
"scales","urca","dlm","seasonalview","stringr","fma","languageserver","PerformanceAnalytics",
"jsonlite","purrr","curl)")

packages_install <- packages [!packages %in% installed.packages()[,"Package"]]
if(length(packages_install) > 0)
{install.packages(packages_install)} else {message("Todos os pacotes já estão instalados.")}

#####################
### Load Packages ### 
#####################

lapply(packages, library, character.only = TRUE)

####################
## Álgebra Linear ##
####################

"Campo da matemática que trabalha com equações lineares e funções lineares que são 
representadas através de matrizes e vetores."

# Tópicos
# - Sistemas de Equações Lineares.
# - Vetores = Representação matemática de uma grandeza vetorial (Módulo, Direção e Sentido)
# - Matrizes
# - Determinantes
# - Espaços vetoriais
# - Transformações lineares
# - Autovalores e Autovetores

# Grandezas
# - Escalar = Só necessita do seu valor para representar a grandeza (Tempo, Massa, Temperatura)
# - Vetorial = Necessita de módulo, direção e sentindo (Força, Velocidade, Aceleração)

#############
## VETORES ##
#############

#Criando um vetor
vetor <- c(1,2,3,4,5,6,7)
class(vetor)

dias <- c("segunda", "terca", "quarta", "quinta", "sexta", "sábado", "domingo")
class(dias)

#Juntando os dois vetores
juntando <- c(vetor, dias)
juntando
class(juntando)
length(juntando) #tamanho

#Colocando em ordem crescente
gastos_dia <- c(300, 400, 5000, 150, 250)
ordem_crescente <- sort(gastos_dia)
ordem_crescente

#Soma dos valores do vetor
total <- sum(gastos_dia) 
total

#Mínimo
minimo <- min(gastos_dia)
min(gastos_dia)

#Máximo
max(gastos_dia)
maximo <- max(gastos_dia)

#Média
media <- mean(gastos_dia)
mean(gastos_dia)

#Limite
limite <- (gastos_dia <= 300)
limite

#Intervalo
intervalo <- (3:8)
intervalo

#Sequência
passo <- seq(2,48,by=5)
passo

#Repetição
repeticao <- rep(2,8)
repeticao

#Repetição Multipla
repeticao_multipla <- rep(c(3,5),c(4,6))
repeticao_multipla

#Repetição Programada
repeticao_programada <- rep(3:5, each = 3)
repeticao_programada

repeticao_programada_2 <- rep(3:6,3)
repeticao_programada_2

##########################
## OPERAÇÕES DE VETORES ##
##########################

u <- c(2,-4,1)
print(u)

v <- c(3,2,-5)
print(v)

#Soma
soma <- u + v
soma

#Produto
produto <- u * v
produto

#Produto Interno (soma do produto)
produto_interno <- u %*% v
produto_interno

#Multiplicação Escalar
multiplicacao <- 5*u
multiplicacao

multiplicacao2 <- 3*v
multiplicacao2

produto_interno <- (5*u) %*% (3*v)
produto_interno 

#Norma
norm(u, type="2")
norm(v, type="2")

w = c(2,4,6,8,10,12)
norm(w, type="2")
round(norm(w, type="2"),3) #forma resumida

#Distância
# Criando Função Distância
dist <- function (vetor1, vetor2) {
  soma_quad = 0
  for (i in 1:length(vetor1)){
    soma_quad = soma_quad+(vetor1[i] - vetor2[i])**2}
  dist = soma_quad**(1/2)
}

# Calculando a distância entre vetores
distancia <- dist(u,v)
print(paste0("A distância entre os vetores: ", round(distancia, 2)))

##############
## MATRIZES ##
##############