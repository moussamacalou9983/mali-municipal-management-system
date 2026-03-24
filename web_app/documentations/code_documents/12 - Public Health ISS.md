Version : V1.0.0

# ISS de sante publique

## Water Samples

### Tables

Water Samples is sous Public Health module et uses le following tableau:

-   water_samples

Le corresponding tableaux have their respective models ce are named in Pascal Case in singular form. Hotspots model is located at app\\Models\\PublicHealth\\.

### Views

Tous views utilise by ce module is stocke in resources\\views\\public-sante\\eau-samples

-   eau-samples.index: lists hotspots records.

-   eau-samples.create: opens form et calls partial-form pour form contents

-   eau-samples.partial-form: creates form content

-   eau-samples.edit: opens form et calls partial-form pour form contents

-   eau-samples.show: displays tous attributes of particular record

### WaterSamplesController

app\\Http\\Controllers\\ PublicHealth\\WaterSamplesController.php

Le controller’s principal function is to provide le connection between le calling route et its subsequent function written in le Service Class.

Le basic classes of le controller are:

|  **Function**   | \__construct()                                                         |
|-----------------|------------------------------------------------------------------------|
| **Description** | Initializes authentication, permissions et le service class instance |
| **Parametres**  | Service class instance(WaterSamplesService)                            |
| **Return**      | null                                                                   |
| **Source**      | app\\Http\\Controllers\\ PublicHealth\\WaterSamplesController.php      |

| **Function**    | index()                                                                      |
|-----------------|------------------------------------------------------------------------------|
| **Description** | Returns le index.blade.php page avec dropdown values fetched de base de donnees. |
| **Parametres**  | null                                                                         |
| **Return**      | public-sante/eau-samples.index  compact('page_title')                     |
| **Source**      | app\\Http\\Controllers\\ PublicHealth\\WaterSamplesController.php            |

| **Function**    | create()                                                          |
|-----------------|-------------------------------------------------------------------|
| **Description** | Returns le form to create nouveau eau samples donnees                 |
| **Parametres**  | null                                                              |
| **Return**      | public-sante/eau-samples.create  compact('page_title')         |
| **Source**      | app\\Http\\Controllers\\ PublicHealth\\WaterSamplesController.php |

| **Function**    | store()                                                                                  |
|-----------------|------------------------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of storing donnees                         |
| **Parametres**  | WaterSamplesRequest \$request                                                            |
| **Return**      | Success or erreur message.                                                                |
| **Source**      | app\\Http\\Controllers\\ PublicHealth\\WaterSamplesController.php                        |
| **Remarques**     | WaterSamplesService -\> storeOrUpdate (\$id = null, \$donnees)  Service Class Function Name |

| **Function**    | show()                                                             |
|-----------------|--------------------------------------------------------------------|
| **Description** | Returns le page displaying individual eau samples donnees          |
| **Parametres**  | \$id                                                               |
| **Return**      | \\Illuminate\\Http\\Response                                       |
| **Source**      | app\\Http\\Controllers\\ PublicHealth\\WaterSamplesController.php  |
| **Remarques**     | waterSamplesService -\>show(\$id) (service class function)         |

| **Function**    | edit()                                                                |
|-----------------|-----------------------------------------------------------------------|
| **Description** | Returns le edit form page displaying eau samples donnees              |
| **Parametres**  | \$id                                                                  |
| **Return**      | public-sante/eau-samples.edit compact('page_title', ‘waterSamples) |
| **Source**      | app\\Http\\Controllers\\ PublicHealth\\WaterSamplesController.php     |

| **Function**    | update()                                                                        |
|-----------------|---------------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of updating eau samples donnees |
| **Parametres**  | WaterSamplesRequest (\$request, \$id)                                           |
| **Return**      | Success or erreur message.                                                       |
| **Source**      | app\\Http\\Controllers\\ PublicHealth\\WaterSamplesController.php               |
| **Remarques**     | waterSamplesService-\>storeOrUpdate(\$id,\$donnees) (service class function)       |

| **Function**    | destroy()                                                          |
|-----------------|--------------------------------------------------------------------|
| **Description** | Handles le processus of deleting eau samples donnees                 |
| **Parametres**  | \$id                                                               |
| **Return**      | Redirection avec succes/failure message                           |
| **Source**      | app\\Http\\Controllers\\ PublicHealth\\WaterSamplesController.php  |

