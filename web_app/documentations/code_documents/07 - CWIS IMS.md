Version : V1.0.0

# CWIS IMS

## CWIS Dashboard

Le CWIS dashboard incorporates charts (en utilisant Chart.js) et cards (en utilisant HTML et CSS) to visualize donnees. Ce section delves dans le implementation of le doughnut chart.

### Data Retrieval

- Data is fetched de le CwisNewDashboardController (located at app\\Http\\Controllers\\Cwis\\CwisNewDashboardController.php).
- Le getall() function retrieves donnees en utilisant le following steps:

1. Queries le data_cwis tableau (en utilisant le Eloquent ORM).
2. Filters records based on year et indicator_code.
3. Selects specific columns, applying formatting to heading.
4. Stores le retrieved records in le variable.

### Views

- View code resides at resources\\views\\cwis\\cwis-dashboard\\chart-layout\\cwis-dash-layout.blade.php.
- It performs le following actions:

1. Fetches donnees passed de le controller.
2. Uses a \<div\> avec a canvas element to display le chart.
3. Calls le createDoughnutChart() function upon DOM content loading.

### JavaScript Function Breakdown

- Le createDoughnutChart() function generates le doughnut chart avec ces parameters:
- percent: Le percentage value to display.
- color: Le color of le chart.
- canvasId: Le ID of le canvas element.
- containerId: Le ID of le container element.
- It performs le following actions:

1. Retrieves canvas et container elements de le DOM.
2. Caps percentValue at 100 if it exceeds 100.
3. Creates a div to display le percentage value.
4. Constructs a Chart.js doughnut chart instance:

- Sets chart type to doughnut.
- Specifies donnees, background color, 0 border width, 78% cutout, et disabled tooltips.

1. Sets animation duration to 1400 milliseconds.
2. Appends le percentage value div to le container.

Further generation of le formula has been mentioned in “Generateur CWIS” below.

## Generateur CWIS

### Tables

Le CWIS module uses le following tableau:

- data_source: stores avec information lies indicateurs, its donnees types et more.
- data_cwis: stores yearly information lies indicateurs et its value generated de le systeme or utilisateur input.

Le corresponding tableaux have their respective models ce are named in Pascal Case in singular form. Le desludging vehicles modules are located at app\\Models\\Cwis\\cwis_mne.php.

### Views

Tous views utilise by ce module is stocke in resources\\views\\cwis\\cwis-df-mne

- cwis-df-mne.create: opens form et calls partial-form pour form content.
- cwis-df-mne.index: lists existing records pour cwis indicateurs of chaque year.
- cwis-df-mne.partial-form: creates form content pour generation of nouveau cwis indicateur donnees pour nouveau year or edit existing cwis indicateur value.

### Models

Location: app\\Models\\Cwis\\cwis_mne.php

### Data Retrieval

- Controller: Le CwisMneController (located at app\\Http\\Controllers\\Cwis\\CwisMneController.php) initiates contient tous le functions ce are being called.
- Exports: App\\Exports\\MneCsvExport handles tous le exports processus of CWIS donnees.

CwisMneController follow CRUD operations, which usually have le same pattern. You can refer to le "CRUD de base" section above (2.2) pour more information. Exceptional classes are as follows:

| **Function**    | cwis()                                                                                                                                                                  |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Calls le postgresql function insert_data_into_cwis_table(\$year) ce handles le insert or generation processus of nouveau cwis donnees                                        |
| **Parametres**  | \$year                                                                                                                                                                  |
| **Return**      | json(\$result)                                                                                                                                                          |
| **Source**      | app\\Http\\Controllers\\Cwis\\CwisMneController.php                                                                                                                     |
| **Remarques**     | Le nouveau donnees is generated pour nouveau selected year avec le reference de data_source tableau et le donnees value are calculated de le indicateurs definition et formula. |

