#recueille la liste des fichiers présents dans un répertoire, ouvre chacun de ces fichiers
#puis affiche leur première ligne
import os

def lire_premiere_ligne_de_fichier(fichier_chemin):
    """Lire la première ligne d'un fichier et la retourner."""
    if  os.path.getsize(fichier_chemin) <=0:
        return None
    with open(fichier_chemin, "r") as file:
        return file.readline()
            

def main():
    # Spécifiez le répertoire que vous souhaitez explorer
    repertoire = r"C:\Users\aslan\OneDrive\Documents\Exploring-CyberSec-Cryptology\S1.Programmation Reseaux\TD 1\e2"

    # Obtenir la liste des fichiers dans le répertoire
    fichiers = os.listdir(repertoire)

    # Parcourir la liste des fichiers et afficher leur première ligne
    for fichier in fichiers:
        chemin_complet = os.path.join(repertoire, fichier)
        if os.path.isfile(chemin_complet):
            first_line = lire_premiere_ligne_de_fichier(chemin_complet)
            print(f"Première ligne de {fichier}: {first_line}")

main()

# import sys,subprocess
# #PIPE pour dire la sortie de la commande 
# resultat_commande = subprocess.run("dir /a",shell=True,stdout=subprocess.PIPE)
# sortie_commande = resultat_commande.stdout
# liste_fichiers = sortie_commande.splitlines()
# for i in liste_fichiers:
#     print(i)