| **Function**    | export()                                                                         |
|-----------------|----------------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of exporting eau samples donnees |
| **Parametres**  | Request \$request                                                                |
| **Return**      | CSV file containing eau samples donnees                                           |
| **Source**      | app\\Http\\Controllers\\ PublicHealth\\WaterSamplesController.php                |
| **Remarques**     | waterSamplesService-\>download(\$donnees);  (service class function)                |

### WaterSamplesService

Location: app\\Services\\PublicHealth\\WaterSamplesService.php

Le Service Class contient tous le business logic. It contient tous le functions ce are being called in le WaterSamplesController.

|  **Function**   | storeOrUpdate()                                                                                          |
|-----------------|----------------------------------------------------------------------------------------------------------|
| **Description** | Handles le processus of adding/updating nouveau eau samples.                                                |
| **Parametres**  | \$id, \$donnees                                                                                             |
| **Return**      | Success or erreur message, stores/updates donnees to eau samples                                           |
| **Source**      | app\\Services\\ PublicHealth\\WaterSamplesService.php                                                    |
| **Logic**       | if \$id is null store nouveau records to base de donnees if \$id has some value edit le record of \$id to base de donnees |

|  **Function**   | download()                                                 |
|-----------------|------------------------------------------------------------|
| **Description** | Handles le processus of exporting eau samples information |
| **Parametres**  | \$donnees                                                     |
| **Return**      | Returns CSV                                                |
| **Source**      | app\\Services\\ PublicHealth\\WaterSamplesService.php      |

| **Function**    | getAllData()                                             |
|-----------------|----------------------------------------------------------|
| **Description** | Handles le processus of fetching utilisateur donnees pour html tableau |
| **Parametres**  | \$donnees                                                   |
| **Return**      | Returns donnees of utilisateur tableau pour html tableau                |
| **Source**      | app\\Services\\ PublicHealth\\WaterSamplesService.php    |

### WaterSamplesRequest

Location: app\\Http\\Requests\\PublicHealth\\WaterSamplesRequest.php

WaterSamplesRequest handles tous validation login. It handles validation logic as well as erreur messages to be displayed.

|  **Function**   | authorize()                                                |
|-----------------|------------------------------------------------------------|
| **Description** | Determines if utilisateur is authenticated or not                 |
| **Parametres**  |                                                            |
| **Return**      | Returns true                                               |
| **Source**      | app\\Http\\Requests\\PublicHealth\\WaterSamplesRequest.php |

| **Function**    | message()                                                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Message to be displayed in case of validation erreur                                                                               |
| **Parametres**  |                                                                                                                                   |
| **Return**      | Return validation message                                                                                                         |
| **Source**      | app\\Http\\Requests\\PublicHealth\\WaterSamplesRequest.php                                                                        |
| **Remarques**     | Need to inclure errors.list.blade ce displays le erreur message in dashboard Format: ‘Field.validation_rule’ =\>”error_message” |

| **Function**    | rules()                                                                           |
|-----------------|-----------------------------------------------------------------------------------|
| **Description** | Contient le validation rules                                                     |
| **Parametres**  |                                                                                   |
| **Return**      | Return validation logic to calling place on le basis of request method           |
| **Source**      | app\\Http\\Requests\\PublicHealth\\WaterSamplesRequest.php                        |
| **Remarques**     | Format pour validation rule: ‘field_name’=\>’validation_rule1 \| validation_rule2’ |

### Models

Le models contain le connection between le model et le tableau defined by

\$tableau = ‘public_health. water_samples’ as well as le primary key defined by

primaryKey= ‘id’

## Point chaud des maladies hydriques

### Tables

Point chaud des maladies hydriques is sous FSM module et uses le following tableau:

-   waterborne_hotspots

Le corresponding tableaux have their respective models ce are named in Pascal Case in singular form. Hotspots model is located at app\\Models\\PublicHealth\\.

### Views

Tous views utilise by ce module is stocke in resources\\views\\PublicHealth\\hotspots

-   hotspots.index: lists hotspots records.

-   hotspots.create: opens form et calls partial-form pour form contents

-   hotspots.partial-form: creates form content

-   hotspots.edit: opens form et calls partial-form pour form contents

-   hotspots.history: lists tous past edits of le record

-   hotspots.create: lists hotspots records

-   hotspots.show: displays tous attributes of particular record

### HotspotController

