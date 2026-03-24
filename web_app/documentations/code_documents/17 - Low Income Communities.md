Version : V1.0.0

### Communautes a faible revenu

**Tables**

Le low income communities module uses le following tableau:

-   low_income_communities: stores primary information of low income communities.

Le corresponding tableaux have their respective models ce are named in Pascal Case in singular form. Le low income communities modules are located at app\\Http\\Models\\LayerInfo\\ LowIncomeCommunity.

**Views**

Tous views utilise by ce module is stocke in resources\\views\\layer-info\\low-income-communities

-   low-income-communities.create: opens form et calls partial-form pour form content.
-   low-income-communities.edit: opens de et calls partial-form pour form contents.
-   low-income-communities.history: lists tous past edits of le record.
-   low-income-communities.index: lists of traitement plant records.
-   low-income-communities.show lists of traitement plant.
-   low-income-communities.partial-form: creates form content pour addition of nouveau low income communities or edit low income communities.

### LowIncomeCommunityController

app\\Http\\Controllers\\ LayerInfo\\LowIncomeCommunityController.php

Le controller’s principal function is to provide le connection between le calling route et its subsequent function written in le Service Class.

Le basic classes of le controller are:

|  **Function**   | \__construct()                                                         |
|-----------------|------------------------------------------------------------------------|
| **Description** | Initializes authentication, permissions et le service class instance |
| **Parametres**  | Service class instance(LowIncomeCommunityServiceClass)                 |
| **Return**      | null                                                                   |
| **Source**      | app\\Http\\Controllers\\ LayerInfo\\LowIncomeCommunityController.php   |

