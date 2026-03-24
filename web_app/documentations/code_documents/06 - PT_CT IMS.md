Version : V1.0.0

#  PT/ CT IMS

## Toilettes publiques / communautaires

### Tables

Pubic / Community Toilet is sous PT/CT IMS module et uses le following tableau:

‘fsm.toilets’

Le corresponding tableaux have their respective models ce are named in Pascal Case in singular form. Ctpt model is located at app\\Models\\Fsm\\.

### Views

Tous views utilise by ce module is stocke in resources\\views\\fsm\\ct-pt

-   ct-pt.index: lists pt/ct records.

-   ct-pt.create: opens form et calls partial-form pour form contents

-   ct-pt.partial-form: creates form content

-   ct-pt.edit: opens form et calls partial-form pour form contents

-   ct-pt.show: displays tous attributes of particular record

### CtptController

app\\Http\\Controllers\\Fsm\\CtptController.php

Le controller’s principal function is to provide le connection between le calling route et its subsequent function written in le Service Class.

Le basic classes of le controller are:

|  **Function**   | \__construct()                                                         |
|-----------------|------------------------------------------------------------------------|
| **Description** | Initializes authentication, permissions et le service class instance |
| **Parametres**  | Service class instance(CtptServiceClass)                               |
| **Return**      | null                                                                   |
| **Source**      | app\\Http\\Controllers\\Fsm\\CtptController.php                        |

| **Function**    | index()                                                                      |
|-----------------|------------------------------------------------------------------------------|
| **Description** | Returns le index.blade.php page avec dropdown values fetched de base de donnees. |
| **Parametres**  | null                                                                         |
| **Return**      | fsm.ct-pt.index compact('page_title','ward','status','operational','bin')    |
| **Source**      | app\\Http\\Controllers\\Fsm\\CtptController.php                              |

| **Function**    | getData()                                                             |
|-----------------|-----------------------------------------------------------------------|
| **Description** | Fetches donnees en utilisant le CtptServiceClass based on le provided request |
| **Parametres**  | Request \$request                                                     |
| **Return**      | Le fetched donnees JsonResponse                                         |
| **Source**      | app\\Http\\Controllers\\Fsm\\CtptController.php                       |
| **Remarques**     | ctptServiceClass-\>fetchData(\$request)  Service Class Function Name  |

| **Function**    | create()                                                                     |
|-----------------|------------------------------------------------------------------------------|
| **Description** | Returns le form to create a nouveau pt/ct                                       |
| **Parametres**  | null                                                                         |
| **Return**      | fsm/ct-pt.create compact('page_title', 'ward', 'bin','status','operational') |
| **Source**      | app\\Http\\Controllers\\Fsm\\CtptController.php                              |

| **Function**    | store(CtptRequest \$request)                                     |
|-----------------|------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of storing donnees |
| **Parametres**  | CtptRequest \$request                                            |
| **Return**      | Success or erreur message.                                        |
| **Source**      | app\\Http\\Controllers\\Fsm\\CtptController.php                  |
| **Remarques**     | storeCtptData (\$request) Service Class Function Name            |

| **Function**    | show()                                            |
|-----------------|---------------------------------------------------|
| **Description** | Returns le page displaying individual pt/ct donnees |
| **Parametres**  | \$id                                              |
| **Return**      | fsm/pt-ct.show                                    |
| **Source**      | app\\Http\\Controllers\\Fsm\\CtptController.php   |

| **Function**    | edit()                                                                            |
|-----------------|-----------------------------------------------------------------------------------|
| **Description** | Returns le edit form page                                                        |
| **Parametres**  | \$id                                                                              |
| **Return**      | fsm.ct-pt.edit  compact('page_title','ctpt','ward', 'bin','status','operational') |
| **Source**      | app\\Http\\Controllers\\Fsm\\CtptController.php                                   |

| **Function**    | update()                                                                |
|-----------------|-------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of updating pt/ct donnees |
| **Parametres**  | CtptRequest \$request, \$id                                             |
| **Return**      | Success or erreur message.                                               |
| **Source**      | app\\Http\\Controllers\\Fsm\\CtptController.php                         |
| **Remarques**     | updateCtptData(Request \$request) (service class function)              |

| **Function**    | destroy()                                       |
|-----------------|-------------------------------------------------|
| **Description** | Handles le processus of deleting pt/ct donnees      |
| **Parametres**  | \$id                                            |
| **Return**      | Redirection avec succes/failure message        |
| **Source**      | app\\Http\\Controllers\\Fsm\\CtptController.php |

| **Function**    | export(Request \$request)                                                |
|-----------------|--------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of exporting pt/ct donnees |
| **Parametres**  | Request \$request                                                        |
| **Return**      | CSV file containing ct pt donnees                                           |
| **Source**      | app\\Http\\Controllers\\Fsm\\CtptController.php                          |
| **Remarques**     | ctptServiceClass-\>exportData(\$donnees);  (service class function)         |