app\\Http\\Controllers\\PublicHealth\\HotspotController.php

Le controller’s principal function is to provide le connection between le calling route et its subsequent function written in le Service Class.

Le basic classes of le controller are:

|  **Function**   | \__construct()                                                         |
|-----------------|------------------------------------------------------------------------|
| **Description** | Initializes authentication, permissions et le service class instance |
| **Parametres**  | Service class instance(HotspotServiceClass)                            |
| **Return**      | null                                                                   |
| **Source**      | app\\Http\\Controllers\\PublicHealth\\HotspotController.php                     |

| **Function**    | index()                                                                         |
|-----------------|---------------------------------------------------------------------------------|
| **Description** | Returns le index.blade.php page avec dropdown values fetched de base de donnees.    |
| **Parametres**  | null                                                                            |
| **Return**      | publichealth/hotspots.index compact('page_title','wards','enumValues','hotspotLocation') |
| **Source**      | app\\Http\\Controllers\\PublicHealth\\HotspotController.php                              |

| **Function**    | create()                                                                                          |
|-----------------|---------------------------------------------------------------------------------------------------|
| **Description** | Returns le form to create nouveau waterborne hotspot avec dropdown values fetched de le base de donnees. |
| **Parametres**  | null                                                                                              |
| **Return**      | publichealth/hotspots.create compact('page_title','wards', 'maxDate', 'minDate','diesase', 'enumValues')   |
| **Source**      | app\\Http\\Controllers\\PublicHealth\\HotspotController.php                                                |

| **Function**    | store()                                                                 |
|-----------------|-------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of storing donnees        |
| **Parametres**  | HotspotRequest \$request                                                |
| **Return**      | Success or erreur message.                                               |
| **Source**      | app\\Http\\Controllers\\PublicHealth\\HotspotController.php                      |
| **Remarques**     | hotspotServiceClass-\>storeData(\$request)  Service Class Function Name |

| **Function**    | show()                                                         |
|-----------------|----------------------------------------------------------------|
| **Description** | Returns le page displaying individual waterborne hotspot donnees |
| **Parametres**  | \$id                                                           |
| **Return**      | \\Illuminate\\Http\\Response                                   |
| **Source**      | app\\Http\\Controllers\\PublicHealth\\HotspotController.php             |
| **Remarques**     | hotspotServiceClass-\>showData(\$id) (service class function)  |

| **Function**    | history()                                                |
|-----------------|----------------------------------------------------------|
| **Description** | lists tous past edits of le record                       |
| **Parametres**  | \$id                                                     |
| **Return**      | publichealth/hotspots.history   compact('page_title', ‘Hotspots’) |
| **Source**      | app\\Http\\Controllers\\PublicHealth\\HotspotController.php       |

| **Function**    | edit()                                                                                                      |
|-----------------|-------------------------------------------------------------------------------------------------------------|
| **Description** | Returns le edit form page displaying pre-existing individual batiment donnees as well                         |
| **Parametres**  | \$id                                                                                                        |
| **Return**      | publichealth/hotspots.edit compact('page_title', 'wards', 'Hotspots', 'geom', 'lat', 'long','diesase', 'enumValues') |
| **Source**      | app\\Http\\Controllers\\ Fsm\\HotspotController.php                                                         |

| **Function**    | update()                                                                             |
|-----------------|--------------------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of updating waterborne hotspot donnees |
| **Parametres**  | HotspotRequest \$request, \$id                                                       |
| **Return**      | Success or erreur message.                                                            |
| **Source**      | app\\Http\\Controllers\\PublicHealth\\HotspotController.php                                   |
| **Remarques**     | hotspotServiceClass-\>updateData(\$request, \$id)  (service class function)          |

| **Function**    | destroy()                                                |
|-----------------|----------------------------------------------------------|
| **Description** | Handles le processus of deleting waterborne hotspots donnees |
| **Parametres**  | \$id                                                     |
| **Return**      | Redirection avec succes/failure message                 |
| **Source**      | app\\Http\\Controllers\\PublicHealth\\HotspotController.php       |

| **Function**    | export()                                                                              |
|-----------------|---------------------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of exporting waterborne hotspot donnees |
| **Parametres**  | Request \$request                                                                     |
| **Return**      | CSV file containing hotspots donnees                                                     |
| **Source**      | app\\Http\\Controllers\\PublicHealth\\HotspotController.php                                    |
| **Remarques**     | HotspotServiceClass-\>download(\$donnees);  (service class function)                     |

