# Markdown — Référence
## Phase 0 — Formation Opérateur

---

## Pourquoi Markdown

Markdown est le standard d'écriture technique. GitHub, Jupyter Notebooks, la documentation, les README — tout utilise Markdown. Un fichier `.md` se transforme automatiquement en document formaté.

---

## Titres

```markdown
# Titre principal (H1)
## Titre secondaire (H2)
### Titre tertiaire (H3)
```

Un seul H1 par document. H2 pour les sections principales. H3 pour les sous-sections.

---

## Mise en forme du texte

```markdown
**texte en gras**
*texte en italique*
~~texte barré~~
```

---

## Listes

```markdown
Liste non ordonnée :
- Premier élément
- Deuxième élément
  - Sous-élément (2 espaces d'indentation)

Liste ordonnée :
1. Première étape
2. Deuxième étape
3. Troisième étape
```

---

## Code

Code inline — pour mentionner une commande ou variable dans une phrase :
```markdown
Utiliser la commande `pwd` pour voir le dossier actuel.
```

Bloc de code avec coloration syntaxique :
````markdown
```python
def saluer(nom):
    print(f"Bonjour {nom}")
```
````

Remplacer `python` par `bash`, `sql`, `javascript`, etc. selon le langage.

---

## Tableau

```markdown
| Colonne 1 | Colonne 2 | Colonne 3 |
|-----------|-----------|-----------|
| Valeur A  | Valeur B  | Valeur C  |
| Valeur D  | Valeur E  | Valeur F  |
```

Les cellules du tableau doivent être courtes et scannables — pas des paragraphes.

---

## Liens et images

```markdown
[Texte visible](https://url.com)
![Texte alternatif](https://url-image.png)
```

---

## Citation

```markdown
> "Le texte de la citation ici." — Auteur
```

---

## Ligne de séparation

```markdown
---
```

---

## Checklist

```markdown
- [x] Tâche complétée
- [ ] Tâche à faire
```

L'espace entre les crochets est obligatoire pour les cases non cochées : `[ ]` et non `[]`.

---

## Règles de qualité

**Titres** : toujours en phrase normale, pas en MAJUSCULES.

**Tableaux** : les descriptions dans les cellules restent courtes. Un tableau n'est pas un paragraphe — il doit être scannable en un coup d'œil.

**Commentaires** : un fichier `.md` ne commente pas ce qu'il fait — il documente une compétence, un projet, un processus.

---

## Prévisualisation dans VS Code

1. Ouvrir un fichier `.md`
2. Cliquer l'icône Preview en haut à droite
3. Le rendu s'affiche en temps réel à droite

---

## Fichiers Markdown dans ce projet

| Fichier | Contenu |
|---------|---------|
| `README.md` | Présentation publique du projet |
| `journal.md` | Suivi chronologique des sessions |
| `docs/*.md` | Référence par compétence |

---

*Phase 0 complétée — github.com/marmicoza/operateur-data*