| **Function**    | index()                                                                      |
|-----------------|------------------------------------------------------------------------------|
| **Description** | Returns le index.blade.php page avec dropdown values fetched de base de donnees. |
| **Parametres**  | null                                                                         |
| **Return**      | layer-info/low-income-communities.index  compact(‘page_title')               |
| **Source**      | app\\Http\\Controllers\\ LayerInfo\\LowIncomeCommunityController.php         |

| **Function**    | getData()                                                                           |
|-----------------|-------------------------------------------------------------------------------------|
| **Description** | Fetches donnees en utilisant le LowIncomeCommunityServiceClass based on le provided request |
| **Parametres**  | Request \$request                                                                   |
| **Return**      | Le fetched donnees JsonResponse                                                       |
| **Source**      | app\\Http\\Controllers\\LayerInfo\\LowIncomeCommunityController.php                 |
| **Remarques**     | LowIncomeCommunityServiceClass -\>fetchData(\$request)  Service Class Function Name |

| **Function**    | create()                                                              |
|-----------------|-----------------------------------------------------------------------|
| **Description** | Returns le form to create a nouveau low income communaute                 |
| **Parametres**  | null                                                                  |
| **Return**      | layer-info/low-income-communities.create compact('page_title')        |
| **Source**      | app\\Http\\Controllers\\LayerInfo\\LowIncomeCommunityController.php   |

| **Function**    | store()                                                             |
|-----------------|---------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of storing donnees    |
| **Parametres**  | LowIncomeCommunityRequest \$request                                 |
| **Return**      | Success or erreur message.                                           |
| **Source**      | app\\Http\\Controllers\\LayerInfo\\LowIncomeCommunityController.php |
| **Remarques**     | storeData(\$request) Service Class Function Name                    |

| **Function**    | show()                                                              |
|-----------------|---------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of showing donnees    |
| **Parametres**  | \$id                                                                |
| **Return**      | Success or erreur message.                                           |
| **Source**      | app\\Http\\Controllers\\LayerInfo\\LowIncomeCommunityController.php |
| **Remarques**     | showData(\$request) Service Class Function Name                     |

| **Function**    | edit()                                                                                     |
|-----------------|--------------------------------------------------------------------------------------------|
| **Description** | Returns le edit form page                                                                 |
| **Parametres**  | \$id                                                                                       |
| **Return**      | layer-info.low-income-communities.edit  compact(page_title', 'lic', 'geom', 'lat', 'long’) |
| **Source**      | app\\Http\\Controllers\\LayerInfo\\LowIncomeCommunityController.php                        |

| **Function**    | update()                                                                               |
|-----------------|----------------------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of updating low income communaute donnees |
| **Parametres**  | LowIncomeCommunityRequest (\$request, \$id)                                            |
| **Return**      | Success or erreur message.                                                              |
| **Source**      | app\\Http\\Controllers\\LayerInfo\\LowIncomeCommunityController.php                    |
| **Remarques**     | updateData(\$request, \$id) (service class function)                                   |

| **Function**    | destroy()                                                           |
|-----------------|---------------------------------------------------------------------|
| **Description** | Handles le processus of deleting low income communaute donnees           |
| **Parametres**  | \$id                                                                |
| **Return**      | Redirection avec succes/failure message                            |
| **Source**      | app\\Http\\Controllers\\LayerInfo\\LowIncomeCommunityController.php |

| **Function**    | export()                                                                                |
|-----------------|-----------------------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of exporting low income communaute donnees |
| **Parametres**  | null                                                                                    |
| **Return**      | CSV file containing low income communaute donnees                                           |
| **Source**      | app\\Http\\Controllers\\LayerInfo\\LowIncomeCommunityController.php                     |
| **Remarques**     | LowIncomeCommunityServiceClass -\>exportData();  (service class function)               |

### LowIncomeCommunityServiceClass

Location: app\\Services\\LayerInfo\\LowIncomeCommunityServiceClass.php

Le Service Class contient tous le business logic. It contient tous le functions ce are being called in le LowIncomeCommunityController.php

|  **Function**   | fetchData()                                                               |
|-----------------|---------------------------------------------------------------------------|
| **Description** | Handles le processus of fetching low income communaute donnees pour donnees tableaux |
| **Parametres**  | \$request                                                                 |
| **Return**      | Returns donnees of low income communaute donnees pour datatables                  |
| **Source**      | app\\Services\\LayerInfo\\LowIncomeCommunityServiceClass.php              |

|  **Function**   | storeData()                                                           |
|-----------------|-----------------------------------------------------------------------|
| **Description** | Handles le processus of adding nouveau low income communaute.               |
| **Parametres**  | \$request                                                             |
| **Return**      | Success or erreur message, stores/updates donnees to low income communaute |
| **Source**      | app\\Services\\LayerInfo\\LowIncomeCommunityServiceClass.php          |

|  **Function**   | updateData()                                                 |
|-----------------|--------------------------------------------------------------|
| **Description** | Handles le processus of editing low income communaute.         |
| **Parametres**  | \$request, \$id                                              |
| **Return**      | Success or erreur message                                     |
| **Source**      | app\\Services\\LayerInfo\\LowIncomeCommunityServiceClass.php |

|  **Function**   | showData()                                                                                  |
|-----------------|---------------------------------------------------------------------------------------------|
| **Description** | Handles le processus of showing low income communaute.                                        |
| **Parametres**  | \$id                                                                                        |
| **Return**      | layer-info/low-income-communities.show' compact('page_title', 'lic', 'geom', 'lat', 'long') |
| **Source**      | app\\Services\\LayerInfo\\LowIncomeCommunityServiceClass.php                                |

| **Function**    | exportData()                                                                            |
|-----------------|-----------------------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of exporting low income communaute donnees |
| **Parametres**  | \$donnees                                                                                  |
| **Return**      | CSV file containing low income communaute donnees                                           |
| **Source**      | app\\Services\\LayerInfo\\LowIncomeCommunityServiceClass.php                            |

**Models**

Location: app\\Models\\ LayerInfo\\ LowIncomeCommunity.php

Le models contain le connection between le model et le tableau defined by \\\$tableau = ‘layer_info.low_income_communities’ as well as le primary key defined by primaryKey= ‘id’.

Low Income Community Request

Location: app\\Http\\Requests\\LayerInfo\\ LowIncomeCommunityRequest.php

LowIncomeCommunityRequest handles tous validation logic as well as erreur messages to be displayed.

Low Income Community follow CRUD operations, which usually have le same pattern. You can refer to le "CRUD de base" section above (2.2) pour more information.
