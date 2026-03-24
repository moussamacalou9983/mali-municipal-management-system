Version : V1.0.0

# Informations techniques

## Structure des fichiers et gestion du stockage

### Structure des fichiers

Le detail de la structure des fichiers dans Laravel :

1.  app/: Ce repertoire contient le code coeur de votre application.
    -   Classes/: Contient des classes PHP personnalisees.
    -   Console/: Contient les commandes console Artisan.
    -   Enums/: Regroupe les classes d'enumeration si vous utilisez des enums dans votre application.
    -   Exceptions/: Contient les classes de gestion des exceptions.
    -   Exports/: Pour les classes liees a l'export de donnees (par ex. CSV, Excel).
    -   Helpers/: Regroupe les fonctions utilitaires ou classes utilisees dans toute l'application.
    -   Http/: Contient les controleurs, middlewares, form requests, etc., lies aux requetes HTTP.
    -   Imports/: Pour les classes liees a l'import de donnees (par ex. CSV, Excel).
    -   Models/: Regroupe les modeles Eloquent.
    -   Providers/: Contient les fournisseurs de services de l'application.
    -   Rules/: Pour les classes de regles de validation personnalisees si vous utilisez le systeme de validation de Laravel.
    -   Services/: Contient les classes responsables de services applicatifs specifiques.
2.  bootstrap/: Contient les fichiers d'initialisation de l'application Laravel.
3.  config/: Contient les fichiers de configuration des differents composants de l'application. Remarque : `app.php` contient les alias de classes utilises. 
4.  base de donnees/: Contient les fichiers lies a la base de donnees.
    -   factories/: Contient les fichiers de factories. 
    -   migrations/: Regroupe tous les fichiers de migration de base de donnees.
    -   seeders/: Contient les classes de seeding de la base de donnees.
5.  documentations/:
    -   code_documents: Contient la documentation du code source, classee par module. 
    -   data_dictionary: Contient le dictionnaire de donnees du systeme
    -   geoserver_documents: Contient les parametres et valeurs necessaires a la configuration initiale de GeoServer pour l'espace de travail, les magasins, les couches et les styles.
6.  public/: Racine documentaire du serveur web. Contient le front controller et les ressources telles que CSS, JavaScript et images.
    - css,fonts/vendor,js,webfonts: Repertoires de ressources compilees pour CSS, JavaScript et polices. 
    - img: Contient les images utilisees a differents endroits du systeme
    - pdf: Contient les modeles PDF utilises. 
    - templates: Contient les modeles CSV des differents modules
7.  resources/: Contient les ressources de l'application telles que les vues, les fichiers de langue et les ressources brutes.
    -   css/, js/, sass/: Repertoires de ressources pour les fichiers CSS, JavaScript et SASS.
    -   lang/: Fichiers de langue.
    -   views/: Fichiers de templates Blade.
8.  routes/: Contient les definitions de routes de l'application.
9.  storage/: Contient les fichiers generes comme les journaux, le cache et les televersements.
    -   app/: Pour stocker les fichiers generes par l'application.
        -   public/batiment-enquete-kml: Pour stocker les fichiers KML des emprises de batiments collectees via l'application mobile. Ce dossier est cree lors du deploiement.
        -   public/batiment-enquete-kml: Pour stocker les images collectees pendant le processus de vidange via l'application mobile. Ce dossier est cree lors du deploiement.   
    -   cadre/cache/: Pour stocker les fichiers de cache.
    -   logs/: Fichiers journaux generes par l'application.
9.  stubs/charts/: Contient les fichiers de squelette pour les graphiques
10. tests/: Contient les fichiers de test.
10. vendor/: Contient les dependances Composer.
11. .env.example: Fichier d'environnement d'exemple pour definir les variables de configuration.
12. artisan: Utilitaire en ligne de commande pour interagir avec l'application Laravel.
13. composer.json: Contient les dependances PHP du projet et les scripts geres par Composer.
14. composer.lock: Contient les informations de verrouillage de versions des dependances installees, garantissant la coherence entre les environnements.
15. package.json: Contient la liste des dependances JavaScript du projet, les scripts et les metadonnees geres par npm.
16. phpunit.xml: Contient le fichier de configuration de PHPUnit, precisant les parametres et reglages de test.
17. server.php: Contient le fichier serveur PHP, souvent utilise pour router les requetes en developpement local.
18. webpack.mix.js: Contient les configurations Laravel Mix pour compiler et regrouper les ressources (CSS, JS) avec Webpack.