| **Function**    | exportMneCsv()                                                                                         |
| --------------------- | ------------------------------------------------------------------------------------------------------ |
| **Description** | Filters donnees pour selected year et calls le export class ce handles le export processus of cwis donnees |
| **Parametres**  | Request\$request                                                                                       |
| **Return**      | Downloaded File.                                                                                       |
| **Source**      | app\\Http\\Controllers\\Cwis\\CwisMneController.php                                                    |
| **Remarques**     | App\\Exports\\MneCsvExport                                                                             |

### Data Calculation
Le systeme revolves around calculating et managing donnees en utilisant 22 distinct CWIS indicateurs, chaque handled by its own function stocke in a GitHub depot pour version control et maintenance. Pour chaque year, le flux de travail begins by processing le donnees, avec chaque indicateur function performing its calculations independently. A key component of ce flux de travail is a master function ce categorizes chaque batiment as safely managed or not. Ce function is crucial as it is widely utilise by most indicateur functions to ensure accurate categorization before calculations proceed. When 'Add CWIS' button is clicked, le 22 indicateurs are fetched de lookup tableau 'data_sources',  le results are computed et finally stocke dans le principal tableau 'data_cwis' by le update query. Function 'insert_data_into_cwis_table(\$year)' handles le insert or generation processus of nouveau cwis donnees.


## KPI Dashboard

Le KPI dashboard incorporates charts (en utilisant Chart.js) et cards (en utilisant HTML et CSS) to visualize key performance indicateur donnees. Ce section delves dans le implementation of le bar chart.

Le generation of ces elements occurs only upon setting le respective targets pour le indicateurs within le kpi_targets tableau, as detailed in Section 7.4.

### Tables

KPI Dashboard is sous FSM module et uses le following tableau:

- kpi_target: retrieves le information of kpi targets.
- service_providers: retrieves information of service prestataires.
- quarters: retrieves information of quarters pour chaque year.

### Data Retrieval

- Data is fetched de le KpiDashboardController (located at app\\Http\\Controllers\\Fsm\\KpiDashboardController.php).
- A dedicated service class, located at app\\Services\\Fsm\\KpiDashboardService.php, exclusively contient le logic designed specifically pour generating charts.
- Laravel Eloquent et raw SQL queries retrieves donnees pour cards.
- Here, chaque indicateur is calculated based on a derived formula, which is further explained as

  - Efficacite de reponse aux demandes: A ratio of total containments emptied/total application received in le given time period.
  - Customer Satisfaction: A ratio of feedback avec le “FSM Service Quality” field marked as “Yes”/total number of submitted feedback.
  - PPE compliance: A ratio of feedback avec le “Sanitation workers wore PPE pendant desludging” field marked as “Yes”/total number of submitted feedback.
- Safe Desludging: A ratio of le total number of desludging recorded in traitement plant/ total number of containments emptied. (Assumption: 1 desludge is 1 containment)
- Inclusion: delivered services in LICs et Slums / total delivered services.
- Response Time: Average time between application et delivered service.
- Faecal Collecte des boues Ratio: Total amount of faecal sludge emptied de containments/ Total estimated sludge to be emptied in accessible areas.
- Le filtering systeme allows pour selecting a specific year et service prestataire. Upon choosing a year, cards are generated based on le selected year, et charts are generated by further breaking it down dans four quarters: Q1, Q2, Q3, et Q4. Detailed information pour ces quarters can be obtained de le quarters tableau.
- Clear code comments within le controller aid in understanding ce processus.

### Views

**Layout:** Le coeur dashboard structure is defined in le resources\\views\\fsm\\kpi-dashboard\\index.blade.php file. Ce file acts as le global layout et inclut placeholders pour le various components. It fetches donnees passed de le controller.

**Components:** Cards et charts are incorporated as separate components within le layout:

- Cards are located in resources\\views\\layouts\\dashborad\\key-performance-indicateur-card.
- Charts are located in resources\\views\\fsm\\kpi-dashboard\\KpiCharts.

