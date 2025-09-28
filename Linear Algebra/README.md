3. Estatística

![435421892-c617cbb7-1da9-4b94-b583-e98f2ae674a0](https://github.com/user-attachments/assets/921125c3-b915-426d-8448-17473013a51c)


> A estatística é definda como a ciência que objetiva coletar, organizar, analisar e interpretar dados. Ela é dividida em 3 partes:

Descritiva é aquela relacionada a descrição dos dados, representada pelas medidas de: centralidade (Média, moda e mediana), posição (Amplitude e Quartis), dispersão (Variância e Desvio Padrão).
Probabilistica é aquela relacionada a conceitos de probabilidades (espaço amostral, eventos) e distribuições de probabilidade discretas e contínuas (Binomial, Poisson, Exponencial e Normal).
Inferencial é aquela relacionada a estimação de parâmetros, intervalo de confiança e testes de hipóteses.
> Outro ponto importante é são as chamadas Técnicas de Amostragem, que são sub-divididas em 4 grupos:

Aleatória Simples: Seleção executada por meio de sorteio, sem nenhum filtro.
Estratificada: Divisão da população em grupos e seleção aleatória de uma amostra de cada grupo. (Ex: divisão por região, classe social, religião…).
Conglomerado (Agrupamento): Divisão da população em grupos com características similares, porém heterogêneas, e seleção aleatória de alguns grupos para analisar todos os elementos destes grupos. (Ex.: Divisão da população de escolas estaduais por região, enfermeiros de uma rede de hospitais… ).
Sistemática: Membros da população são ordenados numericamente e são selecionados aleatoriamente, obedecendo uma sequência numérica. (Ex.: criação de números para cada amostra e seleção obedecendo uma ordem numérica).
3) Testes de hipóteses

> São testes de afirmações sobre um parâmetro. Processo que utiliza estatísticas amostrais para testar uma hipótese (afirmação original) e aceitá-la ou rejeitá-la.

Existem duas hipóteses:

- Hipótese nula (H0)

- Hipótese alternativa (H1):

Tipos de erro

- Erro tipo I: hipótese nula rejeitada quando ela for verdadeira

Erro tipo II: aceita a hipótese nula (não rejeita) sendo ela falsa.
#### Intervalo de confiança

- Intervalo de confiança: Probabilidade de que o parâmetro populacional estimado, esteja no intervalo selecionado.

- Nível de significância: Probabilidade máxima permitida para cometer o erro tipo I.

#### Métricas de Desempenho

Erro absoluto médio (MAE)

