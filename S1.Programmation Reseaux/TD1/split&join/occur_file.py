# Nom du fichier à ouvrir
filename = r"TD1/split&join/texte.txt"
word_count = {}

# Ouvrir le fichier en mode lecture ("r") avec une gestion de contexte (with)
with open(filename, "r") as file:
    # Parcourir chaque ligne dans le fichier
    for line in file:
        # Séparer la ligne en mots en utilisant l'espace comme séparateur
        words = line.split()
        # Parcourir chaque mot dans la liste de mots
        for word in words:
            # Supprimer la ponctuation et convertir en minuscules (si nécessaire)
            word = word.strip(".,!?").lower()
            # Vérifier si le mot est déjà dans le dictionnaire
            if word in word_count:
                # Si oui, incrémenter le compteur de ce mot
                word_count[word] += 1
            else:
                # Sinon, ajouter le mot au dictionnaire avec un compteur initial de 1
                word_count[word] = 1

# Afficher le dictionnaire contenant les occurrences de chaque mot de manière plus visuelle
print("Word Count Results:")
print("-------------------")
for word, count in word_count.items():
    print(f"{word}: {count}")
