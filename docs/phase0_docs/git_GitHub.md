# Récapitulatif Git \& GitHub — Phase 0

## Référence complète — Formation Opérateur

\---

## 1\. Qu'est-ce que Git ?

Git est un système de contrôle de version. Il suit l'historique de chaque modification apportée à un projet. Chaque version est sauvegardée, traçable et récupérable.

**Sans Git :** le code existe uniquement sur la machine locale. Si la machine tombe en panne, tout disparaît.

**Avec Git :** chaque version du travail est sauvegardée localement et peut être synchronisée sur GitHub — accessible depuis n'importe où, visible par n'importe qui.

\---

## 2\. Qu'est-ce que GitHub ?

GitHub est une plateforme en ligne qui héberge des repositories Git. C'est là que le code est stocké à distance et rendu public. C'est aussi le portfolio visible par les recruteurs et les clients.

Git = l'outil local. GitHub = le serveur distant.

\---

## 3\. Installation et configuration initiale

### Installer Git

Télécharger sur **git-scm.com/download/win**.

Pendant l'installation, sélectionner :

> \*\*Git from the command line and also from 3rd-party software\*\*

Vérifier l'installation :

```bash
git --version
```

### Configurer son identité

À faire une seule fois après l'installation. Ces informations apparaissent sur chaque commit.

```bash
git config --global user.name "Prénom Nom"
git config --global user.email "email@exemple.com"
```

Vérifier que les valeurs sont enregistrées :

```bash
git config --global user.name
git config --global user.email
```

Chaque commande retourne la valeur configurée. Si elle ne retourne rien, la configuration n'a pas été enregistrée — recommencer.

Voir toute la configuration Git :

```bash
git config --list
```

\---

## 4\. Les 4 zones de Git

Comprendre ces zones est fondamental. Chaque modification passe par ces étapes dans l'ordre.

```
ZONE 1 — Working Directory
         Tu modifies les fichiers ici.
              ↓  git add
ZONE 2 — Staging Area
         Tu prépares ce que tu vas sauvegarder.
              ↓  git commit
ZONE 3 — Repository local
         La sauvegarde est créée sur ta machine.
              ↓  git push
ZONE 4 — GitHub (origin)
         La sauvegarde est envoyée en ligne, visible par tous.
```

Il n'y a pas de raccourci entre ces zones. L'ordre est toujours respecté.

\---

## 5\. Créer un repository

### Sur GitHub

1. Cliquer sur `+` en haut à droite → **New repository**
2. Remplir le nom du repo
3. Cocher **Public**
4. Cocher **Add a README file**
5. Cliquer **Create repository**

### Cloner le repo en local

Sur la page GitHub du repo, cliquer **Code** → copier l'URL HTTPS.

```bash
git clone https://github.com/username/nom-du-repo.git
cd nom-du-repo
ls
```

Le dossier `nom-du-repo/` est maintenant sur la machine avec le fichier `README.md` dedans.

\---

## 6\. Le cycle quotidien — les commandes fondamentales

C'est la séquence répétée à chaque session de travail.

```bash
# Voir l'état actuel du repo
git status

# Ajouter un fichier spécifique au staging
git add nom\_du\_fichier.py

# Ajouter tous les fichiers modifiés au staging
git add .

# Créer un commit (sauvegarde locale)
git commit -m "type: description courte"

# Envoyer sur GitHub
git push origin main
```

### Voir ce qui a changé avant d'ajouter

```bash
git diff nom\_du\_fichier
```

Affiche les lignes ajoutées en vert et supprimées en rouge.

\---

## 7\. Les messages de commit — convention standard

Un message de commit doit dire **ce qui a changé et pourquoi** en moins de 50 caractères.

|Préfixe|Usage|
|-|-|
|`feat`|Ajout de nouveau code ou fonctionnalité|
|`fix`|Correction d'un bug ou d'une erreur|
|`docs`|Documentation (journal, README, guides)|
|`update`|Modification d'un fichier existant|
|`add`|Ajout d'une ressource (dataset, image, config)|

**Mauvais :** `git commit -m "modifications"`
**Bon :** `git commit -m "feat: analyseur de notes avec boucles"`

\---

## 8\. Comprendre `git push origin main`

Chaque mot a un sens précis :

* **`git push`** — envoie les commits locaux vers un serveur distant
* **`origin`** — le nom donné par défaut au serveur distant (GitHub). Configuré automatiquement lors du `git clone`. Vérifier avec `git remote -v`
* **`main`** — le nom de la branche principale. GitHub crée cette branche par défaut

En français : *"Envoie mes commits vers GitHub, sur la branche main."*

Vérifier l'adresse associée à `origin` :

```bash
git remote -v
```

Résultat typique :

```
origin  https://github.com/username/nom-du-repo.git (fetch)
origin  https://github.com/username/nom-du-repo.git (push)
```

\---

## 9\. Supprimer des fichiers

### Supprimer partout — machine et GitHub

```bash
git rm nom\_du\_fichier.py
git commit -m "fix: suppression fichier inutile"
git push origin main
```

### Retirer de GitHub mais garder sur la machine

```bash
git rm --cached nom\_du\_fichier.py
git commit -m "fix: retrait fichier du suivi Git"
git push origin main
```

