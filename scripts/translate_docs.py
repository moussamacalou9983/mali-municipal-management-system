from pathlib import Path
import re
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
DOC_EXTS = {'.md', '.MD', '.txt', '.rst'}
EXCLUDE = {'web_app/public/robots.txt'}

MANUAL = {
    '.github/CONTRIBUTING.md': '''# Guide de contribution

Merci d'envisager de contribuer a notre projet. Votre soutien nous aide a grandir et a nous ameliorer. Ce document explique comment contribuer de maniere efficace et collaborative.

## 1. Contributions bienvenues

Les contributions sont les bienvenues, qu'il s'agisse de corriger des bogues, de mettre en oeuvre de nouvelles fonctionnalites, d'ameliorer la documentation ou d'apporter d'autres evolutions.

### Comment commencer

- Parcourez le depot afin de comprendre les objectifs du projet et son etat d'avancement.
- Consultez les issues et les discussions ouvertes pour trouver des taches a traiter ou proposer de nouvelles idees.
- Verifiez que vos contributions respectent les conditions de licence de la licence **CC BY-NC-SA 4.0**.

---

## 2. Branches et pull requests

Pour conserver un flux de travail organise :

- Les **pull requests (PR)** doivent cibler la branche `dev`.
  - La branche `dev` est la branche de developpement active dans laquelle les nouvelles contributions sont testees.
- Il est **recommande de recuperer le code depuis la branche `main`** afin de partir de la base de code stable la plus recente.

### Etapes pour soumettre une PR

1. Forkez le depot et creez une branche de fonctionnalite (par exemple `feature/nouvelle-fonctionnalite`).
2. Travaillez sur votre fonctionnalite ou votre correctif en maintenant une bonne qualite de code et une documentation adequate.
3. Poussez vos changements et ouvrez une PR ciblee sur la branche `dev`.
4. Decrivez clairement l'objectif et le contenu de votre contribution dans la description de la PR.

---

## 3. Processus de revue des PR

- Les PR sont examinees periodiquement par l'equipe de developpement.
- Les contributions sont evaluees selon la qualite du code, leur alignement avec les objectifs du projet et le respect des conditions de licence.
- Apres revue, votre PR sera **acceptee** ou **rejetee**, avec un retour detaille dans les deux cas.

---

## 4. Reconnaissance des contributeurs

Chaque contribution compte. Si votre PR est acceptee :

- Votre **nom d'utilisateur GitHub** sera ajoute a la **liste des contributeurs** du projet dans le fichier `README`.
- Les contributions majeures pourront egalement etre mentionnees dans les notes de version ou les mises a jour documentaires.
- Vous pouvez partager votre contribution sur les reseaux sociaux ou les plateformes professionnelles en mentionnant ce projet pour aider a le faire connaitre.

---

## 5. Issues et discussions

- **Issues** : n'hesitez pas a signaler des bogues, proposer de nouvelles fonctionnalites ou poser vos questions via GitHub Issues.
- **Discussions** : utilisez l'onglet Discussions pour partager des idees, poser des questions ou echanger avec la communaute.

---

## 6. Recommandations complementaires pour les contributeurs

Pour assurer une collaboration fluide :

- Respectez les standards de developpement et les bonnes pratiques utilises dans le depot.
- Redigez des messages de commit clairs et concis decrivant vos modifications.
- Ajoutez des commentaires dans votre code lorsque cela est necessaire pour en faciliter la lecture.
- Si vous ajoutez une nouvelle fonctionnalite, incluez des tests pertinents afin d'en valider le comportement.
- Verifiez que toutes vos contributions sont originales et respectent la licence.

---

## 7. Code de conduite

Tous les contributeurs doivent respecter notre [Code de conduite](https://github.com/base-imis/.github/blob/main/CODE_OF_CONDUCT.md). Merci de traiter chaque membre de la communaute avec respect et professionnalisme.

---

En contribuant a ce projet, vous acceptez de respecter les termes de la licence **Creative Commons Attribution - Pas d'utilisation commerciale - Partage dans les memes conditions 4.0 International (CC BY-NC-SA 4.0)**.

Si vous avez des questions, ouvrez une issue ou lancez une discussion. Merci de nous aider a ameliorer ce projet.
''',
    '.github/ORGANIZATION_STRUCTURE.MD': '''# Structure des depots de l'organisation IMIS

![Structure des depots de l'organisation IMIS](https://github.com/user-attachments/assets/c15d6041-b8cb-40ae-9be8-7481f876026f)
''',
    'deployment_documentation/docker_config/src/README.md': '''## Emplacement de votre application Laravel

Supprimez ce fichier avant de cloner ou copier votre projet Laravel dans ce dossier, ou creez un nouveau projet a cet emplacement en executant la commande suivante depuis la racine de ce depot :

```bash
docker-compose run --rm composer create-project --prefer-dist laravel/laravel .
```
''',
    'deployment_documentation/docker_config/README.md': '''# docker-compose-laravel

Flux de travail Docker Compose simplifie qui met en place un reseau LEMP de conteneurs pour le developpement local Laravel. Vous pouvez consulter l'article complet qui a inspire ce depot [ici](https://dev.to/aschmelyun/the-beauty-of-docker-for-local-laravel-development-13c0).

## Utilisation

Pour commencer, assurez-vous que [Docker est installe](https://docs.docker.com/docker-for-mac/install/) sur votre systeme, puis clonez ce depot.

Ensuite, placez-vous dans le terminal dans le dossier clone et lancez les conteneurs du serveur web avec `docker-compose up -d --build site`.

Une fois cette etape terminee, suivez les instructions du fichier [src/README.md](src/README.md) pour ajouter votre projet Laravel ou en creer un nouveau vide.

Le demarrage du reseau Docker Compose avec `site` plutot qu'avec `up` seulement garantit que seuls les conteneurs de notre site sont demarres au debut, et non l'ensemble des conteneurs de commande. Les services suivants sont construits pour le serveur web, avec leurs ports exposes :

- **nginx** - `:80`
- **mysql** - `:3306`
- **php** - `:9000`
- **redis** - `:6379`
- **mailhog** - `:8025`

Trois conteneurs supplementaires sont egalement inclus pour executer les commandes Composer, NPM et Artisan *sans* avoir a installer ces plateformes sur votre ordinateur local. Utilisez les exemples ci-dessous depuis la racine du projet, en les adaptant a votre besoin.

- `docker-compose run --rm composer update`
- `docker-compose run --rm npm run dev`
- `docker-compose run --rm artisan migrate`

## Problemes de permissions

Si vous rencontrez des problemes de permissions sur le systeme de fichiers en accedant a l'application ou en executant une commande dans un conteneur, suivez l'un des jeux d'etapes ci-dessous.

**Si vous utilisez votre serveur ou environnement local en tant qu'utilisateur root :**

- Arretez les conteneurs avec `docker-compose down`
- Remplacez le fichier precedent par `docker-compose.root.yml`
- Reconstruisez les conteneurs avec `docker-compose build --no-cache`

**Si vous utilisez votre serveur ou environnement local avec un utilisateur non root :**

- Arretez les conteneurs avec `docker-compose down`
- Dans votre terminal, executez `export UID=$(id -u)` puis `export GID=$(id -g)`
- Si vous voyez des erreurs concernant des variables en lecture seule lors de l'etape precedente, vous pouvez les ignorer et continuer
- Reconstruisez les conteneurs avec `docker-compose build --no-cache`

Ensuite, redemarrez votre reseau de conteneurs ou relancez la commande que vous essayiez d'executer, puis verifiez si le probleme est resolu.

## Stockage MySQL persistant

Par defaut, lorsque vous arretez le reseau Docker, vos donnees MySQL sont supprimees apres destruction des conteneurs. Si vous souhaitez conserver des donnees persistantes apres arret puis redemarrage des conteneurs, procedez ainsi :

1. Creez un dossier `mysql` a la racine du projet, a cote des dossiers `nginx` et `src`.
2. Sous le service mysql dans votre fichier `docker-compose.yml`, ajoutez les lignes suivantes :

```yaml
volumes:
  - ./mysql:/var/lib/mysql
```

## Utiliser BrowserSync avec Laravel Mix

Si vous souhaitez activer le rechargement a chaud fourni par l'option BrowserSync de Laravel Mix, quelques etapes supplementaires sont necessaires. Commencez par verifier que vous utilisez le `docker-compose.yml` mis a jour avec les ports `:3000` et `:3001` ouverts sur le service npm. Ajoutez ensuite ce qui suit a la fin du fichier `webpack.mix.js` de votre projet Laravel :

```javascript
.browserSync({
    proxy: 'site',
    open: false,
    port: 3000,
});
```

Depuis le terminal a la racine du projet, executez la commande suivante pour surveiller les changements avec le conteneur npm et ses ports associes :

```bash
docker-compose run --rm --service-ports npm run watch
```

Cela laissera ouvert un petit panneau d'information dans votre terminal, que vous pouvez quitter avec `Ctrl + C`. En visitant [localhost:3000](http://localhost:3000) dans votre navigateur, vous devriez alors charger l'application Laravel avec BrowserSync active et le rechargement a chaud en fonctionnement.

## MailHog

La version actuelle de Laravel utilise MailHog comme application par defaut pour tester l'envoi d'emails et le fonctionnement SMTP general pendant le developpement local. Avec l'image Docker Hub fournie, sa mise en place est simple et directe. Le service est inclus dans le fichier `docker-compose.yml` et demarre en meme temps que le serveur web et la base de donnees.

Pour consulter le tableau de bord et visualiser les emails transitant par le systeme, rendez-vous sur [localhost:8025](http://localhost:8025) apres avoir execute `docker-compose up -d site`.
''',
}
MANUAL.update({
    '.github/CODE_OF_CONDUCT.md': '''# Code de conduite du Contributor Covenant

## Notre engagement

En tant que membres, contributeurs et responsables, nous nous engageons a faire de la participation a notre communaute une experience exempte de harcelement pour toutes et tous, quels que soient l'age, la corpulence, un handicap visible ou invisible, l'origine ethnique, les caracteristiques sexuelles, l'identite et l'expression de genre, le niveau d'experience, l'education, la situation socio-economique, la nationalite, l'apparence personnelle, la race, la caste, la couleur, la religion, l'identite sexuelle ou l'orientation sexuelle.

Nous nous engageons a agir et a interagir de maniere a contribuer a une communaute ouverte, accueillante, diverse, inclusive et saine.

## Nos normes

Exemples de comportements qui contribuent a un environnement positif pour notre communaute :

* Faire preuve d'empathie et de bienveillance envers les autres
* Respecter la diversite des opinions, des points de vue et des experiences
* Donner un retour constructif et l'accepter avec elegance
* Assumer ses responsabilites et presenter des excuses aux personnes affectees par ses erreurs, puis apprendre de cette experience
* Se concentrer sur ce qui est benefique non seulement pour soi, mais aussi pour l'ensemble de la communaute

Exemples de comportements inacceptables :

* L'utilisation d'un langage ou d'images sexualises, ainsi que toute attention ou avance sexuelle de quelque nature que ce soit
* Le trolling, les commentaires insultants ou denigrants, ainsi que les attaques personnelles ou politiques
* Le harcelement en public ou en prive
* La publication d'informations privees appartenant a autrui, telles qu'une adresse postale ou electronique, sans autorisation explicite
* Tout autre comportement qui pourrait raisonnablement etre considere comme inapproprie dans un cadre professionnel

## Responsabilites en matiere d'application

Les responsables de la communaute ont la responsabilite de clarifier et de faire respecter nos normes de comportement acceptable. Ils prendront des mesures correctives appropriees et equitables en reponse a tout comportement juge inapproprie, menacant, offensant ou nuisible.

Les responsables de la communaute ont le droit et la responsabilite de supprimer, modifier ou rejeter des commentaires, commits, portions de code, modifications du wiki, issues et autres contributions qui ne sont pas conformes au present Code de conduite, et ils communiqueront, lorsque cela est approprie, les raisons de leurs decisions de moderation.

## Portee

Ce Code de conduite s'applique dans tous les espaces de la communaute, ainsi que lorsqu'une personne represente officiellement la communaute dans des espaces publics. Cela inclut notamment l'utilisation d'une adresse email officielle, la publication via un compte officiel sur les reseaux sociaux ou la participation en tant que representant designe lors d'un evenement en ligne ou hors ligne.

## Application

Les comportements abusifs, harcelants ou autrement inacceptables peuvent etre signales aux responsables de la communaute charges de l'application a l'adresse [INSERT CONTACT METHOD].
Toutes les plaintes seront examinees et instruites rapidement et avec impartialite.

Tous les responsables de la communaute sont tenus de respecter la confidentialite et la securite de toute personne ayant signale un incident.

## Lignes directrices d'application

Les responsables de la communaute suivront les lignes directrices d'impact communautaire ci-dessous pour determiner les consequences de toute action qu'ils considerent comme contraire au present Code de conduite.

### 1. Correction

**Impact sur la communaute** : utilisation d'un langage inapproprie ou de tout autre comportement juge non professionnel ou malvenu au sein de la communaute.

**Consequence** : avertissement prive et ecrit des responsables de la communaute, expliquant clairement la nature de la violation et les raisons pour lesquelles le comportement etait inapproprie. Des excuses publiques peuvent etre demandees.

### 2. Avertissement

**Impact sur la communaute** : violation par un incident unique ou une serie d'actions.

**Consequence** : avertissement assorti de consequences en cas de repetition. Aucune interaction avec les personnes concernees, y compris les interactions non sollicitees avec les personnes chargees de faire respecter le Code de conduite, n'est autorisee pendant une periode definie. Cela inclut l'evitement des interactions dans les espaces communautaires ainsi que sur les canaux externes tels que les reseaux sociaux. Le non-respect de ces conditions peut entrainer une suspension temporaire ou permanente.

### 3. Suspension temporaire

**Impact sur la communaute** : violation grave des normes de la communaute, y compris un comportement inapproprie persistant.

**Consequence** : suspension temporaire de toute interaction ou communication publique avec la communaute pendant une periode definie. Aucune interaction publique ou privee avec les personnes impliquees, y compris les interactions non sollicitees avec les personnes chargees de faire respecter le Code de conduite, n'est autorisee durant cette periode. Le non-respect de ces conditions peut entrainer une exclusion permanente.

### 4. Exclusion permanente

**Impact sur la communaute** : demonstration d'un schema de violations des normes de la communaute, y compris un comportement inapproprie persistant, le harcelement d'une personne ou une agression envers des categories de personnes, ou leur denigrement.

**Consequence** : exclusion permanente de toute forme d'interaction publique au sein de la communaute.

## Attribution

Ce Code de conduite est adapte du [Contributor Covenant][homepage], version 2.1, disponible a l'adresse [https://www.contributor-covenant.org/version/2/1/code_of_conduct.html][v2.1].

Les lignes directrices d'impact communautaire ont ete inspirees de [l'echelle d'application du code de conduite de Mozilla][Mozilla CoC].

Pour obtenir des reponses aux questions frequentes sur ce code de conduite, consultez la FAQ a l'adresse [https://www.contributor-covenant.org/faq][FAQ]. Des traductions sont disponibles a l'adresse [https://www.contributor-covenant.org/translations][translations].

[homepage]: https://www.contributor-covenant.org
[v2.1]: https://www.contributor-covenant.org/version/2/1/code_of_conduct.html
[Mozilla CoC]: https://github.com/mozilla/diversity
[FAQ]: https://www.contributor-covenant.org/faq
[translations]: https://www.contributor-covenant.org/translations
''',
    '.github/profile/README.md': '''<div align=center>
<img src="https://github.com/user-attachments/assets/69f97175-6ee2-4e79-aad9-dfaf5afa4ad1"> </img>
</div>

<p align=justify> Le Systeme integre d'information municipale (IMIS) est une infrastructure publique numerique (DPI) open source, fondee sur les SIG, qui fonctionne a la fois comme systeme d'information municipale et comme solution logicielle. Il integre donnees, processus et services pour renforcer la gouvernance municipale, en particulier dans la gestion de l'assainissement selon l'approche Citywide Inclusive Sanitation (CWIS) afin de contribuer a l'atteinte de l'ODD 6.2. Il fournit aux municipalites des outils d'aide a la decision fondes sur les donnees pour renforcer la gouvernance dans plusieurs secteurs. En s'appuyant sur des technologies open source et sur les systemes d'information geographique (SIG), il facilite :</p>

- la planification, la gestion et le suivi des systemes d'assainissement selon l'approche CWIS ;
- la supervision de bout en bout de la chaine de services FSM (gestion des boues de vidange), y compris le suivi des donnees en temps reel ;
- la production et la visualisation des indicateurs CWIS pour l'evaluation des performances ;
- des tableaux de bord intuitifs permettant de suivre les indicateurs CWIS, les indicateurs cles de performance (KPI) et d'autres metriques essentielles de gouvernance municipale.

<p align=justify> En tant que systeme public de donnees infranational, IMIS contribue au suivi a l'echelle nationale en alimentant des systemes centralises, au service des indicateurs CWIS et d'autres mesures critiques pour l'atteinte des objectifs d'assainissement. Au-dela de l'assainissement, grace a sa conception modulaire et evolutive, Base IMIS donne aux collectivites locales un cadre unifie, pilote par les donnees, qui ameliore l'efficacite, la responsabilite et la qualite de service dans la gouvernance municipale.</p>

<p align=justify> IMIS comprend 10 modules fonctionnels (fig. 1) : Building Information Management System (BIMS), Utility Information Management System (UIMS), Faecal Sludge Information Management System (FSIMS), Community/Public Toilet Information Management System (PTCTIMS), Sewer Connection Information Support System (SCISS), Public Health Information Support System (PHISS) et Urban Management Decision Support System (UMDSS), ainsi que des modules a valeur ajoutee pour la collecte de la taxe fonciere (PTCISS), les dechets solides (SWISS) et l'approvisionnement en eau (WSISS). Ces modules fournissent des tableaux de bord, des outils spatiaux et des capacites d'integration, ainsi que des tableaux de bord avances pour les indicateurs CWIS et les KPI, afin de soutenir une prise de decision fondee sur des preuves. Construit avec des technologies telles que PHP et PostgreSQL et diffuse sous licence CC BY-NC-SA 4.0, IMIS favorise l'innovation dans l'assainissement et la gouvernance urbaine en proposant aux municipalites des solutions evolutives, durables et inclusives. Ce depot fournit le code source, les guides d'installation et la documentation necessaires pour deployer IMIS efficacement.</p>

#### Base IMIS © 2022-2025 par [Innovative Solution Pvt. Ltd. (ISPL)](https://www.innovativesolution.com.np) et [Global Water & Sanitation Center - Asian Institute of Technology (GWSC-AIT)](https://www.gwsc.ait.ac.th/) est diffuse sous licence [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/?ref=chooser-v1) ![image](https://github.com/user-attachments/assets/54870276-c179-490a-986d-e7ca2a228107)

<p align="center">
<img width="100%" src="https://github.com/user-attachments/assets/ae2249c4-c43e-4add-9c2c-d66309ce0ec3" align="center"> </img>
</p>

Fig. 1 Module fonctionnel d'IMIS

# Liens rapides pour IMIS

### Base IMIS open source : [Decouvrir en detail le Systeme integre d'information municipale (IMIS).](https://github.com/base-imis/.github/blob/main/README.md)

### Structure detaillee de l'organisation GitHub : [En savoir plus sur la structure de l'organisation.](https://github.com/base-imis/.github/blob/main/ORGANIZATION_STRUCTURE.MD)

### Code source et documentation de l'application web : [Acceder au depot de l'application web.](https://github.com/base-imis/web_app)

### Code source et documentation de l'application mobile : [Explorer le depot de l'application mobile.](https://github.com/base-imis/mobile_app)

### Documentation et ressources de deploiement : [Consulter la documentation de deploiement.](https://github.com/base-imis/deployment_documentation)

### Manuels utilisateur : [Acceder aux guides utilisateur IMIS.](https://github.com/base-imis/user_manual)

### Ressources complementaires : [Consulter les ressources complementaires.](https://github.com/base-imis/additional_resources)

#### Brochure IMIS : [Un apercu visuel concis d'IMIS.](https://github.com/base-imis/additional_resources/blob/main/IMIS%20Brochure.pdf)

#### Poster IMIS : [Un resume visuel d'IMIS.](https://github.com/base-imis/additional_resources/blob/main/IMIS%20Poster.pdf)

#### Apercu du cadre d'evaluation de preparation : [En savoir plus sur le cadre d'evaluation de preparation.](https://github.com/base-imis/other_resources/blob/main/Readiness%20Assessment.pdf)

#### Questionnaire d'enquete batimentaire : [Acceder au questionnaire d'enquete batimentaire.](https://github.com/base-imis/other_resources/blob/main/Building%20Questionnaire.pdf)

#### Logo IMIS - [Standard : le logo officiel IMIS dans son format standard.](https://github.com/base-imis/additional_resources/blob/main/IMIS%20Logo%20-%20Standard.png)

#### Logo IMIS - [Inverse : le logo IMIS dans une palette de couleurs inversee.](https://github.com/base-imis/additional_resources/blob/main/IMIS%20Logo%20-%20Inverted.png)

#### Texte integral de la licence IMIS - [CC BY-NC-SA 4.0](https://github.com/base-imis/.github/blob/main/LICENSE.md)

#### Guide de contribution IMIS - [Consulter le guide de contribution](https://github.com/base-imis/.github/blob/main/CONTRIBUTING.md)

#### Code de conduite IMIS - [Consulter le code de conduite](https://github.com/base-imis/.github/blob/main/CODE_OF_CONDUCT.md)

#### Contact : pour plus d'informations, ecrivez-nous a [insol@innovativesolution.com.np](insol@innovativesolution.com.np).
''',
    'additional_resources/IMIS Icon Pack.md': '''# Icones

<table id="bkmrk-s.n.-name-icon-1-bui"><thead><tr><th>N°</th><th>Nom</th><th>Icone</th></tr></thead><tbody><tr><td>1</td><td>Batiment - Residentiel</td><td><img alt="Batiment - Residentiel" src="/IMIS Icon Pack/Icons - JPG/Building - Residential.jpg" height="65px" width="auto"> </td></tr>
<tr><td>2</td><td>Batiment - Commercial</td><td><img alt="Batiment - Commercial" src="/IMIS Icon Pack/Icons - JPG/Building - Commercial.jpg" height="65px" width="auto"> </td></tr>
<tr><td>3</td><td>Batiment - Mixte</td><td><img alt="Batiment - Mixte" src="/IMIS Icon Pack/Icons - JPG/Building - Mixed.jpg" height="65px" width="auto"> </td></tr>
<tr><td>4</td><td>Batiment - Gouvernemental</td><td><img alt="Batiment - Gouvernemental" src="/IMIS Icon Pack/Icons - JPG/Building - Government.jpg" height="65px" width="auto"> </td></tr>
<tr><td>5</td><td>Raccorde au reseau d'egout</td><td><img alt="Raccorde au reseau d'egout" src="/IMIS Icon Pack/Icons - JPG/Sewerage Connected.jpg" height="65px" width="auto"> </td></tr>
<tr><td>6</td><td>Fosse septique</td><td><img alt="Fosse septique" src="/IMIS Icon Pack/Icons - JPG/Septic Tank.jpg" height="65px" width="auto"> </td></tr>
<tr><td>7</td><td>Cuve de retention</td><td><img alt="Cuve de retention" src="/IMIS Icon Pack/Icons - JPG/Holding Tank.jpg" height="65px" width="auto"></td></tr>
<tr><td>8</td><td>Fosse</td><td><img alt="Fosse" src="/IMIS Icon Pack/Icons - JPG/Pit.jpg" height="65px" width="auto"> </td></tr>
<tr><td>9</td><td>Confinement</td><td><img alt="Confinement" src="/IMIS Icon Pack/Icons - JPG/Containment.jpg" height="65px" width="auto"> </td></tr>
<tr><td>10</td><td>Non autorise</td><td><img alt="Non autorise" src="/IMIS Icon Pack/Icons - JPG/Unauthorized.jpg" height="65px" width="auto"> </td></tr>
<tr><td>11</td><td>KPI - Efficacite de reponse aux demandes</td><td><img alt="KPI - Efficacite de reponse aux demandes" src="/IMIS Icon Pack/Icons - JPG/KPI - Application Response Efficiency.jpg" height="65px" width="auto"> </td></tr>
<tr><td>12</td><td>KPI - Satisfaction des clients</td><td><img alt="KPI - Satisfaction des clients" src="/IMIS Icon Pack/Icons - JPG/KPI - Customer Satisfaction.jpg" height="65px" width="auto"> </td></tr>
<tr><td>13</td><td>KPI - Service conforme a l'OHS</td><td><img alt="KPI - Service conforme a l'OHS" src='/IMIS Icon Pack/Icons - JPG/KPI - Service followed by OHS.jpg' height="65px" width="auto"> </td></tr>
<tr><td>14</td><td>Paiement / transaction financiere</td><td><img alt="Paiement / transaction financiere" src="/IMIS Icon Pack/Icons - JPG/Payment Financial Transaction.jpg" height="65px" width="auto"> </td></tr>
<tr><td>15</td><td>Demande de vidange</td><td><img alt="Demande de vidange" src="/IMIS Icon Pack/Icons - JPG/Emptying Appication.jpg" height="65px" width="auto"></td></tr>
<tr><td>16</td><td>Route la plus proche du batiment</td><td><img alt="Route la plus proche du batiment" src="/IMIS Icon Pack/Icons - JPG/Nearest Road to Building.jpg" height="65px" width="auto"> </td></tr>
<tr><td>17</td><td>Batiment raccorde au confinement</td><td><img alt="Batiment raccorde au confinement" src="/IMIS Icon Pack/Icons - JPG/Building Connected to Containment.jpg" height="65px" width="auto"> </td></tr>
<tr><td>18</td><td>Confinement raccorde au batiment</td><td><img alt="Confinement raccorde au batiment" src="/IMIS Icon Pack/Icons - JPG/Containment Connected to Building.jpg" height="65px" width="auto"> </td></tr>
<tr><td>19</td><td>Batiments associes (plusieurs batiments raccordes au batiment principal)</td><td><img alt="Batiments associes" src="/IMIS Icon Pack/Icons - JPG/Associated Buildings.jpg" height="65px" width="auto"> </td></tr>
<tr><td>20</td><td>Route</td><td><img alt="Route" src="/IMIS Icon Pack/Icons - JPG/Road.jpg" height="65px" width="auto"> </td></tr>
<tr><td>21</td><td>Systeme d'appui a l'information en sante publique</td><td><img alt="Systeme d'appui a l'information en sante publique" src="/IMIS Icon Pack/Icons - JPG/Public Health Information Support System.jpg" height="65px" width="auto"> </td></tr>
<tr><td>22</td><td>Systeme de gestion des informations sur les batiments</td><td><img alt="Systeme de gestion des informations sur les batiments" src="/IMIS Icon Pack/Icons - JPG/Building Information Management System.jpg" height="65px" width="auto"> </td></tr>
<tr><td>23</td><td>Systeme de gestion des informations sur les boues de vidange KPI - Vidange sure</td><td><img alt="Systeme de gestion des informations sur les boues de vidange KPI - Vidange sure" src="/IMIS Icon Pack/Icons - JPG/Fecal Sludge Information Management System.jpg" height="65px" width="auto"> </td></tr>
<tr><td>24</td><td>Systeme d'aide a la decision pour la gestion urbaine</td><td><img alt="Systeme d'aide a la decision pour la gestion urbaine" src="/IMIS Icon Pack/Icons - JPG/Urban Management Decision Support System.jpg" height="65px" width="auto"> </td></tr>
<tr><td>25</td><td>Systeme d'appui a l'information sur l'approvisionnement en eau</td><td><img alt="Systeme d'appui a l'information sur l'approvisionnement en eau" src="/IMIS Icon Pack/Icons - JPG/Water Supply Information Support System.jpg" height="65px" width="auto"> </td></tr>
<tr><td>26</td><td>Systeme d'appui a l'information sur les dechets solides</td><td><img alt="Systeme d'appui a l'information sur les dechets solides" src="/IMIS Icon Pack/Icons - JPG/Solid Waste Information Support System.jpg" height="65px" width="auto"> </td></tr>
<tr><td>27</td><td>Systeme d'appui a la collecte de la taxe fonciere</td><td><img alt="Systeme d'appui a la collecte de la taxe fonciere" src="/IMIS Icon Pack/Icons - JPG/Property Tax Collection Support System.jpg" height="65px" width="auto"> </td></tr>
<tr><td>28</td><td>Systeme de gestion des informations sur les branchements d'egout</td><td><img alt="Systeme de gestion des informations sur les branchements d'egout" src="/IMIS Icon Pack/Icons - JPG/Sewer Connection Information Management System.jpg" height="65px" width="auto"> </td></tr>
<tr><td>29</td><td>Systeme de gestion des services urbains</td><td><img alt="Systeme de gestion des services urbains" src="/IMIS Icon Pack/Icons - JPG/Utility Information Management System.jpg" height="65px" width="auto"> </td></tr>
<tr><td>30</td><td>Systeme de gestion des informations sur les toilettes communautaires / publiques (CT/PT)</td><td><img alt="Systeme de gestion des informations sur les toilettes communautaires / publiques (CT/PT)" src="/IMIS Icon Pack/Icons - JPG/Community  Public Toilet (CTPT) Information Management System.jpg" height="65px" width="auto"> </td></tr>
<tr><td>31</td><td>Client(s)</td><td><img alt="Client(s)" src="/IMIS Icon Pack/Icons - JPG/Customer.jpg" height="65px" width="auto"> </td></tr>
<tr><td>32</td><td>Centre(s) d'assistance</td><td><img alt="Centre(s) d'assistance" src="/IMIS Icon Pack/Icons - JPG/Help Desk.jpg" height="65px" width="auto"> </td></tr>
<tr><td>33</td><td>Utilisateur(s) final(aux)</td><td><img alt="Utilisateur(s) final(aux)" src="/IMIS Icon Pack/Icons - JPG/End Product User.jpg" height="65px" width="auto"> </td></tr>
<tr><td>34</td><td>Station(s) de traitement</td><td><img alt="Station(s) de traitement" src="/IMIS Icon Pack/Icons - JPG/Treatment Plant.jpg" height="65px" width="auto"> </td></tr>
<tr><td>35</td><td>Prestataire(s) de services</td><td><img alt="Prestataire(s) de services" src="/IMIS Icon Pack/Icons - JPG/Service Provider.jpg" height="65px" width="auto"></td></tr>
<tr><td>36</td><td>Definir la date de vidange</td><td><img alt="Definir la date de vidange" src="/IMIS Icon Pack/Icons - JPG/Set Emptying Date.jpg" height="65px" width="auto"></td></tr>
<tr><td>37</td><td>Details de la vidange</td><td><img alt="Details de la vidange" src="/IMIS Icon Pack/Icons - JPG/Emptying Details.jpg" height="65px" width="auto"> </td></tr>
<tr><td>38</td><td>Details du retour d'information et de la collecte des boues</td><td><img alt="Details du retour d'information et de la collecte des boues" src="/IMIS Icon Pack/Icons - JPG/Feedback Details.jpg" height="65px" width="auto"></td></tr></tbody></table>
''',
})
PHRASES = [
    ('Version: V1.0.0', 'Version : V1.0.0'),
    ('Table of Contents', 'Table des matieres'),
    ('Open-Source Base IMIS', 'Base IMIS open source'),
    ('Quicklinks for IMIS', 'Liens rapides pour IMIS'),
    ('Detailed GitHub Organization Structure', 'Structure detaillee de l\'organisation GitHub'),
    ('Web Application Source Code & Documentation', 'Code source et documentation de l\'application web'),
    ('Mobile Application Source Code & Documentation', 'Code source et documentation de l\'application mobile'),
    ('Deployment Documentation & Resources', 'Documentation et ressources de deploiement'),
    ('User Manuals', 'Manuels utilisateur'),
    ('Additional Resources', 'Ressources complementaires'),
    ('Learn in detail about the Integrated Municipal Information System (IMIS).', 'Decouvrir en detail le Systeme integre d\'information municipale (IMIS).'),
    ('Learn more about the Organization Structure.', 'En savoir plus sur la structure de l\'organisation.'),
    ('Access the Web Application Repository.', 'Acceder au depot de l\'application web.'),
    ('Explore the Mobile App Repository.', 'Explorer le depot de l\'application mobile.'),
    ('View Deployment Documentation.', 'Consulter la documentation de deploiement.'),
    ('Access IMIS User Guides.', 'Acceder aux guides utilisateur IMIS.'),
    ('View Additional Resources.', 'Consulter les ressources complementaires.'),
    ('A concise visual overview of IMIS.', 'Un apercu visuel concis d\'IMIS.'),
    ('A visual summary of IMIS.', 'Un resume visuel d\'IMIS.'),
    ('Learn more about the Readiness Assessment Framework.', 'En savoir plus sur le cadre d\'evaluation de preparation.'),
    ('Access the Building Survey Questionnaire.', 'Acceder au questionnaire d\'enquete batimentaire.'),
    ('The official IMIS logo in its standard format.', 'Le logo officiel IMIS dans son format standard.'),
    ('The IMIS logo in an inverted color scheme.', 'Le logo IMIS dans une palette de couleurs inversee.'),
    ('View the Contributing Guideline', 'Consulter le guide de contribution'),
    ('View the Code of Conduct', 'Consulter le code de conduite'),
    ('Contact Us: For further information, reach out to us at', 'Contact : pour plus d\'informations, ecrivez-nous a'),
    ('Evolution of IMIS', 'Evolution d\'IMIS'),
    ('Functional Modules of Base IMIS', 'Modules fonctionnels de Base IMIS'),
    ('Roles and Permissions', 'Roles et permissions'),
    ('IMIS Driven Sanitation Service Delivery Chain', 'Chaine de prestation des services d\'assainissement pilotee par IMIS'),
    ('Entities in IMIS-driven sanitation service delivery model', 'Entites du modele de prestation des services d\'assainissement pilote par IMIS'),
    ('Processes in IMIS-driven sanitation service delivery model', 'Processus du modele de prestation des services d\'assainissement pilote par IMIS'),
    ('Technical Stack', 'Pile technique'),
    ('IMIS Implementation Framework for New Cities', 'Cadre de mise en oeuvre d\'IMIS pour les nouvelles villes'),
    ('Accessing IMIS', 'Acces a IMIS'),
    ('Organization Structure', 'Structure de l\'organisation'),
    ('Branch Structure', 'Structure des branches'),
    ('Version Management', 'Gestion des versions'),
    ('Organization Maintenance', 'Maintenance de l\'organisation'),
    ('License Text', 'Texte de la licence'),
    ('Full License', 'Licence complete'),
    ('Contents', 'Sommaire'),
    ('Purpose', 'Objectif'),
    ('Target Audience', 'Public cible'),
    ('The Integrated Municipal Information System (IMIS) is an open-source GIS-based Digital Public Infrastructure (DPI) that serves as both a municipal information system and a software solution.', 'Le Systeme integre d\'information municipale (IMIS) est une infrastructure publique numerique open source, fondee sur les SIG, qui sert a la fois de systeme d\'information municipale et de solution logicielle.'),
    ('The development of IMIS has undergone multiple phases of growth, expanding from its initial scope into a more comprehensive tool.', 'Le developpement d\'IMIS a connu plusieurs phases de croissance, passant de son perimetre initial a un outil plus complet.'),
    ('The purpose of the document is to outline the technical process flow of IMIS and the coding conventions that have been followed.', 'L\'objectif de ce document est de presenter le flux de processus technique d\'IMIS ainsi que les conventions de developpement appliquees.'),
    ('The main target of this documentation is to provide insight on how IMIS has been developed in terms of coding, conventions followed and work flow of the system.', 'Cette documentation vise avant tout a expliquer comment IMIS a ete developpe en termes de code, de conventions suivies et de flux de travail du systeme.'),
    ('This document shall act as a reference to any developers working on IMIS about the work flow and technicalities of the code.', 'Ce document sert de reference pour tout developpeur travaillant sur IMIS concernant le flux de travail et les aspects techniques du code.'),
    ('Technical Information', 'Informations techniques'),
    ('File Structure & Storage Management', 'Structure des fichiers et gestion du stockage'),
    ('File Structure', 'Structure des fichiers'),
    ('Storage Management', 'Gestion du stockage'),
    ('The breakdown of file structure in Laravel:', 'Le detail de la structure des fichiers dans Laravel :'),
    ('This directory contains your application\'s core code.', 'Ce repertoire contient le code coeur de votre application.'),
    ('Contains custom PHP classes.', 'Contient des classes PHP personnalisees.'),
    ('Holds artisan console commands.', 'Contient les commandes console Artisan.'),
    ('Houses enumeration classes if you\'re using enums in your application.', 'Regroupe les classes d\'enumeration si vous utilisez des enums dans votre application.'),
    ('Contains exception handler classes.', 'Contient les classes de gestion des exceptions.'),
    ('For classes related to exporting data (e.g., to CSV, Excel).', 'Pour les classes liees a l\'export de donnees (par ex. CSV, Excel).'),
    ('Houses helper functions or classes used throughout your application.', 'Regroupe les fonctions utilitaires ou classes utilisees dans toute l\'application.'),
    ('Contains controllers, middleware, form requests, etc., related to HTTP requests.', 'Contient les controleurs, middlewares, form requests, etc., lies aux requetes HTTP.'),
    ('For classes related to importing data (e.g., from CSV, Excel).', 'Pour les classes liees a l\'import de donnees (par ex. CSV, Excel).'),
    ('Houses the Eloquent models.', 'Regroupe les modeles Eloquent.'),
    ('Contains service providers for the application.', 'Contient les fournisseurs de services de l\'application.'),
    ('For custom validation rule classes if you\'re using Laravel\'s validation system.', 'Pour les classes de regles de validation personnalisees si vous utilisez le systeme de validation de Laravel.'),
    ('Contains classes responsible for specific application services.', 'Contient les classes responsables de services applicatifs specifiques.'),
    ('Contains files for bootstrapping the Laravel application.', 'Contient les fichiers d\'initialisation de l\'application Laravel.'),
    ('Contains configuration files for various components of your application. Note: app.php contains class aliases used.', 'Contient les fichiers de configuration des differents composants de l\'application. Remarque : `app.php` contient les alias de classes utilises.'),
    ('Contains database-related files.', 'Contient les fichiers lies a la base de donnees.'),
    ('Contains the factories files.', 'Contient les fichiers de factories.'),
    ('Houses all database migration files.', 'Regroupe tous les fichiers de migration de base de donnees.'),
    ('Contains database seeder classes.', 'Contient les classes de seeding de la base de donnees.'),
    ('Contains the source code documentations, which is categorized according to the modules.', 'Contient la documentation du code source, classee par module.'),
    ('Contains the data dictionary of the system', 'Contient le dictionnaire de donnees du systeme'),
    ('Contains the parameters and values required for the initial geoserver setup for workspace, stores, layers and styles.', 'Contient les parametres et valeurs necessaires a la configuration initiale de GeoServer pour l\'espace de travail, les magasins, les couches et les styles.'),
    ('The web server\'s document root. Contains the front controller and assets like CSS, JavaScript, and image files.', 'Racine documentaire du serveur web. Contient le front controller et les ressources telles que CSS, JavaScript et images.'),
    ('Compiled asset directories for CSS, javascript and fonts.', 'Repertoires de ressources compilees pour CSS, JavaScript et polices.'),
    ('Contains the images used in various different places of the system', 'Contient les images utilisees a differents endroits du systeme'),
    ('Contains the template PDF\'s used.', 'Contient les modeles PDF utilises.'),
    ('Contains the CSV templates for the different modules', 'Contient les modeles CSV des differents modules'),
    ('Contains your application\'s assets like views, language files, and raw asset files.', 'Contient les ressources de l\'application telles que les vues, les fichiers de langue et les ressources brutes.'),
    ('Asset directories for CSS, JavaScript, and SASS files.', 'Repertoires de ressources pour les fichiers CSS, JavaScript et SASS.'),
    ('Language files.', 'Fichiers de langue.'),
    ('Blade template files.', 'Fichiers de templates Blade.'),
    ('Contains route definitions for your application.', 'Contient les definitions de routes de l\'application.'),
    ('Contains generated files like logs, cache, and file uploads.', 'Contient les fichiers generes comme les journaux, le cache et les televersements.'),
    ('For storing files generated by your application.', 'Pour stocker les fichiers generes par l\'application.'),
    ('For storing the KML files of the building footprint collected through the mobile application. This folder is created during the deployment process.', 'Pour stocker les fichiers KML des emprises de batiments collectees via l\'application mobile. Ce dossier est cree lors du deploiement.'),
    ('For storing the images collected during the emptying process through the mobile application. This fodler is created during the deployment process.', 'Pour stocker les images collectees pendant le processus de vidange via l\'application mobile. Ce dossier est cree lors du deploiement.'),
    ('For storing cached files.', 'Pour stocker les fichiers de cache.'),
    ('Log files generated by the application.', 'Fichiers journaux generes par l\'application.'),
    ('Contains the stub files for the charts', 'Contient les fichiers de squelette pour les graphiques'),
    ('Contains test files.', 'Contient les fichiers de test.'),
    ('Contains Composer dependencies.', 'Contient les dependances Composer.'),
    ('Example environment file for setting configuration variables.', 'Fichier d\'environnement d\'exemple pour definir les variables de configuration.'),
    ('Command-line utility for interacting with your Laravel application.', 'Utilitaire en ligne de commande pour interagir avec l\'application Laravel.'),
    ('Contains the PHP project dependencies and scripts for Composer to manage.', 'Contient les dependances PHP du projet et les scripts geres par Composer.'),
    ('Contains the version control information that locks the exact versions of dependencies installed, ensuring consistency across environments.', 'Contient les informations de verrouillage de versions des dependances installees, garantissant la coherence entre les environnements.'),
    ('Contains list of JavaScript project dependencies, scripts, and metadata for npm to manage.', 'Contient la liste des dependances JavaScript du projet, les scripts et les metadonnees geres par npm.'),
    ('Contains configuration file for PHPUnit, specifying testing parameters and settings.', 'Contient le fichier de configuration de PHPUnit, precisant les parametres et reglages de test.'),
    ('Contains the PHP server file, often for routing requests in local development.', 'Contient le fichier serveur PHP, souvent utilise pour router les requetes en developpement local.'),
    ('Contains configurations for Laravel Mix for compiling and bundling assets (CSS, JS) with Webpack.', 'Contient les configurations Laravel Mix pour compiler et regrouper les ressources (CSS, JS) avec Webpack.'),
    ('The files received during form submissions are stored in the application side server into the directory /storage/app/public/.', 'Les fichiers recus lors des soumissions de formulaires sont stockes sur le serveur applicatif dans le repertoire /storage/app/public/.'),
    ('The KML files uploaded via the mobile application during the building survey process are stored in the file path /storage/app/public/building-survey-kml.', 'Les fichiers KML televerses via l\'application mobile lors de l\'enquete batimentaire sont stockes dans /storage/app/public/building-survey-kml.'),
    ('The images of the building are stored in the file path /storage/app/public/emptyings/houses.', 'Les images du batiment sont stockees dans /storage/app/public/emptyings/houses.'),
    ('The images of the receipts are stored in the file path /storage/app/public/emptyings/ receipts.', 'Les images des recus sont stockees dans /storage/app/public/emptyings/receipts.'),
    ('Note: The above folder needs to be created during a initial project installation process.', 'Remarque : le dossier ci-dessus doit etre cree lors du processus initial d\'installation du projet.'),
    ('Laravel provides a convenient way to manage file storage through the Storage facade. By default, Laravel uses the local disk driver, which stores files in the storage directory. However, you can configure multiple disks for various storage solutions including cloud storage providers.', 'Laravel fournit un moyen pratique de gerer le stockage des fichiers via la facade Storage. Par defaut, Laravel utilise le pilote de disque local, qui stocke les fichiers dans le repertoire storage. Cependant, vous pouvez configurer plusieurs disques pour diverses solutions de stockage, y compris des fournisseurs de cloud.'),
    ('For example, to create File storage in Config file:', 'Par exemple, pour creer un stockage de fichiers dans le fichier de configuration :'),
    ('To store a file:', 'Pour stocker un fichier :'),
    ('When a user login normally, session expires in two hours for now. It can be changed via .env file with SESSION_LIFETIME variable.', 'Lorsqu\'un utilisateur se connecte normalement, la session expire actuellement au bout de deux heures. Cela peut etre modifie via la variable `SESSION_LIFETIME` du fichier `.env`.'),
    ('When a user login with remember me, session will be stored in cookie and it will expire when cookie expires. For now, cookie expiry time is 3 days. It can also be changed via .env file with REMEMBER_ME variable.', 'Lorsqu\'un utilisateur se connecte avec l\'option de memorisation, la session est stockee dans un cookie et expire en meme temps que lui. Actuellement, la duree d\'expiration du cookie est de 3 jours. Elle peut aussi etre modifiee via la variable `REMEMBER_ME` du fichier `.env`.'),
    ('The system uses NPM for package management. All packages that are required is installed using NPM.', 'Le systeme utilise NPM pour la gestion des paquets. Tous les paquets necessaires sont installes via NPM.'),
    ('The system uses JavaScript for all of the frontend related dynamic changes and map interface.', 'Le systeme utilise JavaScript pour tous les changements dynamiques lies a l\'interface frontale ainsi que pour l\'interface cartographique.'),
    ('There are three main layouts used in the system, one each for the landing page, dashboard and the map interface.', 'Le systeme utilise trois mises en page principales : une pour la page d\'accueil, une pour le tableau de bord et une pour l\'interface cartographique.'),
    ('Laravel Web App Session and Cookies', 'Session et cookies de l\'application web Laravel'),
    ('NPM Package Manager', 'Gestionnaire de paquets NPM'),
    ('Frontend', 'Interface frontale'),
    ('Dashboard Layout', 'Disposition du tableau de bord'),
    ('General Layout', 'Organisation generale'),
    ('Standard Conventions', 'Conventions standard'),
    ('General Convention', 'Convention generale'),
    ('PostgreSQL Convention', 'Convention PostgreSQL'),
    ('Postgres Naming Convention', 'Convention de nommage Postgres'),
    ('Schema Name', 'Nom du schema'),
    ('Demonstration', 'Demonstration'),
    ('Basic CRUD', 'CRUD de base'),
    ('API Documentation', 'Documentation API'),
    ('Success Response', 'Reponse en cas de succes'),
    ('Error Response', 'Reponse en cas d\'erreur'),
    ('POST Params', 'Parametres POST'),
    ('GET Params', 'Parametres GET'),
    ('Required/Optional', 'Obligatoire/Optionnel'),
    ('Method', 'Methode'),
    ('Headers', 'En-tetes'),
    ('Parameter', 'Parametre'),
    ('Data Type Standard for IMIS', 'Standard des types de donnees pour IMIS'),
    ('Building IMS', 'IMS Batiments'),
    ('Building Survey', 'Enquete batimentaire'),
    ('Low Income Communities', 'Communautes a faible revenu'),
    ('Fecal Sludge IMS', 'IMS des boues de vidange'),
    ('Containment IMS', 'IMS du confinement'),
    ('Containments', 'Confinements'),
    ('Service Provider IMS', 'IMS des prestataires de services'),
    ('Service Providers', 'Prestataires de services'),
    ('Employee Information', 'Informations sur les employes'),
    ('Desludging Vehicles Information', 'Informations sur les vehicules de vidange'),
    ('Treatment Plant IMS', 'IMS des stations de traitement'),
    ('Treatment Plants', 'Stations de traitement'),
    ('Performance Efficiency Standards', 'Normes d\'efficacite de performance'),
    ('Performance Efficiency Test', 'Test d\'efficacite de performance'),
    ('Emptying Service IMS', 'IMS du service de vidange'),
    ('Application Response Efficiency', 'Efficacite de reponse aux demandes'),
    ('Application', 'Demande'),
    ('Emptying', 'Vidange'),
    ('Sludge Collection', 'Collecte des boues'),
    ('Feedback', 'Retour d\'information'),
    ('Help Desk', 'Centre d\'assistance'),
    ('Sewer Connection IMS', 'IMS des branchements d\'egout'),
    ('Public / Community Toilets', 'Toilettes publiques / communautaires'),
    ('PT Users Log', 'Journal des utilisateurs PT'),
    ('CWIS Generator', 'Generateur CWIS'),
    ('CWIS Setting', 'Parametres CWIS'),
    ('NSD Setting', 'Parametres NSD'),
    ('KPI Target', 'Objectif KPI'),
    ('Utility IMS', 'IMS des services urbains'),
    ('Road Network Information', 'Informations sur le reseau routier'),
    ('Sewer Network Information', 'Informations sur le reseau d\'egout'),
    ('Water Supply Network Information', 'Informations sur le reseau d\'approvisionnement en eau'),
    ('Drain Network Information', 'Informations sur le reseau de drainage'),
    ('Solid Waste ISS', 'ISS des dechets solides'),
    ('Property Tax Collection IMS', 'IMS de collecte de la taxe fonciere'),
    ('Water Supply ISS', 'ISS d\'approvisionnement en eau'),
    ('Urban Management DSS', 'SAD de gestion urbaine'),
    ('Map Feature Layers', 'Couches d\'entites cartographiques'),
    ('Wards', 'Quartiers'),
    ('Grids', 'Grilles'),
    ('City Polygon', 'Polygone de la ville'),
    ('Ward Boundary', 'Limite du quartier'),
    ('Landuse', 'Occupation du sol'),
    ('Places', 'Lieux'),
    ('Sanitation System', 'Systeme d\'assainissement'),
    ('Ward Overlay', 'Superposition des quartiers'),
    ('Waterbodies', 'Plans d\'eau'),
    ('Public Health ISS', 'ISS de sante publique'),
    ('Water Sample Information', 'Informations sur les echantillons d\'eau'),
    ('Waterborne Hotspot', 'Point chaud des maladies hydriques'),
    ('Waterborne Cases Information', 'Informations sur les cas hydriques'),
    ('User Information Management', 'Gestion des informations utilisateur'),
    ('Roles & Permission Matrix', 'Matrice des roles et des permissions'),
    ('Roles', 'Roles'),
    ('Permissions', 'Permissions'),
    ('Miscellaneous Tables', 'Tables diverses'),
    ('Spatial refrencing', 'Referencement spatial'),
    ('Authentication Log', 'Journal d\'authentification'),
    ('Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International', 'Creative Commons Attribution - Pas d\'utilisation commerciale - Partage dans les memes conditions 4.0 International'),
    ('Official License Notice', 'Avis officiel de licence'),
    ('For the sake of brevity', 'Par souci de concision'),
    ('Licensed Rights', 'Droits concedes'),
    ('Licensed Material', 'Materiel sous licence'),
    ('Licensor', 'Donneur de licence'),
    ('Copyright and Similar Rights', 'Droits d\'auteur et droits similaires'),
    ('Sui Generis Database Rights', 'Droits sui generis sur les bases de donnees'),
    ('Effective Technological Measures', 'Mesures techniques efficaces'),
    ('Exceptions and Limitations', 'Exceptions et limitations'),
    ('License Elements', 'Elements de licence'),
    ('NonCommercial', 'Utilisation non commerciale'),
    ('ShareAlike', 'Partage dans les memes conditions'),
    ('Adapter\'s License', 'Licence de l\'adaptateur'),
    ('Adapted Material', 'Materiel adapte'),
    ('Public License', 'Licence publique'),
    ('Section 1 -- Definitions.', 'Section 1 -- Definitions.'),
    ('Section 2 -- Scope.', 'Section 2 -- Portee.'),
    ('Section 3 -- License Conditions.', 'Section 3 -- Conditions de la licence.'),
    ('Section 4 -- Sui Generis Database Rights.', 'Section 4 -- Droits sui generis sur les bases de donnees.'),
    ('Section 5 -- Disclaimer of Warranties and Limitation of Liability.', 'Section 5 -- Exclusion de garanties et limitation de responsabilite.'),
    ('Section 6 -- Term and Termination.', 'Section 6 -- Duree et resiliation.'),
    ('Section 7 -- Other Terms and Conditions.', 'Section 7 -- Autres termes et conditions.'),
    ('Section 8 -- Interpretation.', 'Section 8 -- Interpretation.'),
]

