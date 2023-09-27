import socket
import sys
import re

# Informations de connexion HTTP à google.com
portServeur = 80
adresseServeur = socket.gethostbyname("google.com")
tsapServeur = (adresseServeur, portServeur)

# Création de la socket du client
socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
try:
    socketClient.connect(tsapServeur)
except Exception as e:
    print("Problème de connexion " + str(e.args))
    sys.exit(1)

# Envoi de la requête HTTP GET à google.com
requete = b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n"

socketClient.sendall(requete)

# Récupération des informations de la réponse HTTP
ligne = socketClient.recv(16384)
ligneStr = ligne.decode("utf-8")

# Utilisation d'une expression régulière pour extraire le contenu de la balise <title>
monExpression = re.compile("<title>(.*?)</title>", re.I)
resultat = monExpression.search(ligneStr)

if resultat is None:
    print("Pas de titre trouvé dans la page.")
else:
    print("Le contenu de la balise <title> : " + resultat.group(1))

# Fermeture de la connexion
socketClient.close()
