# VS Code — Référence
## Phase 0 — Formation Opérateur

---

## Pourquoi VS Code

VS Code est l'éditeur de code le plus utilisé au monde. Léger, extensible, gratuit. Il supporte tous les langages qu'on utilisera — Python, SQL, Markdown, Bash, JavaScript.

---

## Installation

Télécharger sur **code.visualstudio.com**. Installation standard, aucune option particulière requise.

---

## Extensions installées — Phase 0

Ouvrir le panneau Extensions : icône carrés sur la gauche ou `Ctrl+Shift+X`

| Extension | Éditeur | Utilité |
|-----------|---------|---------|
| Python | Microsoft | Support Python, exécution, debug |
| Pylance | Microsoft | Autocomplétion intelligente Python |

**Règle :** installer uniquement ce qui est nécessaire. Trop d'extensions ralentit VS Code.

---

## Configurer le terminal par défaut

Par défaut VS Code utilise PowerShell sur Windows. On le configure pour utiliser Git Bash.

1. `Ctrl+Shift+P`
2. Taper : `Terminal: Select Default Profile`
3. Sélectionner **Git Bash**
4. Fermer et rouvrir le terminal

---

## Configurer l'interpréteur Python

VS Code doit savoir quel Python utiliser — celui de l'environnement virtuel, pas le global.

1. Cliquer sur la version Python en bas à gauche de la fenêtre
2. Dans la liste, sélectionner l'option contenant `venv` dans le chemin
3. Si `venv` n'apparaît pas : cliquer **Browse** et naviguer vers `venv/Scripts/python.exe`

L'interpréteur actif est visible en bas à gauche en permanence.

---

## Raccourcis essentiels

| Raccourci | Action |
|-----------|--------|
| `Ctrl+N` | Nouveau fichier |
| `Ctrl+S` | Sauvegarder |
| `Ctrl+Shift+S` | Sauvegarder sous |
| `Ctrl+`` ` `` | Ouvrir / fermer le terminal intégré |
| `Ctrl+Shift+P` | Palette de commandes (accès à tout) |
| `Ctrl+Shift+X` | Panneau Extensions |
| `Ctrl+/` | Commenter / décommenter une ligne |
| `Alt+↑` / `Alt+↓` | Déplacer une ligne vers le haut / bas |
| `Ctrl+D` | Sélectionner l'occurrence suivante du mot |
| `Ctrl+F` | Chercher dans le fichier |
| `Ctrl+H` | Chercher et remplacer |
| `Ctrl+Z` | Annuler |

---

## Prévisualisation Markdown

Pour voir le rendu Markdown en temps réel pendant l'écriture :

1. Ouvrir un fichier `.md`
2. Cliquer l'icône **Preview** en haut à droite (deux colonnes avec une loupe)
3. Le rendu s'affiche à droite, le code à gauche

---

## Exécuter un fichier Python

**Via le terminal intégré :**
```bash
python nom_fichier.py
```

S'assurer que le terminal est dans le bon dossier (`pwd`) avant d'exécuter.

---

*Phase 0 complétée — github.com/marmicoza/operateur-data*