WORDS = [
    ('Introduction', 'Introduction'), ('Description', 'Description'), ('Good', 'Bon'), ('Bad', 'Mauvais'), ('Remarks', 'Remarques'),
    ('the', 'le'), ('The', 'Le'), ('and', 'et'), ('And', 'Et'), ('for', 'pour'), ('For', 'Pour'), ('with', 'avec'), ('With', 'Avec'),
    ('from', 'de'), ('From', 'De'), ('this', 'ce'), ('This', 'Ce'), ('that', 'ce'), ('That', 'Ce'), ('these', 'ces'), ('These', 'Ces'),
    ('those', 'ces'), ('Those', 'Ces'), ('into', 'dans'), ('Into', 'Dans'), ('through', 'via'), ('Through', 'Via'), ('during', 'pendant'),
    ('During', 'Pendant'), ('under', 'sous'), ('Under', 'Sous'), ('each', 'chaque'), ('Each', 'Chaque'), ('all', 'tous'), ('All', 'Tous'),
    ('other', 'autres'), ('Other', 'Autres'), ('overall', 'global'), ('Overall', 'Global'), ('related', 'lies'), ('Related', 'Lies'),
    ('initial', 'initial'), ('Initial', 'Initial'), ('core', 'coeur'), ('Core', 'Coeur'), ('main', 'principal'), ('Main', 'Principal'),
    ('new', 'nouveau'), ('New', 'Nouveau'), ('local', 'local'), ('Local', 'Local'), ('global', 'global'), ('Global', 'Global'),
    ('city', 'ville'), ('City', 'Ville'), ('cities', 'villes'), ('Cities', 'Villes'), ('municipal', 'municipal'), ('Municipal', 'Municipal'),
    ('municipalities', 'municipalites'), ('Municipalities', 'Municipalites'), ('urban', 'urbain'), ('Urban', 'Urbain'),
    ('directory', 'repertoire'), ('directories', 'repertoires'), ('contains', 'contient'), ('Contains', 'Contient'), ('stored', 'stocke'),
    ('Stored', 'Stocke'), ('includes', 'inclut'), ('Includes', 'Inclut'), ('include', 'inclure'), ('Include', 'Inclure'),
    ('used', 'utilise'), ('Used', 'Utilise'), ('using', 'en utilisant'), ('Using', 'En utilisant'),
    ('users', 'utilisateurs'), ('Users', 'Utilisateurs'), ('user', 'utilisateur'), ('User', 'Utilisateur'), ('developers', 'developpeurs'), ('developer', 'developpeur'),
    ('deployment', 'deploiement'), ('development', 'developpement'), ('documentation', 'documentation'), ('guide', 'guide'),
    ('guides', 'guides'), ('manual', 'manuel'), ('manuals', 'manuels'), ('repository', 'depot'), ('repositories', 'depots'),
    ('database', 'base de donnees'), ('databases', 'bases de donnees'),
    ('module', 'module'), ('modules', 'modules'), ('service', 'service'), ('services', 'services'), ('system', 'systeme'),
    ('systems', 'systemes'), ('settings', 'parametres'), ('building', 'batiment'), ('buildings', 'batiments'),
    ('survey', 'enquete'), ('treatment', 'traitement'), ('provider', 'prestataire'), ('providers', 'prestataires'),
    ('community', 'communaute'), ('public', 'public'), ('health', 'sante'), ('water', 'eau'), ('waste', 'dechets'),
    ('language', 'langue'), ('roles', 'roles'), ('permission', 'permission'), ('permissions', 'permissions'),
    ('success', 'succes'), ('error', 'erreur'), ('required', 'obligatoire'), ('optional', 'optionnel'), ('table', 'tableau'),
    ('tables', 'tableaux'), ('license', 'licence'), ('licenses', 'licences'), ('scope', 'portee'), ('means', 'designe'),
    ('process', 'processus'), ('processes', 'processus'), ('workflow', 'flux de travail'), ('framework', 'cadre'),
    ('planning', 'planification'), ('monitoring', 'suivi'), ('evaluation', 'evaluation'), ('decision', 'decision'),
    ('support', 'appui'), ('delivery', 'prestation'), ('chain', 'chaine'), ('indicators', 'indicateurs'), ('indicator', 'indicateur'),
    ('performance', 'performance'), ('sustainable', 'durable'), ('inclusive', 'inclusive'), ('equitable', 'equitable'),
    ('technical', 'technique'), ('information', 'information'), ('approach', 'approche'), ('tool', 'outil'), ('tools', 'outils'),
    ('solution', 'solution'), ('solutions', 'solutions'), ('governance', 'gouvernance'), ('data', 'donnees'),
    ('digital', 'numerique'), ('infrastructure', 'infrastructure'), ('open-source', 'open source'),
]