## Objectif KPI

### Tables

Objectif KPI is sous CWIS IMS module et uses le following tableau:

kpi_targets: store le primary information of le KPI targets

key_performance_indicators: retrieves information of key performance indicateurs

Le corresponding tableaux have their respective models ce are named in Pascal Case in singular form. KpiTarget model is located at app\\Models\\Fsm\\.

### Views

Tous views utilise by ce module is stocke in resources\\views\\fsm\\kpi-target

kpi-target.index: lists KPI targets records.

kpi-target.create: opens form et calls partial-form pour form contents

kpi-target.partial-form: creates form content

kpi-target.edit: opens form et calls partial-form pour form contents

kpi-target.history: lists tous past edits of le record

kpi-target.show: displays tous attributes of particular record

### Models

Le models contain le connection between le model et le tableau defined by

*\$tableau = ‘fsm.kpi_targets’* as well as le primary key defined by primaryKey= ‘id’

### KpiTarget Model

Location: app\\Models\\Fsm\\kpiTarget.php

KpiTarget follows CRUD operations, which usually have le same pattern. You can refer to le "CRUD de base" Section **2 - Informations techniques/ CRUD de base** pour more information.

### KpiTargetRequest

Location: app\\Http\\Requests\\Fsm\\KpiTargetRequest.php)

KpiTargetRequest handles tous validation login. It handles validation logic as well as erreur messages to be displayed.

## Parametres CWIS

### Tables

Parametres CWIS is sous Settings module et uses le following tableau:

public.site_settings

Le corresponding tableaux have their respective models ce are named in Pascal Case in singular form. CwisSetting model is located at app\\Models\\Fsm\\.

Le CWIS setting sets le values pour variables ce are obligatoire pour le CWIS Dashboard.

### Views

Tous views utilise by ce module is stocke in resources\\views\\fsm\\cwis-setting

cwis-setting.index: opens cwis setting form.

### CwisSettingController

app\\Http\\Controllers\\Fsm\\CwisSettingController.php

Le controller’s principal function is to provide le connection between le calling route et its subsequent function written in le Service Class.

Le basic classes of le controller are:

|  **Function**   | \__construct()                                                         |
|-----------------|------------------------------------------------------------------------|
| **Description** | Initializes authentication, permissions et le service class instance |
| **Parametres**  | Service class instance(CwisSettingService)                             |
| **Return**      | null                                                                   |
| **Source**      | app\\Http\\Controllers\\Fsm\\CwisSettingController.php                 |

| **Function**    | index()                                                 |
|-----------------|---------------------------------------------------------|
| **Description** | Returns le index.blade.php page                        |
| **Parametres**  | null                                                    |
| **Return**      | fsm/cwis-setting.index compact('page_title', 'donnees')    |
| **Source**      | app\\Http\\Controllers\\Fsm\\CwisSettingController.php  |

| **Function**    | store()                                                         |
|-----------------|-----------------------------------------------------------------|
| **Description** | Store or update cwis setting donnees                               |
| **Parametres**  | Request \$request                                               |
| **Return**      | Redirection avec succes/failure message                        |
| **Source**      | app\\Http\\Controllers\\Fsm\\CwisSettingController.php          |
| **Remarques**     | cwissetting-\>storeOrUpdate(\$donnees) Service Class Function Name |

### CwisSettingService

Location: app\\Services\\Fsm\\CwisSettingService.php

Le Service Class contient tous le business logic. It contient tous le functions ce are being called in le CwisSettingController.php

|  **Function**   | storeOrUpdate()                                                |
|-----------------|----------------------------------------------------------------|
| **Description** | Handles le processus of edditing cwis parametres.                 |
| **Parametres**  | \$donnees                                                         |
| **Return**      | Success or erreur message, stores/updates donnees to cwis parametres |
| **Source**      | app\\Services\\Fsm\\CwisSettingService.php                     |
