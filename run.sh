#!/bin/bash


# Variables par défaut
MODE=""
VENV_DIR=".venv"
REQUIREMENTS="requirements.txt"



# Fonction d'aide
usage() {
    echo "Usage: $0 [-m mode]"
    echo "Options:"
    echo "  -m mode  : Choisir le mode d'exécution ( prod / dev )"
    exit 1
}


# Fonction pour initialiser l'environnement
setup_venv() {
    if [ ! -d $VENV_DIR ]; then
        echo "Creation de l'environnement virtuel."
        python3 -m venv "$VENV_DIR"
    fi

    echo "Activation de l'environnement.."
    source "$VENV_DIR/bin/activate"

    if [ -f $REQUIREMENTS ]; then
        echo "Installation des dépendances..."
        pip install -r "$REQUIREMENTS"
    else
        echo "Fichier $REQUIREMENTS non trouvé"
    fi
}

# Fonction pour désactiver l'environnement
cleanup() {
    echo "Désactivation de l'environnement"
    deactivate
}


# Traitement des arguments
while getopts ":m:" opt; do
    case $opt in
        m)
            MODE="$OPTARG"
            ;;
        \?)
            echo "Option invalide: -$OPTARG"
            usage
            ;;
        :)
            echo "L'option -$OPTARG nécessite un argument."
            usage
            ;;
    esac
done

# Vérification du mode
if [[ -z "$MODE" ]]; then
    echo "Erreur: Vous devez spécifier le mode avec -m"
    echo "Info: -m prod (production) / -m dev (Developement)"
    usage
fi

# Décalage des arguments traités
shift $((OPTIND-1))

# Logique en fonction du mode
case "$MODE" in
    "prod")
        echo "Mode Prod"
        setup_venv
        flask run
        cleanup
        ;;
    "dev")
        echo "Mode Dev"
        setup_venv
        flask run --debug
        cleanup
        ;;
    *)
        echo "Mode inconnu: $MODE"
        echo $MODE
        usage
        ;;
esac

# flask --app ./src/Main run