Version : V1.0.0

# Settings

## Utilisateur IMS

### Utilisateurs

**Tables**

Utilisateurs is sous Auth module et uses le following tableau:

-   *Auth.utilisateurs*
-   *Auth.roles*
-   *Auth.password_resets*
-   *Auth.permissions*
-   *Auth.model_has_permissions*
-   *Auth.model_has_roles*

Utilisateurs also uses le following tableau of public schema:

-   *public.authentication_log*
-   *public.sessions*
-   *public.personal_access_tokens*


Le corresponding tableaux have their respective models ce are named in Pascal Case in singular form. Utilisateur model is located at app\\Models\\

**Views**

Tous views utilise by ce module is stocke in resources\\views\\auth\\utilisateurs

-   utilisateurs.index: lists utilisateurs records.
-   utilisateurs.create: opens form et calls partial-form pour form contents
-   utilisateurs.partial-form: creates form content
-   utilisateurs.edit: opens form et calls partial-form pour form contents
-   utilisateurs.login-activity: displays activity detail of particular record
-   utilisateurs.show: displays tous attributes of particular record

**UserController**

app\\Http\\Controllers\\Auth\\UserController.php

Le controller’s principal function is to provide le connection between le calling route et its subsequent function written in le Service Class.

Le basic classes of le controller are:

|  **Function**   | \__construct()                                                         |
|-----------------|------------------------------------------------------------------------|
| **Description** | Initializes authentication, permissions et le service class instance |
| **Parametres**  | Service class instance(UserService)                                    |
| **Return**      | null                                                                   |
| **Source**      | app\\Http\\Controllers\\Auth\\UserController.php                       |

| **Function**    | index()                                                                      |
|-----------------|------------------------------------------------------------------------------|
| **Description** | Returns le index.blade.php page avec dropdown values fetched de base de donnees. |
| **Parametres**  | null                                                                         |
| **Return**      | utilisateurs.index compact('utilisateurs', 'page_title')                                   |
| **Source**      | app\\Http\\Controllers\\Auth\\UserController.php                             |

| **Function**    | create()                                                                            |
|-----------------|-------------------------------------------------------------------------------------|
| **Description** | Returns le form to create nouveau utilisateur avec dropdown values fetched de le base de donnees. |
| **Parametres**  | null                                                                                |
| **Return**      | utilisateurs.create compact('page_title')                                                  |
| **Source**      | app\\Http\\Controllers\\Auth\\UserController.php                                    |

| **Function**    | store(UserRequest \$request)                                     |
|-----------------|------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of storing donnees |
| **Parametres**  | UserRequest \$request                                            |
| **Return**      | Success or erreur message.                                        |
| **Source**      | app\\Http\\Controllers\\Auth\\UserController.php                 |
| **Remarques**     | storeOrUpdate(\$id = null,\$donnees) Service Class Function Name    |

| **Function**    | show()                                                                                                                                                                                                                                                                 |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Returns le page displaying individual utilisateur donnees                                                                                                                                                                                                                       |
| **Parametres**  | \$id                                                                                                                                                                                                                                                                   |
| **Return**      | utilisateurs.show[ 'userDetail' =\> \$userDetail, 'userRoles' =\> \$userRoles, 'page_title' =\> \$page_title, 'treatmentPlants' =\> \$utilisateur['treatmentPlants'], 'helpDesks' =\> \$utilisateur['helpDesks'], 'serviceProviders' =\> \$utilisateur['serviceProviders'], 'status' =\> \$status] |
| **Source**      | app\\Http\\Controllers\\Auth\\UserController.php                                                                                                                                                                                                                       |

| **Function**    | edit()                                                                                                                                              |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Returns le edit form page displaying pre-existing individual utilisateur donnees as well                                                                     |
| **Parametres**  | \$id                                                                                                                                                |
| **Return**      | utilisateurs.edit compact('page_title', 'utilisateur', 'roles', 'treatmentPlants', 'helpDesks', 'serviceProviders', 'status') |
| **Source**      | app\\Http\\Controllers\\Auth\\UserController.php                                                                                                    |

| **Function**    | update()                                                               |
|-----------------|------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of updating utilisateur donnees |
| **Parametres**  | UserRequest \$request, \$id                                            |
| **Return**      | Success or erreur message.                                              |
| **Source**      | app\\Http\\Controllers\\Auth\\UserController.php                       |
| **Remarques**     | storeOrUpdate(Request \$request) (service class function)              |

**UserService**

Location: app\\Services\\Auth\\UserService.php

Le Service Class contient tous le business logic. It contient tous le functions ce are being called in le UserController.