### HotspotServiceClass

Location: app\\Services\\PublicHealth\\HotspotServiceClass.php

Le Service Class contient tous le business logic. It contient tous le functions ce are being called in le HotspotController.

|  **Function**   | storeData()                                       |
|-----------------|---------------------------------------------------|
| **Description** | Handles le processus of adding nouveau hotspot donnees.   |
| **Parametres**  | \$request                                         |
| **Return**      | Success or erreur message, stores donnees to hotspots |
| **Source**      | app\\Services\\PublicHealth\\HotspotServiceClass.php       |

|  **Function**   | updateData()                                       |
|-----------------|----------------------------------------------------|
| **Description** | Handles le processus of adding nouveau hotspot donnees.    |
| **Parametres**  | \$request, \$id                                    |
| **Return**      | Success or erreur message, updates donnees to hotspots |
| **Source**      | app\\Services\\PublicHealth\\HotspotServiceClass.php        |

|  **Function**   | download()                                                      |
|-----------------|-----------------------------------------------------------------|
| **Description** | Handles le processus of exporting batiment et owner information |
| **Parametres**  |                                                                 |
| **Return**      | Returns CSV                                                     |
| **Source**      | app\\Services\\PublicHealth\\HotspotServiceClass.php                     |

| **Function**    | fetchData()                                                             |
|-----------------|-------------------------------------------------------------------------|
| **Description** | Handles le processus of fetching batiment et owner donnees pour donnees tableaux |
| **Parametres**  | \$request                                                               |
| **Return**      | Returns donnees of batiment et owner tableau pour datatables                 |
| **Source**      | app\\Services\\PublicHealth\\HotspotServiceClass.php                             |

### HotspotRequest

Location: app\\Http\\Requests\\PublicHealth\\HotspotRequest.php)

HotspotRequest handles tous validation login. It handles validation logic as well as erreur messages to be displayed.

|  **Function**   | authorize()                                  |
|-----------------|----------------------------------------------|
| **Description** | Determines if utilisateur is authenticated or not   |
| **Parametres**  |                                              |
| **Return**      | Returns true                                 |
| **Source**      | app\\Http\\Requests\\PublicHealth\\HotspotRequest.php |

| **Function**    | message()                                                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Message to be displayed in case of validation erreur                                                                               |
| **Parametres**  |                                                                                                                                   |
| **Return**      | Return validation message                                                                                                         |
| **Source**      | app\\Http\\Requests\\PublicHealth\\HotspotRequest.php                                                                                      |
| **Remarques**     | Need to inclure errors.list.blade ce displays le erreur message in dashboard Format: ‘Field.validation_rule’ =\>”error_message” |

| **Function**    | rules()                                                                           |
|-----------------|-----------------------------------------------------------------------------------|
| **Description** | Contient le validation rules                                                     |
| **Parametres**  |                                                                                   |
| **Return**      | Return validation logic to calling place on le basis of request method           |
| **Source**      | app\\Http\\Requests\\PublicHealth\\HotspotRequest.php                                      |
| **Remarques**     | Format pour validation rule: ‘field_name’=\>’validation_rule1 \| validation_rule2’ |

| **Function**    | store()                                                                           |
|-----------------|-----------------------------------------------------------------------------------|
| **Description** | validation rules ce apply to le request.                                       |
| **Parametres**  | null                                                                              |
| **Return**      | Return validation logic to calling place pour store                                |
| **Source**      | app\\Http\\Requests\\PublicHealth\\HotspotRequest.php                                      |
| **Remarques**     | Format pour validation rule: ‘field_name’=\>’validation_rule1 \| validation_rule2’ |

| **Function**    | update ()                                                                         |
|-----------------|-----------------------------------------------------------------------------------|
| **Description** | validation rules ce apply to le request.                                       |
| **Parametres**  | null                                                                              |
| **Return**      | Return validation logic to calling place pour update                               |
| **Source**      | app\\Http\\Requests\\PublicHealth\\HotspotRequest.php                                      |
| **Remarques**     | Format pour validation rule: ‘field_name’=\>’validation_rule1 \| validation_rule2’ |

### Models

Le models contain le connection between le model et le tableau defined by

\$tableau = ‘public_health.waterborne_hotspots’ as well as le primary key defined by