![Captura de tela 2023–12–23 220021](https://github.com/HenrySchall/R/assets/96027335/f5bcb70b-8869-46b5-819c-11266879e2b1)

- Oi = valores observados

- Pi = valores previstos

Raiz do erro quadrático médio (RMSE)

#### Outliers

São dados discrepantes, isto é, são dados muito diferentes dos demais dados pertencentes à variável em análise. A relevância deles deve ser analisada para definir se continuarão no dataset ou se devem ser tratados (corrigidos, excluídos ou substituídos), pois se não forem relevantes, podem interferir significativamente nos resultados das análises


 Mínimos Quadrados Ordinários (MQO): Este é o método mais comum de estimativa em regressão linear. O MQO busca minimizar a soma dos quadrados das diferenças entre os valores observados e os valores previstos pelo modelo.

Mínimos Quadrados Generalizados (MQG): Este método é uma extensão do MQO que é utilizado quando as suposições de homocedasticidade (variância constante dos erros) não são atendidas. O MQG leva em conta a estrutura de variância dos erros.

Regressão de Mínimos Quadrados Pesados: Utiliza pesos diferentes para as observações, o que pode ser útil em situações onde algumas observações são mais confiáveis do que outras

Máxima Verossimilha (MV)





### Mínimos Quadrados em 2 Estágios

 assumir que os termos de erro no modelo
 de regressão linear são contemporaneamente não
 correlacionados com as variáveis explanatórias, ou mesmo que
 eles seriam independentes de todas as variáveis explanatórias.1 Com
 efeito, poderíamos interpretar o modelo de regressão linear como
 descrevendo a expectativa condicional de yt, dado um conjunto de
 variáveis xt


Os Mínimos Quadrados em Dois Estágios (MQ2E), = caso onde não podemos assumir exogeneidade das
 variáveis explanatórias, o que implica que os estimadores de MQO
 serão viesados e inconsistentes

 $y =Xβ+ε$


β é um estimador de MQO não viesado para β se estamos
 assumindo que ε possui média zero, dado X, isto é, E {ε|X} = 0.
 Isso implica que o conhecimento sobre qualquer uma das variáveis
 explanatórias não informa nada sobre o valor esperado dos termos
 de erro. 

  Em muitos casos, a hipótese de que ε é independente de X é
 muito forte (erro nao teeem relacao com as variáveix explnatrorias)


 Como exemplo, considere a hipótese de mercados
 eficientes, sob retornos esperados constantes. Essa hipótese implica
 que o retorno de qualquer ativo será imprevisível a partir de
 informações públicas. Sob sua forma fraca, o retorno de ativos não
 pode ser previsto a partir dos retornos passados. A hipótese pode
 ser, aliás, estatisticamente testada, considerando um modelo de
 regressão linear e testando se os retornos passados explicam o
 retorno presente

yt = β1 +β2yt−1 +β3yt−2 +εt

 onde yt denota o retorno no período t, a hipótese nula implica que
 β2 = β3 =0. Dado que as variáveis explanatórias são variáveis
 defasadas (sendo assim função dos termos de erro defasados), a
 premissa de que E {ε|X} = 0 é inapropriada. Se a autocorrelação
 nos termos de erro for, de algum modo, restringida, será ainda
 possível fazer inferência de modo apropriado, utilizando a estimativa
 de Newey-West para a matriz de covariância


  Observe, ademais, que mesmo que consideremos a hipótese de que
 E {εtxt} = 0, isto é, que os termos de erro e as variáveis
 explanatórias não são contemporaneamente correlacionadas, haverá
 casos em que isso não será necessariamente válido. Para esses, não
 mais poderemos dizer que o estimador de MQO será não viesado e
 consistente. Exemplos desses casos são: presença de variáveis
 dependentes defasadas e correlacionadas com o termo de erro, erros
 de medida e simultaneidade ou endogeneidade dos regressores.
 Vamos tratar a seguir do último e mais interessante caso

também conhecidos como Two-Stage Least Squares (2SLS), são uma técnica utilizada em econometria para estimar modelos de regressão quando há endogeneidade nas variáveis explicativas. A endogeneidade pode ocorrer quando uma variável independente está correlacionada com o erro do modelo, o que pode levar a estimativas viesadas e inconsistentes.


Viés = O problema de viés gerado por variável omitida aparece se uma
 variável explanatória relevante, correlacionada com os regressores
 incluídos, é omitida do modelo  Esse viés é particularmente preocupante
 quando estamos interessados em fazer uma interpretação
 causal dos nossos coeficientes estimados

 yi = x1iβ1 + x2iβ2 + uiγ +vi

 onde, yi é o salário em log de um determinado indivíduo, x1i é um
 vetor de características individuais, incluindo o intercepto e x2i
 denota anos de escolaridade. Ademais, ui é uma variável não
 observado que reflete a habilidade de um determinado indivíduo.
 Pessoas com níveis elevados de habilidade tendem a possuir salários
 mais altos (γ > 0), mas também mais prováveis de terem maior
 escolaridade.

  Assim, podemos esperar que cov {x2i,ui} > 0. Dado que ui é não
 observado, o econometrista irá estimar


yi = x′iβ +εi,

 Assumindo E {xiei} = 0, isso nos permite mostrar que o limite de
 probabilidade para b é dado por

habilidade não obseervacvel  a habilidade não observada deveria
 ser não correlacionada com a escolaridade e as demais
 variáveis do modelo

Causalidade inversa
Uma outra forma do problema de endogeneidade é a causalidade
 reversa


 Isto é, não apenas xi possui impacto sobre yi, como ao
 mesmo tempo yi tem impacto sobre um ou mais elementos de xi,
 como x2i. Por exemplo, o nível de criminalidade em uma
 determinada cidade será afetada pelo quantidade de dinheiro gasto
 no cumprimento da lei, enquanto funcionários públicos podem
 decidir aumentar o orçamento da segurança em função do nível
 esperado de criminalidade. Estimar o impacto causal da aplicação
 da lei sobre o nível de criminalidade usando uma amostra de corte
 transversal estará assim sujeito ao viés de endogeneidade

Se considerarmos uma equação
 onde um ou mais variáveis explanatórias são determinadas
 conjuntamente com a variável do lado esquerdo (a variável
 independente), o estimador de MQO proverá estimativas
 inconsistentes para os parâmetros comportamentais.


Variáveis instrumentais

 De forma a contornar o problema da endogeneidade, podemos
 deixar a variável não observada no termo de erro, mas ao
 invés de estimar o modelo por MQO, nós fazemos uso de um
 método de estimação que reconhece a presença da variável
 omitida. É basicamente isso que o método de variáveis
 instrumentais faz. Variáveis instrumentais são, a propósito, uma
 poderosa ferramenta para identificar e estimar relações causais


  Para ilustrar, considere o modelo simples de regressão linear abaixo
 especificado
 y =β0+β1x +u

 O estimador de MQO para o parâmetro de inclinação é dado por
 ˆ
 βMQO = Cov(x,y) / Var(x)

 Se supormos, por suposto, que o regressor x é correlacionado com o
 termo de erro u, esse estimador será viesado e inconsistente.

  Se tivermos um instrumento válido z, nós podemos estimar β1 de
 forma consistente usando o estimador de variáveis instrumentais
 ˆ
 βIV =Cov(z,y) / Cov(z,x)

 Isto é, um instrumento válido é correlacionado com o regressor
 x, o que implica que o denominador de 11 é diferente de zero.
 Ele também deve ser não correlacionado como o termo de
 erro u.

Método de Momentos Generalizados (GMM)

introducao - chtgpt

 Diversos métodos tais como mínimos quadrados, máxima
 verossimilhança ou variáveis instrumentais podem ser vistos como
 baseados em algumas condições de momento, o que faz deles um
 caso especial do GMM.

  Como expõe Bueno [2011], O Método dos Momentos
 Generalizado (GMM) minimiza uma função representando as
 condições de momento devidamente ponderadas. Se essas condições
 de momentos estiverem corretas, terão média 0. Isso conduz a um
 teste de superidentificação usando o valor minimizado da função.
 Trata-se do teste j, definido como

 J =TgT(w,θ)sⁿ-1gT(w,θ) ∼ χ2m−k




<<<<<<< HEAD
=======





- Teoria Econômica & Econometria
> Por meio da Econometria é possível avaliar empiricamente a teoria econômica e explicar fatos passados, testar hipóteses, prever resultados de políticas ou eventos futuros e estimar relações entre variáveis econômicas. Isso é viável porque, em geral, há relações de equilíbrio de longo prazo entre variáveis econômicas.

Etapa da Ciência de Dados
1) Coleta de Dados: Envolve a obtenção de dados de diversas fontes, como bancos de dados, APIs, sensores, e web scraping.
2) Limpeza e Preparação de Dados: Os dados coletados frequentemente contêm erros, valores ausentes ou inconsistências. A limpeza e a preparação são etapas cruciais para garantir a qualidade dos dados.
3) Análise Exploratória de Dados (EDA): Consiste em explorar os dados para entender suas características, padrões e tendências, utilizando visualizações e estatísticas descritivas.
4) Modelagem: Envolve a aplicação de algoritmos de machine learning e estatística para criar modelos preditivos ou descritivos. Isso pode incluir regressão, classificação, clustering, entre outros.
5) Avaliação de Modelos: Após a modelagem, é importante validar a eficácia do modelo utilizando métricas apropriadas de desempenho, monitorado e ajustado o modelo conforme necessário.
6) Resultados: A capacidade de comunicar insights de forma clara e eficaz é fundamental. Isso pode incluir a criação de relatórios, dashboards e apresentações.