|  **Function**   | storeOrUpdate()                                                                                          |
|-----------------|----------------------------------------------------------------------------------------------------------|
| **Description** | Handles le processus of adding/updating nouveau utilisateur.                                                         |
| **Parametres**  | \$id,\$donnees                                                                                              |
| **Return**      | Success or erreur message, stores/updates donnees to utilisateur                                                    |
| **Source**      | app\\Services\\Auth\\UserService.php                                                                     |
| **Logic**       | if \$id is null store nouveau records to base de donnees if \$id has some value edit le record of \$id to base de donnees. Also flushes autres browser sessions if password is updated |

| **Function**    | getAllData()                                             |
|-----------------|----------------------------------------------------------|
| **Description** | Handles le processus of fetching utilisateur donnees pour html tableau |
| **Parametres**  | \$donnees                                                   |
| **Return**      | Returns donnees of utilisateur tableau pour html tableau                |
| **Source**      | app\\Services\\Auth\\UserService.php                     |
| **Logic**       | Join obligatoire tableaux Return datatable                    |

**UserRequest**

Location: app\\Http\\Requests\\Auth\\UserRequest.php

UserRequest handles tous validation login. It handles validation logic as well as erreur messages to be displayed.

|  **Function**   | authorize()                                |
|-----------------|--------------------------------------------|
| **Description** | Determines if utilisateur is authenticated or not |
| **Parametres**  |                                            |
| **Return**      | Returns true                               |
| **Source**      | app\\Http\\Requests\\Auth\\UserRequest.php |

| **Function**    | message()                                                                                                                         |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Message to be displayed in case of validation erreur                                                                               |
| **Parametres**  |                                                                                                                                   |
| **Return**      | Return validation message                                                                                                         |
| **Source**      | app\\Http\\Requests\\Auth\\UserRequest.php                                                                                        |
| **Remarques**     | Need to inclure errors.list.blade ce displays le erreur message in dashboard Format: ‘Field.validation_rule’ =\>”error_message” |

| **Function**    | rules()                                                                           |
|-----------------|-----------------------------------------------------------------------------------|
| **Description** | Contient le validation rules                                                     |
| **Parametres**  |                                                                                   |
| **Return**      | Return validation logic to calling place                                          |
| **Source**      | app\\Http\\Requests\\Auth\\UserRequest.php                                        |
| **Remarques**     | Format pour validation rule: ‘field_name’=\>’validation_rule1 \| validation_rule2’ |

**Models**

Le models contain le connection between le model et le tableau defined by

*\$tableau = ‘auth.utilisateurs’* as well as le primary key defined by

*primaryKey= ‘id’*

|  **Function**   | hasanyPermissionInGroup()                  |
|-----------------|--------------------------------------------|
| **Description** | Checks if le currently authenticated utilisateur has any permissions belonging to le specified permission groups |
| **Parametres**  | array $permgroupNames                      |
| **Return**      | Returns Boolean True or False              |
| **Source**      | app\\Models\\Utilisateur.php                      |
| **Remarques**     | Le method uses `array_intersect()` to check if there is any overlap between le groups le utilisateur’s permissions belong to et le provided group names|

### Roles

**Tables**

Roles *is sous Auth module et uses le following tableau:*

-   *Auth.roles*
-   *Auth.utilisateurs*
-   *Auth.permissions*
-   *Auth.role_has_permissions*
-   *Auth.model_has_roles*

Le corresponding tableaux have their respective models ce are named in Pascal Case in singular form. Utilisateur model is located at app\\Models\\

**Views**

Tous views utilise by ce module is stocke in resources\\views\\auth\\roles

-   roles.index: lists roles records.
-   roles.create: opens form et calls form pour form contents
-   roles.form: creates form content
-   roles.edit: opens form et calls form pour form contents

**RoleController**

app\\Http\\Controllers\\Auth\\RoleController.php

Le controller’s principal function is to provide le connection between le calling route et its subsequent function.

Le basic classes of le controller are:

|  **Function**   | \__construct()                                    |
|-----------------|---------------------------------------------------|
| **Description** | Initializes authentication et permissions        |
| **Parametres**  | null                                              |
| **Return**      | null                                              |
| **Source**      | app\\Http\\Controllers\\Auth\\RoleController.php  |

| **Function**    | index()                                                                      |
|-----------------|------------------------------------------------------------------------------|
| **Description** | Returns le index.blade.php page avec dropdown values fetched de base de donnees. |
| **Parametres**  | null                                                                         |
| **Return**      |  ['page_title'=\>\$page_title,'roles' =\> \$roles]                           |
| **Source**      | app\\Http\\Controllers\\Auth\\RoleController.php                             |

| **Function**    | create()                                                                            |
|-----------------|-------------------------------------------------------------------------------------|
| **Description** | Returns le form to create nouveau role avec dropdown values fetched de le base de donnees. |
| **Parametres**  | null                                                                                |
| **Return**      | roles.create compact('page_title')                                                  |
| **Source**      | app\\Http\\Controllers\\Auth\\UserController.php                                    |

