# Openclassrooms : DA Python : Projet 11
# Améliorez un projet existant en Python

## Contexte

Projet réalisé dans le cadre de la formation OpenClassrooms, parcours Développement d'applications Python.


## Présentation

### Organisation

Application centrale du projet :
- **purbeurre_project** : avec le fichier de paramètrage et les routes pour l'accés aux autres applications

Le projet contient trois applications liées à des fonctionnalités précises :
- **Users** : fonctionnalités permettant la gestion des utilisateurs
- **Products** : l'application permettant la sauvegarde des favoris préférés
- **Pages** : l'application se chargeant des produits en eux-mêmes

Et un dossier 
- **purbeurre_project/static** : fichiers nécessaires pour l'application (images, css...)


### Déploiement




### Données fournis par l'api

Pour l'import des données, la commande est  `python manage.py import_api`

### Tests

L'éxécution des tests se fait à partir de la commande `python manage.py test`.
La mesure de la couverture se lance avec `coverage run manage.py test`