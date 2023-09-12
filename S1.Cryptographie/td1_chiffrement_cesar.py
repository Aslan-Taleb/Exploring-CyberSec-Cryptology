# Texte d'entrée que vous souhaitez chiffrer
text = "CESAR VAINCRA"
text_rot13 = "PRFNE INVAPEN"

# Chaîne de caractères pour stocker le texte chiffré
crypted = ""

# Clé de décalage pour le chiffrement de César
key = -3

# Boucle à travers chaque caractère dans le texte d'entrée
for letter in text:
    # Si le caractère est un espace, ajoutez un espace au texte chiffré
    if letter == " ":
        crypted += " "
    # Si le caractère est une lettre majuscule
    elif 'A' <= letter <= 'Z':
        # Effectuez le chiffrement de César en ajustant le code ASCII
        # de la lettre en fonction de la clé et du modulo 26
        # pour gérer le rebouclage dans l'alphabet, puis ajoutez 'A'
        # pour obtenir la lettre chiffrée en majuscules
        crypted += chr((ord(letter) - ord('A') + key) % 26 + ord('A'))
    # Si le caractère est une lettre minuscule
    elif 'a' <= letter <= 'z':
        crypted += chr((ord(letter) - ord('a') + key) % 26 + ord('a'))
    # Si le caractère n'est pas une lettre, conservez-le tel quel
    else:
        crypted += letter

# Affichez le texte chiffré
print(crypted)