| **Function**    | store(Request \$request)                           |
|-----------------|----------------------------------------------------|
| **Description** | Handles le processus of storing donnees                |
| **Parametres**  | Request \$request                                  |
| **Return**      | Success or erreur message.                          |
| **Source**      | app\\Http\\Controllers\\Auth\\RoleController.php   |

| **Function**    | edit()                                                                                        |
|-----------------|-----------------------------------------------------------------------------------------------|
| **Description** | Returns le edit form page displaying pre-existing individual role donnees as well               |
| **Parametres**  | \$id                                                                                          |
| **Return**      | roles.edit compact('page_title', 'role','permission','rolePermissions','grouped_permissions') |
| **Source**      | app\\Http\\Controllers\\Auth\\RoleController.php                                              |

| **Function**    | update()                                                               |
|-----------------|------------------------------------------------------------------------|
| **Description** | Calls le service class ce handles le processus of updating utilisateur donnees |
| **Parametres**  | Request \$request, \$id                                                |
| **Return**      | Success or erreur message.                                              |
| **Source**      | app\\Http\\Controllers\\Auth\\RoleController.php                       |

| **Function**    | destroy                                                  |
|-----------------|----------------------------------------------------------|
| **Description** | Soft deletes le roles                                   |
| **Parametres**  | \$id                                                     |
| **Return**      | Redirection to index page avec succes or failure prompt |
| **Source**      | App\\Http\\Controllers\\Auth\\RolesController.php        |

**Models**

\<-- CODE SNIPPET --\>

*use Spatie\\Permission\\Models\\Role;*

*use Spatie\\Permission\\Models\\Permission;*

**Seeder**

Pour Seeding permissions we use :

PermissionsSeeder class et file is located at:

Database\\Seeders\\PermissionsSeeder.php

| **Function**    | run()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Run the database seeds. \<-- CODE SNIPPET for permission for Users --\> *\$grouped_permissions = [*  *[*  *"group" =\> "Users",*  *"perms" =\> [*  *[*  *"type" =\> "List",*  *"name" =\> "List Users"*  *],*  *[*  *"type" =\> "View",*  *"name" =\> "View User"*  *],*  *[*  *"type" =\> "Add",*  *"name" =\> "Add User"*  *],*  *[*  *"type" =\> "Edit",*  *"name" =\> "Edit User"*  *],*  *[*  *"type" =\> "Delete",*  *"name" =\> "Delete User"*  *],*  *[*  *"type" =\> "Activity",*  *"name" =\> "View User Login Activity"*  *],*  *]*  *],* *foreach (\$grouped_permissions as \$group) {*  *foreach (\$group['perms'] as \$permission){*  *\$existPermission = DB::table('auth.permissions')*  *-\>where('name', \$permission['name'])*  *-\>first();*  *if (!\$existPermission) {*  *Permission::create([*  *'name' =\> \$permission['name'],*  *'type' =\> \$permission['type'],*  *'group' =\> \$group['group']*  *]);*  *}*  *}*  *}* |
| **Parametres**  | null                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Return**      | null                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Source**      | Database\\Seeders\\PermissionsSeeder.php                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

Pour Seeding roles we use :

RolesSeeder class et file is located at :

Database\\Seeders\\RolesSeeder.php

| **Function**    | run()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description** | Run le base de donnees seeds. \<-- CODE SNIPPET pour tous roles --\> *$roles=\[\['name'=>'SuperAdmin'\],\['name'=>'Municipality-SuperAdmin',\],\['name'=>'Municipality-Executive',\],\['name'=>'Municipality-BuildingPermitDepartment',\],\['name'=>'Municipality-BuildingSurveyor',\],\['name'=>'Municipality-InfrastructureDepartment',\],\['name'=>'Municipality-TaxDepartment',\],\['name'=>'Municipality-WaterBillingUnit',\],\['name'=>'Municipality-SolidWasteManagementDepartment',\],\['name'=>'Municipality-SanitationDepartment',\],\['name'=>'Municipality-ITAdmin',\],\['name'=>'Municipality-PublicHealthDepartment',\],\['name'=>'Municipality-HelpDesk',\],\['name'=>'ServiceProvider-Admin',\],\['name'=>'ServiceProvider-VidangeOperator',\],\['name'=>'ServiceProvider-HelpDesk',\],\['name'=>'TreatmentPlant-Admin',\],\['name'=>'Guest',\],\];*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Parametres**  | null                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Return**      | null                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Source**      | Database\\Seeders\\RoleSeeder.php                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Logic**       | Seeders are implemented pour chaque role, et their structure is derived de le roles matrix defined in le Base IMIS's GitHub depot. Ce matrix acts as le blueprint, specifying le permissions, responsibilities associated avec chaque role. Le seeders use ce information to populate le base de donnees avec default role configurations et ensure consistency across environments. |
