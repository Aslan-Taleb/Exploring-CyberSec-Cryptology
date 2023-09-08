# Définition des noms de fichiers
filename1 = "e2/premier.txt"  # Nom du fichier source en lecture
new_filename = "e2/deuxieme.txt"  # Nom du fichier de destination en écriture

# Initialisation de la variable 'i' pour alterner entre les lignes à copier et à ignorer
i = -1

# Initialisation du compteur de lignes copiées
cpt = 0

# Ouvrir le fichier source en mode lecture binaire ("rb") avec une gestion de contexte (with)
with open(filename1, "r") as file:
    # Ouvrir le fichier de destination en mode écriture ("w") avec une gestion de contexte (with)
    with open(new_filename, "w") as file2:
        # Parcourir chaque ligne du fichier source
        for line in file:
            # Inverser la valeur de 'i' à chaque itération pour alterner entre les lignes à copier et à ignorer
            i = i * -1
            
            # Si 'i' est positif (l'itération actuelle doit copier la ligne), écrire la ligne dans le fichier de destination
            if i > 0:
                file2.write(line)
                # Incrémenter le compteur de lignes copiées
                cpt += 1

# Afficher le nombre de lignes copiées
print(f"Nombre de lignes copiées : {cpt}")


# au lieu du i on peut utiliser "enumerate" ca a l'air plus simple