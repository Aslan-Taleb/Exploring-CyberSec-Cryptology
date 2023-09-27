import socket
import sys
import re
from bs4 import BeautifulSoup


# Les informations de connexion de la socket du client
portServeur = 80
adresseServeur = socket.gethostbyname("www.unilim.fr")
tsapServeur = (adresseServeur, portServeur)

# Création de la socket du client
socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
try:
    socketClient.connect(tsapServeur)
except Exception as e:
    print("Problème de connexion " + str(e.args))
    sys.exit(1)

# On demande à Google de récupérer la page
requete = b"GET / HTTP/1.0\r\nHost: www.unilim.fr\r\n\r\n"
socketClient.sendall(requete)


# Récupération des information
response = socketClient.recv(10000000).decode("utf-8")
soup = BeautifulSoup(response, 'html.parser')
formatted_html = soup.prettify()
print(formatted_html)








