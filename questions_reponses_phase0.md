# Questions & Réponses — Phase 0 : Forge
## Formation Opérateur — Référence personnelle

---

## TERMINAL & LIGNE DE COMMANDE

---

### Q1 — Comment quitter un dossier et naviguer vers un autre ?

`cd ..` remonte d'un niveau (vers le dossier parent).

```bash
cd ..              # remonter d'un niveau
cd ../phase1       # remonter d'un niveau ET entrer dans un autre dossier
cd ~/Desktop       # aller directement à un chemin absolu
```

---

### Q2 — Comment créer un fichier depuis le terminal (pas juste un dossier) ?

Sur Linux/Mac :
```bash
touch session2.py
```

Sur Windows (PowerShell) :
```bash
ni session2.py
```

Mais la méthode la plus rapide reste VS Code : `Ctrl+N` → `Ctrl+S` → nommer le fichier avec son extension.

---

### Q3 — `touch` n'est pas reconnu sur Windows. Pourquoi ?

`touch` est une commande Linux/Mac. Par défaut, le terminal VS Code sur Windows tourne sous PowerShell qui ne la reconnaît pas.

**Solution définitive : configurer Git Bash comme terminal par défaut dans VS Code.**

1. `Ctrl+Shift+P`
2. Taper : `Terminal: Select Default Profile`
3. Sélectionner **Git Bash**
4. Fermer et rouvrir le terminal

Git Bash émule un environnement Linux sur Windows. Toutes les commandes Linux (`touch`, `ls`, `pwd`, `mkdir`, etc.) fonctionnent dedans. C'est l'environnement de travail standard pour tout développeur sur Windows.

---

### Q4 — Récapitulatif complet des commandes terminal essentielles

```bash
pwd                # afficher le dossier actuel (Print Working Directory)
ls                 # lister les fichiers et dossiers ici
mkdir nom          # créer un dossier
cd nom             # entrer dans un dossier
cd ..              # remonter d'un niveau
cd ../autre        # remonter puis aller ailleurs
touch nom.py       # créer un fichier vide (Git Bash / Linux)
ni nom.py          # créer un fichier vide (PowerShell Windows)
```

Ces 8 commandes couvrent 90% de l'usage quotidien du terminal.

---

## GIT & GITHUB

---

### Q5 — `git config --list` n'affiche pas mon nom et email après les avoir configurés

**Cause :** Les commandes `git config --global` n'avaient pas encore été exécutées.

**Diagnostic :** Au lieu de `git config --list` (qui affiche tout), taper les commandes ciblées :

```bash
git config --global user.name
git config --global user.email
```

Si elles ne retournent rien → les valeurs ne sont pas enregistrées. Il faut les configurer :

```bash
git config --global user.name "Ton Nom"
git config --global user.email "ton@email.com"
```

Puis vérifier à nouveau avec les commandes ciblées. Elles doivent retourner les valeurs entrées.

---

### Q6 — Pourquoi `docs` pour journal.md et `feat` pour les fichiers Python ?

Les préfixes de commit suivent une convention standard. Chaque préfixe dit **ce que fait** le commit :

| Préfixe | Usage |
|--------|-------|
| `feat` | Ajout d'une nouvelle fonctionnalité ou de nouveau code |
| `fix` | Correction d'un bug ou d'une erreur |
| `docs` | Documentation pure (journal, README, guides) |
| `update` | Modification d'un fichier existant |
| `add` | Ajout d'une ressource (dataset, image, config) |

**Règle :** Le message de commit doit dire à quelqu'un qui ne voit pas le code ce qui a changé et pourquoi. En moins de 50 caractères.

Mauvais : `git commit -m "modifications"`
Bon : `git commit -m "feat: analyseur de notes avec boucles"`

---

### Q7 — Comment modifier journal.md (ou n'importe quel fichier) après un premier commit ?

Le cycle Git est toujours le même, peu importe le fichier :

```bash
# 1. Modifier le fichier dans VS Code et sauvegarder (Ctrl+S)

# 2. Vérifier ce qui a changé
git status

# 3. Ajouter la modification au staging
git add journal.md

# 4. Commiter avec un message descriptif
git commit -m "docs: mise à jour journal session 4"

# 5. Envoyer sur GitHub
git push origin main
```

Pour voir exactement ce qui a changé avant de commiter :
```bash
git diff journal.md
```
Affiche les lignes ajoutées en vert et supprimées en rouge.

---

### Q8 — Comment supprimer des fichiers de Git ?

**Cas 1 — Supprimer le fichier partout (machine + GitHub) :**

```bash
git rm nom_du_fichier.py
git commit -m "fix: suppression fichier inutile"
git push origin main
```

**Cas 2 — Retirer de GitHub mais garder sur la machine :**

```bash
git rm --cached nom_du_fichier.py
git commit -m "fix: retrait fichier du suivi Git"
git push origin main
```

`--cached` signifie "retire du suivi Git uniquement, ne touche pas au fichier réel". Utile si on a accidentellement ajouté un fichier avec des mots de passe ou des données sensibles.

