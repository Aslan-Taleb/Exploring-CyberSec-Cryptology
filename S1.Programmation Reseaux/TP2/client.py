import socket  # Importation du module pour la gestion des sockets
import struct  # Importation du module pour manipuler des données binaires
import os
MCAST_GRP =   '224.0.0.127'
MCAST_PORT = 7182
FORMAT = 'utf-8'
# 1. Création de la structure pour rejoindre le groupe multicast
#    - struct.pack() est utilisé pour créer une structure binaire.
#    - "4sl" indique le format de la structure :
#         - "4s" signifie qu'il y a un champ de 4 octets pour stocker une chaîne de caractères (adresse IP).
#         - "l" signifie qu'il y a un champ de 4 octets pour stocker un entier long (interface réseau).
#    - socket.inet_aton("224.0.0.127") convertit l'adresse IP "224.0.0.127" en format binaire.
#    - socket.INADDR_ANY est une constante représentant "n'importe quelle" interface réseau.
gestion_mcast = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)

# 2. Configuration de la socket pour rejoindre le groupe multicast
socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Création d'une socket UDP

# Option de socket pour réutiliser l'adresse.
# Permet de réutiliser l'adresse IP et le port même si la socket a été utilisée précédemment.
socket_client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


socket_client.bind((MCAST_GRP, MCAST_PORT))
def send(msg):
    message = msg.encode(FORMAT)
    socket_client.sendto(message, (MCAST_GRP, MCAST_PORT))


# Configuration de la socket pour rejoindre le groupe multicast spécifié.
socket_client.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, gestion_mcast)
print(f"[LISTENING] client is listening on {MCAST_GRP}:{MCAST_PORT}")

try:
    pid = os.fork()
    while True:
        if pid == 0:
            user_input = input("\n\n\nYour Message : \n")
            send(user_input)
            
        else:
            data, addr = socket_client.recvfrom(1024)  # Recevoir des données multicast (jusqu'à 1024 octets)
            # Afficher les données reçues en décodant en UTF-8 (supposant que les données sont en texte).
            print("Données reçues de", addr, ":", data.decode("utf-8"))
except KeyboardInterrupt:
    print("Deconexion Client.")
finally:
    socket_client.close()  # Fermer la socket lorsque vous avez terminé
