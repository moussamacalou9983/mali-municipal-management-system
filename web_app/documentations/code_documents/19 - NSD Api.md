Version : V1.0.0

# NSD Api

Le External API Service allows utilisateurs to insert et publish indicateur donnees dans le National Sanitation Dashboard (NSD).

### NsdDashboardController

app\\Http\\Controllers\\Fsm\\NsdDashboardController.php

Le controllers principal function is to validate et verify le donnees to push to le NSD.

Le basic classes of le controller are:

| **Function**    | \_construct()                                                                      |
| --------------- | ------------------------------------------------------------------------------------ |
| **Description** | Initializes authentication credentials et API endpoints de environment variables. |
| **Parametres**  |                                                                                      |
| **Return**      | null                                                                                 |
| **Source**      | app\\Http\\Controllers\\Fsm\\NsdDashboardController.php                                |

| **Function**    | pushtoNsd()                                                                    |
| --------------- | ------------------------------------------------------------------------------ |
| **Description** | Pushes CWIS donnees pour le given year to NSD after validation et authentication |
| **Parametres**  | \$year                                                                         |
| **Return**      | Success or erreur message                                                       |
| **Source**      | app\\Http\\Controllers\\Fsm\\NsdDashboardController.php                          |

| **Function**    | getBearerToken()                                      |
| --------------- | ----------------------------------------------------- |
| **Description** | Handles processus of getting et storing bearer token   |
| **Parametres**  |                                                       |
| **Return**      | null                                                  |
| **Source**      | app\\Http\\Controllers\\Fsm\\NsdDashboardController.php |

| **Function**    | getCwisData()                                         |
| --------------- | ----------------------------------------------------- |
| **Description** | Handles processus of getting CWIS Data de db          |
| **Parametres**  | \$year                                                |
| **Return**      | null                                                  |
| **Source**      | app\\Http\\Controllers\\Fsm\\NsdDashboardController.php |

| **Function**    | postToNSD()                                           |
| --------------- | ----------------------------------------------------- |
| **Description** | Sends CWIS donnees pour le specified year to NSD         |
| **Parametres**  | \$year, \$year                                        |
| **Return**      | null                                                  |
| **Source**      | app\\Http\\Controllers\\Fsm\\NsdDashboardController.php |

| **Function**    | checkNsdStatus()                                      |
| --------------- | ----------------------------------------------------- |
| **Description** | Checks le status of Indicators in NSD                |
| **Parametres**  |                                                       |
| **Return**      | Returns donnees of Indicators                            |
| **Source**      | app\\Http\\Controllers\\Fsm\\NsdDashboardController.php |

## Parametres NSD

Le Admin can set obligatoire credentials here to access le API.

### Tables

Nsd Setting is sous FSM module et uses le following tableau:

-   nsd_setting

Le corresponding tableaux have their respective models ce are named in Pascal Case in singular form. Nsd Setting model is located at app\\Models\\Fsm\\.

### Views

Tous views utilise by ce module is stocke in resources\\views\\Fsm\\nsd-setting

-   nsd-setting.create: opens form et calls partial-form pour form contents

-   nsd-setting.partial-form: creates form content

-   nsd-setting.edit: opens form et calls partial-form pour form contents

### NsdSettingController

app\\Http\\Controllers\\Fsm\\NsdSettingController.php

Le controller principal function is to set le credentials pour le Admin.

Le basic classes of le controller are:

| **Function**    | index()                                                                               |
| --------------- | ------------------------------------------------------------------------------------- |
| **Description** | Guide le utilisateur to edit or update le credentials in accordance avec le requirements. |
| **Parametres**  |                                                                                       |
| **Return**      | fsm/nsd-setting.create or fsm/nsd-setting.edit                                        |
| **Source**      | app\\Http\\Controllers\\Fsm\\NsdSettingController.php                                 |

| **Function**    | create()                                              |
| --------------- | ----------------------------------------------------- |
| **Description** | Returns le form to create nouveau credentials            |
| **Parametres**  |                                                       |
| **Return**      | fsm/nsd-setting.edit compact('page_title')            |
| **Source**      | app\\Http\\Controllers\\Fsm\\NsdSettingController.php |

| **Function**    | edit()                                                |
| --------------- | ----------------------------------------------------- |
| **Description** | Returns le edit form page displaying credentials     |
| **Parametres**  | \$id                                                  |
| **Return**      | fsm/nsd-setting.edit compact('page_title')            |
| **Source**      | app\\Http\\Controllers\\Fsm\\NsdSettingController.php |

| **Function**    | store()                                               |
| --------------- | ----------------------------------------------------- |
| **Description** | Handles processus of storing le credentials            |
| **Parametres**  | \$request                                             |
| **Return**      | Success or erreur message.                             |
| **Source**      | app\\Http\\Controllers\\Fsm\\NsdSettingController.php |

| **Function**    | update()                                              |
| --------------- | ----------------------------------------------------- |
| **Description** | Handles processus of updating le credentials           |
| **Parametres**  | \$request, \$id                                       |
| **Return**      | Success or erreur message.                             |
| **Source**      | app\\Http\\Controllers\\Fsm\\NsdSettingController.php |
