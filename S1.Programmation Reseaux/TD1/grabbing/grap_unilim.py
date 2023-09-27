#Le principe : établir une connexion TCP avec le service,
# recevoir la bannière d'accueil et afficher les informations obtenues.
import socket
import sys

# Les informations de connexion de la socket du client
portServeur = 25
adresseServeur = socket.gethostbyname("smtp.unilim.fr")
tsapServeur = (adresseServeur, portServeur)

# Création de la socket du client
socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
try:
    socketClient.connect(tsapServeur)
except Exception as e:
    print("Problème de connexion " + str(e.args))
    sys.exit(1)

# Récupération des informations, affichage et fermeture de la socket client
ligne = socketClient.recv(1024)
print(ligne.decode("utf-8"))
socketClient.close()
