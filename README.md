# Projet de Gestionnaire de Mots de Passe Sécurisé avec AES-256


## Description
Ce projet consiste en la création d’un gestionnaire de mots de passe sécurisé utilisant l’algorithme de chiffrement AES-256 en mode CBC (Cipher Block Chaining). Le programme demande l’entrée d’un mot de passe maître pour accéder aux mots de passe stockés et permet de rechercher, ajouter, ou supprimer des mots de passe pour des applications spécifiques.

## Objectifs et Fonctionnalités

- **Chiffrement et Déchiffrement sécurisés** : Le gestionnaire utilise AES-256 pour chiffrer et déchiffrer les mots de passe. Une clé de chiffrement est dérivée d’un mot de passe maître via une fonction de hachage SHA-256.
- **Stockage sécurisé** : Les mots de passe sont sauvegardés sous forme de paires chiffrées dans un fichier JSON, garantissant qu'ils restent illisibles sans le mot de passe maître.
- **Authentification par mot de passe maître** : Un contrôle par mot de passe maître est mis en place pour protéger l’accès au gestionnaire. L'algorithme utilise un hash SHA-256 pour comparer le mot de passe maître saisi avec une valeur pré-enregistrée, garantissant une protection efficace contre les accès non autorisés.
- **Fonctionnalités de gestion des mots de passe** :
-   **Recherche** : Permet de rechercher un mot de passe par nom d’application, avec déchiffrement automatique pour l'affichage sécurisé du mot de passe.
-   **Ajout** : Facilite l'ajout d’un nouveau mot de passe pour une application, en chiffrant d’abord les données avant de les sauvegarder.
-   **Suppression** : Permet la suppression sécurisée des mots de passe associés à une application donnée après confirmation.

## Technologies Utilisées

- **Python** : Langage de programmation principal.
- **PyCryptodome** : Librairie pour l’implémentation de l’algorithme AES.
- **JSON** : Format de stockage des mots de passe.
- **OS** : Module pour la gestion de la console (clear screen) et la vérification de l’existence du fichier de mots de passe.

## Code et Structure

- **Fonction `get_forms()`** : Récupère tous les formulaires de la page web.
- **Fonction `form_details()`** : Analyse chaque formulaire et collecte les détails des champs.
- **Fonction `vulnerable()`** : Vérifie les réponses pour détecter des indices de vulnérabilité SQL injection.
- **Fonction `sql_injection_scan()`** : Coordonne l'analyse et envoie des charges aux formulaires pour tester leur résilience.

## Exemple d’Utilisation
En exécutant le script et en fournissant l'URL d'une page cible, l’outil analyse les formulaires, exécute les tests d’injection SQL et fournit un retour sur les vulnérabilités potentielles.
