# CONSTRUCTION D'UN ÉVALUATEUR DE PROGRESSION
# Données de départ
heures_par_jour = 1.5
jours_ecoules = 100
objectif_jours = 365

# Investissement mesuré en jours
heures_investies = heures_par_jour * jours_ecoules

# Calculer le pourcentage de progression (jours écoulés / objectif * 100)
progression = (jours_ecoules / objectif_jours) * 100

# Afficher les deux résultats avec f-strings, 2 décimales pour les floats
print(f"Jusqu'ici, {heures_investies:.2f} heures ont été investies")
print(f"Le pourcentage de progression est de {progression:.2f} %")

# Ajouter une condition:
#    - Si progression >= 75% : affiche "Phase finale, tiens bon"
#    - Si progression >= 50% : affiche "Mi-parcours, le plus dur est derrière"
#    - Si progression >= 25% : affiche "En bonne voie, continue"
#    - Sinon : affiche "Début du chemin, construis l'habitude"
if progression >= 75:
    print("Phase finale, tiens bon")
elif progression >= 50:
    print("Mi-parcours, le plus dur est derrière")
elif progression >= 25:
    print("En bonne voie, continue")
else:
    print("Début du chemin, construis l'habitude")
