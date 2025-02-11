#!/bin/bash

# Variables
VENV_DIR=".venv"
REQUIREMENTS="requirements.txt"

# Fonction pour installer les dépendances sur Ubuntu
install_dependencies_ubuntu() {
    echo "Installation des dépendances"
    sudo apt update
    sudo apt install -y python3 python3-pip libzbar0
    # Ajoutez ici d'autres dépendances spécifiques à votre application
}

# Fonction pour installer les dépendances sur Arch Linux
install_dependencies_arch() {
    echo "Installation des dépendances"
    sudo pacman -Syu --noconfirm python python-pip libzbar0
    # Ajoutez ici d'autres dépendances spécifiques à votre application
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
        pip install -U pip
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

# Fonction principale d'installation
install_app() {

    echo "Installation des dépendances Python..."
    setup_venv
    cleanup
    echo "Installation terminée !"
}

# Détecter la distribution et installer les dépendances
if [ -f /etc/os-release ]; then
    . /etc/os-release
    case $ID in
        ubuntu)
            install_dependencies_ubuntu
            ;;
        arch)
            install_dependencies_arch
            ;;
        *)
            echo "Distribution non supportée : $ID"
            exit 1
            ;;
    esac
else
    echo "Impossible de détecter la distribution."
    exit 1
fi

# Installer l'application
install_app
