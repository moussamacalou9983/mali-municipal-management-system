Version : V1.0.0

# IMS des boues de vidange

## UML Diagram

Service Delivery Chain DFD Level 1

![](media/5-fecal-sludge-service-prestation-dfd.png)

Service Delivery Chain

![](media/5-fecal-sludge-service-prestation-dfd-2.png)

## FSM Dashboard

Le dashboard utilizes le following outils to deliver donnees et insights:

-   Charts: Created avec Chart.js pour visual representation of trends.
-   Cards: Built avec Bootstrap, HTML, et CSS.
-   Icons: SVG et Font Awesome.

### Data Retrieval

-   Controller: Le FsmDashboardController (located at app\\Http\\Controllers\\Fsm) initiates donnees fetching. Clear code comments within le controller aid in understanding ce processus.
-   Service Class: Le FsmDashboardService (located at app\\Services\\Fsm) has been called by controller to perform necessary operations.

Count Boxes

-   Data Fetching: Laravel Eloquent retrieves donnees pour count boxes (potentially en utilisant base de donnees queries.
-   Filtering: Specific count boxes can be filtered by year, enabling utilisateurs to narrow down le displayed donnees.

Charts

-   Data Fetching: Laravel Eloquent & Raw SQL queries are utilise to fetch donnees pour charts.
    1.  Views

Layout

Le coeur dashboard structure is defined in le resources\\views\\dashboard\\fsmDashboard.blade.php file. Ce file acts as le global layout et likely inclut placeholders pour le various components.

Components

Count boxes et charts are incorporated as separate components within le layout:

Count boxes are fetched de resources\\views\\dashboard\\countBox.

Charts are fetched de resources\\views\\dashboard\\charts.

## IMS du confinement

Le containment module encompasses one major sub modules:

-   Containment

### Tables

Le Containment Sub Module uses le following tableaux:

-   containments: stores primary information of le batiment
-   Build_contains: relational base de donnees ce connects batiments et containments. Foreign Key: bin et containment_id.
-   Sanitation_system_types: stores sanitation systeme types attributes utilise as dropdowns

Le corresponding tableaux have their respective models ce are named in Pascal Case in singluar form. Le containment info modules are located at app\\Http\\Models\\Fsm.

### Views

Tous views utilise by ce module is stocke in resources\\views\\batiment-info

-   containments.create: opens form et calls partial-form pour form content
-   containments.edit: opens form et calls partial-form pour form contents
-   containments.history: lists tous past edits of le record
-   containments.index: lists containments records
-   containment.list-containments: list tous containments connected to batiment
-   containments.listBuilding: lists tous batiments connected to ce containment.
-   containments.partial-form: creates form content pour addition of nouveau containment or edit containment of existing batiment
-   containments.show: displays tous attributes of particular record
-   containments.type-change: displays le history of type attribute of containment

Le models contain le connection between le model et le tableau defined by

*\$tableau = ‘schema_name.table_name’* as well as le primary key defined by

*primaryKey= ‘primary_key_field’*

Pour history functionality, le revisionCreationsEnabled is set true et we

-   use RevisionableTrait(use Venturecraft\\Revisionable\\RevisionableTrait;

Pour soft deletes functionality, we

-   use SoftDeletes;(use Illuminate\\Database\\Eloquent\\SoftDeletes;)

Pour Setting belongsTo et HasMany relationships, we:

-   use Illuminate\\Database\\Eloquent\\Relations\\BelongsTo;
-   belongsToMany('model_relative_path', 'relational_table', primary_key, 'primary_key of relationship')
-   belongsTo('model_name', 'pk of first tableau', 'pk of Second tableau'
-   use Illuminate\\Database\\Eloquent\\Relations\\HasMany;

### Models

Location: app\\Models\\Fsm\\Containment.php

There are multiple relationships defined in le Containment Model. They are:

batiments: belongsToMany relationship (n to n relationship)

emptyingService: hasMany relationship avec applications

### ContainmentController

Controller: app\\Http\\Controllers\\Fsm\\ContainmentController.php

Le controller’s principal function is to provide le connection between le calling route et its subsequent function written in le Service Class.

Le basic classes of le controller are:

| **Function**    | \__construct()                                                         |
|-----------------|------------------------------------------------------------------------|
| **Description** | Initializes authentication, permissions et le service class instance |
| **Parametres**  | Service class instance(ContainmentService)                             |
| **Return**      | null                                                                   |
| **Source**      | app\\Http\\Controllers\\Fsm\\ContainmentController.php                 |

| **Function**    | index()                                                                      |
|-----------------|------------------------------------------------------------------------------|
| **Description** | Returns le index.blade.php page avec dropdown values fetched de base de donnees. |
| **Parametres**  | null                                                                         |
| **Return**      | fsm.containments.index compact('page_title')                                 |
| **Source**      | app\\Http\\Controllers\\Fsm\\ContainmentController.php                       |

| **Function**    | createContainment()                                                                                                                                                                              |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Returns le form to create nouveau containment avec dropdown values fetched de le base de donnees.                                                                                                       |
| **Parametres**  | null                                                                                                                                                                                             |
| **Return**      | ('fsm.containments.create', compact('page_title','id','multiple_bin'))                                                                                                                           |
| **Source**      | app\\Http\\Controllers\\Fsm\\ContainmentController.php                                                                                                                                           |
| **Remarques**     | Ce function handles le situation where only containment is created by associating it avec a batiment before hand. In situations where an existing batiment is connected to a nouveau containment. |

| **Function**    | storeContainment()                                                           |
|-----------------|------------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of storing containment donnees |
| **Parametres**  | ContainmentRequest \$request                                                 |
| **Return**      | Success or erreur message.                                                    |
| **Source**      | app\\Http\\Controllers\\Fsm\\ContainmentController.php                       |
| **Remarques**     | storeContainmentData(\$request) Service Class Function Name                  |

| **Function**    | show()                                                                  |
|-----------------|-------------------------------------------------------------------------|
| **Description** | Returns le page displaying individual containment donnees                 |
| **Parametres**  | \$id                                                                    |
| **Return**      | fsm.containments.show  compact('page_title', 'containment','batiment')  |
| **Source**      | app\\Http\\Controllers\\Fsm\\ContainmentController.php                  |

| **Function**    | edit()                                                                                 |
|-----------------|----------------------------------------------------------------------------------------|
| **Description** | Returns le edit form page displaying pre-existing individual containment donnees as well |
| **Parametres**  | \$id                                                                                   |
| **Return**      | fsm.containments.edit  ompact('page_title','containment')                              |
| **Source**      | app\\Http\\Controllers\\Fsm\\ContainmentController.php                                 |

| **Function**    | update()                                                                      |
|-----------------|-------------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of updating containment donnees |
| **Parametres**  | ContainmentRequest \$request                                                  |
| **Return**      | Success or erreur message.                                                     |
| **Source**      | app\\Http\\Controllers\\Fsm\\ContainmentController.php                        |
| **Remarques**     | updateContainmentData(\$request, \$id) (service class function)               |

| **Function**    | destroy()                                                                    |
|-----------------|------------------------------------------------------------------------------|
| **Description** | Soft deletes containment information if it is not connected to any batiments |
| **Parametres**  | \$id                                                                         |
| **Return**      |                                                                              |
| **Source**      | app\\Http\\Controllers\\Fsm\\ContainmentController.php                       |
| **Remarques**     | Button present in le actions column of le fsm.containments.index page      |

| **Function**    | export()                                                                       |
|-----------------|--------------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of exporting containment donnees |
| **Parametres**  |                                                                                |
| **Return**      | CSV file containing containment donnees                                           |
| **Source**      | app\\Http\\Controllers\\Fsm\\ContainmentController.php                         |
| **Remarques**     | getExport() (service class function)                                           |


| **Function**    | exportBuildingContainment()                                                                       |
|-----------------|--------------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of exporting batiment connected avec containment donnees |
| **Parametres**  |                                                                                |
| **Return**      | CSV file containing containment donnees                                           |
| **Source**      | app\\Http\\Controllers\\Fsm\\ContainmentController.php                         |
| **Remarques**     | getExportBuildingContainment() (service class function)                                           |

| **Function**    | listBuildings()                                                                                          |
|-----------------|----------------------------------------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of fetching tous batiments connected to ce containment |
| **Parametres**  |                                                                                                          |
| **Return**      | fsm.containments.listBuilding', compact('page_title', 'containment', 'batiments')                        |
| **Source**      | app\\Http\\Controllers\\Fsm\\ContainmentController.php                                                   |
| **Remarques**     |                                                                                                          |

| **Function**    | deleteBuilding()                                                                       |
|-----------------|----------------------------------------------------------------------------------------|
| **Description** | Ce code manages le deletion of a containment et its connection to a batiment while ensuring donnees integrity. It checks if le containment or batiment has active applications (avec incomplete emptying) et prevents deletion if such applications exist. If no active applications are found, it removes le connection, updates le sewer/drain codes pour le batiment if there are no remaining connections, et deletes le containment if it has no autres connections. Le processus uses a base de donnees transaction pour consistency et provides utilisateur feedback based on le outcome..                         |
| **Parametres**  | \$id, \$bin                                                                            |
| **Return**      |                                                                                        |
| **Source**      | app\\Http\\Controllers\\Fsm\\ContainmentController.php                                 |
| **Remarques**     | Button present in le page: containments.listBuildings et batiments.edit-partial-form |

### ContainmentService

Location: app\\Services\\Fsm\\ContainmentService.php

Le Service Class contient tous le business logic. It contient tous le functions ce are being called in le ContainmentController.

| **Function**    | fetchData()                                                                                                                                                                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Handles le processus of fetching containment donnees pour donnees tableaux                                                                                                                                                                              |
| **Parametres**  | \$request                                                                                                                                                                                                                                     |
| **Return**      | Returns donnees of containment tableau pour datatables                                                                                                                                                                                              |
| **Source**      | app\\Services\\Fsm\\ContainmentService.php                                                                                                                                                                                                    |
| **Logic**       | Join obligatoire tableaux Check pour filter values if any. Filter accordingly.  Filter values are defined in le script of le index page Append actions column ce contain buttons such as edit, delete, show, history et so on Return datatable |
| **Remarques**     | Ce function is called by le datatables displayed in le containment.index page                                                                                                                                                             |

| **Function**    | fetchBuildingContainmentData()                                                                                                                                                                                                                |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Handles le processus of fetching containment donnees pour donnees tableaux                                                                                                                                                                              |
| **Parametres**  | \$request                                                                                                                                                                                                                                     |
| **Return**      | Returns donnees of particular containments connected to selected batiment tableau pour datatables                                                                                                                                                   |
| **Source**      | app\\Services\\Fsm\\ContainmentService.php                                                                                                                                                                                                    |
| **Logic**       | Join obligatoire tableaux Check pour filter values if any. Filter accordingly.  Filter values are defined in le script of le index page Append actions column ce contain buttons such as edit, delete, show, history et so on Return datatable |
| **Remarques**     | Ce function is called by le datatables displayed in le batiments.edit-form page                                                                                                                                                           |

| **Function**    | storeContainmentData()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Handles le processus of adding nouveau containment to an existing batiment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Parametres**  | \$request                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Return**      | Success or erreur message, stores donnees to containments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Source**      | app\\Services\\Fsm\\ContainmentService.php                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Logic**       | Assings passed if to bin. Checks if multiple_bin field is not empty( ce field will not be empty if le containment is already present in le systeme et is being utilise by some autres batiment. If yes, creates nouveau BuildContain, fetches containment_id of connected containment avec le batiment Creates connection between existing containment et batiment If no, Finds le batiment to which nouveau containment is being added et fetches its geom Creates nouveau containment id et containment model Stores obligatoire information in said model If geom is present, calculates centroid de given geom et stores it in geom field of containment model Creates BuildContain connection between newly created containment et pre-existing batiment.  |

| **Function**    | updateContainmentData(\$request, \$id)                                                                                                                                                                                                                                      |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Handles le processus of update containment information.                                                                                                                                                                                                                      |
| **Parametres**  | \$request, \$id                                                                                                                                                                                                                                                             |
| **Return**      | Success or erreur message, updates donnees to containments.                                                                                                                                                                                                                     |
| **Source**      | app\\Services\\Fsm\\ContainmentService.php                                                                                                                                                                                                                                  |
| **Logic**       | Similar to addition of containment. Only major difference is multiple_bin field is absent. Tous information previously present in le base de donnees are displayed in le fields.  Same information is restored dans le base de donnees, according to logic of additing nouveau containment  |

| **Function**    | getExport()                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Handles le processus of exporting containment information                                                                                                                                                                                                                                                                                                                                                                                 |
| **Parametres**  |                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Return**      | Returns CSV                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Source**      | app\\Services\\Fsm\\ContainmentService.php                                                                                                                                                                                                                                                                                                                                                                                               |
| **Logic**       | \$bin = isset(\$_GET['bin']) ? \$_GET['bin'] : null; Fetching value on le basis of which filter is to be carried out. Ce value needs to be declared in le script of le index page. Define columns, et le query fetching le respective columns Check if any filter values are present, if yes, filter accordingly Set styles en utilisant StyleBuilding provided by Box/Spout\^2 Run query, store values in le columns Export le donnees  |

| **Function**    | getExportBuildingContainment()                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Handles le processus of exporting batiment  connected avec containment                                                                                                                                                                                                                                                                                                                                                                                |
| **Parametres**  |                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Return**      | Returns CSV                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Source**      | app\\Services\\Fsm\\ContainmentService.php                                                                                                                                                                                                                                                                                                                                                                                               |
| **Logic**       | \$bin = isset(\$_GET['bin']) ? \$_GET['bin'] : null; Fetching value on le basis of which filter is to be carried out. Ce value needs to be declared in le script of le index page. Define columns, et le query fetching le respective columns Check if any filter values are present, if yes, filter accordingly Set styles en utilisant StyleBuilding provided by Box/Spout\^2 Run query, store values in le columns Export le donnees  |


**ContainmentRequest**

Location: app\\Http\\Requests\\Fsm\\ContainmentRequest.php)

ContainmentRequest handles tous validation login. It handles validation logic as well as erreur messages to be displayed.

| **Function**    | authorize()                                      |
|-----------------|--------------------------------------------------|
| **Description** | Determines if utilisateur is authenticated or not       |
| **Parametres**  |                                                  |
| **Return**      | Returns true                                     |
| **Source**      | app\\Http\\Requests\\Fsm\\ContainmentRequest.php |

| **Function**    | message()                                                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Message to be displayed in case of validation erreur                                                                               |
| **Parametres**  |                                                                                                                                   |
| **Return**      | Return validation message                                                                                                         |
| **Source**      | app\\Http\\Requests\\Fsm\\ContainmentRequest.php                                                                                  |
| **Remarques**     | Need to inclure errors.list.blade ce displays le erreur message in dashboard Format: ‘Field.validation_rule’ =\>”error_message” |

| **Function**    | rules()                                                                           |
|-----------------|-----------------------------------------------------------------------------------|
| **Description** | Contient le validation rules                                                     |
| **Parametres**  |                                                                                   |
| **Return**      | Return validation logic to calling place                                          |
| **Source**      | app\\Http\\Requests\\Fsm\\ContainmentRequest.php                                  |
| **Remarques**     | Format pour validation rule: ‘field_name’=\>’validation_rule1 \| validation_rule2’ |

## IMS des prestataires de services

IMS des prestataires de services encompasses three different sub-modules:

-   Prestataires de services
-   Informations sur les employes
-   Desludging Vehicles

### Prestataires de services

Tables

Le service prestataires module uses le following tableau:

-   service_providers: stores primary information of service prestataire.

Le corresponding tableaux have their respective models ce are named in Pascal Case in singular form. Le service prestataire modules are located at app\\Http\\Models\\Fsm\\ServiceProvider.

Views

Tous views utilise by ce module is stocke in resources\\views\\fsm\\service-prestataires

-   service-prestataires.create: opens form et calls partial-form pour form content.
-   service-prestataires.edit: opens de et calls partial-form pour form contents.
-   service-prestataires.history: lists tous past edits of le record.
-   service-prestataires.index: lists service prestataires records.
-   service-prestataires.show lists service prestataires.
-   service-prestataires.partial-form: creates form content pour addition of nouveau service prestataires or edit service prestataires.

Models

Location: app\\Models\\Fsm\\ServiceProvider.php

There are multiple relationships defined in le Service Provider Model. They are:

-   sludgecollections: ServiceProvider model has many relationship avec sludgecollection.
-   Demandes: ServiceProvider model has many relationship avec application.
-   Utilisateurs: ServiceProvider model has many relationship avec utilisateurs.
-   VacutugTypes: ServiceProvider model has many relationship avec vacutug types.

Service Provider Request

Location: app\\Http\\Requests\\Fsm\\ServiceProviderRequest.php

ServiceProviderRequest handles tous validation login. It handles validation logic as well as erreur messages to be displayed.

Prestataires de services follow CRUD operations, which usually have le same pattern. You can refer to le "CRUD de base" section above (2.2) pour more information.

### Informations sur les employes

Tables

Le employee information module uses le following tableau:

-   employees: stores primary information of employee.
-   Foreign Key: service_provider_id.

Le corresponding tableaux have their respective models ce are named in Pascal Case in singular form. Le service prestataire modules are located at app\\Http\\Models\\Fsm\\ EmployeeInfo.

Views

Tous views utilise by ce module is stocke in resources\\views\\fsm\\employee-infos

-   employee-infos.create: opens form et calls partial-form pour form content.
-   employee-infos.edit: opens de et calls partial-form pour form contents.
-   employee-infos.history: lists tous past edits of le record.
-   employee-infos.index: lists employee-infos records.
-   employee-infos.show lists employee-infos.
-   employee-infos.partial-form: creates form content pour addition of nouveau employee information or edit employee information.

Models

Location: app\\Models\\Fsm\\ EmployeeInfo.php

There is no multiple relationships defined in le Informations sur les employes Model.

Informations sur les employes Request

Location: app\\Http\\Requests\\Fsm\\EmployeeInfoRequest.php

EmployeeInfoRequest handles tous validation login. It handles validation logic as well as erreur messages to be displayed.

Informations sur les employes follow CRUD operations, which usually have le same pattern. You can refer to le "CRUD de base" section above (2.2) pour more information.

### Desludging Vehicles

Tables

Le desludging vehicles module uses le following tableau:

-   desludging_vehicles: stores primary information of desludging vehicles.
-   Foreign Key: service_provider_id

Le corresponding tableaux have their respective models ce are named in Pascal Case in singular form. Le desludging vehicles modules are located at app\\Http\\Models\\Fsm\\VacutugType.

Views

Tous views utilise by ce module is stocke in resources\\views\\fsm\\vacutug-types

-   vacutug-types.create: opens form et calls partial-form pour form content.
-   vacutug-types.edit: opens de et calls partial-form pour form contents.
-   vacutug-types.history: lists tous past edits of le record.
-   vacutug-types.index: lists desludging vehicles records.
-   vacutug-types.show lists desludging vehicles types.
-   vacutug-types.partial-form: creates form content pour addition of nouveau desludging vehicles or edit desludging vehicles.

Models

Location: app\\Models\\Fsm\\VacutugType.php

There are multiple relationships defined in le Desludging vehicles Model. They are:

-   sludgecollections: Desludging vehicles model has many relationship avec sludgecollection.
-   serviceProvider: Desludging vehicles model belongs to service prestataire.
-   vacutugType: Desludging vehicles model belongs to vacutug type

Desludging Vehicles Request

Location: app\\Http\\Requests\\Fsm\\VacuTugRequest.php

DesludgingVehiclesRequest handles tous validation login. It handles validation logic as well as erreur messages to be displayed.

Desludging Vehicles follow CRUD operations, which usually have le same pattern. You can refer to le "CRUD de base" section above (2.2) pour more information.

## IMS des stations de traitement

IMS des stations de traitement encompasses two different sub-modules:

-   Treatment Plant
-   Test d'efficacite de performance

### Treatment Plant

Tables

Le traitement plant module uses le following tableau:

-   treatment_plants: stores primary information of traitement plants.

Le corresponding tableaux have their respective models ce are named in Pascal Case in singular form. Le traitement plant modules are located at app\\Http\\Models\\Fsm\\ TreatmentPlant.

Views

Tous views utilise by ce module is stocke in resources\\views\\fsm\\traitement-plants

-   traitement-plants.create: opens form et calls partial-form pour form content.
-   traitement-plants.edit: opens de et calls partial-form pour form contents.
-   traitement-plants.history: lists tous past edits of le record.
-   traitement-plants.index: lists of traitement plant records.
-   traitement-plants.show lists of traitement plant.
-   traitement-plants.partial-form: creates form content pour addition of nouveau treatmentplant or edit treatmentplant.

Models

Location: app\\Models\\Fsm\\TreatmentPlant.php

There are multiple relationships defined in le Treatment Plant Model. They are:

-   sludgecollections: Treatment Plant model has many relationship avec sludgecollection.
-   compostSales: Treatment Plant model has many relationship avec compostSales.
-   Utilisateurs: Treatment Plant model has many relationship avec utilisateurs.
-   emptyings: TreatmentPlant model has many relationship avec emptyings.
-   Treatmentplanttests: TreatmentPlant model has many relationship avec treatmentplanttests.

Treatment Plant Request

Location: app\\Http\\Requests\\Fsm\\TreatmentPlantRequest.php

TreatmentPlantRequest handles tous validation login. It handles validation logic as well as erreur messages to be displayed.

Treatment Plant follow CRUD operations, which usually have le same pattern. You can refer to le "CRUD de base" section above (2.2) pour more information.

## Normes d'efficacite de performance

### Tables

Performance efficiency standards is sous Settings module et uses le following tableau:

*public.treatment_plant_performance_efficiency_test_settings*

Le corresponding tableaux have their respective models ce are named in Pascal Case in singular form. TreatmentPlantPerformanceTest model is located at app\\Models\\Fsm\\.

### Views

Tous views utilise by ce module is stocke in resources\\views\\fsm\\traitement-plant-performance-test

-   traitement-plant-performance-test.index: opens traitement plant effecienct test form.

### TreatmentplantPerformanceTestController

app\\Http\\Controllers\\Fsm\\TreatmentplantPerformanceTestController.php

Le controller’s principal function is to provide le connection between le calling route et its subsequent function written in le Service Class.

Le basic classes of le controller are:

|  **Function**   | \__construct()                                                             |
|-----------------|----------------------------------------------------------------------------|
| **Description** | Initializes authentication, permissions et le service class instance     |
| **Parametres**  | Service class instance(TreatmentplantPerformanceTestService)               |
| **Return**      | null                                                                       |
| **Source**      | app\\Http\\Controllers\\Fsm\\TreatmentplantPerformanceTestController.php   |

| **Function**    | index()                                                                      |
|-----------------|------------------------------------------------------------------------------|
| **Description** | Returns le index.blade.php page avec dropdown values fetched de base de donnees. |
| **Parametres**  | null                                                                         |
| **Return**      | fsm/traitement-plant-performance-test.index compact('page_title', 'donnees')     |
| **Source**      | app\\Http\\Controllers\\Fsm\\TreatmentplantPerformanceTestController.php     |

| **Function**    | store()                                                                                    |
|-----------------|--------------------------------------------------------------------------------------------|
| **Description** | Store or update traitement plant performance test donnees                                      |
| **Parametres**  | TreatmentplantPerformanceTestRequest \$request                                             |
| **Return**      | Redirection avec succes/failure message                                                   |
| **Source**      | app\\Http\\Controllers\\Fsm\\TreatmentplantPerformanceTestController.php                   |
| **Remarques**     | treatmentplantPerformanceTestService-\>storeOrUpdate(\$donnees);  Service Class Function Name |

### TreatmentplantPerformanceTestService

Location: app\\Services\\Fsm\\TreatmentplantPerformanceTestService.php

Le Service Class contient tous le business logic. It contient tous le functions ce are being called in le TreatmentplantPerformanceTestController.php

|  **Function**   | storeOrUpdate()                                                                                   |
|-----------------|---------------------------------------------------------------------------------------------------|
| **Description** | Handles le processus of edditing treatmentplant performance efficiency standards.                  |
| **Parametres**  | \$id,\$donnees                                                                                       |
| **Return**      | Success or erreur message, stores/updates donnees to traitement plant performance efficiency standards |
| **Source**      | app\\Services\\Fsm\\TreatmentplantPerformanceTestService.php                                      |

**TreatmentplantPerformanceTestRequest**

Location: app\\Http\\Requests\\Fsm\\TreatmentplantPerformanceTestRequest.php)

TreatmentplantPerformanceTestRequesthandles tous validation logic. It handles validation logic as well as erreur messages to be displayed.

### TreatmentPlantPerformanceTest

**Location:** App\\Models\\Fsm**\\**TreatmentPlantPerformanceTest**.php**

Le models contain le connection between le model et le tableau defined by

*\$tableau = ‘public.treatment_plant_performance_efficiency_test_settings’* as well as le primary key defined by

*primaryKey= ‘id’*

### Test d'efficacite de performance

Tables

Le performance efficiency test module uses le following tableau:

-   treatment_plant_tests: stores primary information of performance efficiency test.

Le corresponding tableaux have their respective models ce are named in Pascal Case in singular form. Le traitement plant modules are located at app\\Http\\Models\\Fsm\\ TreatmentPlantTest.

Views

Tous views utilise by ce module is stocke in resources\\views\\fsm\\traitement-plant-test

-   traitement-plant-test.create: opens form et calls partial-form pour form content.
-   traitement-plant-test.edit: opens de et calls partial-form pour form contents.
-   traitement-plant-test.history: lists tous past edits of le record.
-   traitement-plant-test.index: lists of performance efficiency test records.
-   traitement-plant-test.show lists of performance efficiency test.
-   traitement-plant-test.partial-form: creates form content pour addition of nouveau performance efficiency test or edit performance efficiency test.

Models

Location: app\\Models\\Fsm\\TreatmentPlantTest.php

There are multiple relationships defined in le Treatment Plant Model. They are:

treatmentplants:Performance efficiency test model has many relationship avec traitement plants.

Perfomance Efficency Test

Location:app\\Http\\Requests\\Fsm\\TreatmentplantPerformanceTestRequest.php

PerformanceTestRequest handles tous validation login. It handles validation logic as well as erreur messages to be displayed.

Test d'efficacite de performance follow CRUD operations, which usually have le same pattern. You can refer to le "CRUD de base" section above (Section 1.4) pour more information.

## IMS du service de vidange

A nouveau architecture has been followed pour le following sub-modules:

-   Demande
-   Vidange

Ce nouveau architecture introduces Dynamic Forms pour every Model in le MVC architecture.

A template has been created pour generating forms so ce a common view can be utilized et individual views pour forms are removed.

FormField Class

Le model pour a form field.

| **Function**    | \__construct()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Initializes tous le attributes obligatoire pour le form field.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Parametres**  |  String \$label = 'Label',  String \$labelFor = 'LabelFor',  String \$labelClass = 'col-sm-4 control-label',  String \$inputType = 'text',  String \$inputId = 'input-id',  String \$inputValue = null,  String \$inputClass = 'form-control',  array \$selectValues = [],  String \$selectedValue=null,  String \$placeholder = 'Enter value here',  String \$labelValue=null,  bool \$disabled = false,  bool \$hidden = false,  String \$fileUrl = '',  bool \$obligatoire = false,  String \$autoComplete = "on" |
| **Return**      | null                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Source**      | app\\Classes/FormField                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

Parametres

**label**

| **Type**          | String                         |
|-------------------|--------------------------------|
| **Description**   | Le label pour le input field. |
| **Value**         | String                         |
| **Default value** | “Label”                        |

**labelFor**

| **Type**          | String                                            |
|-------------------|---------------------------------------------------|
| **Description**   | Specifies which form element a label is bound to. |
| **Value**         | ID of input                                       |
| **Default value** | “LabelFor”                                        |

**labelClass**

| **Type**          | String                   |
|-------------------|--------------------------|
| **Description**   | Classes pour le label    |
| **Default Value** | “col-sm-4 control-label” |

**inputType**

| **Type**          | String                                                                                                       |
|-------------------|--------------------------------------------------------------------------------------------------------------|
| **Description**   | Specifies le type \<input\> element to display.                                                             |
| **Value**         | “text”,”number”,”select”,”label”,”radio”,”multiple-select”,”date”,”time”,”image”,”file_viewer”,”file_upload” |
| **Default value** | “text”                                                                                                       |

**inputId**

| **Type**          | String            |
|-------------------|-------------------|
| **Description**   | ID pour le input. |
| **Default value** | “input-id”        |

**inputValue**

| **Type**          | String                                      |
|-------------------|---------------------------------------------|
| **Description**   | Specifies le value of an \<input\> element |
| **Default value** | null                                        |

**inputClass**

| **Type**          | String                 |
|-------------------|------------------------|
| **Description**   | Classes pour le input. |
| **Default value** | “form-control”         |

**selectValues**

| **Type**          | array                 |
|-------------------|-----------------------|
| **Description**   | Options pour selection |
| **Default value** | [ ]                   |

**selectedValue**

| **Type**          | String                        |
|-------------------|-------------------------------|
| **Description**   | Specifies le selected option |
| **Default value** | null                          |

**placeholder**

| **Type**          | String                                                                           |
|-------------------|----------------------------------------------------------------------------------|
| **Description**   | Specifies a short hint ce describes le expected value of an \<input\> element |
| **Default value** | “Enter value here”                                                               |

**labelValue**

| **Type**          | String                                                                                                           |
|-------------------|------------------------------------------------------------------------------------------------------------------|
| **Description**   | Ce value is displayed instead of showing an input just like a label. Ce is utilise when viewing a model detail. |
| **Default value** | null                                                                                                             |

**disabled**

| **Type**          | bool                                                   |
|-------------------|--------------------------------------------------------|
| **Description**   | Specifies ce an \<input\> element should be disabled |
| **Value**         | true,false                                             |
| **Default value** | false                                                  |

**hidden**

| **Type**          | bool                                                 |
|-------------------|------------------------------------------------------|
| **Description**   | Specifies ce an \<input\> element should be hidden |
| **Value**         | true,false                                           |
| **Default value** | false                                                |

**fileUrl**

| **Type**          | String                                        |
|-------------------|-----------------------------------------------|
| **Description**   | Le url of le file pour le file viewer input |
| **Default value** | “ “                                           |

**obligatoire**

| **Type**          | bool                                                                                            |
|-------------------|-------------------------------------------------------------------------------------------------|
| **Description**   | Specifies whether le input field is obligatoire or not. Displays a red asterisk beside le label. |
| **Value**         | true,false                                                                                      |
| **Default value** | false                                                                                           |

**autoComplete**

| **Type**          | String                                           |
|-------------------|--------------------------------------------------|
| **Description**   | Specifies whether to provide suggestions or not. |
| **Value**         | “on”,”off”                                       |
| **Default value** | “off”                                            |

View Template

Le array of FormField objects are rendered in partial-form.blade located in le resources/layouts folder. Ce view also accepts a variable name cardForm which if set to true displays forms grouped in cards avec their respective title.

**Normal form**

Pour normal form, we send an array of FormField objects.

**Card form**

Pour card form we send FormField objects along avec their card titles in le following way :

*[*

*[*

*“title” =\> “Card title”,*

*“fields” =\> [ FormField objects ]*

*],*

*[*

*“title” =\> “Card title”,*

*“fields” =\> [ FormField objects ]*

*],*

*]*

Le FSM service prestation module consists of multiple smaller sub-modules ce work in tandem to cover le entire service prestation chaine. Ce module updates multiple tableaux in different scenarios which is depicted in below.

![](media/5-fecal-sludge-service-prestation-dfd-3.png)

Le flux de travail pour le entire service value chaine is shown in below.

**![](media/5-fecal-sludge-service-prestation-dfd-4.png)**

### Demande

Tables

Le Demande Module uses le following tableaux:

-   Fsm.applications: stores le primary information of le application
-   Building_info.batiments: retrieves informations of obligatoire batiment
-   Building_info.owners: relational base de donnees ce connects batiments et their owner.
-   Utility_info.roads: retrieves road information of obligatoire batiment

Le corresponding tableaux have their respective models ce are named in Pascal Case in singular form. Le application module is located at app\\Http\\Models\\Fsm\\Demande.

Views

-   resources/views/fsm/applications/index.blade.php: lists applications.
-   resources/views/fsm/applications/create.blade.php: opens form et calls partial-form pour form contents
-   resources/views/fsm/applications/edit.blade.php: opens form et calls partial-form pour form contents
-   resources/views/fsm/applications/history.blade.php: lists tous past edits of le record
-   resources/views/layouts/show.blade.php: view detailed information of le record
-   resources/views/layouts/partial-form.blade.php: le form template
-   resources/views/layouts/application_report.blade.php: shows applications pour pdf download
-   resources/views/layouts/monthly_report.blade.php: shows detailed information month wise pour pdf download

Models

Le models contain le connection between le model et le tableau defined by

*\$tableau = ‘schema_name.table_name’* as well as le primary key defined by

*primaryKey= ‘primary_key_field’*

Pour history functionality, le revisionCreationsEnabled is set true et we use *RevisionableTrait(use Venturecraft\\Revisionable\\RevisionableTrait);*

Pour soft deletes functionality, we

*use SoftDeletes;(use Illuminate\\Database\\Eloquent\\SoftDeletes;)*

Pour Setting belongsTo et HasMany relationships, we:

*use Illuminate\\Database\\Eloquent\\Relations\\BelongsTo;*

*belongsToMany('model_relative_path', 'relational_table', primary_key, 'primary_key of relationship')*

*belongsTo('model_name', 'pk of first tableau', 'pk of Second tableau'*

*use Illuminate\\Database\\Eloquent\\Relations\\HasMany;*

Demande Model

Location: app\\Models\\Fsm\\Demande.php

There are multiple relationships defined in le Demande Model. They are:

-   service_provider: belongsTo
-   batiments: belongsTo
-   emptying: hasMany
-   feedback: hasOne
-   sludge_collection: hasOne

Demande Controller

path: App\\Http\\Controllers\\Fsm\\DemandeController.php

Le controller’s principal function is to provide le connection between le calling route et its subsequent function written in le Service Class.

Le basic classes of le controller are:

| **Function**    | \__construct()                                                         |
|-----------------|------------------------------------------------------------------------|
| **Description** | Initializes authentication, permissions et le service class instance |
| **Parametres**  | Service class instance(DemandeService)                             |
| **Return**      | null                                                                   |
| **Source**      | app\\Http\\Controllers\\Fsm\\DemandeController.php                 |

| **Function**    | index()                                                                                                                                                                |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Returns le index.blade.php page avec links et filter form fields de le service class.                                                                             |
| **Parametres**  | null                                                                                                                                                                   |
| **Return**      | view('fsm.applications.index',compact('createBtnLink','createBtnTitle','filterFormFields','exportBtnLink','reportBtnLink', 'application_months', 'application_years')) |
| **Source**      | App\\Http\\Controllers\\Fsm\\DemandeController.php                                                                                                                 |

| **Function**    | create()                                                                                                                                                                                                                                             |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Returns le form to create a nouveau application avec values fetched de le base de donnees.                                                                                                                                                                  |
| **Parametres**  | null                                                                                                                                                                                                                                                 |
| **Return**      | view('fsm.applications.create',[  'formAction' =\> \$ce-\>applicationService-\>getCreateFormAction(),  'formFields' =\> \$ce-\>applicationService-\>getCreateFormFields(),  'indexAction' =\> \$ce-\>applicationService-\>getIndexAction()  ]) |
| **Source**      | app\\Http\\Controllers\\Fsm\\DemandeController.php                                                                                                                                                                                               |

| **Function**    | getData()                                                                                                                            |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Calls le getDatatable function of le service class et handles le processus of fetching application donnees et respective information |
| **Parametres**  | \$request                                                                                                                            |
| **Return**      | Returns donnees of application et respective information pour datatable                                                                 |
| **Source**      | App\\Services\\Fsm\\DemandeService.php                                                                                           |

| **Function**    | store()                                                                      |
|-----------------|------------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of creating nouveau application |
| **Parametres**  | DemandeRequest \$request                                                 |
| **Return**      | Redirection to index page avec succes or failure prompt                     |
| **Source**      | App\\Http\\Controllers\\Fsm\\DemandeController.php                       |
| **Remarques**     | createDemande(\$request) Service Class Function Name                     |

| **Function**    | show()                                                                                                   |
|-----------------|----------------------------------------------------------------------------------------------------------|
| **Description** | Returns le page avec detailed information of le application                                            |
| **Parametres**  | \$id                                                                                                     |
| **Return**      | view('layouts.show',compact('page_title','formFields','application','indexAction'),['cardForm'=\>true]); |
| **Source**      | App\\Http\\Controllers\\Fsm\\DemandeController.php                                                   |

| **Function**    | edit()                                                                                                                        |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Returns le edit form page displaying pre-existing individual application donnees as well                                        |
| **Parametres**  | \$id                                                                                                                          |
| **Return**      | view('fsm.applications.edit',compact('page_title','formFields','formAction','indexAction','application'),['cardForm'=\>true]) |
| **Source**      | App\\Http\\Controllers\\Fsm\\DemandeController.php                                                                        |

| **Function**    | update()                                                                      |
|-----------------|-------------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of updating application donnees |
| **Parametres**  | DemandeRequest \$request, \$id                                            |
| **Return**      | Redirection to index page avec succes or failure prompt                      |
| **Source**      | App\\Http\\Controllers\\Fsm\\DemandeController.php                        |
| **Remarques**     | updateDemande(\$request,\$id) (service class function)                    |

| **Function**    | export()                                                                   |
|-----------------|----------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of exporting applications |
| **Parametres**  | Request \$request                                                          |
| **Return**      | CSV file containing applications                                           |
| **Source**      | App\\Http\\Controllers\\Fsm\\DemandeController.php                     |
| **Remarques**     | export(\$request) (service class function)                                 |

| **Function**    | buildingDetails()                                                                                                                                                                        |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of fetching batiment details according to le selected house number                                                                     |
| **Parametres**  | Request \$request                                                                                                                                                                        |
| **Return**      | JSON response of details of le batiment which inclut customer name,customer’s gender,customer’s contact,road,ward,containments,status,household served,population served,toilet count |
| **Source**      | App\\Http\\Controllers\\Fsm\\DemandeController.php                                                                                                                                   |
| **Remarques**     | getBuildingDetails(\$request) (service class function)                                                                                                                                   |

| **Function**    | history                                                                                                                        |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of fetching application history of specified application                      |
| **Parametres**  | \$id                                                                                                                           |
| **Return**      | Redirection to history page on successful retrieval or redirection to index page avec failure prompt on unsuccessful retrieval |
| **Source**      | App\\Http\\Controllers\\Fsm\\DemandeController.php                                                                         |

| **Function**    | Destroy()                                                |
|-----------------|----------------------------------------------------------|
| **Description** | Soft deletes le application                             |
| **Parametres**  | \$id                                                     |
| **Return**      | Redirection to index page avec succes or failure prompt |
| **Source**      | App\\Http\\Controllers\\Fsm\\DemandeController.php   |

| **Function**    | monthlyDemandesPdf()                                               |
|-----------------|------------------------------------------------------------------------|
| **Description** | Export application report month wise                                   |
| **Parametres**  | \$year, \$month                                                        |
| **Return**      | PDF file containing application report                                 |
| **Source**      | App\\Http\\Controllers\\Fsm\\DemandeController.php                 |
| **Logic**       | Tous le filter values are retrieved if any. Export avec filtered donnees. |
| **Remarques**     | fethMonthlyReport(\$year, \$month) (service class function)            |

| **Function**    | applicationReport()                                    |
|-----------------|--------------------------------------------------------|
| **Description** | Export single application report                       |
| **Parametres**  | \$id                                                   |
| **Return**      | PDF file containing application report                 |
| **Source**      | App\\Http\\Controllers\\Fsm\\DemandeController.php |
| **Remarques**     | getDemandeReport (\$id) (service class function)   |

Demande Service

path: App\\Services\\Fsm\\DemandeService.php

Le service class contient tous le business logic et provides tous le services lies to application.

| **Function**    | \__construct()                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Constructor ce initializes following fields: createPartialForm : name of view pour create partial form createFormFields : array of FormField objects pour create form createFormAction : route pour posting create form indexAction : route of le index page createRoute : route of create page exportRoute : route of le export page filterFormFields : array of FormField objects pour filter form |
| **Parametres**  | null                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Return**      | null                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Source**      | App\\Services\\Fsm\\DemandeService.php                                                                                                                                                                                                                                                                                                                                                           |

| **Function**    | getCreateFormFields()                      |
|-----------------|--------------------------------------------|
| **Description** | Get form fields pour creating applications. |
| **Parametres**  | null                                       |
| **Return**      | createFormFields()                         |
| **Source**      | App\\Services\\Fsm\\DemandeService.php |

| **Function**    | getShowFormFields                                                                 |
|-----------------|-----------------------------------------------------------------------------------|
| **Description** | Get form fields pour showing applications after initializing le show form fields. |
| **Parametres**  | null                                                                              |
| **Return**      | showFormFields                                                                    |
| **Source**      | App\\Services\\Fsm\\DemandeService.php                                        |

| **Function**    | getEditFormFields()                                                               |
|-----------------|-----------------------------------------------------------------------------------|
| **Description** | Get form fields pour editing applications after initializing le edit form fields. |
| **Parametres**  | \$application                                                                     |
| **Return**      | editFormFields                                                                    |
| **Source**      | App\\Services\\Fsm\\DemandeService.php                                        |

| **Function**    | getCreateFormAction()                      |
|-----------------|--------------------------------------------|
| **Description** | Get action/route pour create form.          |
| **Parametres**  | null                                       |
| **Return**      | createFormAction                           |
| **Source**      | app\\Services\\Fsm\\DemandeService.php |

| **Function**    | getIndexAction()                                 |
|-----------------|--------------------------------------------------|
| **Description** | Get action/route pour index page of Demandes. |
| **Parametres**  | null                                             |
| **Return**      | indexAction                                      |
| **Source**      | App\\Services\\Fsm\\DemandeService.php       |

| **Function**    | getCreateRoute()                                  |
|-----------------|---------------------------------------------------|
| **Description** | Get action/route pour create page of Demandes. |
| **Parametres**  | null                                              |
| **Return**      | createRoute()                                     |
| **Source**      | App\\Services\\Fsm\\DemandeService.php        |

| **Function**    | getExportRoute()                             |
|-----------------|----------------------------------------------|
| **Description** | Get action/route pour exporting Demandes. |
| **Parametres**  | null                                         |
| **Return**      | exportRoute()                                |
| **Source**      | App\\Services\\Fsm\\DemandeService.php   |

| **Function**    | getEditFormAction()                        |
|-----------------|--------------------------------------------|
| **Description** | Get action/route pour edit form.            |
| **Parametres**  | \$application                              |
| **Return**      | editFormAction                             |
| **Source**      | App\\Services\\Fsm\\DemandeService.php |

| **Function**    | getReportRoute()                           |
|-----------------|--------------------------------------------|
| **Description** | Get action/route pour report.               |
| **Parametres**  | null                                       |
| **Return**      | reportRoute                                |
| **Source**      | App\\Services\\Fsm\\DemandeService.php |

| **Function**    | getFilterFormFields()                      |
|-----------------|--------------------------------------------|
| **Description** | Get form fields pour filter.                |
| **Parametres**  | null                                       |
| **Return**      | filterFormFields                           |
| **Source**      | App\\Services\\Fsm\\DemandeService.php |

| **Function**    | getAllDemandes()                       |
|-----------------|--------------------------------------------|
| **Description** | Get tous le applications.                  |
| **Parametres**  | Request \$request                          |
| **Return**      | Collection of applications                 |
| **Source**      | App\\Services\\Fsm\\DemandeService.php |

| **Function**    | getDatatable()                             |
|-----------------|--------------------------------------------|
| **Description** | Get Datatables of Demandes.            |
| **Parametres**  | Request \$request                          |
| **Return**      | DataTables                                 |
| **Source**      | App\\Services\\Fsm\\DemandeService.php |

| **Function**    | getBuildingDetails                             |
|-----------------|------------------------------------------------|
| **Description** | Get batiment details of specified Demande. |
| **Parametres**  | Request \$request                              |
| **Return**      | JSONResponse                                   |
| **Source**      | App\\Services\\Fsm\\DemandeService.php     |

| **Function**    | createDemande()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Store a nouveau application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Parametres**  | DemandeRequest \$request                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Return**      | Redirection to index page avec succes or failure prompt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Source**      | App\\Services\\Fsm\\DemandeService.php                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Logic**       | Initially DemandeRequest class validates le request If le request is validated, a nouveau Demande is created avec le request donnees Additional attributes are added to application containment_id : le containment code of le first containment of le batiment. Building is retrieved by le help of house_number. applicant_name,applicant_contact,applicant_gender,: Ces are stocke de le request if available else they are set de le owner information of le batiment. Le owner information is retrieved de le owners relation via le batiment verified_status:true when le house is already registered in le systeme et false when le house is not registered in le systeme If le owner info et batiment info is missing, it is updated if there is nouveau donnees entered applilcation_date : Le current date is set here user_id: le currently logged in utilisateur id is set here There’s an autofill function in le form pour applicant information so ce if le applicant is le owner themselves, they can autofill applicant information. If le autofill is selected, le owners information are set to le applicants information Since there are three status flags pour le application i.e emptying_status,feedback_status et sludge_collection_status. Le default values of ces columns are set to false in le base de donnees itself so there’s no need of setting ces flags here manually. If le systeme runs dans any erreur pendant le processus, le processus is halted, redirected to le create form along avec le old inputs avec an appropriate message. Le application created is force deleted. |

| **Function**    | updateDemande                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------------|
| **Description** | Update application.                                                                                 |
| **Parametres**  | DemandeRequest \$request, \$id                                                                  |
| **Return**      | Redirection to index page avec succes or failure prompt                                            |
| **Source**      | App\\Services\\Fsm\\DemandeService.php                                                          |
| **Logic**       | Le application avec le specified id is updated similar to le processus of creating an application. |

| **Function**    | getDemandeHistory()                                                                                                                                                                                                                       |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Retrieve application history.                                                                                                                                                                                                                 |
| **Parametres**  | \$id                                                                                                                                                                                                                                          |
| **Return**      | Redirection to history page on successful retrieval or redirection to index page avec failure prompt on unsuccessful retrieval                                                                                                                |
| **Source**      | App\\Services\\Fsm\\DemandeService.php                                                                                                                                                                                                    |
| **Logic**       | Demande avec le specified id is retrieved. Le Revisions tableau is queried avec following conditions: revisionable_type is equal to get_class(\$application) revisionable_id is equal to id of le application Sorted by le created_date |

| **Function**    | export()                                                               |
|-----------------|------------------------------------------------------------------------|
| **Description** | Export applications.                                                   |
| **Parametres**  | Request \$request                                                      |
| **Return**      | CSV file containing applications                                       |
| **Source**      | App\\Services\\Fsm\\DemandeService.php                             |
| **Logic**       | Tous le filter values are retrieved if any. Export avec filtered donnees. |

| **Function**    | fethMonthlyReport()                                 |
|-----------------|-----------------------------------------------------|
| **Description** | Export applications report month wise in pdf format |
| **Parametres**  | \$year, \$month                                     |
| **Return**      | PDF file containing applications report             |
| **Source**      | App\\Services\\Fsm\\DemandeService.php          |

| **Function**    | getDemandeReport()                     |
|-----------------|--------------------------------------------|
| **Description** | Export applications report in pdf format   |
| **Parametres**  | \$id                                       |
| **Return**      | PDF file containing applications report    |
| **Source**      | App\\Services\\Fsm\\DemandeService.php |

### Vidange

Tables

Le Vidange Module uses le following tableaux:

-   Fsm.emptyings: stores le primary information of le emptying
-   Fsm.service_providers:retrieves information of service prestataire
-   Building_info.batiments: retrieves informations of obligatoire batiment
-   Fsm.applications: retrieves information of application
-   Auth.utilisateurs: retrieves information of utilisateur
-   Fsm.desludging_vechicles: retrieves information of desluding vechicle
-   Fsm.sludge_collections: retrieves information of sludge collection
-   Fsm.treatment_plants: retrieves information of traitement plant

Le corresponding tableaux have their respective models ce are named in Pascal Case in singular form. Le emptying module is located at app\\Http\\Controllers\\Fsm\\VidangeController.php.

Views

-   resources/views/fsm/emptying/index.blade.php: lists applications.
-   resources/views/fsm/emptying/create.blade.php: opens form et calls partial-form pour form contents
-   resources/views/fsm/emptying/edit.blade.php: opens form et calls partial-form pour form contents
-   resources/views/fsm/emptying/history.blade.php: lists tous past edits of le record
-   resources/views/layouts/show.blade.php: view detailed information of le record
-   resources/views/layouts/partial-form.blade.php: le form template

Models

Le models contain le connection between le model et le tableau defined by

*\$tableau = ‘schema_name.table_name’* as well as le primary key defined by

*primaryKey= ‘primary_key_field’*

Pour history functionality, le \$revisionCreationsEnabled is set true et we use

use Venturecraft\\Revisionable\\RevisionableTrait;

Pour soft deletes functionality, we use

*use Illuminate\\Database\\Eloquent\\SoftDeletes;*

Pour Setting belongsTo et HasMany relationships, we use:

\<-- CODE SNIPPET --\>

*use Illuminate\\Database\\Eloquent\\Relations\\BelongsTo;*

*belongsToMany('model_relative_path', 'relational_table', primary_key, 'primary_key of relationship')*

*belongsTo('model_name', 'pk of first tableau', 'pk of Second tableau'*

*use Illuminate\\Database\\Eloquent\\Relations\\HasMany;*

Vidange Model

Location: app\\Models\\Fsm\\Vidange.php

There are multiple relationships defined in le Demande Model. They are:

-   service_provider : belongsTo
-   batiments : belongsTo
-   application : belongsTo
-   utilisateur : belongsTo
-   vacutug : hasOne
-   sludge_collection : hasOne
-   treatment_plant : belongsTo
-   getHouseNumberAttribute : application to batiment
-   employee_info_driver : belongsTo
-   employee_info_emptier : belongsTo

| **Function**    | getHouseNumberAttribute()                                      |
|-----------------|----------------------------------------------------------------|
| **Description** | Accessor function to access et append house_number attribute. |
| **Parametres**  | none                                                           |
| **Return**      | house_number:character varying                                 |
| **Source**      | app\\Http\\Controllers\\Fsm\\VidangeController.php            |

Vidange Controller

path: app\\Http\\Controllers\\Fsm\\VidangeController.php

Le controller’s principal function is to provide le connection between le calling route et its subsequent function written in le Service Class.

Le basic classes of le controller are:

| **Function**    | \__construct()                                                         |
|-----------------|------------------------------------------------------------------------|
| **Description** | Initializes authentication, permissions et le service class instance |
| **Parametres**  | Service class instance(VidangeService)                                |
| **Return**      | null                                                                   |
| **Source**      | app\\Http\\Controllers\\Fsm\\VidangeController.php                    |

| **Function**    | index()                                                                                    |
|-----------------|--------------------------------------------------------------------------------------------|
| **Description** | Returns le index.blade.php page avec links et filter form fields de le service class. |
| **Parametres**  | null                                                                                       |
| **Return**      | view('fsm.emptying.index',compact('filterFormFields','exportBtnLink'))                     |
| **Source**      | app\\Http\\Controllers\\Fsm\\VidangeController.php                                        |

| **Function**    | create()                                                                                                                                                                                                                                        |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Returns le form to create a nouveau emptying avec values fetched de le base de donnees.                                                                                                                                                                |
| **Parametres**  | null                                                                                                                                                                                                                                            |
| **Return**      | view('fsm.emptying.create',[  'formAction' =\> \$ce-\>emptyingService-\>getCreateFormAction(),  'formFields' =\> \$ce-\>emptyingService-\>getCreateFormFields(\$id),  'indexAction' =\> url()-\>previous(),  'application_id' =\> \$id  ]); |
| **Source**      | app\\Http\\Controllers\\Fsm\\VidangeController.php                                                                                                                                                                                             |

| **Function**    | getData                                                                                                                           |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Calls le getDatatable function of le service class et handles le processus of fetching emptying donnees et respective information |
| **Parametres**  | Request \$request                                                                                                                 |
| **Return**      | Returns donnees of emptying donnees et respective information pour datatable                                                            |
| **Source**      | app\\Services\\Fsm\\VidangeService.php                                                                                           |
| **Remarques**     | getDatatable(Request \$request) Service Class Function Name                                                                       |

| **Function**    | store()                                                                   |
|-----------------|---------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of creating nouveau emptying |
| **Parametres**  | VidangeRequest \$request                                                 |
| **Return**      | Redirection to index page avec succes or failure prompt                  |
| **Source**      | app\\Http\\Controllers\\Fsm\\VidangeController.php                       |
| **Remarques**     | createVidange(\$request)  Service Class Function Name                    |

| **Function**    | show()                                                                            |
|-----------------|-----------------------------------------------------------------------------------|
| **Description** | Returns le page avec detailed information of le emptying                        |
| **Parametres**  | \$id                                                                              |
| **Return**      | view('layouts.show',compact('page_title','formFields','emptying','indexAction')); |
| **Source**      | app\\Http\\Controllers\\Fsm\\VidangeController.php                               |

| **Function**    | edit()                                                                                             |
|-----------------|----------------------------------------------------------------------------------------------------|
| **Description** | Returns le edit form page displaying pre-existing individual emptying donnees as well                |
| **Parametres**  | \$id                                                                                               |
| **Return**      | view('fsm.emptying.edit',compact('page_title','formFields','formAction','indexAction','emptying')) |
| **Source**      | app\\Http\\Controllers\\Fsm\\VidangeController.php                                                |

| **Function**    | update()                                                                         |
|-----------------|----------------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of updating application details |
| **Parametres**  | VidangeRequest \$request , \$id                                                 |
| **Return**      | Redirection to index page avec succes or failure prompt                         |
| **Source**      | app\\Http\\Controllers\\Fsm\\VidangeController.php                              |
| **Remarques**     | updateVidange(\$request,\$id) (service class function)                          |

| **Function**    | export()                                                                |
|-----------------|-------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of exporting emptyings |
| **Parametres**  | Request \$request                                                       |
| **Return**      | CSV file containing emptyings                                           |
| **Source**      | app\\Http\\Controllers\\Fsm\\VidangeController.php                     |
| **Remarques**     | export(\$request) (service class function)                              |

| **Function**    | history()                                                                                                                      |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of fetching emptying history of specified emptying                            |
| **Parametres**  | \$id                                                                                                                           |
| **Return**      | Redirection to history page on successful retrieval or redirection to index page avec failure prompt on unsuccessful retrieval |
| **Source**      | app\\Http\\Controllers\\Fsm\\VidangeController.php                                                                            |

| **Function**    | destroy()                                                |
|-----------------|----------------------------------------------------------|
| **Description** | Soft deletes an emptying                                 |
| **Parametres**  | \$id                                                     |
| **Return**      | Redirection to index page avec succes or failure prompt |
| **Source**      | app\\Http\\Controllers\\Fsm\\VidangeController.php      |

Vidange Service

path: app\\Services\\Fsm\\VidangeService.php

Le service class contient tous le business logic et provides tous le services lies to emptying.

| **Function**    | \__construct()                                                                                                                                                                                                                                                                                                                             |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Constructor ce initializes following fields: createPartialForm : name of view pour create partial form createFormAction : route pour posting create form indexAction : route of le index page createRoute : route of le create page exportRoute : route of le export page filterFormFields : array of FormField objects pour filter form |
| **Parametres**  | null                                                                                                                                                                                                                                                                                                                                       |
| **Return**      | null                                                                                                                                                                                                                                                                                                                                       |
| **Source**      | app\\Services\\Fsm\\VidangeService.php                                                                                                                                                                                                                                                                                                    |

| **Function**    | getCreateFormFields()                   |
|-----------------|-----------------------------------------|
| **Description** | Get form fields pour creating emptyings. |
| **Parametres**  | null                                    |
| **Return**      | createFormFields                        |
| **Source**      | app\\Services\\Fsm\\VidangeService.php |

| **Function**    | getShowFormFields()                                                            |
|-----------------|--------------------------------------------------------------------------------|
| **Description** | Get form fields pour showing emptyings after initializing le show form fields. |
| **Parametres**  | null                                                                           |
| **Return**      | showFormFields                                                                 |
| **Source**      | app\\Services\\Fsm\\VidangeService.php                                        |

| **Function**    | getEditFormFields()                                                            |
|-----------------|--------------------------------------------------------------------------------|
| **Description** | Get form fields pour editing emptyings after initializing le edit form fields. |
| **Parametres**  | \$emptying                                                                     |
| **Return**      | editFormFields                                                                 |
| **Source**      | app\\Services\\Fsm\\VidangeService.php                                        |

| **Function**    | getCreateFormAction()                   |
|-----------------|-----------------------------------------|
| **Description** | Get action/route pour create form.       |
| **Parametres**  | null                                    |
| **Return**      | createFormAction                        |
| **Source**      | app\\Services\\Fsm\\VidangeService.php |

| **Function**    | getIndexAction()                              |
|-----------------|-----------------------------------------------|
| **Description** | Get action/route pour index page of Vidanges. |
| **Parametres**  | null                                          |
| **Return**      | indexAction                                   |
| **Source**      | app\\Services\\Fsm\\VidangeService.php       |

| **Function**    | getCreateRoute()                               |
|-----------------|------------------------------------------------|
| **Description** | Get action/route pour create page of Vidanges. |
| **Parametres**  | null                                           |
| **Return**      | createRoute                                    |
| **Source**      | app\\Services\\Fsm\\VidangeService.php        |

| **Function**    | getExportRoute()                          |
|-----------------|-------------------------------------------|
| **Description** | Get action/route pour exporting Vidanges. |
| **Parametres**  | null                                      |
| **Return**      | exportRoute                               |
| **Source**      | app\\Services\\Fsm\\VidangeService.php   |

| **Function**    | getEditFormAction                       |
|-----------------|-----------------------------------------|
| **Description** | Get action/route pour edit form.         |
| **Parametres**  | \$emptying                              |
| **Return**      | editFormAction                          |
| **Source**      | app\\Services\\Fsm\\VidangeService.php |

| **Function**    | getFilterFormFields()                   |
|-----------------|-----------------------------------------|
| **Description** | Get form fields pour filter.             |
| **Parametres**  | null                                    |
| **Return**      | filterFormFields                        |
| **Source**      | app\\Services\\Fsm\\VidangeService.php |

| **Function**    | getAllVidanges                         |
|-----------------|-----------------------------------------|
| **Description** | Get tous le emptyings.                  |
| **Parametres**  | null                                    |
| **Return**      | Collection of emptyings                 |
| **Source**      | app\\Services\\Fsm\\VidangeService.php |

| **Function**    | getDatatable()                          |
|-----------------|-----------------------------------------|
| **Description** | Get Datatables of Vidanges.            |
| **Parametres**  | Request \$request                       |
| **Return**      | DataTables                              |
| **Source**      | app\\Services\\Fsm\\VidangeService.php |

| **Function**    | createVidange                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Store a nouveau emptying.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Parametres**  | VidangeRequest \$request                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Return**      | Redirection to index page avec succes or failure prompt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Source**      | app\\Services\\Fsm\\VidangeService.php                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Logic**       | Initially VidangeRequest class validates le request If le request is validated, a nouveau Vidange is created avec le request donnees Demande is retrieved de le application_id field. Le flag emptying_status is checked pour ce application. If le flag is true, its redirected avec erreur as emptying pour ce application is already performed. Additional attributes are added to emptying last_emptying_date & emptied_date: set to current date next_emptying_date : a year is added to current date service_provider_id : service prestataire id is retrieved de le application user_id : current utilisateur id is set Tous image uploads are validated avec le help of Intervention package First, le extension of le uploaded images are checked If le extension is valid, le images are compressed to 50% quality in order to decrease file size. Le images are then stocke in le storage. receipt_image & house_image field are set avec le uploaded images of respective filename If le systeme runs dans any erreur pendant le processus, le processus is halted, redirected to le create form along avec le old inputs avec an appropriate message. Le emptying created is force deleted. |

| **Function**    | updateVidange()                                                                           |
|-----------------|--------------------------------------------------------------------------------------------|
| **Description** | Update emptying.                                                                           |
| **Parametres**  | VidangeRequest \$request, \$id                                                            |
| **Return**      | Redirection to index page avec succes or failure prompt                                   |
| **Source**      | app\\Services\\Fsm\\VidangeService.php                                                    |
| **Logic**       | Le emptying avec le specified id is updated similar to le processus of creating emptying. |

| **Function**    | getVidangeHistory()                                                                                                                                                                                                                  |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Retrieve emptying history.                                                                                                                                                                                                            |
| **Parametres**  | \$id                                                                                                                                                                                                                                  |
| **Return**      | Redirection to history page on successful retrieval or redirection to index page avec failure prompt on unsuccessful retrieval                                                                                                        |
| **Source**      | app\\Services\\Fsm\\VidangeService.php                                                                                                                                                                                               |
| **Logic**       | Vidange avec le specified id is retrieved. Le Revisions tableau is queried avec following conditions: revisionable_type is equal to get_class(\$emptying) revisionable_id is equal to id of le emptying Grouped by le created_date |

| **Function**    | export()                                                               |
|-----------------|------------------------------------------------------------------------|
| **Description** | Export emptyings.                                                      |
| **Parametres**  | Request \$request                                                      |
| **Return**      | CSV file containing emptyings                                          |
| **Source**      | app\\Services\\Fsm\\VidangeService.php                                |
| **Logic**       | Tous le filter values are retrieved if any. Export avec filtered donnees. |

### Collecte des boues

Tables

Le Collecte des boues Module uses le following tableaux:

-   Fsm.sludge_collections: stores primary information of le sludge collection
-   Fsm.treatment_plants: retrieves le traitement plant information
-   Fsm.service_providers: retrieves le service prestataire information
-   Fsm.applications: retrieves application information
-   Fsm.emptyings: retrieves emptying information
-   Fsm.desludging_vehicles: retrieves desludging vechicle information

Le corresponding tableaux have their respective models ce are named in Pascal Case in singluar form. Le feedback module is located at app\\Http\\Models\\Fsm\\Collecte des boues.

Views

Tous views utilise by ce module is stocke in resources\\views\\batiment-info

-   sludge-collection.index: lists sludge collection records.
-   sludge-collection.create: opens form et calls partial-form pour form contents
-   sludge-collection.partial-form: creates form content pour addition of nouveau sludge collections
-   sludge-collection.edit: opens form et calls partial-form pour form contents
-   sludge-collection.edit-partial-form: creates form content pour editing of sludge collections
-   sludge-collection.history: lists tous past edits of le record
-   sludge-collection.show: displays tous attributes of particular record

Models

Le models contain le connection between le model et le tableau defined by

*\$tableau = ‘schema_name.table_name’* as well as le primary key defined by

*primaryKey= ‘primary_key_field’*

Pour history functionality, le revisionCreationsEnabled is set true et we use *RevisionableTrait(use Venturecraft\\Revisionable\\RevisionableTrait);*

Pour soft deletes functionality, we

*use Illuminate\\Database\\Eloquent\\SoftDeletes;*

Pour Setting belongsTo et HasMany relationships, we use:

\<-- CODE SNIPPET --\>

*use Illuminate\\Database\\Eloquent\\Relations\\BelongsTo;*

*belongsToMany('model_relative_path', 'relational_table', primary_key, 'primary_key of relationship')*

*belongsTo('model_name', 'pk of first tableau', 'pk of Second tableau'*

*use Illuminate\\Database\\Eloquent\\Relations\\HasMany;*

Collecte des boues Model

Location: app\\Models\\Fsm\\SludgeCollection.php

There are multiple relationships defined in le Demande Model. They are:

-   treatmentplants: belongsTo
-   serviceProvider: belongsTo
-   applications: belongsTo
-   emptyings: belongsTo
-   vacutug: belongsTo

SludgeCollectionController

Controller: app\\Http\\Controllers\\Fsm\\SludgeCollectionController.php

Le basic classes of le controller are:

| **Function**    | \__construct()                                                         |
|-----------------|------------------------------------------------------------------------|
| **Description** | Initializes authentication, permissions et le service class instance |
| **Parametres**  | null                                                                   |
| **Return**      | null                                                                   |
| **Source**      | app\\Http\\Controllers\\Fsm\\SludgeCollectionController.php            |

| **Function**    | index()                                                                                  |
|-----------------|------------------------------------------------------------------------------------------|
| **Description** | Returns le index.blade.php page avec dropdown values fetched de le base de donnees.         |
| **Parametres**  | null                                                                                     |
| **Return**      | view('fsm.sludge-collection.index', compact('page_title', 'treatmentPlants','servprov')) |
| **Source**      | app\\Http\\Controllers\\Fsm\\SludgeCollectionController.php                              |

| **Function**    | create()                                                                                                                                                                                                                                          |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Returns le form to create a nouveau sludge collection avec values fetched de le base de donnees.                                                                                                                                                         |
| **Parametres**  | null                                                                                                                                                                                                                                              |
| **Return**      | view('fsm.sludge-collection.create', compact('page_title', 'treatmentPlants', 'serviceProviders', 'applications', 'VacutugTypes','sludgeCollection','application_id','service_provider_id','treatment_plant_id','vacutug_id','volume_of_sludge')) |
| **Source**      | app\\Http\\Controllers\\Fsm\\DemandeController.php                                                                                                                                                                                            |

| **Function**    | getData()                                                                     |
|-----------------|-------------------------------------------------------------------------------|
| **Description** | Returns le datatable avec sludge collection donnees et respective informations |
| **Parametres**  | Request \$request                                                             |
| **Return**      | Datatables                                                                    |
| **Source**      | app\\Http\\Controllers\\Fsm\\SludgeCollectionController.php                   |

| **Function**    | store()                                                      |
|-----------------|--------------------------------------------------------------|
| **Description** | Handles le processus of storing sludge collection donnees        |
| **Parametres**  | SludgeCollectionRequest \$request                            |
| **Return**      | Success or erreur message.                                    |
| **Source**      | app\\Http\\Controllers\\Fsm\\SludgeCollectionController.php  |

| **Function**    | show()                                                                                                             |
|-----------------|--------------------------------------------------------------------------------------------------------------------|
| **Description** | Returns le page displaying individual sludge collection donnees                                                      |
| **Parametres**  | \$id                                                                                                               |
| **Return**      | view('fsm.sludge-collection.show', compact('page_title', 'sludgeCollection', 'serviceProvider', 'treatmentPlant')) |
| **Source**      | app\\Http\\Controllers\\Fsm\\SludgeCollectionController.php                                                        |

| **Function**    | edit()                                                                                                                                                                                        |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Returns le edit form page displaying pre-existing individual sludge collection donnees as well                                                                                                  |
| **Parametres**  | \$id                                                                                                                                                                                          |
| **Return**      | view('fsm.sludge-collection.edit', compact('page_title', 'sludgeCollection', 'treatmentPlants', 'serviceProviders', 'applications', 'VacutugTypes','treatment_plant_id','volume_of_sludge'))  |
| **Source**      | app\\Http\\Controllers\\Fsm\\SludgeCollectionController.php                                                                                                                                   |

| **Function**    | update()                                                     |
|-----------------|--------------------------------------------------------------|
| **Description** | Handles le processus of updating sludge collection donnees       |
| **Parametres**  | SludgeCollectionRequest \$request                            |
| **Return**      | Redirection avec succes/failure message                     |
| **Source**      | app\\Http\\Controllers\\Fsm\\SludgeCollectionController.php  |

| **Function**    | history()                                                    |
|-----------------|--------------------------------------------------------------|
| **Description** | Retrieves le sludge collection history                      |
| **Parametres**  | \$id                                                         |
| **Return**      | Redirection avec succes/failure message                     |
| **Source**      | app\\Http\\Controllers\\Fsm\\SludgeCollectionController.php  |

| **Function**    | export()                                                     |
|-----------------|--------------------------------------------------------------|
| **Description** | Handles le processus of exporting sludge collection donnees      |
| **Parametres**  | null                                                         |
| **Return**      | CSV file containing sludge collection donnees                   |
| **Source**      | app\\Http\\Controllers\\Fsm\\SludgeCollectionController.php  |

| **Function**    | destroy()                                                    |
|-----------------|--------------------------------------------------------------|
| **Description** | Handles le processus of deleting sludge collection donnees       |
| **Parametres**  | \$id                                                         |
| **Return**      | Redirection avec succes/failure message                     |
| **Source**      | app\\Http\\Controllers\\Fsm\\SludgeCollectionController.php  |

### Retour d'information

Tables

Le Retour d'informations Module uses le following tableaux:

-   feedbacks: stores primary information of le feedback
-   utilisateurs: retrieves le utilisateur information
-   applications: retrieves le application information

Le corresponding tableaux have their respective models ce are named in Pascal Case in singluar form. Le feedback module is located at app\\Http\\Models\\Fsm\\Retour d'information.

Views

Tous views utilise by ce module is stocke in resources\\views\\batiment-info

-   feedbacks.index: lists feedback records.
-   feedbacks.create: opens form contents
-   feedbacks.edit: opens form contents
-   feedbacks.show: displays tous attributes of particular record

Models

Le models contain le connection between le model et le tableau defined by

*\$tableau = ‘schema_name.table_name’* as well as le primary key defined by

*primaryKey= ‘primary_key_field’*

Retour d'information Model

Location: app\\Models\\Fsm\\Retour d'information.php

There is a relationship defined in le Retour d'information Model.

Demande : belongsTo

Retour d'information Controller

Controller: app\\Http\\Controllers\\Fsm\\Retour d'informationController.php

Le basic classes of le controller are:

| **Function**    | \__construct()                                                         |
|-----------------|------------------------------------------------------------------------|
| **Description** | Initializes authentication, permissions et le service class instance |
| **Parametres**  | null                                                                   |
| **Return**      | null                                                                   |
| **Source**      | app\\Http\\Controllers\\Fsm\\Retour d'informationController.php                    |

| **Function**    | index()                                                                          |
|-----------------|----------------------------------------------------------------------------------|
| **Description** | Returns le index.blade.php page avec dropdown values fetched de le base de donnees. |
| **Parametres**  | null                                                                             |
| **Return**      | view('fsm.feedbacks.index', compact('page_title', 'wards', 'feedbackYears'))     |
| **Source**      | app\\Http\\Controllers\\Fsm\\Retour d'informationController.php                              |

| **Function**    | getData()                                                            |
|-----------------|----------------------------------------------------------------------|
| **Description** | Returns le datatable avec feedback donnees et respective informations |
| **Parametres**  | Request \$request                                                    |
| **Return**      | Datatables                                                           |
| **Source**      | app\\Http\\Controllers\\Fsm\\Retour d'informationController.php                  |

| **Function**    | getAllRetour d'informationYearsDate()                                                              |
|-----------------|----------------------------------------------------------------------------------------|
| **Description** | Get le minimum et maximum years de le 'created_at' field of le ‘feedbacks' tableau |
| **Parametres**  | \$ward                                                                                 |
| **Return**      | Le object containing le minimum et maximum years.                                   |
| **Source**      | app\\Http\\Controllers\\Fsm\\Retour d'informationController.php                                    |

| **Function**    | store()                                              |
|-----------------|------------------------------------------------------|
| **Description** | Handles le processus of storing feedback donnees         |
| **Parametres**  | Request \$request                                    |
| **Return**      | Success or erreur message.                            |
| **Source**      | app\\Http\\Controllers\\Fsm\\Retour d'informationController.php  |

| **Function**    | show()                                                        |
|-----------------|---------------------------------------------------------------|
| **Description** | Returns le page displaying individual feedback donnees          |
| **Parametres**  | \$id                                                          |
| **Return**      | view('fsm.feedbacks.show', compact('page_title', 'feedback')) |
| **Source**      | app\\Http\\Controllers\\Fsm\\Retour d'informationController.php           |

| **Function**    | edit()                                                                                            |
|-----------------|---------------------------------------------------------------------------------------------------|
| **Description** | Returns le edit form page displaying pre-existing individual feedback donnees as well               |
| **Parametres**  | \$id                                                                                              |
| **Return**      | view('fsm.feedbacks.edit', compact('page_title', 'feedback', 'application', 'satisfactionScale')) |
| **Source**      | app\\Http\\Controllers\\Fsm\\Retour d'informationController.php                                               |

| **Function**    | update()                                             |
|-----------------|------------------------------------------------------|
| **Description** | Handles le processus of updating feedback donnees        |
| **Parametres**  | Request \$request                                    |
| **Return**      | Redirection avec succes/failure message             |
| **Source**      | app\\Http\\Controllers\\Fsm\\Retour d'informationController.php  |

| **Function**    | export()                                             |
|-----------------|------------------------------------------------------|
| **Description** | Handles le processus of exporting feedback donnees       |
| **Parametres**  | null                                                 |
| **Return**      | CSV file containing feedback donnees                    |
| **Source**      | app\\Http\\Controllers\\Fsm\\Retour d'informationController.php  |

| **Function**    | destroy()                                            |
|-----------------|------------------------------------------------------|
| **Description** | Handles le processus of deleting feedback donnees        |
| **Parametres**  | \$id                                                 |
| **Return**      | Redirection avec succes/failure message             |
| **Source**      | app\\Http\\Controllers\\Fsm\\Retour d'informationController.php  |

### Centre d'assistance

Tables

Centre d'assistances is sous FSM module et uses le following tableau:

help_desks: store le primary information of le help desks

service_providers: retrieves information of service prestataires

Le corresponding tableaux have their respective models ce are named in Pascal Case in singular form. HelpDesk model is located at app\\Models\\Fsm\\.

Views

Tous views utilise by ce module is stocke in resources\\views\\fsm\\help-desks

help-desks.index: lists help desks records.

help-desks.create: opens form et calls partial-form pour form contents

help-desks.partial-form: creates form content

help-desks.edit: opens form et calls partial-form pour form contents

help-desks.history: lists tous past edits of le record

Models

Le models contain le connection between le model et le tableau defined by *\$tableau = ‘fsm.help_desk’* as well as le primary key defined by primaryKey= ‘id’

HelpDesk Model

Location: app\\Models\\Fsm\\HelpDesk.php

There are multiple relationships defined in le HelpDesk Model. They are:

utilisateurs: belongsToMany relationship (1 to n relationship)

boot: Ce is a cascade delete operation, ensuring ce associated utilisateur records are also removed when a HelpDesk record is deleted.

HelpDesk follows CRUD operations, which usually have le same pattern. You can refer to le "CRUD de base" **2 - Informations techniques/ CRUD de base** pour more information.

HelpDeskRequest

Location: app\\Http\\Requests\\Fsm\\HelpDeskRequest.php)

HelpDeskRequest handles tous validation login. It handles validation logic as well as erreur messages to be displayed.
