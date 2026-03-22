#!/bin/bash
# Ligne obligatoire — dit à la machine d'utiliser bash

NOM_PROJET=$1
# Récupère le premier argument (le nom du projet)
# Ex: bash nouveau_projet.sh mon-projet → NOM_PROJET = "mon-projet"

DATE_AUJOURD_HUI=$(date +%Y-%m-%d)
# $(commande) exécute une commande et met le résultat dans une variable
# date +%Y-%m-%d retourne la date du jour au format 2025-03-20

if [ -z "$NOM_PROJET" ]; then
    echo "Erreur : tu dois donner un nom au projet."
    exit 1
fi
# Si aucun argument donné, affiche erreur et arrête

mkdir -p $NOM_PROJET/{docs,data/raw,data/processed,notebooks,scripts,outputs}
# Crée le dossier projet et tous ses sous-dossiers d'un coup

mkdir -p $NOM_PROJET/{docs,data/raw,data/processed,notebooks,scripts,outputs}
# Crée le dossier projet et tous ses sous-dossiers d'un coup

cat > $NOM_PROJET/README.md << EOF
# $NOM_PROJET
EOF
# Crée README.md avec du contenu dedans

git init
git add .
git commit -m "feat: initialisation projet $NOM_PROJET"
# Initialise Git et fait le premier commit automatiquement
