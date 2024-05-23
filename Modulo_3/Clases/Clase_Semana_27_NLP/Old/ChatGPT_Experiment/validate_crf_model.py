
import pickle
import sklearn_crfsuite
from sklearn_crfsuite import metrics

# Cargar el modelo entrenado
with open("crf_model.pkl", "rb") as f:
    crf = pickle.load(f)

# Suponiendo que los datos de prueba se llaman X_test.pkl y y_test.pkl
# Cargar los datos de prueba
with open("X_test.pkl", "rb") as f:
    X_test = pickle.load(f)

with open("y_test.pkl", "rb") as f:
    y_test = pickle.load(f)

# Predecir las etiquetas para los datos de prueba
y_pred = crf.predict(X_test)

# Calcular y mostrar métricas de rendimiento
print("Precision:", metrics.flat_precision_score(y_test, y_pred, average="weighted"))
print("Recall:", metrics.flat_recall_score(y_test, y_pred, average="weighted"))
print("F1-Score:", metrics.flat_f1_score(y_test, y_pred, average="weighted"))