---

### Q9 — Est-ce qu'il faut commiter le .gitignore ?

**Oui.** `.gitignore` est un fichier comme les autres. Git doit le suivre pour qu'il soit actif sur GitHub.

```bash
git add .gitignore
git commit -m "docs: ajout gitignore"
git push origin main
```

**Règle générale :** Tout fichier créé dans le repo doit être commité pour exister sur GitHub. Sans `add` + `commit` + `push`, GitHub ne le voit jamais.

**Contenu typique d'un .gitignore Python :**
```
*.csv            # ignorer tous les fichiers CSV (données brutes)
*.env            # ignorer les fichiers de config sensibles (mots de passe, clés API)
__pycache__/     # ignorer les dossiers Python temporaires
*.pyc            # ignorer les fichiers compilés Python
.DS_Store        # ignorer les fichiers système Mac
```

---

### Q10 — Mon commit est fait mais les fichiers n'apparaissent pas sur GitHub

**Cause :** Le commit existe en local mais n'a pas été pushé. `git status` affiche alors :
```
Your branch is ahead of 'origin/main' by 1 commit.
```
L'onglet "outgoing changes" dans VS Code indique la même chose.

**Solution :**
```bash
git push origin main
```

Le push envoie **tous** les commits en attente d'un coup.

---

## PYTHON

---

### Q11 — `.sort()` retourne `None` — pourquoi mon code plante ?

```python
notes_dcr = notes.sort()   # PIÈGE : retourne None
```

`.sort()` modifie la liste **directement** et retourne `None`. Donc `notes_dcr` vaut `None`. Indexer `None` plante le programme.

**Preuve :**
```python
test = [3, 1, 2]
resultat = test.sort()
print(resultat)   # None
print(test)       # [1, 2, 3] — la liste originale est modifiée
```

**Solution — trouver max/min avec un accumulateur (pattern fondamental) :**

```python
note_haute = notes[0]       # on suppose le premier est le plus grand
for note in notes:
    if note > note_haute:   # si on trouve plus grand
        note_haute = note   # on met à jour

note_basse = notes[0]       # même logique pour le minimum
for note in notes:
    if note < note_basse:   # si on trouve plus petit
        note_basse = note
```

Ce pattern s'appelle un **accumulateur**. C'est l'un des patterns les plus utilisés en programmation.

---

### Q12 — Un commentaire qui répète le code vs un commentaire utile

```python
# MAUVAIS — répète ce que le code dit déjà
heures_investies = heures_par_jour * jours_ecoules

# BON — explique le POURQUOI, pas le QUOI
# Règle métier : on mesure l'investissement en heures, pas en jours
heures_investies = heures_par_jour * jours_ecoules
```

**Règle :** Un bon commentaire explique **pourquoi** ce choix a été fait, pas **ce que** le code fait. Le code dit déjà ce qu'il fait.

---

### Q13 — Formater un float pour limiter les décimales

```python
valeur = 52.142857142857146
print(valeur)              # 52.142857142857146 — illisible
print(f"{valeur:.2f}")     # 52.14 — 2 décimales
print(f"{valeur:.1f}")     # 52.1  — 1 décimale
print(f"{valeur:.0f}")     # 52    — aucune décimale
```

La syntaxe `:.2f` dans une f-string signifie : afficher comme un float avec 2 décimales.
**Règle :** Dans le vrai travail data, on formate toujours les floats pour la lisibilité.

---

## CONCEPTS FONDAMENTAUX

---

### Le cycle Git complet — à mémoriser

```
ZONE 1 — Working Directory    (tu modifies le fichier)
              ↓  git add
ZONE 2 — Staging Area         (tu prépares ce que tu vas sauvegarder)
              ↓  git commit
ZONE 3 — Repository local     (sauvegarde sur ta machine)
              ↓  git push
ZONE 4 — GitHub               (sauvegarde distante, visible par tous)
```

---

### Les types Python fondamentaux

| Type | Exemple | Description |
|------|---------|-------------|
| `str` | `"Cotonou"` | Texte, toujours entre guillemets |
| `int` | `42` | Nombre entier |
| `float` | `3.14` | Nombre décimal |
| `bool` | `True` / `False` | Vrai ou faux, exactement deux valeurs |

**Attention critique :** `"5" + "3"` = `"53"` (concaténation de texte). `5 + 3` = `8` (addition). Python se comporte différemment selon le type.

---

### Opérateurs de comparaison

```python
x == y    # égal à (≠ de = qui assigne)
x != y    # différent de
x > y     # strictement supérieur
x < y     # strictement inférieur
x >= y    # supérieur ou égal
x <= y    # inférieur ou égal
```

`=` assigne une valeur. `==` compare deux valeurs. Ce sont deux choses différentes.

---

*Dernière mise à jour : Phase 0 — Sessions 1 à 3 complétées*
*Repository : github.com/marmicoza/operateur-data*
