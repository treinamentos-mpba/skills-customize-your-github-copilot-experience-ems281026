# 📘 Atividade: Classificador de Mensagens com IA

## 🎯 Objetivo

Crie e avalie um classificador de mensagens em português usando aprendizado de máquina. Você vai preparar os dados, medir o desempenho do modelo e analisar erros, vieses e limites antes de considerar qualquer uso real.

## 📝 Tarefas

### 🛠️ Preparar os dados e treinar um modelo

#### Descrição
Use o arquivo `messages.csv`, que contém mensagens fictícias rotuladas como `legitima` ou `spam`. Instale as bibliotecas necessárias com `python -m pip install pandas scikit-learn` e complete e execute o código inicial para separar os dados e treinar um classificador de texto.

#### Requisitos
O programa concluído deve:

- Carregar as colunas `mensagem` e `categoria` do arquivo CSV
- Dividir os dados em conjuntos de treino e teste sem misturar exemplos do teste no treinamento
- Usar `TfidfVectorizer` e `LogisticRegression` em um pipeline de classificação
- Manter a proporção das categorias na divisão e usar `random_state=42` para tornar o resultado reproduzível

### 🛠️ Medir e melhorar o desempenho

#### Descrição
Avalie as previsões no conjunto de teste e faça experimentos para entender como as escolhas de preparação e treinamento afetam os resultados.

#### Requisitos
O programa concluído deve:

- Exibir precisão, recall e F1-score para cada categoria, além da matriz de confusão
- Acrescentar mensagens fictícias variadas até o conjunto ter pelo menos 80 exemplos, sem copiar mensagens reais ou incluir dados pessoais
- Comparar pelo menos duas configurações do modelo ou do texto e registrar qual métrica mudou e por quê
- Usar sempre o mesmo conjunto de teste ao comparar as configurações

### 🛠️ Investigar erros e limites

#### Descrição
Examine mensagens que o modelo classificou incorretamente e considere como os dados e o contexto afetam suas decisões.

#### Requisitos
O programa concluído deve:

- Exibir pelo menos três previsões incorretas, incluindo a categoria correta e a prevista
- Descrever um padrão ou limitação observado nos erros, sem afirmar que o modelo entende o contexto como uma pessoa
- Escrever uma breve nota sobre falsos positivos, falsos negativos, vieses e por que mensagens privadas não devem ser usadas sem autorização
- Explicar por que este modelo de exercício não deve ser usado sozinho para bloquear ou denunciar mensagens reais