Exemplos de campos da econometria:

Econometria básica (regressão linear múltipla, …)
Econometria de séries temporais (AR, MA, ARMA, ARIMA, ARCH, GARCH, VAR, VEC, …)
Econometria não-paramétrica (regressão não-paramétrica, ….)
Microeconometria (dados em painel, …)
- Macroeconometria (DSGE, DSGE-VAR, VAR, VEC, …)

2. Estrutura dos dados econômicos

> Os dados econômicos apresentam-se em uma variedade de tipos. Embora alguns métodos econométricos possam ser aplicados com pouca ou nenhuma modificação para muitos tipos de informações, as características especiais de alguns dados devem ser consideradas ou deveriam ser exploradas. Descreveremos a seguir as estruturas de dados mais importantes encontradas nos trabalhos aplicados.

Corte Transversal: Um conjunto de dados de corte transversal consiste em uma amostra de indivíduos, consumidores, empresas, cidades, estados, países ou uma variedade de outras unidades, tomada em um determinado ponto no tempo, sendo assim não podemos considerar que eles foram obtidos por uma amostra aleatória, os dados das unidades não precisam corresponder ao mesmo período e a ordenação dos dados não importa para a análise econométrica.
Série Temporal: Um conjunto de séries temporais consiste em observações sobre uma variável ou muitas variáveis ao longo do tempo. Exemplos de dados de séries temporais incluem preços de ações, oferta de moeda, índice de preços ao consumidor, produto interno bruto, taxas anuais de homicídios e números de automóveis vendidos. Sendo assim, podemos considerar que eventos passados podem influenciar eventos futuros e a ordenação cronológica das observações transmite informações importantes.
Dados em Painel: Um conjunto de dados em painel consiste em uma série temporal para cada registro de corte transversal. Como exemplo, suponha que tenhamos o histórico de salário, educação e emprego para um conjunto de indivíduos ao longo de um período de dez anos. Sendo assim, as mesmas unidades de corte transversal são acompanhadas ao longo de um determinado período e a ordenação no corte transversal de um conjunto de dados em painel não é importante.
3. Estatística

