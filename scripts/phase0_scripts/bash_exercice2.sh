#!/bin/bash
prenom=$1
nombre=$2

if [ -z "$prenom" ] || [ -z "$nombre" ]; then
    echo "Erreur: usage bash bash_exercice2.sh prénom nombre"
    exit 1
echo "Bonjour $prenom, tu as $nombre jours de travail derrière toi."