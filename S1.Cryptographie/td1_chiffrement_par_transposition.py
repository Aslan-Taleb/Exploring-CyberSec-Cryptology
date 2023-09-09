# Définition de la chaîne de caractères d'origine
text = "MASTERLIMOGES"

# Initialisation de la chaîne de caractères chiffrée
crypted = ""

# Boucle pour les caractères d'indices pairs (0, 2, 4, ...)
for i in range(0, len(text), 2):
    # Ajouter le caractère à la chaîne chiffrée
    crypted += text[i]

# Boucle pour les caractères d'indices impairs (1, 3, 5, ...)
for i in range(1, len(text), 2):
    # Ajouter le caractère à la chaîne chiffrée
    crypted += text[i]

# Afficher la chaîne chiffrée
print(crypted)