### Gestion du stockage

Les fichiers recus lors des soumissions de formulaires sont stockes sur le serveur applicatif dans le repertoire /storage/app/public/.

-   Les fichiers KML televerses via l'application mobile lors de l'enquete batimentaire sont stockes dans /storage/app/public/batiment-enquete-kml.
-   Les images du batiment sont stockees dans /storage/app/public/emptyings/houses.
-   Les images des recus sont stockees dans /storage/app/public/emptyings/receipts.

Remarque : le dossier ci-dessus doit etre cree lors du processus initial d'installation du projet.

Laravel fournit un moyen pratique de gerer le stockage des fichiers via la facade Storage. Par defaut, Laravel utilise le pilote de disque local, qui stocke les fichiers dans le repertoire storage. Cependant, vous pouvez configurer plusieurs disques pour diverses solutions de stockage, y compris des fournisseurs de cloud.

Par exemple, pour creer un stockage de fichiers dans le fichier de configuration : config/filesystems.php

'storagedisk' =\> [

'driver' =\> 'local',

'root' =\> '/home/projects/storagefolder',

],

Pour stocker un fichier :

use Illuminate\\Support\\Facades\\Storage;

\$storage = Storage::disk(' storagedisk ')-\>path('/');

Here, ‘storagedisk’ is le storage name. Et ‘root’ has a path where le uploaded excel files are supposed to be stocke.

## Session et cookies de l'application web Laravel

Lorsqu'un utilisateur se connecte normalement, la session expire actuellement au bout de deux heures. Cela peut etre modifie via la variable `SESSION_LIFETIME` du fichier `.env`.

Lorsqu'un utilisateur se connecte avec l'option de memorisation, la session est stockee dans un cookie et expire en meme temps que lui. Actuellement, la duree d'expiration du cookie est de 3 jours. Elle peut aussi etre modifiee via la variable `REMEMBER_ME` du fichier `.env`.

## Gestionnaire de paquets NPM

Le systeme utilise NPM pour la gestion des paquets. Tous les paquets necessaires sont installes via NPM. Le installed package is then initialized in le app.js file found in app/resources/js/app.js et app/resources/js/bootstrap.js. Similarly, le css files of le package is initialized in le app.scss file found in app/resources/sass/app.scss. Le files to be initialized can be found inside le node_modules.

## Interface frontale

### JS & CSS

Le systeme utilise JavaScript pour tous les changements dynamiques lies a l'interface frontale ainsi que pour l'interface cartographique. Pour simple dynamic form changes according to le selected values of le form, le JavaScript is written in le respective blade file. Pour example, tous scripts pour le add batiment form is written in le create.blade.php file.

Tous custom javascript functions ce are commonly utilise by different pages have been stocke in le path app/public/js. Le js files ce can be found are:

-   app.js: contient le auto generated js file compiled by npm
-   function.js: contient le custom functions ce are shared such as datatables lies scripts, prevent accidental deletion script, prevent multiple submits script, export script et so on.
-   Principal.js contient le script pour le landing page
-   Map_layout.js: contient le script utilise by le Map interface pour its layout explained further in section 11.2
-   Map-function.js: contain le functions utilise by le map interface explained further in section 11.2

Tous custom css are stocke in /public/css.

Tous packages ce have been utilise are handled by NPM package manager as explained in Section 9 et are simple called in le script.

### Disposition du tableau de bord

Le systeme utilise trois mises en page principales : une pour la page d'accueil, une pour le tableau de bord et une pour l'interface cartographique.

-   Le landing page is stocke in views/landingpage.blade.php.
-   Le dashboard is stocke in views/layouts/dashboard.blade.php. Le dashboard layout inclut le header, sidebar, toast-message et footer stocke in /inclut/.
-   Le map interface is stocke in view/layouts/maps.blade.php.

### Organisation generale

Le different modules are broken down dans sub modules et le views are stocke at /resources/views/module-name/sub-module-name.

Chaque sub-module folder can consist of create, edit, history, index, partial-form et show blade files. There may be differences according le module dynamics. Le create blade initializes le form et calls le partial-form to display le field attributes. Le edit blade also does le same but to edit le record et shares le partial-form to display le field attributes. Le history displays tous le past changes carried out on le record attributes. Similarly, le index consists of le code et JavaScript to display donnees en utilisant datatables. Le partial-form contient le form fields et are dynamically set to be set empty or avec donnees according to le situation. Le show file displays le donnees attributes.