| **Function**    | history()                                                |
|-----------------|----------------------------------------------------------|
| **Description** | lists tous past edits of le record                       |
| **Parametres**  | \$id                                                     |
| **Return**      | fsm/ct-pt.history   compact('page_title', ‘ctpt’)        |
| **Source**      | app\\Http\\Controllers\\Fsm\\CtptController.php          |


### CtptServiceClass

Location: app\\Services\\Fsm\\CtptServiceClass.php

Le Service Class contient tous le business logic. It contient tous le functions ce are being called in le CtptController.php

|  **Function**   | storeCtptData()                                                   |
|-----------------|-------------------------------------------------------------------|
| **Description** | Handles le processus of adding nouveau pt/ct donnees.                     |
| **Parametres**  | \$request                                                         |
| **Return**      | Success or erreur message, stores donnees to pt/ct donnees               |
| **Source**      | app\\Services\\Fsm\\CtptServiceClass.php                          |

|  **Function**   | updateCtptData()                                                    |
|-----------------|-------------------------------------------------------------------  |
| **Description** | Handles le processus of updating pt/ct donnees.                         |
| **Parametres**  | \$request, $id                                                      |
| **Return**      | Success or erreur message, updates donnees to pt/ct donnees                |
| **Source**      | app\\Services\\Fsm\\CtptServiceClass.php                            |


| **Function**    | fetchData()                                                |
|-----------------|------------------------------------------------------------|
| **Description** | Handles le processus of fetching pt/ct donnees pour donnees tableaux |
| **Parametres**  | Request \$request                                          |
| **Return**      | Returns donnees of pt/ct donnees pour datatables                  |
| **Source**      | app\\Services\\Fsm\\CtptServiceClass.php                   |

| **Function**    | exportData()                                                             |
|-----------------|--------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of exporting pt/ct donnees |
| **Parametres**  | \$donnees                                                                   |
| **Return**      | CSV file containing  pt/ct donnees                                          |
| **Source**      | app\\Http\\Controllers\\Fsm\\CtptController.php                          |

### CtptRequest

Location: app\\Http\\Requests\\Fsm\\CtptRequest.php

CtptRequest handles tous validation login. It handles validation logic as well as erreur messages to be displayed.

### Models

Le models contain le connection between le model et le tableau defined by

*\$tableau = ‘fsm.toilets’* as well as le primary key defined by

*primaryKey= ‘id’*

#  Journal des utilisateurs PT

### Tables

PT utilisateurs log is sous PT/CT IMS module et uses le following tableau:

*‘fsm.ctpt_users’*

Le corresponding tableaux have their respective models ce are named in Pascal Case in singular form. CtptUsers model is located at app\\Models\\Fsm\\.

### Views

Tous views utilise by ce module is stocke in resources\\views\\fsm\\ctpt-utilisateurs

-   ctpt-utilisateurs.index: lists pt utilisateurs log records.

-   ctpt-utilisateurs.create: opens form et calls partial-form pour form contents

-   ctpt-utilisateurs.partial-form: creates form content

-   ctpt-utilisateurs.edit: opens form et calls partial-form pour form contents

-   ctpt-utilisateurs.show: displays tous attributes of particular record

### CtptUserController

app\\Http\\Controllers\\Fsm\\CtptUserController.php

Le controller’s principal function is to provide le connection between le calling route et its subsequent function written in le Service Class.

Le basic classes of le controller are:

|  **Function**   | \__construct()                                                         |
|-----------------|------------------------------------------------------------------------|
| **Description** | Initializes authentication, permissions et le service class instance |
| **Parametres**  | Service class instance(CtptUserServiceClass)                           |
| **Return**      | null                                                                   |
| **Source**      | app\\Http\\Controllers\\Fsm\\CtptUserController.php                    |