NORMALIZE = {
    'Â©': '©', 'Â ': ' ', 'Â': '', 'â€™': "'", 'â€œ': '"', 'â€': '"', 'â€˜': "'", 'â€“': '-', 'â€”': '-', 'â€¢': '-', 'â€¦': '...',
}
def normalize(text: str) -> str:
    for src, dst in NORMALIZE.items():
        text = text.replace(src, dst)
    return text


def slugify(text: str) -> str:
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii')
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text


def read_text(path: Path) -> str:
    for enc in ('utf-8', 'utf-8-sig', 'cp1252', 'latin-1'):
        try:
            return path.read_text(encoding=enc)
        except UnicodeDecodeError:
            pass
    return path.read_text(encoding='utf-8', errors='ignore')


def looks_code_like(stripped: str) -> bool:
    if re.match(r'^\[[^\]]+\]\([^)]+\)', stripped):
        return False
    code_prefixes = (
        '{', '}', ']', '"', "'", '$', 'use ', 'create index ', 'create unique index ',
        'docker-compose ', 'yarn ', 'npm ', 'cp ', 'cd ', 'git clone ', 'APP_CONFIG=', 'BASE_URL=',
        '.browserSync(', 'volumes:', 'proxy:', 'port:', 'open:', 'create-project', 'php ', 'node '
    )
    if stripped.startswith(code_prefixes):
        return True
    if '->' in stripped or '::' in stripped:
        return True
    if re.match(r'^[A-Za-z0-9_./\\-]+\s*=\s*.+$', stripped):
        return True
    return False


