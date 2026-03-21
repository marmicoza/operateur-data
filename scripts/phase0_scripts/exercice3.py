# Analyseur de données
# Données brutes — notes d'étudiants sur 20
notes = [14, 7, 18, 11, 9, 16, 13, 5, 19, 12, 8, 15, 10, 17, 6]

print("=== Analyse des notes ===")
print(f"Nombre d'étudiants : {len(notes)}")

# Déterminer la plus forte note
note_haute = notes[0]
for note in notes:
    if note > note_haute:
        note_haute = note

print(f"Notes la plus haute : {note_haute}")

# Déterminer la plus faible note
note_basse = notes[0]
for note in notes:
    if note < note_basse:
        note_basse = note

print(f"Notes la plus basse : {note_basse}")

# Déterminer la moyenne
total = 0
for note in notes:
    total = total + note

moyenne = total / len(notes)

print(f"Moyenne : {moyenne}")

print("=== Distributions ===")

for index, note in enumerate(notes):
    if note >= 16:
       print(f"{index+1}. Note {note} - Excellent") 
    elif note >= 12:
        print(f"{index+1}. Note {note} - Bien")
    elif note >= 10:
        print(f"{index+1}. Note {note} - Passable")
    else:
        print(f"{index+1}. Note {note} - Insuffisant")


print("=== Bilan ===")
etudiants_recus = 0
etudiants_recales = 0
for note in notes:
    if note >= 10:
        etudiants_recus = etudiants_recus+1
    else:
        etudiants_recales = etudiants_recales+1

print(f"Reçus (note >= 10) : {etudiants_recus} étudiants")
print(f"Recalés (note < 10) : {etudiants_recales} étudiants")