`--cached` signifie : retirer du suivi Git uniquement, sans toucher au fichier réel. Utile si un fichier sensible (mots de passe, clés API) a été ajouté par erreur.

\---

## 10\. Le fichier .gitignore

`.gitignore` liste les fichiers et dossiers que Git doit ignorer automatiquement. Ces fichiers ne seront jamais ajoutés, jamais commités, jamais envoyés sur GitHub.

### Créer le fichier

```bash
touch .gitignore
```

### Contenu typique pour un projet Python

```
venv/            # environnement virtuel — lourd et inutile sur GitHub
\*.pyc            # fichiers compilés Python — générés automatiquement
\_\_pycache\_\_/     # dossier cache Python
\*.env            # fichiers de configuration sensibles (mots de passe, clés API)
\*.csv            # données brutes volumineuses
.DS\_Store        # fichier système Mac
```

### Vérifier que le fichier est bien ignoré

```bash
git status
```

Les fichiers listés dans `.gitignore` ne doivent pas apparaître dans cet output.

### Commiter le .gitignore

`.gitignore` est un fichier comme les autres. Il doit être commité pour être actif sur GitHub.

```bash
git add .gitignore
git commit -m "docs: ajout gitignore"
git push origin main
```

\---

## 11\. Les environnements virtuels Python

### Pourquoi c'est nécessaire

Chaque projet peut avoir besoin de versions différentes des mêmes bibliothèques. Sans isolation, les projets entrent en conflit. Un environnement virtuel crée une installation Python isolée par projet.

### Créer l'environnement

```bash
python -m venv venv
```

Un dossier `venv/` apparaît dans le repo. Il contient une installation Python indépendante. Ce dossier doit toujours être dans `.gitignore` — il est lourd et chaque machine recrée le sien.

### Activer l'environnement

```bash
source venv/Scripts/activate     # Windows (Git Bash)
source venv/bin/activate         # Linux / Mac
```

Le terminal affiche `(venv)` au début de la ligne quand l'environnement est actif. Tout ce qui est installé avec `(venv)` actif va dans l'environnement isolé, pas dans le Python global.

### Désactiver l'environnement

```bash
deactivate
```

Le `(venv)` disparaît. Le Python global est à nouveau actif.

### Installer une bibliothèque

```bash
pip install nom\_bibliotheque
```

### Voir ce qui est installé

```bash
pip list
```

\---

## 12\. Le fichier requirements.txt

### Pourquoi c'est nécessaire

Quand quelqu'un clone le repo, il n'a pas le dossier `venv/`. Le fichier `requirements.txt` liste toutes les dépendances du projet avec leurs versions exactes. Il permet de recréer un environnement identique sur n'importe quelle machine.

### Générer le fichier

Avec l'environnement virtuel actif `(venv)` :

```bash
pip freeze > requirements.txt
```

`pip freeze` liste toutes les bibliothèques installées avec leurs versions. `>` redirige cet output vers le fichier `requirements.txt` au lieu de l'afficher dans le terminal.

### Vérifier le contenu

```bash
cat requirements.txt
```

Affiche le contenu du fichier. Résultat typique :

```
certifi==2026.2.25
charset-normalizer==3.4.6
idna==3.11
requests==2.32.5
urllib3==2.6.3
```

### Recréer l'environnement depuis le fichier

Sur une nouvelle machine ou pour un collègue :

```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

`-r` signifie "lire depuis un fichier". Toutes les bibliothèques listées sont installées automatiquement avec les bonnes versions.

### Commiter le fichier

```bash
git add requirements.txt
git commit -m "feat: ajout requirements.txt"
git push origin main
```

\---

## 13\. Vérifier l'état du repo à tout moment

```bash
git status
```

Quatre états possibles pour un fichier :

|Message|Signification|
|-|-|
|`Untracked files`|Fichier nouveau, jamais suivi par Git|
|`Changes not staged`|Fichier modifié mais pas encore ajouté au staging|
|`Changes to be committed`|Fichier dans le staging, prêt à être commité|
|`Your branch is ahead by N commits`|Commits locaux non encore envoyés sur GitHub — faire `git push`|

\---

## 14\. Voir l'historique des commits

```bash
git log
```

Affiche tous les commits avec leur identifiant, auteur, date et message.

Version compacte — une ligne par commit :

```bash
git log --oneline
```

\---

## 15\. Résumé des commandes — référence rapide

|Commande|Action|
|-|-|
|`git config --global user.name "Nom"`|Configurer le nom|
|`git config --global user.email "email"`|Configurer l'email|
|`git clone URL`|Cloner un repo distant en local|
|`git status`|Voir l'état actuel du repo|
|`git add fichier`|Ajouter un fichier au staging|
|`git add .`|Ajouter tous les fichiers modifiés|
|`git commit -m "message"`|Créer une sauvegarde locale|
|`git push origin main`|Envoyer sur GitHub|
|`git diff fichier`|Voir les modifications non staged|
|`git log --oneline`|Voir l'historique compact|
|`git rm fichier`|Supprimer un fichier partout|
|`git rm --cached fichier`|Retirer du suivi Git sans supprimer|
|`git remote -v`|Voir l'adresse du serveur distant|

\---

*Dernière mise à jour : Phase 0 complétée
Repository : github.com/marmicoza/operateur-data*

