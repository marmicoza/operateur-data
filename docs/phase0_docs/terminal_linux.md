# Terminal & Linux — Référence
## Phase 0 — Formation Opérateur

---

## Pourquoi le terminal

Le terminal permet de parler directement à la machine sans interface graphique. Tous les serveurs, outils cloud, pipelines de données et environnements de production fonctionnent via le terminal. C'est une compétence non négociable.

---

## Configurer Git Bash sur Windows

Par défaut, VS Code utilise PowerShell sur Windows. PowerShell ne reconnaît pas les commandes Linux standard. Git Bash émule un environnement Linux sur Windows.

**Configuration :**
1. `Ctrl+Shift+P` dans VS Code
2. Taper : `Terminal: Select Default Profile`
3. Sélectionner **Git Bash**
4. Fermer et rouvrir le terminal (`Ctrl+`` ` ``)

Le terminal affiche maintenant `user@machine MINGW64 ~/...` au lieu de `PS C:\...`

---

## Navigation

```bash
pwd                      # afficher le dossier actuel (Print Working Directory)
ls                       # lister les fichiers et dossiers ici
ls -la                   # lister avec détails (permissions, taille, dates)
cd nom_dossier           # entrer dans un dossier
cd ..                    # remonter d'un niveau (dossier parent)
cd ../autre_dossier      # remonter puis entrer dans un autre dossier
cd ~                     # aller directement au dossier home
cd -                     # retourner au dossier précédent
```

---

## Créer et supprimer

```bash
mkdir nom_dossier        # créer un dossier
mkdir -p a/b/c           # créer des dossiers imbriqués en une commande
touch nom_fichier.py     # créer un fichier vide
rm nom_fichier.py        # supprimer un fichier
rm -r nom_dossier        # supprimer un dossier et tout son contenu
cp source destination    # copier un fichier
mv source destination    # déplacer ou renommer un fichier
```

---

## Lire et écrire des fichiers

```bash
cat nom_fichier          # afficher le contenu d'un fichier
cat fichier.txt          # afficher requirements.txt, .gitignore, etc.
>                        # rediriger l'output vers un fichier (écrase)
>>                       # rediriger l'output vers un fichier (ajoute à la fin)
```

Exemple :
```bash
pip freeze > requirements.txt    # écrit l'output de pip freeze dans le fichier
echo "venv/" >> .gitignore       # ajoute une ligne à .gitignore
```

---

## Informations utiles

```bash
clear                    # vider l'écran du terminal
history                  # voir les dernières commandes tapées
which python             # savoir quel Python est utilisé
python --version         # vérifier la version de Python
git --version            # vérifier la version de Git
```

---

## Différence Windows / Linux

| Action | Windows (PowerShell) | Linux / Git Bash |
|--------|---------------------|-----------------|
| Créer un fichier | `ni fichier.py` | `touch fichier.py` |
| Lister les fichiers | `dir` | `ls` |
| Afficher le dossier actuel | `cd` | `pwd` |
| Supprimer un fichier | `del fichier` | `rm fichier` |

En travaillant sous Git Bash, les commandes Linux fonctionnent sur Windows.

---

## Raccourcis terminal essentiels

| Raccourci | Action |
|-----------|--------|
| `Tab` | Autocomplétion du nom de fichier ou dossier |
| `↑` / `↓` | Naviguer dans l'historique des commandes |
| `Ctrl+C` | Interrompre une commande en cours |
| `Ctrl+L` | Vider l'écran (équivalent de `clear`) |

---

## Structure de dossiers recommandée pour un projet

```
mon-projet/
├── docs/           # documentation et référence
├── projets/        # code organisé par phase
├── venv/           # environnement virtuel (jamais sur GitHub)
├── .gitignore
├── README.md
└── requirements.txt
```

---

*Phase 0 complétée — github.com/marmicoza/operateur-data*
