# Systeme de gestion municipale - Mali

Ce projet est une personnalisation de **Base IMIS** pour une utilisation locale au Mali. Il rassemble une application web Laravel/PHP, une application mobile de collecte terrain, la documentation de deploiement, les manuels utilisateur et des ressources complementaires.

## Objectif

Cette version vise a fournir un socle numerique reutilisable pour une mairie ou un service administratif local, avec :

- une interface orientee gestion municipale ;
- une localisation francaise ;
- un parametage par defaut pour le fuseau horaire `Africa/Bamako` ;
- un branding configurable pour vos liens publics, votre organisation et vos informations de contact.

## Contenu du depot

- [`web_app`](./web_app) : application web Laravel/PHP
- [`mobile_app`](./mobile_app) : application mobile React Native
- [`deployment_documentation`](./deployment_documentation) : guides et ressources de deploiement
- [`user_manual`](./user_manual) : manuels utilisateur PDF
- [`additional_resources`](./additional_resources) : ressources pedagogiques et visuelles
- [`.github`](./.github) : fichiers de gouvernance, credits et publication GitHub

## Installation rapide

### Application web

1. Copier [`web_app/.env.example`](./web_app/.env.example) vers un fichier `.env`.
2. Renseigner la base de donnees, l'URL de l'application et les variables de branding.
3. Installer les dependances PHP et JavaScript.
4. Executer les migrations, imports et builds necessaires selon votre environnement.

### Application mobile

1. Copier `mobile_app/example.env.dev` ou `mobile_app/example.env.prod` vers le fichier d'environnement attendu.
2. Renseigner l'URL de l'API et les liens publics de votre organisation.
3. Installer les dependances puis lancer le build Android ou iOS.

### Documentation

Consulter en priorite :

- [`deployment_documentation/README.md`](./deployment_documentation/README.md)
- [`web_app/README.md`](./web_app/README.md)
- [`user_manual/README.md`](./user_manual/README.md)

## Credits et licence

Ce projet est **base sur Base IMIS** :

- Projet original : [Base IMIS](https://github.com/base-imis/.github)
- Createurs originaux : Innovative Solution Pvt. Ltd. (ISPL) et GWSC-AIT
- Licence d'origine : [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1)

Les fichiers de licence existants sont conserves dans le depot. Avant toute diffusion publique ou usage institutionnel, verifiez la compatibilite de votre mode d'utilisation avec les obligations de la licence.
