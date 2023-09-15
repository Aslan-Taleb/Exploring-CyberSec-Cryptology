def transformationNaive(i, j, a, b, I, D, S):
    n, m = len(a), len(b)

    # Si les deux chaînes sont entièrement parcourues, le coût est de 0.
    if i >= n and j >= m:
        print(f"TransformationNaive({i}, {j}) => 0")
        return 0
    
    # Si a est épuisé, ajoute le coût de l'ajout pour chaque caractère restant dans b.
    if i >= n and j < m:
        cost = I[ord(b[j])] + transformationNaive(i, j + 1, a, b, I, D, S)
    
    # Si b est épuisé, ajoute le coût de la suppression pour chaque caractère restant dans a.
    elif i < n and j >= m:
        cost = D[ord(a[i])] + transformationNaive(i + 1, j, a, b, I, D, S)
    
    # Sinon, calcule le coût d'ajout, de suppression et de remplacement.
    else:
        costAdd = I[ord(b[j])] + transformationNaive(i, j + 1, a, b, I, D, S)
        costDelete = D[ord(a[i])] + transformationNaive(i + 1, j, a, b, I, D, S)
        costReplace = S[ord(a[i])][ord(b[j])] + transformationNaive(i + 1, j + 1, a, b, I, D, S)
        
        # Retourne le coût minimum parmi les trois options.
        cost = min(costAdd, costDelete, costReplace)
    
    print(f"TransformationNaive({i}, {j}) => {cost}")  # Ajout d'un print pour suivre les étapes.
    return cost

# Exemple d'utilisation avec des coûts d'opération arbitraires.
a = "chat"
b = "chien"

I = {'c': 1, 'h': 1, 'a': 1, 't': 1, 'i': 1, 'e': 1}
D = {'c': 1, 'h': 1, 'a': 1, 't': 1, 'i': 1, 'e': 1}
S = {
    'c': {'c': 0, 'h': 2, 'a': 2, 't': 3, 'i': 3, 'e': 3},
    'h': {'c': 2, 'h': 0, 'a': 1, 't': 3, 'i': 3, 'e': 3},
    'a': {'c': 2, 'h': 1, 'a': 0, 't': 3, 'i': 3, 'e': 3},
    't': {'c': 3, 'h': 3, 'a': 3, 't': 0, 'i': 1, 'e': 1},
    'i': {'c': 3, 'h': 3, 'a': 3, 't': 1, 'i': 0, 'e': 1},
    'e': {'c': 3, 'h': 3, 'a': 3, 't': 1, 'i': 1, 'e': 0}
}

result = transformationNaive(0, 0, a, b, I, D, S)
print(f"Le coût minimal de transformation de '{a}' en '{b}' est {result}.")
