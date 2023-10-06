import random
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Définir le nombre de points dans chaque ensemble
nombre_de_points = 50

# Créer l'ensemble de points de classe 0 dans la zone (0 <= x <= 10) et (0 <= y <= 10)
ensemble_classe_0 = []
for _ in range(nombre_de_points):
    x = random.uniform(0, 10)  # Génère une abscisse aléatoire entre 0 et 10
    y = random.uniform(0, 10)  # Génère une ordonnée aléatoire entre 0 et 10
    ensemble_classe_0.append((x, y))

# Créer l'ensemble de points de classe 1 dans la zone (-10 <= x < 0) et (0 <= y <= 10)
ensemble_classe_1 = []
for _ in range(nombre_de_points):
    x = random.uniform(-10, 0)  # Génère une abscisse aléatoire entre -10 et 0
    y = random.uniform(0, 10)   # Génère une ordonnée aléatoire entre 0 et 10
    ensemble_classe_1.append((x, y))

# Combinez les ensembles de classe en un seul ensemble de données
ensemble_de_donnees = ensemble_classe_0 + ensemble_classe_1
etiquettes = [0] * len(ensemble_classe_0) + [1] * len(ensemble_classe_1)

# Convertissez les listes en tableaux NumPy pour l'entraînement
X = np.array(ensemble_de_donnees)
y = np.array(etiquettes)

# Divisez l'ensemble de données en ensembles d'entraînement (80%) et de test (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Créer un modèle séquentiel
model = Sequential()

# Ajouter une couche Dense avec 3 unités en tant que couche d'entrée et spécifier la forme d'entrée
model.add(Dense(units=3, input_shape=(2,)))
model.add(Dense(units=64, activation='relu'))  # Ajoutez une couche cachée avec activation ReLU
model.add(Dense(units=1, activation='sigmoid'))  # Couche de sortie avec activation sigmoïde

# Compilez le modèle avec une fonction de perte et un optimiseur appropriés
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entraînez le modèle
model.fit(X_train, y_train, epochs=1000)

# Évaluez le modèle sur l'ensemble de test
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Perte (loss) : {loss}')
print(f'Précision (accuracy) : {accuracy}')

# Maintenant, vous pouvez continuer à ajouter d'autres couches à votre modèle ou effectuer des prédictions.
predictions = model.predict(X_test)
print('Prédictions :')
print(predictions)
print('Étiquettes réelles :')
print(y_test)
