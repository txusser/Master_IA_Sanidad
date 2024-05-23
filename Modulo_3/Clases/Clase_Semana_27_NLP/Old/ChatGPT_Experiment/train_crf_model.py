
import pickle
import sklearn_crfsuite

# Cargar los datos
with open("X_data.pkl", "rb") as f:
    X_data = pickle.load(f)

with open("y_data.pkl", "rb") as f:
    y_data = pickle.load(f)

# Iniciar y entrenar el modelo CRF
crf = sklearn_crfsuite.CRF(
    algorithm='lbfgs',
    c1=0.1,
    c2=0.1,
    max_iterations=100,
    all_possible_transitions=True
)
crf.fit(X_data, y_data)

print("Modelo CRF entrenado exitosamente.")

# Puedes guardar el modelo entrenado, evaluarlo en datos de prueba, o usarlo para predicciones.
