# Objectif : Compter le nombre de lignes dans un fichier sur le disque

# Initialisation du compteur de lignes
lines_number = 0

# Nom du fichier à ouvrir
filename = "e1/test.txt"

try:
    # Ouvrir le fichier en mode lecture binaire ("rb") avec une gestion de contexte (with)
    with open(filename, "rb") as file:
        # Parcourir chaque ligne dans le fichier
        for line in file:
            # Incrémenter le compteur de lignes
            lines_number += 1

    # Afficher le nombre de lignes comptées
    print(f"Le nombre de lignes est : {lines_number}")

except FileNotFoundError:
    # Gérer l'exception si le fichier n'est pas trouvé
    print(f"Le fichier '{filename}' n'a pas été trouvé.")
except Exception as e:
    # Gérer d'autres exceptions possibles
    print(f"Une erreur s'est produite : {e}")
