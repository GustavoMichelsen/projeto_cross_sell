<img src="https://gustavomichelsen.github.io/portifolio_projetos/images/fulls/04.jpg" alt="" />

## Projeto Health Insurance Cross Sell
O objetivo deste projeto foi prever a probabilidade de um cliente adquirir um novo produto. Essa informação permite identificar quais clientes têm interesse no novo produto e quais não têm. Com esses dados em mãos, os gestores da empresa podem direcionar seus esforços de vendas de forma mais eficiente.

A entrega desse projeto é realizada por meio de uma API. No vídeo que pode ser acessado pelo link abaixo, apresento os resultados para o negócio e demonstro como desenvolvi essa solução.

[YouTube](https://www.youtube.com/embed/mHOuzAENaBk)

Para demonstrar a resposta da API, criei uma planilha disponível no link abaixo. No entanto, é importante ressaltar que as informações geradas pela API podem ser integradas a qualquer sistema existente na empresa.

[Planilha Google Sheets](https://docs.google.com/spreadsheets/d/1l1-B-_nI68OW3eXZL-8ofAkRY_5pEP_RPTru8iQrkVI/edit#gid=0)

Caso queira fazer uma consulta diretamente na API, você pode utilizar o endereço abaixo passando os seguintes parâmetros:

Base URL: https://cross-sell-classification.onrender.com/cross_sell/predict

#### Parametros Passados

<ul>
  <li>{"id": “qualquer valor”, </li>
  <li>"Gender": “Male”, “Female”, </li>
  <li>"Age": “18 - ... – 85”, </li>
  <li>"Driving_License": “0, 1”, 0 = Não tem CNH, 1 = Tem CNH</li>
  <li>"Region_Code": “0 - ... – 52”, </li>
  <li>"Previously_Insured": “0, 1”, 0 = Não sofreu acidente, 1 = Sofreu acidente</li>
  <li>"Vehicle_Age": “> 2 Years”, “1-2 Year”, “< 1 Year”, </li>
  <li>"Vehicle_Damage": “Yes”, “No”, </li>
  <li>"Annual_Premium": “2630 - ... – 540 000”, </li>
  <li>"Policy_Sales_Channel": “10 - ... – 152”, </li>
  <li>"Vintage": “10 - ... – 299”}</li>
</ul>

#### Parametros Retornados

<ul>
  <li>{"id": , </li>
  <li>"Gender": , </li>
  <li>"Age": , </li>
  <li>"Driving_License": ,</li>
  <li>"Region_Code": , </li>
  <li>"Previously_Insured": ,</li>
  <li>"Vehicle_Age": , </li>
  <li>"Vehicle_Damage": , </li>
  <li>"Annual_Premium": , </li>
  <li>"Policy_Sales_Channel": , </li>
  <li>"Vintage": ,</li>
  <li>"Classification": }</li>
</ul>

A seguir você poderá entender mais a respeito de desenvolvimento desse projeto.

### Detalhes do Projeto

#### Premissas de Negócio – O que se procurou resolver?
O problema fictício se baseia em uma empresa de seguros de saúde que está expandindo seu portfólio de produtos, incluindo o seguro automotivo como um dos seus serviços. Para entender o interesse do público, a equipe de marketing realizou uma pesquisa de interesse com aproximadamente 380 mil clientes.

No entanto, a empresa não possui recursos suficientes para entrar em contato com todos os clientes em sua base. Portanto, o diretor de marketing e vendas solicitou uma solução que permita otimizar o direcionamento desses recursos de forma mais eficiente.

### Planejamento da Solução

##### Qual o plano utilizado para resolver o problema?

<ul>
  <li>Coleta dos dados - Fiz no https://www.kaggle.com/;</li>
  <li>Limpeza dos dados – Verifiquei se havia algum dado a ser ajustado;</li>
  <li>Criação de novas Features – Criei novas features baseadas nas originais;</li>
  <li>Seleção de colunas – Excluí colunas que eu não iria mais precisar ou de dados que eu não utilizaria;</li>
  <li>Exploração dos dados – Explorei os dados buscando entender o fenômeno e gerar Insigths;</li>
  <li>Preparação dos dados – Preparei os dados para o treinamento dos algoritmos de Machine Learning;</li>
  <li>Seleção das Features mais relevantes – Para isso utilizei o algoritmo Boruta;</li>
  <li>Treinamento dos algoritmos de Machine Learning – Treinei 3 tipos de algoritmos de Machine Learning para poder comprar o desempenho de cada um deles, escolhendo por fim o melhor;</li>
  <li>Ajuste dos hiperparâmetros do modelo – Testei o modelo escolhido com diferentes hiperparâmetros e comparei os resultados;</li>
  <li>Treinamento do modelo de Machine Learning – Treinei o modelo com os hiperparâmetros que apresentaram o melhor desempenho;</li>
  <li>Análise dos resultados – Levantei os resultados financeiros do projeto para empresa e comparei os resultados obtidos com os dados originais para descobrir a confiabilidade do modelo;</li>
  <li>Criação da API – Criei e testei a API.</li>
</ul>

### Principais Insights de dados
<ul>
  <li>Pessoas com idade entre 40 e 49 anos tem maior probabilidade de adquirir um seguro automotivo;</li>
  <li>Pessoas com carro entre 1 e 2 anos de uso tem maior probabilidade de adquirir um seguro.</li>
</ul>

### Resultados financeiros para o negócio

Com a implementação desse modelo em produção, a empresa poderá obter uma economia significativa no contato com seus clientes, pois o contato será direcionado, priorizando aqueles que têm maior interesse em adquirir um seguro automotivo.

O gráfico abaixo ilustra esse cenário, demonstrando que com aproximadamente 20% do conjunto de dados, é possível acertar cerca de 57% dos clientes interessados. Já com 40% do conjunto de dados, é possível identificar aproximadamente 90% dos clientes interessados.

<img src="https://gustavomichelsen.github.io/portifolio_projetos/images/fulls/04-2.jpg" alt="" />

Esses resultados destacam a eficácia do modelo na segmentação dos clientes e na otimização dos recursos de contato, permitindo à empresa focar em abordar diretamente os clientes com maior probabilidade de adquirir o seguro automotivo. Isso proporcionará uma abordagem mais eficiente e aumentará as chances de sucesso nas vendas.

### Lições aprendidas
Uma das principais lições que aprendi com esse projeto foi a importância de utilizar as métricas corretas para avaliar modelos de aprendizado de máquina. No caso deste projeto, minha prioridade foi alcançar a maior precisão possível.

Outra lição importante foi a necessidade de comunicar os resultados de forma eficaz, mostrando para a equipe de negócios o valor que pode ser alcançado com base nas decisões que eles tomarem.

Ao enfatizar a importância da precisão do modelo, posso garantir que as previsões sejam mais confiáveis e úteis para a empresa. Além disso, ao comunicar os resultados de maneira clara e compreensível, posso fornecer informações valiosas para a equipe de negócios, permitindo que eles tomem decisões informadas com base nos insights fornecidos pelo modelo.

Essas lições me ajudaram a entender a importância de selecionar as métricas adequadas para cada projeto e de estabelecer uma comunicação eficiente para que os resultados sejam compreendidos e aplicados corretamente no contexto empresarial.

### Próximos passos
Entre os próximos passos, está o aprofundamento do seu conhecimento sobre o negócio de seguros automotivos. Isso permitirá uma compreensão mais aprofundada dos aspectos específicos desse setor e ajudará a aprimorar ainda mais o modelo de produção.

Uma possibilidade interessante é buscar novas características relevantes para o conjunto de dados, o que pode enriquecer o modelo e melhorar sua capacidade de previsão. A incorporação de variáveis adicionais, como informações demográficas dos clientes, histórico de sinistros, dados econômicos e outros fatores relevantes para o setor de seguros automotivos, pode ser uma abordagem promissora.

Além disso, existem outros projetos relacionados que podem ser desenvolvidos para agregar valor à empresa. Por exemplo, a avaliação de risco do cliente é uma área importante, pois permite identificar os perfis de risco dos clientes e tomar medidas preventivas ou personalizar as ofertas de seguros com base nesses dados. A análise da elasticidade do preço é outra área interessante, pois ajuda a compreender como a demanda por seguros automotivos é

### Contatos
<p> Email: gtv.michelsen@gmail.com
<br> Linkedin: <a href="https://www.linkedin.com/in/gustavo-michelsen-30946a223/"> Clique aqui!!! </a> </p>
