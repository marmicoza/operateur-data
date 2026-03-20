# Python — Bases
## Phase 0 — Formation Opérateur

---

## Les types de données fondamentaux

```python
# String — texte, toujours entre guillemets
nom = "Opérateur"
ville = 'Cotonou'        # guillemets simples ou doubles, même résultat

# Integer — nombre entier
age = 22
jours = 365

# Float — nombre décimal
heures = 1.5
score = 98.7

# Boolean — exactement deux valeurs possibles
actif = True
diplome = False
```

Vérifier le type d'une variable :
```python
print(type(nom))         # <class 'str'>
print(type(age))         # <class 'int'>
print(type(heures))      # <class 'float'>
print(type(actif))       # <class 'bool'>
```

**Point critique :** Python se comporte différemment selon le type.
`"5" + "3"` donne `"53"` (concaténation). `5 + 3` donne `8` (addition).
Toujours savoir avec quel type on travaille.

---

## Opérations arithmétiques

```python
a = 17
b = 5

print(a + b)    # addition         → 22
print(a - b)    # soustraction     → 12
print(a * b)    # multiplication   → 85
print(a / b)    # division         → 3.4
print(a // b)   # division entière → 3 (ignore les décimales)
print(a % b)    # modulo (reste)   → 2 (17 = 3×5 + 2)
print(a ** b)   # puissance        → 17 exposant 5
```

**Le modulo `%`** répond à la question : "est-ce que ce nombre est divisible par X ?"
Si `n % 2 == 0` → le nombre est pair.

---

## Manipulation de strings

```python
prenom = "kofi"
nom = "mensah"

# Mise en forme
print(prenom.upper())           # KOFI
print(nom.capitalize())         # Mensah

# Longueur
print(len(prenom))              # 4

# Concaténation
nom_complet = prenom + " " + nom
print(nom_complet)              # kofi mensah
```

### F-strings — la méthode moderne (à utiliser par défaut)

```python
print(f"Nom complet : {prenom} {nom}")
print(f"En majuscules : {prenom.upper()} {nom.upper()}")

# Formater un float — limiter les décimales
valeur = 52.142857142857146
print(f"Résultat : {valeur:.2f}")    # 52.14 — 2 décimales
print(f"Résultat : {valeur:.0f}")    # 52    — aucune décimale
```

**Règle :** dans le travail data, toujours formater les floats pour la lisibilité.
`:.2f` signifie : afficher comme float avec 2 décimales.

---

## Conditions — if / elif / else

```python
score = 75

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Bien")
elif score >= 50:
    print("Passable")
else:
    print("Insuffisant")
```

**Règles absolues :**
- Les deux points `:` à la fin de chaque condition sont obligatoires
- L'indentation (4 espaces) est obligatoire — c'est comme ça que Python délimite les blocs
- Python lit de haut en bas et s'arrête à la première condition vraie

### Opérateurs de comparaison

```python
x == y    # égal à
x != y    # différent de
x > y     # strictement supérieur
x < y     # strictement inférieur
x >= y    # supérieur ou égal
x <= y    # inférieur ou égal
```

**Distinction critique :** `=` assigne une valeur. `==` compare deux valeurs.

---

## Listes

```python
notes = [14, 7, 18, 11, 9, 16]
pays = ["Bénin", "Nigeria", "Sénégal"]

# Accès par index — commence à 0
print(notes[0])     # 14  — premier élément
print(notes[2])     # 18  — troisième élément
print(notes[-1])    # 16  — dernier élément
print(notes[-2])    # 9   — avant-dernier

# Longueur
print(len(notes))   # 6

# Slice — extraire une portion
print(notes[1:4])   # [7, 18, 11] — index 1 inclus, 4 exclu
print(notes[:3])    # [14, 7, 18] — du début jusqu'à l'index 3 exclu
print(notes[3:])    # [11, 9, 16] — de l'index 3 jusqu'à la fin
```

### Modifier une liste

```python
notes = [15, 12, 18, 9, 14]

notes.append(17)        # ajouter à la fin → [15, 12, 18, 9, 14, 17]
notes[3] = 11           # modifier un élément → remplace 9 par 11
notes.remove(12)        # supprimer par valeur → retire le 12
notes.sort()            # trier en ordre croissant
notes.sort(reverse=True)# trier en ordre décroissant
```

**Piège classique :**
```python
resultat = notes.sort()   # retourne None — .sort() modifie la liste sur place
print(resultat)           # None — pas ce qu'on attend
print(notes)              # la liste est bien triée
```

---

## Boucles

### Boucle for sur une liste

```python
villes = ["Cotonou", "Porto-Novo", "Parakou"]

for ville in villes:
    print(f"Ville : {ville}")
```

La variable `ville` prend la valeur de chaque élément tour à tour.

### Pattern accumulateur — fondamental

```python
temperatures = [28, 31, 27, 35, 29]

total = 0
for temp in temperatures:
    total = total + temp

print(f"Moyenne : {total / len(temperatures):.2f}°C")
```

`total = 0` — on part de zéro. À chaque tour, on ajoute la valeur courante. C'est un accumulateur. Ce pattern est utilisé constamment.

### Trouver max et min avec un accumulateur

```python
notes = [14, 7, 18, 11, 9]

note_haute = notes[0]
for note in notes:
    if note > note_haute:
        note_haute = note

note_basse = notes[0]
for note in notes:
    if note < note_basse:
        note_basse = note
```

### range() — boucler sans liste

```python
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 20, 5):   # 0, 5, 10, 15
    print(i)
```

### enumerate() — index + valeur simultanément

```python
equipe = ["Alice", "Bob", "Carlos"]

for index, membre in enumerate(equipe):
    print(f"{index + 1}. {membre}")
# 1. Alice
# 2. Bob
# 3. Carlos
```

---

## Commentaires

```python
# Un commentaire commence par #
# Python ignore tout ce qui suit le # sur cette ligne

# MAUVAIS commentaire — répète ce que le code dit déjà
total = heures_par_jour * jours_ecoules

# BON commentaire — explique le POURQUOI
# Règle métier : on mesure l'investissement en heures, pas en jours
total = heures_par_jour * jours_ecoules
```

Un bon commentaire explique **pourquoi** ce choix a été fait, pas **ce que** le code fait.

---

## Exécuter un fichier Python

```bash
python nom_fichier.py
```

S'assurer que le terminal est dans le bon dossier avant d'exécuter.

---

*Phase 0 complétée — github.com/marmicoza/operateur-data*
