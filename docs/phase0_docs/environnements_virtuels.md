# Environnements virtuels Python — Référence
## Phase 0 — Formation Opérateur

---

## Pourquoi les environnements virtuels

Chaque projet peut nécessiter des versions différentes des mêmes bibliothèques. Sans isolation, les projets entrent en conflit et se cassent mutuellement.

Un environnement virtuel crée une installation Python complètement isolée par projet. Ce qu'on installe dedans n'affecte pas les autres projets ni le Python global de la machine.

En data science, chaque projet aura ses propres dépendances. Les environnements virtuels ne sont pas optionnels.

---

## Créer un environnement virtuel

Dans le dossier du projet :

```bash
python -m venv venv
```

Un dossier `venv/` apparaît. Il contient une installation Python indépendante. Par convention, ce dossier s'appelle toujours `venv`.

---

## Activer l'environnement

```bash
source venv/Scripts/activate      # Windows (Git Bash)
source venv/bin/activate          # Linux / Mac
```

Quand l'environnement est actif, le terminal affiche `(venv)` au début :

```
(venv) ADMIN@DESKTOP ~/projet (main)
```

Tout ce qui est installé avec `(venv)` visible va dans l'environnement isolé, pas dans le Python global.

---

## Désactiver l'environnement

```bash
deactivate
```

Le `(venv)` disparaît. Le Python global est à nouveau actif.

---

## Installer des bibliothèques

Toujours avec l'environnement actif `(venv)` :

```bash
pip install nom_bibliotheque
pip install pandas numpy matplotlib    # installer plusieurs en une fois
pip install pandas==2.0.0              # installer une version spécifique
```

---

## Voir ce qui est installé

```bash
pip list
```

Affiche toutes les bibliothèques installées dans l'environnement actif avec leurs versions.

---

## Le fichier requirements.txt

### Pourquoi il existe

Quand quelqu'un clone le repo, il n'a pas le dossier `venv/` (il est dans `.gitignore`). Le fichier `requirements.txt` liste toutes les dépendances avec leurs versions exactes. Il permet de recréer un environnement identique sur n'importe quelle machine.

### Générer le fichier

Avec l'environnement actif :

```bash
pip freeze > requirements.txt
```

`pip freeze` liste toutes les bibliothèques installées avec leurs versions.
`>` redirige cet output vers le fichier `requirements.txt` au lieu de l'afficher.

### Vérifier le contenu

```bash
cat requirements.txt
```

Résultat typique :
```
certifi==2026.2.25
charset-normalizer==3.4.6
idna==3.11
requests==2.32.5
urllib3==2.6.3
```

### Recréer l'environnement depuis le fichier

Sur une nouvelle machine :

```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

`-r` signifie "lire depuis un fichier". Toutes les bibliothèques sont installées automatiquement avec les bonnes versions.

### Mettre à jour le fichier après une nouvelle installation

À chaque fois qu'une nouvelle bibliothèque est installée, régénérer le fichier :

```bash
pip freeze > requirements.txt
git add requirements.txt
git commit -m "update: ajout nouvelle dépendance"
git push origin main
```

---

## Le .gitignore et venv

Le dossier `venv/` ne doit jamais être envoyé sur GitHub. Il est lourd (des centaines de fichiers) et chaque machine recrée le sien.

Dans `.gitignore` :
```
venv/
```

Vérifier que Git l'ignore bien :
```bash
git status
```

`venv/` ne doit pas apparaître dans la liste.

---

## Configurer VS Code pour utiliser le bon Python

VS Code doit pointer vers le Python de l'environnement virtuel, pas le global.

1. Cliquer sur la version Python en bas à gauche dans VS Code
2. Sélectionner l'option contenant `venv` dans le chemin
3. Si non visible : cliquer **Browse** → naviguer vers `venv/Scripts/python.exe`

---

## Résumé — séquence complète pour un nouveau projet

```bash
# 1. Créer le dossier projet et entrer dedans
mkdir mon-projet && cd mon-projet

# 2. Créer l'environnement virtuel
python -m venv venv

# 3. Activer
source venv/Scripts/activate

# 4. Installer les bibliothèques nécessaires
pip install pandas numpy

# 5. Générer requirements.txt
pip freeze > requirements.txt

# 6. Ajouter venv/ au .gitignore
echo "venv/" >> .gitignore

# 7. Commiter
git add requirements.txt .gitignore
git commit -m "feat: setup environnement virtuel"
git push origin main
```

---

*Phase 0 complétée — github.com/marmicoza/operateur-data*
