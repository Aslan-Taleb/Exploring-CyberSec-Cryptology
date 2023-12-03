import os
import socket
import sys
import signal


# Saisie du pseudo de l'utilisateur, encodé en UTF-8
pseudo = bytes(input("Veuillez rentrer votre pseudo : "), "utf-8")

# Définition du TSAP (Tuple Service Access Point)
adresseServeur = "224.0.0.127"  # Adresse IP multicast pour le groupe
numeroPort = 7182  # Numéro de port associé
tsap = (adresseServeur, numeroPort)

# Création de la socket UDP
maSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

# Utilisation du même port pour plusieurs sockets
maSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Réglage d'options pour UDP
gestionGroupe = bytes([int(x) for x in b"224.0.0.127".split(b".")] + [0] * 4)
maSocket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, gestionGroupe)
maSocket.setsockopt(
    socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1
)  # Mettre à 1 pour que les données reviennent sur la loopback et parviennent au serveur

# Bind de la socket à l'adresse et au port spécifiés
maSocket.bind(("", numeroPort))

# Création d'un processus fils avec fork
pid = os.fork()

if pid > 0:
    # On est dans le parent (processus serveur)
    while True:
        # Réception des messages
        message, adresseSource = maSocket.recvfrom(1024)
        messageStr = message.decode("utf-8")

        print("Message recu:", messageStr)

        # Si le message est "FIN", on arrête le serveur
        if messageStr == "FIN":
            break

    # Envoi d'un signal SIGUSR1 au processus fils pour le terminer
    os.kill(pid, signal.SIGUSR1)

    # N’oublions pas de fermer la socket
    maSocket.close()
else:
    # Gestion du signal SIGUSR1
    def handlerSIGUSR1(signum, frame):
        maSocket.close()
        sys.exit(0)

    signal.signal(signal.SIGUSR1, handlerSIGUSR1)

    # On est dans le fils
    while True:
        # Saisie du message et envoi à la socket avec le pseudo
        message = bytes(input(""), "utf-8")
        maSocket.sendto(pseudo + b":" + message, tsap)