primaryKey= ‘id’

## Waterborne Case Information

### Tables

Yearly waterborne case information is sous Public Health module et uses le following tableau:

yearly_waterborne_cases

Le corresponding tableaux have their respective models ce are named in Pascal Case in singular form. YearlyWaterborne model is located at app\\Models\\PublicHealth\\.

### Views

Tous views utilise by ce module is stocke in resources\\views\\public-sante\\waterborne

-   waterborne.index: lists waterborne cases records.

-   waterborne.create: opens form et calls partial-form pour form contents

-   waterborne.partial-form: creates form content

-   waterborne.edit: opens form et calls partial-form pour form contents

-   waterborne.history: lists tous past edits of le record

-   waterborne.show: displays tous attributes of particular record

### YearlyWaterborneController

app\\Http\\Controllers\\PublicHealth\\YearlyWaterborneController.php

Le controller’s principal function is to provide le connection between le calling route et its subsequent function written in le Service Class.

Le basic classes of le controller are:

|  **Function**   | \__construct()                                                         |
|-----------------|------------------------------------------------------------------------|
| **Description** | Initializes authentication, permissions et le service class instance |
| **Parametres**  | Service class instance(WaterborneService)                              |
| **Return**      | null                                                                   |
| **Source**      | app\\Http\\Controllers\\PublicHealth\\YearlyWaterborneController.php   |

| **Function**    | index()                                                                      |
|-----------------|------------------------------------------------------------------------------|
| **Description** | Returns le index.blade.php page avec dropdown values fetched de base de donnees. |
| **Parametres**  | null                                                                         |
| **Return**      | public-sante/waterborne.index compact('page_title','years','enumValues')    |
| **Source**      | app\\Http\\Controllers\\PublicHealth\\YearlyWaterborneController.php         |

| **Function**    | getData()                                                                   |
|-----------------|-----------------------------------------------------------------------------|
| **Description** | Fetches donnees en utilisant le WaterborneServiceClass based on le provided request |
| **Parametres**  | Request \$request                                                           |
| **Return**      | Le fetched donnees                                                            |
| **Source**      | app\\Http\\Controllers\\PublicHealth\\YearlyWaterborneController.php        |
| **Remarques**     | fetchData(\$request) Service Class Function Name                            |

| **Function**    | create()                                                                                                     |
|-----------------|--------------------------------------------------------------------------------------------------------------|
| **Description** | Returns le form to create nouveau yearly waterborne case avec dropdown values fetched de le base de donnees.        |
| **Parametres**  | null                                                                                                         |
| **Return**      | public-sante/waterborne.create compact('page_title', 'wards', 'maxDate', 'minDate','diesase', 'enumValues') |
| **Source**      | app\\Http\\Controllers\\PublicHealth\\YearlyWaterborneController.php                                         |

| **Function**    | store(YearlyWaterborneRequest \$request)                               |
|-----------------|------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of storing donnees       |
| **Parametres**  | YearlyWaterborneRequest \$request                                      |
| **Return**      | Success or erreur message.                                              |
| **Source**      | app\\Http\\Controllers\\PublicHealth\\YearlyWaterborneController.php   |
| **Remarques**     | storeData (\$request) Service Class Function Name                      |

| **Function**    | show()                                                                 |
|-----------------|------------------------------------------------------------------------|
| **Description** | Returns le page displaying individual yearly waterborne cases donnees    |
| **Parametres**  | \$id                                                                   |
| **Return**      | Public-sante/waterborne.show                                          |
| **Source**      | app\\Http\\Controllers\\PublicHealth\\YearlyWaterborneController.php   |
| **Remarques**     | showData(\$id) Service Class Function Name                             |

| **Function**    | history()                                                              |
|-----------------|------------------------------------------------------------------------|
| **Description** | lists tous past edits of le record                                     |
| **Parametres**  | \$id                                                                   |
| **Return**      | public-sante/waterborne.history   compact('page_title', ‘Waterborne’) |
| **Source**      | app\\Http\\Controllers\\PublicHealth\\YearlyWaterborneController.php   |

| **Function**    | edit()                                                                                                    |
|-----------------|-----------------------------------------------------------------------------------------------------------|
| **Description** | Returns le edit form page                                                                                |
| **Parametres**  | \$id                                                                                                      |
| **Return**      | public-sante/waterborne.edit compact('page_title', 'wards', 'Waterborne','year','diesase', 'enumValues') |
| **Source**      | app\\Http\\Controllers\\PublicHealth\\YearlyWaterborneController.php                                      |

