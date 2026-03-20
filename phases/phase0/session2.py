# LES TYPES DE BASE

# String (texte) - toujours entre guillemets
nom = "Opérateur"
ville = 'Cotonou'   # guillemets simples ou doubles, même chose

# Integer (nombre entier)
age = 22
jours = 365

# Float (nomre décimal)
heures = 1.5
score = 98.7

# Boolean (vrai ou faux - exactement deux valeurs possibles)
en_formation = True
a_diplome = False

# Afficher le type d'une variable
print(type(nom))
print(type(age))
print(type(heures))
print(type(en_formation))



# OPÉRATIONS ARITHMÉTIQUES
a = 17
b = 5

print(a + b)    # addition  22
print(a - b)    # soustraction  12
print(a * b)    # multiplication    85
print(a / b)    # division  3.4
print(a // b)   # division entière  3 (ignore les décimales)
print(a % b)    # modulo (reste)    2 (17 = 3*5 +2)
print(a ** b)   # puissance     1 exposant 5


# MANIPULATION DES STRINGS
prenom = "koffi"
nom = "mensah"

# Mettre en majuscule
print(prenom.upper())       # KOFFI
print(nom.capitalize())     # Mensah

# Combiner des strings (concatenation)
nom_complet = prenom + " " + nom
print(nom_complet)           # koffi mensah

# F-string : la manière moderne et propre
print(f"Nom complet : {prenom} {nom}")
print(f"En majuscules : {prenom.upper()} {nom.upper()}")

# Longueur d'un string
print(len(prenom))      # 4

# Formater un nombre décimal (rappel semaines)
semaines = 52.142857142857146
print(f"Semaines : {semaines:.2f}")     # 52.14 - .2f = 2 décimales


# CONDITIONS
score = 75

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Bien")
elif score >= 50:
    print("Passable")
else:
    print("Insuffisant")

x = 1
y = 2

x == y      # égal à
x != y      # différent
x > y       # strictement supérieur
x < y       # strictement inférieur
x >= y      # supérieur ou égal
x <= y      # inférieur ou égal


