"""
Ce programme réalise l'insertion d'une liste d'éléments dans une liste existante à un emplacement spécifique, identifié par son indice.
"""

# Liste à insérer
list_to_add = ["3.1", "3.2", "3.3", "3.4", "3.5"]

# Liste existante
main_list = ["1", "2", "3", "4", "5"]

# Indice d'insertion
index = 3

# Insérer la liste_to_add dans la main_list à l'indice spécifié
main_list = main_list[:index] + list_to_add + main_list[index:]

# Afficher le résultat
print(main_list)


