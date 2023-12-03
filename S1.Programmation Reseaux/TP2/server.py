# Importation des modules nécessaires
import os, socket, sys, signal, struct

# Définition du TSAP (Transport Service Access Point)
adresseServeur = "224.0.0.127"  # Adresse IP du serveur en mode multidiffusion
numeroPort = 7182  # Numéro de port sur lequel le serveur écoutera les connexions
tsap = (adresseServeur, numeroPort)  # Combinaison de l'adresse IP et du numéro de port

# Création de la socket
maSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
# La ligne suivante permet la réutilisation du même port pour plusieurs sockets
maSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Configuration des options de la socket pour le protocole UDP
gestionGroupe = struct.pack("4sl", socket.inet_aton("224.0.0.127"), socket.INADDR_ANY)
# Elle indique à la socket de rejoindre le groupe multicast spécifié (224.0.0.127) et
# d'accepter les messages provenant de n'importe quelle interface (INADDR_ANY).
maSocket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, gestionGroupe)
# Désactivation de la boucle de multidiffusion locale pour éviter une boucle infinie de réception
maSocket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 0)
# Association de la socket à l'adresse IP et au port spécifiés
maSocket.bind(("", numeroPort))

print("Serveur en attente de messages...")

# Boucle principale du serveur
while 1:
    # Réception d'un message (jusqu'à 1024 octets) et récupération de l'adresse source
    message, adresseSource = maSocket.recvfrom(1024)
    # Décodage du message en UTF-8
    messageStr = message.decode("utf-8")

    # Affichage du message reçu côté serveur
    print("Message reçu : " + messageStr)
    # Envoi du message à tous les clients connectés
    maSocket.sendto(message, tsap)

    # Condition de sortie de la boucle si le message est "FIN"
    if messageStr == "FIN":
        break

# Fermeture de la socket à la fin de l'exécution
maSocket.close()
