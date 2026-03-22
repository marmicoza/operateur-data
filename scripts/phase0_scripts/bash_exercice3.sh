#!/bin/bash

if [ -z "$1" ]; then
    echo "Erreur: usage bash bash_exercice3.sh niveau"
    exit 1
fi

if [ "$1" -ge 80 ]; then
    echo "Excellent niveau"
elif [ "$1" -ge 60 ]; then
    echo "Bon niveau"
elif [ "$1" -ge 40 ]; then
    echo "Niveau moyen"
else
    echo "Niveau insuffisant"
fi