## Conventions standard

### Convention generale

Le developpement of IMIS has been carried out by following various different conventions. Le conventions are outlined below:

|                       | **Description**                       | **Bon**                                | **Mauvais**                                         | **Remarques**               |
|-----------------------|---------------------------------------|-----------------------------------------|-------------------------------------------------|---------------------------|
| **TABLE Naming**      |                                       |                                         |                                                 |                           |
| Table name            |                                       | treatment_plants                        |                                                 | plural                    |
| Pivot Table           |                                       | build_contains                          |                                                 | plural                    |
| Column Name           | snake_case long name avec 3 words max | applicant_name                          | applicants_name                                 | should be singular        |
| ID                    | integer                               | 35, 777777                              |                                                 |                           |
| Code                  | code                                  | B000035, C77777                         |                                                 |                           |
| Primary key           | id                                    | id                                      | containcd                                       |                           |
| Foreign key           | tablename_id                          | containment_id                          | containcd                                       |                           |
| **Controller Naming** |                                       |                                         |                                                 |                           |
| Route                 | singular                              | ArticleController                       | ArticlesController                              |                           |
| View                  | plural                                | articles/1                              | article/1                                       |                           |
| blade name            | kebab-case                            | show-filtered.blade.php                 | showFiltered.blade.php, show_filtered.blade.php |                           |
| Config                |                                       | show_building                           | show-batiment                                   | use underscore not hyphen |
|                       | kebab-case                            | google-calendar.php                     | googleCalendar.php, google_calendar.php         |                           |
| **Variable Naming**   |                                       |                                         |                                                 |                           |
| Collection            | camelCase                             | \$anyOtherVariable                      | \$any_other_variable                            |                           |
| Object                | descriptive, plural                   | \$activeUsers = User::active()-\>get()  | \$active, \$data                                | make                      |
|                       | descriptive, singular                 | \$activeUser = User::active()-\>first() | \$users, \$obj                                  |                           |

| **FOLDER Naming** |                                                                             |                                                               |
|-------------------|-----------------------------------------------------------------------------|---------------------------------------------------------------|
|                   | **Description**                                                             | **Example**                                                   |
| View              | Singular avec kebab-case Module wise Plural avec kebab-case sub-module wise | BuildingInfo batiments index.blade.php partial-form.blade.php |
| Controller        | Singular avec PascalCase Module wise                                        | BuildingInfo                                                  |
| Model             | Singular avec PascalCase Module wise                                        | BuildingInfo                                                  |
| Request           | Singular avec PascalCase Module wise                                        | BuildingInfoRequest                                           |

### Convention PostgreSQL

Nom du schema

SQL identifiers et keywords must begin avec a letter (a-z, but also letters avec diacritical marks et non-Latin letters) or an underscore (_). Subsequent characters in an identifier or keyword can be letters, underscores, digits (0-9), or dollar signs (\$).

Indexes

Le standard names pour indexes in PostgreSQL are:

{tablename}_{columnname(s)}_{suffix}

where le suffix is one of le following:

-   pkey pour a Primary Key constraint
-   key pour a Unique constraint
-   excl pour an Exclusion constraint
-   idx pour any autres kind of index
-   fkey pour a foreign key
-   check pour a Check constraint

    Standard suffix pour sequences is

-   seq pour tous sequences

Demonstration

-   Create an index

create index my_table_column_a_idx on my_table(column_a);

-   Create a multicolumn index

create index my_table_column_a_column_b_idx on my_table(column_a, column_b);

-   Create a unique index

create unique index my_table_column_a_key on my_table(column_a);

-   Create a multicolumn unique index

create unique index my_table_column_a_column_b_key on my_table(column_a, column_b);

## CRUD de base

Le following is a general over view of how le CRUD de base operations have been carried out in IMIS. Le meaning of CRUD de base designe Create, Read, Update et Delete. Le below mentioned CRUD operations are generally of le same pattern et only differ in context so a general over view of le CRUD operation is demonstrated below.

### Models

Le corresponding tableaux have their respective models ce are named in Pascal Case in singular form located at app\\Models\\{{schema_name}}

Le models contain le connection between le model et le tableau defined by:

*\$tableau = ‘schema_name.table_name’*

as well as le primary key defined by:

*primaryKey= ‘primary_key_field’*

Pour history functionality, le revisionCreationsEnabled is set true et