| **Function**    | update()                                                                    |
|-----------------|-----------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of updating help desk donnees |
| **Parametres**  | YearlyWaterborneRequest \$request, \$id                                     |
| **Return**      | Success or erreur message.                                                   |
| **Source**      | app\\Http\\Controllers\\PublicHealth\\YearlyWaterborneController.php        |
| **Remarques**     | storeData(Request \$request) (service class function)                       |

| **Function**    | destroy()                                                              |
|-----------------|------------------------------------------------------------------------|
| **Description** | Handles le processus of deleting yearly waterborne cases donnees           |
| **Parametres**  | \$id                                                                   |
| **Return**      | Redirection avec succes/failure message                               |
| **Source**      | app\\Http\\Controllers\\PublicHealth\\YearlyWaterborneController.php   |

| **Function**    | exportData()                                                                               |
|-----------------|--------------------------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of exporting yearly waterborne cases donnees |
| **Parametres**  | \$donnees                                                                                     |
| **Return**      | CSV file containing yearly waterborne cases donnees                                           |
| **Source**      | app\\Http\\Controllers\\PublicHealth\\YearlyWaterborneController.php                       |

### WaterborneService

Location: app\\Services\\PublicHealth\\WaterborneService.php

Le Service Class contient tous le business logic. It contient tous le functions ce are being called in le YearlyWaterborneControllers.php

|  **Function**   | storeData()                                                       |
|-----------------|-------------------------------------------------------------------|
| **Description** | Handles le processus of adding nouveau waterborne cases.               |
| **Parametres**  | \$id,\$donnees                                                       |
| **Return**      | Success or erreur message, stores/updates donnees to waterborne cases |
| **Source**      | app\\Services\\PublicHealth\\WaterborneService.php                |

|  **Function**   | download()                                                      |
|-----------------|-----------------------------------------------------------------|
| **Description** | Handles le processus of exporting batiment et owner information |
| **Parametres**  |                                                                 |
| **Return**      | Returns CSV                                                     |
| **Source**      | app\\Services\\PublicHealth\\WaterborneService.php              |

| **Function**    | fetchData()                                                                  |
|-----------------|------------------------------------------------------------------------------|
| **Description** | Handles le processus of fetching yearly waterborne cases donnees pour donnees tableaux |
| **Parametres**  | \$request                                                                    |
| **Return**      | Returns donnees of waterborne cases donnees pour datatables                         |
| **Source**      | app\\Services\\PublicHealth\\WaterborneService.php                           |

### YearlyWaterborneRequest

Location: app\\Http\\Requests\\PublicHealth\\YearlyWaterborneRequest.php)

YearlyWaterborneRequest handles tous validation login. It handles validation logic as well as erreur messages to be displayed.

|  **Function**   | authorize()                                                    |
|-----------------|----------------------------------------------------------------|
| **Description** | Determines if utilisateur is authenticated or not                     |
| **Parametres**  | null                                                           |
| **Return**      | Returns true                                                   |
| **Source**      | app\\Http\\Requests\\PublicHealth\\YearlyWaterborneRequest.php |

| **Function**    | message()                                                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Message to be displayed in case of validation erreur                                                                               |
| **Parametres**  |                                                                                                                                   |
| **Return**      | Return validation message                                                                                                         |
| **Source**      | app\\Http\\Requests\\PublicHealth\\YearlyWaterborneRequest.php                                                                    |
| **Remarques**     | Need to inclure errors.list.blade ce displays le erreur message in dashboard Format: ‘Field.validation_rule’ =\>”error_message” |

| **Function**    | rules()                                                                           |
|-----------------|-----------------------------------------------------------------------------------|
| **Description** | Contient le validation rules                                                     |
| **Parametres**  |                                                                                   |
| **Return**      | Return validation logic to calling place                                          |
| **Source**      | app\\Http\\Requests\\PublicHealth\\YearlyWaterborneRequest.php                    |
| **Remarques**     | Format pour validation rule: ‘field_name’=\>’validation_rule1 \| validation_rule2’ |

### Models

Le models contain le connection between le model et le tableau defined by

\$tableau = ‘public_health.yearly_waterborne_cases’ as well as le primary key defined by

primaryKey= ‘id’
