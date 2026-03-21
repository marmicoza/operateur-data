# Une liste = plusieurs valeurs dans une seule variable
scores = [87, 42, 95, 61, 78, 55, 90]
pays = ["Bénin", "Nigéria", "Sénégal", "Ghana", "Côte d'Ivoire"]
mixte = [42, "Cotonou", True, 3.14]         # autorisé mais pas conseillé en pratique


# Accéder à un élément - l'index commence à 0, pas à 1
print(scores[0])    # 87  — premier élément
print(scores[2])    # 95  — troisième élément
print(scores[-1])   # 90  — dernier élément (index négatif = depuis la fin)
print(scores[-2])   # 55  — avant-dernier

# Longueur d'une liste
print(len(scores))  # 7

# Slice — extraire une portion
print(scores[1:4])  # [42, 95, 61] — index 1 inclus, 4 exclu
print(scores[:3])   # [87, 42, 95] — du début jusqu'à l'index 3 exclu
print(scores[4:])   # [78, 55, 90] — de l'index 4 jusqu'à la fin

notes = [15, 12, 18, 9, 14]

# Ajouter à la fin
notes.append(17)
print(notes)    # [15, 12, 18, 9, 14, 17]

# Modifier un élément existant
notes[3] = 11   # remplace le 9 par 11
print(notes)    # [15, 12, 18, 11, 14, 17]

# Supprimer un élément par valeur
notes.remove(12)
print(notes)    # [15, 18, 11, 14, 17]

# Trier
notes.sort()
print(notes)    # [11, 14, 15, 17, 18]

notes.sort(reverse=True)
print(notes)    # [18, 17, 15, 14, 11]


# BOUCLES
villes = ["Cotonou", "Porto-Novo", "Parakou", "Abomey"]

# Pour chaque élément dans la liste, exécuter ce bloc
for ville in villes:
    print(f"Ville : {ville}")

temperatures = [28, 31, 27, 35, 29, 33, 30]

# Calculer la somme manuellement avec une boucle
total = 0
for temp in temperatures:
    total = total + temp

print(f"Somme : {total}")
print(f"Moyenne : {total / len(temperatures):.2f}°C")

# range(n) génère les entiers de 0 à n-1
for i in range(5):
    print(i)        # 0, 1, 2, 3, 4

# range(debut, fin)
for i in range(1, 6):
    print(i)        # 1, 2, 3, 4, 5

# range(debut, fin, pas)
for i in range(0, 20, 5):
    print(i)        # 0, 5, 10, 15

# Boucle avec index — enumerate(). 
# enumerate() donne en même temps l'index et la valeur. Plus besoin de gérer un compteur à la main.
equipe = ["Alice", "Bob", "Carlos", "Djamila"]

for index, membre in enumerate(equipe):
    print(f"{index + 1}. {membre}")
