# Importation des modules nécessaires
import os, socket, sys

# Définition du numéro de port sur lequel le serveur écoutera
numero_port = 80

# Création d'une socket en utilisant IPv4, TCP/IP
socketConnexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

# Configuration de la socket pour réutiliser rapidement l'adresse et le port après la fermeture
socketConnexion.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Liaison de la socket à l'adresse IP vide ('') et au numéro de port 80
socketConnexion.bind(('', numero_port))

# Mise en écoute de la socket avec une file d'attente maximale
socketConnexion.listen(socket.SOMAXCONN)

# Boucle infinie pour accepter les connexions entrantes
while 1:
    # Acceptation d'une nouvelle connexion
    (connexion, TSAPclient) = socketConnexion.accept()
    
    # Affichage d'un message pour signaler la nouvelle connexion
    connexion.send(f'Connexion TSAPclient : {TSAPclient}'.encode())
    ligne = connexion.recv(1024)
    print(ligne)

    # Fermeture de la connexion avec le client
    connexion.close()

# Fermeture de la socket d'écoute
socketConnexion.close()