def protect_inline(text: str):
    store = {}

    def keep(match):
        key = f'__PH_{len(store)}__'
        store[key] = match.group(0)
        return key

    patterns = [
        r'`[^`]+`',
        r'https?://[^\s)\]>]+',
        r'<img[^>]+>',
        r'\b[A-Za-z]:\\[^\s]+',
    ]
    for pattern in patterns:
        text = re.sub(pattern, keep, text)
    return text, store


def restore_inline(text: str, store) -> str:
    for key, value in reversed(list(store.items())):
        text = text.replace(key, value)
    return text


def translate_line(line: str) -> str:
    stripped = line.strip()
    if not stripped or looks_code_like(stripped):
        return line
    line, store = protect_inline(line)
    for src, dst in sorted(PHRASES, key=lambda item: len(item[0]), reverse=True):
        line = line.replace(src, dst)
    for src, dst in WORDS:
        line = re.sub(rf'\b{re.escape(src)}\b', dst, line)
    return restore_inline(line, store)


def translate_text(text: str) -> str:
    text = normalize(text)
    parts = re.split(r'(```.*?```)', text, flags=re.S)
    translated = []
    for part in parts:
        if part.startswith('```') and part.endswith('```'):
            translated.append(part)
            continue
        lines = part.splitlines(keepends=True)
        translated.append(''.join(translate_line(line) for line in lines))
    output = ''.join(translated)

    heading_map = {}
    for line in text.splitlines():
        match = re.match(r'^(#{1,6})\s+(.*)$', normalize(line))
        if match:
            original = match.group(2).strip()
            converted = translate_line(original).strip()
            heading_map[slugify(original)] = slugify(converted)
    for old, new in heading_map.items():
        if old and new and old != new:
            output = re.sub(rf'\(#%s\)' % re.escape(old), f'(#'+new+')', output, flags=re.I)
    return output


def iter_targets():
    for path in ROOT.rglob('*'):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel in EXCLUDE:
            continue
        if path.suffix not in DOC_EXTS:
            continue
        yield rel, path


def main():
    touched = []
    for rel, path in iter_targets():
        if rel in MANUAL:
            new_text = MANUAL[rel].rstrip() + '\n'
        else:
            new_text = translate_text(read_text(path))
        old_text = read_text(path)
        if new_text != old_text:
            path.write_text(new_text, encoding='utf-8', newline='\n')
            touched.append(rel)
    print(f'Traduit: {len(touched)} fichier(s)')
    for rel in touched:
        print(rel)


if __name__ == '__main__':
    main()
