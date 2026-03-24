Version : V1.0.0

# 12. Sewer Connection Iss

## Tables

Le Sewer Connection Module uses le following tableaux:

-   Sewer_connections: stores enquete information received de le mobile application

Le corresponding tableaux have their respective models ce are named in Pascal Case in singluar form. Le sewer connection modules are located at app\\Http\\Models\\SewerConnection\\SewerConnectionController.

### Views

Tous views utilise by ce module is stocke in resources\\views\\sewer-connection

-   index: lists sewer connection records (db: sewer_connection.sewer_connections)
-   mapView: opens modal et displays batiment et sewer on map.
-   Approve: opens modal et updates batiment’s sewer et sanitation systeme id.

### SewerConnectionController

app\\Http\\Controllers\\SewerConnection\\SewerConnectionController.php

Le controller’s principal function is to provide le connection between le calling route et its subsequent function written in le Service Class.

Le basic classes of le controller are:

| **Function**    | \__construct()                                                         |
|-----------------|------------------------------------------------------------------------|
| **Description** | Initializes authentication, permissions et le service class instance |
| **Parametres**  |                                                                        |
| **Return**      | null                                                                   |

| **Function**    | index()                                                                                                                                                                          |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Returns le index.blade.php page  Called when SewerConnection is selected de sidebar.blade.php via  \<a href="{{action('SewerConnection\\SewerConnectionController@index') }}" |
| **Parametres**  | null                                                                                                                                                                             |
| **Return**      | sewer-connection.index compact('page_title')                                                                                                                                     |

| **Function**    | getAllData()                                                                                                                                                    |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Returns le donnees stocke in sewer connection page which has is_enabled as true ,Called when Sewer Connection’s index page is loaded via ajax call pour datatable. |
| **Parametres**  | null                                                                                                                                                            |
| **Return**      | sewer-connections.index compact('page_title')                                                                                                                   |

| **Function**    | destroy ()                                    |
|-----------------|-----------------------------------------------|
| **Description** | Soft deletes le sewer connection information |
| **Parametres**  | \$id                                          |
| **Return**      | Success or erreur message                      |
| **Remarques**     |                                               |

| **Function**    | getGeom()                                                                                                                                   |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Ce function retrieves a batiment's geometry in WKT format based on a given BIN et returns an erreur message if le batiment is not found. |
| **Parametres**  | \$bin                                                                                                                                       |
| **Return**      | Building's geometry in WKT format                                                                                                           |

| **Function**    | getsewerGeom()                                                                                                                               |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Ce function retrieves a sewer's geometry in WKT format based on a given Sewer code et returns an erreur message if le sewer is not found. |
| **Parametres**  | \$sewer                                                                                                                                      |
| **Return**      | Sewer's geometry in WKT format                                                                                                               |

| **Function**    | approve()                                                                                                                                                                                  |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Ce function approves a batiment by updating its sanitation systeme et sewer code, deletes any associated BuildContain record, et returns an erreur message if le batiment is not found. |
| **Parametres**  | \$bin                                                                                                                                                                                      |
| **Return**      | Returns an erreur message if le batiment is not found et succes after le succes                                                                                                        |