> A estatística é definda como a ciência que objetiva coletar, organizar, analisar e interpretar dados. Ela é dividida em 3 partes:

Descritiva é aquela relacionada a descrição dos dados, representada pelas medidas de: centralidade (Média, moda e mediana), posição (Amplitude e Quartis), dispersão (Variância e Desvio Padrão).
Probabilistica é aquela relacionada a conceitos de probabilidades (espaço amostral, eventos) e distribuições de probabilidade discretas e contínuas (Binomial, Poisson, Exponencial e Normal).
Inferencial é aquela relacionada a estimação de parâmetros, intervalo de confiança e testes de hipóteses.
> Outro ponto importante é são as chamadas Técnicas de Amostragem, que são sub-divididas em 4 grupos:

Aleatória Simples: Seleção executada por meio de sorteio, sem nenhum filtro.
Estratificada: Divisão da população em grupos e seleção aleatória de uma amostra de cada grupo. (Ex: divisão por região, classe social, religião…).
Conglomerado (Agrupamento): Divisão da população em grupos com características similares, porém heterogêneas, e seleção aleatória de alguns grupos para analisar todos os elementos destes grupos. (Ex.: Divisão da população de escolas estaduais por região, enfermeiros de uma rede de hospitais… ).
Sistemática: Membros da população são ordenados numericamente e são selecionados aleatoriamente, obedecendo uma sequência numérica. (Ex.: criação de números para cada amostra e seleção obedecendo uma ordem numérica).
3) Testes de hipóteses

> São testes de afirmações sobre um parâmetro. Processo que utiliza estatísticas amostrais para testar uma hipótese (afirmação original) e aceitá-la ou rejeitá-la.

Existem duas hipóteses:

- Hipótese nula (H0)

- Hipótese alternativa (H1):

Tipos de erro

- Erro tipo I: hipótese nula rejeitada quando ela for verdadeira

Erro tipo II: aceita a hipótese nula (não rejeita) sendo ela falsa.
#### Intervalo de confiança

- Intervalo de confiança: Probabilidade de que o parâmetro populacional estimado, esteja no intervalo selecionado.

- Nível de significância: Probabilidade máxima permitida para cometer o erro tipo I.

#### Métricas de Desempenho

Erro absoluto médio (MAE)

![Captura de tela 2023–12–23 220021](https://github.com/HenrySchall/R/assets/96027335/f5bcb70b-8869-46b5-819c-11266879e2b1)

- Oi = valores observados

- Pi = valores previstos

Raiz do erro quadrático médio (RMSE)

#### Outliers

São dados discrepantes, isto é, são dados muito diferentes dos demais dados pertencentes à variável em análise. A relevância deles deve ser analisada para definir se continuarão no dataset ou se devem ser tratados (corrigidos, excluídos ou substituídos), pois se não forem relevantes, podem interferir significativamente nos resultados das análises.






### Álgebra Linear 
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



#####
##   COMPARAR VETORES
#####

# Vetores com acessos ao LinkedIn and Facebook
linkedin <- c(16, 9, 13, 5, 2, 17, 14)
facebook <- c(17, 7, 5, 16, 8, 13, 14)

# Dias populares
linkedin > 15
#sum(linkedin > 15)

# Dias com pouco acesso
linkedin <= 5

# Dias em que o LinkedIn foi mais popular que o Facebook
linkedin > facebook

#####
##   COMPARAR MATRIZES
#####

# Matriz com as visualizações do LinkedIn e Facebook
views <- matrix(c(linkedin, facebook), nrow = 2, byrow = TRUE)

rownames(views) <- c("linkedin","facebook")
colnames(views) <- c("Sun","Mon","Tues","Wed","Thur","Fri","Sat")


# Quando as visualizações foram iguais a 13?
views == 13

# Quando as visualizações foram menores ou iguais a 14?
views <= 14

# Com que frequência o Facebook tem visualizações iguais ou superiores às do LinkedIn multiplicado por 2?
testeSoma <- linkedin * 2
testeSoma2 <- sum(facebook >= linkedin * 2)





 Mínimos Quadrados Ordinários (MQO): Este é o método mais comum de estimativa em regressão linear. O MQO busca minimizar a soma dos quadrados das diferenças entre os valores observados e os valores previstos pelo modelo.

Mínimos Quadrados Generalizados (MQG): Este método é uma extensão do MQO que é utilizado quando as suposições de homocedasticidade (variância constante dos erros) não são atendidas. O MQG leva em conta a estrutura de variância dos erros.

Regressão de Mínimos Quadrados Pesados: Utiliza pesos diferentes para as observações, o que pode ser útil em situações onde algumas observações são mais confiáveis do que outras

Máxima Verossimilha (MV)


>>>>>>> 460b46cb4535bcba3da4981fbef7a7cbab1caede