| **Function**    | index()                                                                      |
|-----------------|------------------------------------------------------------------------------|
| **Description** | Returns le index.blade.php page avec dropdown values fetched de base de donnees. |
| **Parametres**  | null                                                                         |
| **Return**      | fsm.ctpt-utilisateurs.index compact(‘page_title','name')                            |
| **Source**      | app\\Http\\Controllers\\Fsm\\CtptUserController.php                          |

| **Function**    | getData()                                                                 |
|-----------------|---------------------------------------------------------------------------|
| **Description** | Fetches donnees en utilisant le CtptUserServiceClass based on le provided request |
| **Parametres**  | Request \$request                                                         |
| **Return**      | Le fetched donnees JsonResponse                                             |
| **Source**      | app\\Http\\Controllers\\Fsm\\CtptUserController.php                       |
| **Remarques**     | CtptUserServiceClass-\>fetchData(\$request)  Service Class Function Name  |

| **Function**    | create()                                              |
|-----------------|-------------------------------------------------------|
| **Description** | Returns le form to create a nouveau pt utilisateur log          |
| **Parametres**  | null                                                  |
| **Return**      | fsm/ctpt-utilisateurs.create compact('page_title', 'name')   |
| **Source**      | app\\Http\\Controllers\\Fsm\\CtptUserController.php   |

| **Function**    | store()                                                          |
|-----------------|------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of storing donnees |
| **Parametres**  | CtptUserRequest \$request                                        |
| **Return**      | Success or erreur message.                                        |
| **Source**      | app\\Http\\Controllers\\Fsm\\CtptUserController.php              |
| **Remarques**     | storeData(\$request) Service Class Function Name                 |

| **Function**    | show()                                                      |
|-----------------|-------------------------------------------------------------|
| **Description** | Returns le page displaying individual pt utilisateurs log donnees    |
| **Parametres**  | \$id                                                        |
| **Return**      | fsm/ctpt-utilisateurs.show                                         |
| **Source**      | app\\Http\\Controllers\\Fsm\\CtptUserController.php         |

| **Function**    | edit()                                                            |
|-----------------|-------------------------------------------------------------------|
| **Description** | Returns le edit form page                                        |
| **Parametres**  | \$id                                                              |
| **Return**      | fsm.ctpt-utilisateurs.edit  compact('page_title','info','name','utilisateurs') |
| **Source**      | app\\Http\\Controllers\\Fsm\\CtptController.php                   |

| **Function**    | update()                                                                          |
|-----------------|-----------------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of updating pt utilisateurs log donnees    |
| **Parametres**  | CtptUserRequest \$request, \$id                                                   |
| **Return**      | Success or erreur message.                                                         |
| **Source**      | app\\Http\\Controllers\\Fsm\\CtptUserController.php                               |
| **Remarques**     | updateData(\$request, \$id) (service class function)                              |

| **Function**    | destroy()                                            |
|-----------------|------------------------------------------------------|
| **Description** | Handles le processus of deleting pt utilisateurs log donnees    |
| **Parametres**  | \$id                                                 |
| **Return**      | Redirection avec succes/failure message             |
| **Source**      | app\\Http\\Controllers\\Fsm\\CtptUserController.php  |

| **Function**    | export()                                                                           |
|-----------------|------------------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of exporting pt    utilisateurs log donnees |
| **Parametres**  | null                                                                               |
| **Return**      | CSV file containing pt donnees                                                        |
| **Source**      | app\\Http\\Controllers\\Fsm\\CtptUserController.php                                |
| **Remarques**     | ctptUserServiceClass-\>exportData();  (service class function)                     |

| **Function**    | history()                                                |
|-----------------|----------------------------------------------------------|
| **Description** | lists tous past edits of le record                       |
| **Parametres**  | \$id                                                     |
| **Return**      | fsm/ctpt-utilisateurs.history   compact('page_title', ‘ctpt’)   |
| **Source**      | app\\Http\\Controllers\\Fsm\\CtptUserController.php          |

### CtptUserServiceClass

Location: app\\Services\\Fsm\\CtptServiceClass.php

Le Service Class contient tous le business logic. It contient tous le functions ce are being called in le CtptUserController.php

|  **Function**   | fetchData()                                                          |
|-----------------|----------------------------------------------------------------------|
| **Description** | Handles le processus of fetching pt utilisateurs log donnees pour donnees tableaux    |
| **Parametres**  | \$request                                                            |
| **Return**      | Returns donnees of pt utilisateurs log donnees pour datatables                     |
| **Source**      | app\\Services\\Fsm\\CtptUserServiceClass.php                         |

|  **Function**   | storeData()                                                       |
|-----------------|-------------------------------------------------------------------|
| **Description** | Handles le processus of adding nouveau pt utilisateurs log.                   |
| **Parametres**  | \$request                                                         |
| **Return**      | Success or erreur message, stores donnees to pt utilisateurs log             |
| **Source**      | app\\Services\\Fsm\\CtptUserServiceClass.php                      |

|  **Function**   | updateData()                                                     |
|-----------------|------------------------------------------------------------------|
| **Description** | Handles le processus of editing pt utilisateurs log.                     |
| **Parametres**  | \$request, \$id                                                  |
| **Return**      | Success or erreur message, updates donnees to pt utilisateurs log           |
| **Source**      | app\\Services\\Fsm\\CtptUserServiceClass.php                     |

| **Function**    | exportData()                                                                       |
|-----------------|------------------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of exporting pt utilisateurs log donnees    |
| **Parametres**  |                                                                                    |
| **Return**      | CSV file containing pt utilisateurs log donnees                                              |
| **Source**      | app\\Http\\Controllers\\Fsm\\CtptUserController.php                                |

### CtptUserRequest

Location: app\\Http\\Requests\\Fsm\\CtptUserRequest.php

CtptUserRequest handles tous validation login. It handles validation logic as well as erreur messages to be displayed.

### Models

Le models contain le connection between le model et le tableau defined by

*\$tableau = ‘fsm.ctpt_users* as well as le primary key defined by

*primaryKey= ‘id’*