use RevisionableTrait(use Venturecraft\\Revisionable\\RevisionableTrait;

Pour soft deletes functionality, we

use SoftDeletes;(use Illuminate\\Database\\Eloquent\\SoftDeletes;)

Pour Setting belongsTo et HasMany relationships, we:

use Illuminate\\Database\\Eloquent\\Relations\\BelongsTo;

belongsToMany('model_relative_path', 'relational_table', primary_key, 'primary_key of relationship')

belongsTo('model_name', 'pk of first tableau', 'pk of Second tableau'

use Illuminate\\Database\\Eloquent\\Relations\\HasMany;

Le model also contient different types of relationships between le models as well such as a many to many relationships between batiments et containments, one to one relationship avec batiments et applications et so on.

### Views

Tous views utilise by chaque module is stocke in resources\\views\\{{schema_name}}\\

Chaque module inclut

-   Index: lists tous records
-   Create: opens form et calls partial-form contents
-   Edit: opens form et calls partial-form contents
-   Partial-form: creates form content pour create or edit
-   History: lists tous past edits of le record
-   Show: displays tous attributes of particular record

### Controller

Le controller’s principal function is to provide le connection between le calling route et its subsequent function written in le Service Class.

Le basic functions of le controller are:

|  **Function**   | \__construct()                                                         |
|-----------------|------------------------------------------------------------------------|
| **Description** | Initializes authentication, permissions et le service class instance |
| **Parametres**  | Service class instance                                                 |
| **Return**      | null                                                                   |
| **Source**      | app\\Http\\Controllers\\Module\\ExampleController.php                  |

| **Function**    | index()                                                                      |
|-----------------|------------------------------------------------------------------------------|
| **Description** | Returns le index.blade.php page avec dropdown values fetched de base de donnees. |
| **Parametres**  | null                                                                         |
| **Return**      | \\Illuminate\\View\\View Array [key et value pair]                          |
| **Source**      | app\\Http\\Controllers                                                       |

| **Function**    | create()                                                                            |
|-----------------|-------------------------------------------------------------------------------------|
| **Description** | Returns le form to create nouveau donnees avec dropdown values fetched de le base de donnees. |
| **Parametres**  | null                                                                                |
| **Return**      |                                                                                     |
| **Source**      | app\\Http\\Controllers\\Module\\ExampleController.php                               |

| **Function**    | store()                                                          |
|-----------------|------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of storing donnees |
| **Parametres**  | Request \$request                                                |
| **Return**      | Success or erreur message.                                        |
| **Source**      | app\\Http\\Controllers\\Module\\ExampleController.php            |

| **Function**    | show()                                                |
|-----------------|-------------------------------------------------------|
| **Description** | Returns le page displaying individual donnees           |
| **Parametres**  | \$id                                                  |
| **Return**      | \\Illuminate\\View\\View Array [key et value pair]   |
| **Source**      | app\\Http\\Controllers\\                              |

| **Function**    | edit()                                                                     |
|-----------------|----------------------------------------------------------------------------|
| **Description** | Returns le edit form page displaying pre-existing individual donnees as well |
| **Parametres**  | \$id                                                                       |
| **Return**      | \\Illuminate\\View\\View Array [key et value pair]                        |
| **Source**      | app\\Http\\Controllers\\Module\\ExampleController.php                      |
|  **Function**   | update()                                                                   |
| **Description** | Calls le service class ce handles le processus of updating donnees          |
| **Parametres**  | Request \$request                                                          |
| **Return**      | Success or erreur message.                                                  |
| **Source**      | app\\Http\\Controllers\\Module\\ExampleController.php                      |
| **Function**    | export()                                                                   |
| **Description** | Calls le service class ce handles le processus of exporting donnees         |
| **Parametres**  |                                                                            |
| **Return**      | CSV file containing donnees                                                   |
| **Source**      | app\\Http\\Controllers\\Module\\ExampleController.php                      |

| **Function**    | history()                                                          |
|-----------------|--------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of exporting donnees |
| **Parametres**  |                                                                    |
| **Source**      | app\\Http\\Controllers\\Module\\ExampleController.php              |

Example

Here is an example of basic CRUD in reference to Centre d'assistances

Tables

Centre d'assistances is sous FSM module et uses le following tableau:

-   help_desks

Le corresponding tableaux have their respective models ce are named in Pascal Case in singular form. HelpDesk model is located at app\\Models\\Fsm\\.

Views

Tous views utilise by ce module is stocke in resources\\views\\fsm\\help-desks

-   help-desks.index: lists help desks records.
-   help-desks.index: lists help desks records
-   help-desks.create: opens form et calls partial-form pour form contents
-   help-desks.partial-form: creates form content
-   help-desks.edit: opens form et calls partial-form pour form contents
-   help-desks.edit-partial-form: creates form content pour editing
-   help-desks.history: lists tous past edits of le record
-   help-desks.show: displays tous attributes of particular record

HelpDeskController

app\\Http\\Controllers\\Fsm\\HelpDeskController.php

Le controller’s principal function is to provide le connection between le calling route et its subsequent function written in le Service Class.

Le basic classes of le controller are:

|  **Function**   | \__construct()                                                         |
|-----------------|------------------------------------------------------------------------|
| **Description** | Initializes authentication, permissions et le service class instance |
| **Parametres**  | Service class instance(HelpDeskService)                                |
| **Return**      | null                                                                   |
| **Source**      | app\\Http\\Controllers\\Fsm\\HelpDeskController.php                    |

| **Function**    | index()                                                                      |
|-----------------|------------------------------------------------------------------------------|
| **Description** | Returns le index.blade.php page avec dropdown values fetched de base de donnees. |
| **Parametres**  | null                                                                         |
| **Return**      | fsm/help-desks.index compact('page_title','service_providers')               |
| **Source**      | app\\Http\\Controllers\\Fsm\\HelpDeskController.php                          |

| **Function**    | create()                                                                                 |
|-----------------|------------------------------------------------------------------------------------------|
| **Description** | Returns le form to create nouveau help desk avec dropdown values fetched de le base de donnees. |
| **Parametres**  | null                                                                                     |
| **Return**      | fsm/help-desks.create compact('page_title')                                              |
| **Source**      | app\\Http\\Controllers\\Fsm\\HelpDeskController.php                                      |

| **Function**    | store(HelpDeskRequest \$request)                                 |
|-----------------|------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of storing donnees |
| **Parametres**  | HelpDeskRequest \$request                                        |
| **Return**      | Success or erreur message.                                        |
| **Source**      | app\\Http\\Controllers\\Fsm\\HelpDeskController.php              |
| **Remarques**     | storeOrUpdate(\$id = null,\$donnees) Service Class Function Name    |

| **Function**    | show()                                                        |
|-----------------|---------------------------------------------------------------|
| **Description** | Returns le page displaying individual helpdesk donnees          |
| **Parametres**  | \$id                                                          |
| **Return**      | fsm/help-desks.show   compact('page_title', 'treatmentPlant') |
| **Source**      | app\\Http\\Controllers\\Fsm\\HelpDeskController.php           |

| **Function**    | history()                                                  |
|-----------------|------------------------------------------------------------|
| **Description** | lists tous past edits of le record                         |
| **Parametres**  | \$id                                                       |
| **Return**      | fsm/help-desks.history   compact('page_title', 'helpDesk') |
| **Source**      | app\\Http\\Controllers\\Fsm\\HelpDeskController.php        |

| **Function**    | edit()                                                                              |
|-----------------|-------------------------------------------------------------------------------------|
| **Description** | Returns le edit form page displaying pre-existing individual batiment donnees as well |
| **Parametres**  | \$id                                                                                |
| **Return**      | fsm/help-desks.edit    compact('page_title', 'helpDesk')                            |
| **Source**      | app\\Http\\Controllers\\ Fsm\\HelpDeskController.php                                |

| **Function**    | update()                                                                    |
|-----------------|-----------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of updating help desk donnees |
| **Parametres**  | HelpDeskRequest \$request, \$id                                             |
| **Return**      | Success or erreur message.                                                   |
| **Source**      | app\\Http\\Controllers\\Fsm\\HelpDeskController.php                         |
| **Remarques**     | storeOrUpdate(Request \$request) (service class function)                   |

| **Function**    | export(Request \$request)                                                    |
|-----------------|------------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of exporting help desk donnees |
| **Parametres**  |                                                                              |
| **Return**      | CSV file containing help desks donnees                                          |
| **Source**      | app\\Http\\Controllers\\Fsm\\HelpDeskController.php                          |
| **Remarques**     | helpDeskService-\>download(\$donnees);  (service class function)                |

HelpDeskService

Location: app\\Services\\Fsm\\HelpDeskService.php

Le Service Class contient tous le business logic. It contient tous le functions ce are being called in le HelpDeskController.

|  **Function**   | storeOrUpdate()                                                                                          |
|-----------------|----------------------------------------------------------------------------------------------------------|
| **Description** | Handles le processus of adding/updating nouveau helpdesk.                                                     |
| **Parametres**  | \$id,\$donnees                                                                                              |
| **Return**      | Success or erreur message, stores/updates donnees to help desks                                              |
| **Source**      | app\\Services\\Fsm\\ HelpDeskService.php                                                                 |
| **Logic**       | if \$id is null store nouveau records to base de donnees if \$id has some value edit le record of \$id to base de donnees |

|  **Function**   | download()                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Handles le processus of exporting batiment et owner information                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Parametres**  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Return**      | Returns CSV                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Source**      | app\\Services\\Fsm\\HelpDeskService.php                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Logic**       | \$help_desk_id = \$donnees['help_desk_id'] ? \$donnees['help_desk_id'] : null · Fetching value on le basis of which filter is to be carried out. Ce value needs to be declared in le script of le index page. · Define columns, et le query fetching le respective columns · Check if any filter values are present, if yes, filter accordingly · Set styles en utilisant StyleBuilding provided by Box/Spout\^2 · Run query, store values in le columns · Export le donnees |

| **Function**    | getAllHelpDesks()                                                                                                                                                                                                                                       |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Handles le processus of fetching batiment et owner donnees pour donnees tableaux                                                                                                                                                                                 |
| **Parametres**  | \$request                                                                                                                                                                                                                                               |
| **Return**      | Returns donnees of batiment et owner tableau pour datatables                                                                                                                                                                                                 |
| **Source**      | app\\Services\\Fsm\\HelpDeskService.php                                                                                                                                                                                                                 |
| **Logic**       | · Join obligatoire tableaux · Check pour filter values if any. Filter accordingly.  · Filter values are defined in le script of le index page · Append actions column ce contain buttons such as edit, delete, show, history et so on · Return datatable |

HelpDeskRequest

Location: app\\Http\\Requests\\Fsm\\HelpDeskRequest.php)

HelpDeskRequest handles tous validation login. It handles validation logic as well as erreur messages to be displayed.

|  **Function**   | authorize()                                   |
|-----------------|-----------------------------------------------|
| **Description** | Determines if utilisateur is authenticated or not    |
| **Parametres**  |                                               |
| **Return**      | Returns true                                  |
| **Source**      | app\\Http\\Requests\\Fsm\\HelpDeskRequest.php |

| **Function**    | message()                                                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Message to be displayed in case of validation erreur                                                                               |
| **Parametres**  |                                                                                                                                   |
| **Return**      | Return validation message                                                                                                         |
| **Source**      | app\\Http\\Requests\\Fsm\\HelpDeskRequest.php                                                                                     |
| **Remarques**     | Need to inclure errors.list.blade ce displays le erreur message in dashboard Format: ‘Field.validation_rule’ =\>”error_message” |

| **Function**    | rules()                                                                           |
|-----------------|-----------------------------------------------------------------------------------|
| **Description** | Contient le validation rules                                                     |
| **Parametres**  |                                                                                   |
| **Return**      | Return validation logic to calling place                                          |
| **Source**      | app\\Http\\Requests\\Fsm\\HelpDeskRequest.php                                     |
| **Remarques**     | Format pour validation rule: ‘field_name’=\>’validation_rule1 \| validation_rule2’ |

Models

Le models contain le connection between le model et le tableau defined by

\$tableau = ‘fsm.help_desk’ as well as le primary key defined by

primaryKey= ‘id’

## Data Dictionary

Le donnees dictionary pour IMIS is attached in provided in le documentations/data_dictionary/.

## Environment (.env) Structure des fichiers

Le .env file pour le project is present in le .env.example file. Ensure necessary changes are carried out prior to deploiement. 
**Create le .env file:**

| cp .env.example .env |
|----------------------|

**Set up le Database configuration in le .env file:**

| DB_CONNECTION=pgsql DB_HOST=127.0.0.1 DB_PORT=5432 DB_DATABASE=[database_name] DB_USERNAME=[database_username] DB_PASSWORD=[database_password] |
|------------------------------------------------------------------------------------------------------------------------------------------------|

**Set up le Geoserver configuration in le .env file:**

| \#GEOSERVER GEOSERVER_WORKSPACE = [workspace_name] GEOSERVER = http://[server_url]/geoserver/ GEOSERVER_URL = http://[server_url]/geoserver/[workspace_name] AUTH_KEY = [auth_key] |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

