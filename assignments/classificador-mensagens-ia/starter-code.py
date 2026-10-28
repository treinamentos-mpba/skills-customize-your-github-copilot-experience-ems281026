# Código Inicial: Classificador de Mensagens com IA

from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline


data_path = Path(__file__).with_name("messages.csv")
messages = pd.read_csv(data_path)

X_train, X_test, y_train, y_test = train_test_split(
    messages["mensagem"],
    messages["categoria"],
    test_size=0.25,
    random_state=42,
    stratify=messages["categoria"],
)

model = Pipeline(
    [
        ("text", TfidfVectorizer()),
        ("classifier", LogisticRegression(max_iter=1000, random_state=42)),
    ]
)

model.fit(X_train, y_train)
predictions = model.predict(X_test)

print("Relatório de classificação:")
print(classification_report(y_test, predictions, zero_division=0))
print("Matriz de confusão:")
print(confusion_matrix(y_test, predictions, labels=["legitima", "spam"]))

# Tarefas:
# - Acrescente mensagens fictícias variadas a messages.csv.
# - Compare configurações sem alterar a divisão entre treino e teste.
# - Examine previsões incorretas e registre os limites do classificador.
