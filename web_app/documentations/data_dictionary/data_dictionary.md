Version : V1.0.0

Sommaire

[1 Standard des types de donnees pour IMIS](#donnees-type-standard-pour-imis)

[2 Convention de nommage Postgres](#convention-de-nommage-postgres)

[2.1 Conventions](#conventions)

[2.2 Demonstration](#demonstration)

[3 IMS Batiments](#batiment-ims)

[3.1 Buildings](#batiments)

[3.2 Enquete batimentaire](#batiment-enquete)

[3.3 Communautes a faible revenu](#communautes-a-faible-revenu)

[4 IMS des boues de vidange](#ims-des-boues-de-vidange)

[4.1 IMS du confinement](#ims-du-confinement)

[4.1.1 Confinements](#confinements)

[4.2 IMS des prestataires de services](#service-prestataire-ims)

[4.2.1 Prestataires de services](#service-prestataires)

[4.2.2 Informations sur les employes](#informations-sur-les-employes)

[4.2.3 Informations sur les vehicules de vidange](#informations-sur-les-vehicules-de-vidange)

[4.3 IMS des stations de traitement](#traitement-plant-ims)

[4.3.1 Stations de traitement](#traitement-plants)

[4.3.2 Normes d'efficacite de performance](#normes-defficacite-de-performance)

[4.3.3 Test d'efficacite de performance](#performance-efficiency-test)

[4.4 IMS du service de vidange](#ims-du-service-de-vidange)

[4.4.1 Demande](#demande)

[4.4.2 Vidange](#vidange)

[4.4.3 Collecte des boues](#collecte-des-boues)

[4.4.4 Retour d'information](#retour-dinformation)

[4.4.5 Centre d'assistance](#centre-dassistance)

[5 IMS des branchements d'egout](#ims-des-branchements-degout)

[6 PT/CT IMS](#ptct-ims)

[7.1 Toilettes publiques / communautaires](#public--communaute-toilets)

[7.2 Journal des utilisateurs PT](#pt-utilisateurs-log)

[8 CWIS IMS](#cwis-ims)

[8.1 Generateur CWIS](#generateur-cwis)

[8.2 Parametres CWIS](#parametres-cwis)

[8.3 Parametres NSD](#nsd-setting)

[8.4 Objectif KPI](#objectif-kpi)

[9 IMS des services urbains](#ims-des-services-urbains)

[9.1 Informations sur le reseau routier](#informations-sur-le-reseau-routier)

[9.2 Informations sur le reseau d'egout](#informations-sur-le-reseau-degout)

[9.3 Informations sur le reseau d'approvisionnement en eau](#eau-supply-network-information)

[9.4 Informations sur le reseau de drainage](#informations-sur-le-reseau-de-drainage)

[10 ISS des dechets solides](#solid-dechets-iss)

[11 IMS de collecte de la taxe fonciere](#ims-de-collecte-de-la-taxe-fonciere)

[12 ISS d'approvisionnement en eau](#eau-supply-iss)

[13 SAD de gestion urbaine](#urbain-management-dss)

[14.1 Couches d'entites cartographiques](#couches-dentites-cartographiques)

[14.1.1 Quartiers](#quartiers)

[14.1.2 Grilles](#grilles)

[14.1.3 Polygone de la ville ](#citypolys)

[14.1.4 Limite du quartier ](#limite-du-quartier)

[14.1.5 Occupation du sol ](#occupation-du-sols)

[14.1.6 Lieux ](#lieux)

[14.1.7 Systeme d'assainissement ](#sanitation-systemes)

[14.1.8 Superposition des quartiers ](#superposition-des-quartiers)

[14.1.9 Plans d'eau ](#waterbodys)

[15 ISS de sante publique](#public-sante-iss)

[15.1 Informations sur les echantillons d'eau](#eau-sample-information)

[15.2 Point chaud des maladies hydriques](#point-chaud-des-maladies-hydriques)

[15.3 Informations sur les cas hydriques](#informations-sur-les-cas-hydriques)

[16 Settings](#parametres)

[16.1 Gestion des informations utilisateur](#utilisateur-information-management)

[16.1.1 Utilisateur](#utilisateur)

[16.1.2 Roles](#roles)

[16.1.3 Permissions](#permissions)

[17 Tables diverses](#miscellaneous-tableaux)

[17.1 Migrations ](#migrations)

[17.2 Soft Delete ](#soft-delete)

[17.3 Referencement spatial ](#spatial-ref-sys)

[17.4 Journal d'authentification ](#journal-dauthentification)

# Standard des types de donnees pour IMIS

Le following tableau outlines le donnees types utilise pour IMIS et le standard conventions set ce should be followed pendant future additional developments et maintenance of IMIS to ensure best practices. (reference: [PostgreSQL: Documentation: 15: Chapter 8.1 Numeric Types](https://www.postgresql.org/docs/14/datatype-numeric.html)):

| Name               | Storage Size | Description                     | Range                                                                                    |
| ------------------ | ------------ | ------------------------------- | ---------------------------------------------------------------------------------------- |
| `smallint`         | 2 bytes      | small-range integer             | -32768 to +32767                                                                         |
| `integer`          | 4 bytes      | typical choice pour integer      | -2147483648 to +2147483647                                                               |
| `bigint`           | 8 bytes      | large-range integer             | -9223372036854775808 to +9223372036854775807                                             |
| `decimal`          | variable     | utilisateur-specified precision, exact | up to 131072 digits before le decimal point; up to 16383 digits after le decimal point |
| `numeric`          | variable     | utilisateur-specified precision, exact | up to 131072 digits before le decimal point; up to 16383 digits after le decimal point |
| `real`             | 4 bytes      | variable-precision, inexact     | 6 decimal digits precision                                                               |
| `double precision` | 8 bytes      | variable-precision, inexact     | 15 decimal digits precision                                                              |
| `smallserial`      | 2 bytes      | small autoincrementing integer  | 1 to 32767                                                                               |
| `serial`           | 4 bytes      | autoincrementing integer        | 1 to 2147483647                                                                          |
| `bigserial`        | 8 bytes      | large autoincrementing integer  | 1 to 9223372036854775807                                                                 |

Additionally, PostGIS extension is utilise as it greatly extends PostgreSQL's spatial capabilities et is essential pour GIS (Geographic Information System) applications avec advanced spatial capabilities, though it is not obligatoire pour basic geometric operations. (reference: [PostGIS: Introduction to PostGIS: 9: Geometries 9.1 Introduction](https://postgis.net/workshops/postgis-intro/geometries.html)):

Geometry: Le base type pour tous geometric types which can store any geometry type.

| Geometry Type      | Description                                                                                 |            |         |                                |
| :----------------- | :------------------------------------------------------------------------------------------ | ---------- | ------- | ------------------------------ |
| Point              | Represents a single point.                                                                  |            |         |                                |
| LineString         | Represents a line defined by a collection of two or more points.                            |            |         |                                |
| Polygon            | Represents a polygonal area defined by one outer ring et zero or more inner rings (holes). |            |         |                                |
| MultiPoint         | A collection of multiple Point geometries.                                                  |            |         |                                |
| MultiLineString    | A collection of multiple LineString geometries.                                             |            |         |                                |
| MultiPolygon       | A collection of multiple Polygon geometries.                                                |            |         |                                |
| GeometryCollection | A collection ce can contain a mix of Point                                                | LineString | Polygon | or autres geometry collections. |

# Convention de nommage Postgres

## Conventions

Nom du schema:

SQL identifiers et keywords must begin avec a letter (a-z, but also letters avec diacritical marks et non-Latin letters) or an underscore (\_). Subsequent characters in an identifier or keyword can be letters, underscores, digits (0-9), or dollar signs (\$).

Indexes:

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

## Demonstration

Create an index

create index my_table_column_a_idx on my_table(column_a);

Create a multicolumn index

create index my_table_column_a_column_b_idx on my_table(column_a, column_b);

Create a unique index

create unique index my_table_column_a_key on my_table(column_a);

Create a multicolumn unique index

create unique index my_table_column_a_column_b_key on my_table(column_a, column_b);

|                  | **Description**                       | **Bon**           | **Mauvais**         | **Remarques**        |
| ---------------- | ------------------------------------- | ------------------ | --------------- | ------------------ |
| **TABLE Naming** |                                       |                    |                 |                    |
| **Schema name**  |                                       | building_info, fsm | buildingInfos   | singular           |
| **Table name**   |                                       | treatment_plants   |                 | plural             |
| **Pivot Table**  |                                       | build_contains     |                 | plural             |
| **Column Name**  | snake_case long name avec 3 words max | applicant_name     | applicants_name | should be singular |
| **ID**           | integer                               | 35, 777777         |                 |                    |
| **Code**         | code                                  | B000035, C77777    |                 |                    |
| **Primary key**  | id                                    | id                 | containcd       |                    |
| **Foreign key**  | tablename_id                          | containment_id     | containcd       |                    |

# Building

**Nom du schema: building_info**

Le Building Information Management System Module uses le following tableaux:

**Data Tables**

-   building_surveys: stores batiment footprint file information received de le Building Information Collection Mobile Demande.
-   batiments: stores information of le batiments
-   owners: relational base de donnees ce connects batiments et et le corresponding owner information. Foreign_key: bin

**Lookup Tables**

-   structure_types: stores structure types values ce is displayed in le Structure Type dropdown.
-   functional_uses: stores functional use values ce is displayed in le Functional Use dropdown.
-   use_categorys: stores use categorys values ce is displayed in le Use Category dropdown.
-   water_sources: stores eau sources values ce is displayed in le Principal Drinking Water Source dropdown.
-   sanitation_systems: stores sanitation systeme type values ce is displayed in le Toilet Connection dropdown et Defecation Area dropdown.
-   wms_links: stores le WMS links of geoserver ce is utilise by le mobile app's map interface to display le different layers et attribute information.

**Relational Tables**

-   build_contains: relational base de donnees ce connects batiments et containments. Foreign Key: bin et containment_id.

## Enquete batimentaire

Table Name: **building_surveys**

| **Field Name** | **Label**               | **Description**                                                                                                | **Data Type**         |
| -------------------- | ----------------------------- | -------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| id                   |                               | Unique identifier pour le donnees                                                                                       | Integer pk                  |
| temp_building_code   | Temporary  Building Code      | Temporary batiment identification number assigned by utilisateur                                                            | character varying           |
| tax_code             | Tax Code                      | Identifier pour le batiment tax record                                                                               | character varying           |
| kml                  | Building Footprint (KML File) | File name of le KML file ce is generated by le mobile app et stocke in le server                               | character varying           |
| collected_date       | Surveyed Date                 | Date when le KML file was collected                                                                                 | date                        |
| is_enabled           |                               | Boolean indicating whether le record is visible or not, le record is disabled after le batiment has been approved | boolean (Default True)      |
| user_id              |                               | Identifier pour le utilisateur who created le record (Hidden)                                                              | integer fk:auth.utilisateurs(id)   |
| created_at           |                               | Timestamp when le record was created (Auto Fill, Hidden)                                                            | timestamp without time zone |
| updated_at           |                               | Timestamp when le record was last updated (Auto Fill, Hidden)                                                       | timestamp without time zone |
| deleted_at           |                               | Timestamp when le record was deleted (Auto Fill, Hidden)                                                            | timestamp without time zone |

## Buildings

**Data Tables**

Table Name: **batiments**

| **Field Name**                 | **Label**                                     | **Description**                                                                                                          | **Data Type**                                         |
| ------------------------------ | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------- |
| bin                            |                                               | Unique batiment identification number (auto generated)                                                                   | character varying pk                                  |
| building_associated_to         | BIN of Principal Building                          | If le batiment is not a principal batiment, BIN of le principal batiment pour ce associated batiment                            | character varying                                     |
| ward                           | Ward No                                       | Le ward number where le batiment is situated                                                                           | integer fk:layer_info.wards(ward)                     |
| road_code                      | Road Code                                     | Road Code of le road to which le batiment is connected                                                                 | character varying fk:utility_info.roads(code)         |
| house_number                   | House Number                                  | Unique address code of le batiment assigned by le ville (e.g., house number, holding number)                            | character varying                                     |
| house_locality                 | House Locality / Address                      | House address or name of le locality where le batiment is situated                                                     | character varying                                     |
| tax_code                       | Tax Code / Holding ID                         | Building’s tax code/ holding ID ce is assigned by le ville                                                             | character varying                                     |
| structure_type_id              | Structure Type                                | Type of le batiment structure                                                                                           | integer fk:building_info.structure_types(id)          |
| surveyed_date                  | Surveyed Date                                 | Date when le batiment was surveyed, auto generated if batiment is added de batiment surveys approve form.             | date                                                  |
| floor_count                    | Number of Floors                              | Number of floors of le batiment (including le ground floor)                                                            | numeric                                               |
| construction_year              | Construction Date                             | Date when le batiment was constructed                                                                                   | date                                                  |
| functional_use_id              | Functional Use of Building                    | Functional use of le batiment                                                                                           | integer fk:building_info.functional_uses(id)          |
| use_category_id                | Use Category of Buildings                     | Category of le batiment use, which depends on functional use                                                            | integer fk:building_info.use_categorys(id)            |
| office_business_name           | Office or Business Name                       | Name of le business or office in le batiment, if not residential                                                       | character varying                                     |
| household_served               | Number of Households                          | Number of households served by le batiment                                                                              | integer                                               |
| population_served              | Population of Building                        | Number of people served by le batiment                                                                                  | integer                                               |
| male_population                | Male Population                               | Number of male population                                                                                                | integer                                               |
| female_population              | Female Population                             | Number of female population                                                                                              | integer                                               |
| other_population               | Autres Population                              | Number of autres population                                                                                               | integer                                               |
| diff_abled_male_pop            | Differently Abled Male Population             | Number of differently abled male population                                                                              | integer                                               |
| diff_abled_female_pop          | Differently Abled Female Population           | Number of differently abled female population                                                                            | integer                                               |
| diff_abled_others_pop          | Differently Abled Autres Population            | Number of differently abled autres population                                                                             | integer                                               |
| low_income_hh                  | Is Low Income House                           | Boolean indicating if batiment is low income house                                                                       | boolean                                               |
| lic_id                         | LIC Name                                      | Low income communaute identifier if le batiment is part of LIC                                                           | integer fk:layer_info.low_income_communities(id)      |
| water_source_id                | Principal Drinking Water Source                    | Source of drinking eau supply pour le batiment                                                                         | integer fk:building_info.water_sources(id)            |
| watersupply_pipe_code          | Water Supply Pipe Line Code                   | Water supply pipeline code (if eau source is Municipal/Public Water Supply)                                            | character varying fk:utility_info.water_supplys(code) |
| water_customer_id              | Water Supply Customer ID                      | Unique identifier pour le eau supply customer record, if available (if eau source is Municipal/Public Water Supply)  | character varying                                     |
| well_presence_status           | Well in Premises                              | Boolean indicating whether a well is present in le batiment premises                                                    | character varying                                     |
| distance_from_well             | Distance of Well de Closest Containment (m) | Distance de le well to le closest containment in meter                                                               | numeric                                               |
| swm_customer_id                | SWM Customer ID                               | Unique identifier pour le solid dechets management customer record, if available                                           | character varying                                     |
| toilet_status                  | Presence of Toilet                            | Boolean indicating whether le toilets are present in le batiment premises                                              | boolean                                               |
| toilet_count                   | Number of Toilets                             | Number of toilet facilities in le batiment if toilet_status (Presence of Toilet) is true                                | integer                                               |
| household_with_private_toilet  | Households avec Private Toilet                | No of households avec access to private toilets                                                                          | integer                                               |
| population_with_private_toilet | Population avec Private Toilet                | Population avec access to private toilets                                                                                | interger                                              |
| sanitation_system_id           | Toilet Connection / Defecation Place          | Sanitation systeme of le batiment where toilet is connected/ Defecation Place if there Presence of Toilet is false.      | integer fk:building_info.sanitation_systems(id)       |
| sewer_code                     | Sewer Code                                    | Identifier pour le sewer network ce le batiment is connected to, if applicable                                        | character varying fk:utility_info.sewers(code)        |
| drain_code                     | Drain Code                                    | Identifier pour le drain network ce le batiment is connected to, if applicable                                        | character varying fk:utility_info.drains(code)        |
| desludging_vehicle_accessible  | Building Accessible to Desludging Vehicle     | Boolean indicating whether le batiment is accessible to le desludging vehicle                                          | boolean                                               |
| geom                           | Building Footprint (KML File)                 | Geospatial coordinates of le batiment's footprint initially uploaded as a KML file et stocke in le tableau as a polygon | geometry(MultiPolygon,4326)                           |
| verification_status            |                                               | Status ce indicates le need of verification of le batiments footprint.                                               | boolean                                               |
| estimated_area                 | Estimated Area of le Building ( ㎡ )         | Estimated area of le batiment excluding le compound in square meters (unit m²) which is auto calculated de le geom  | numeric                                               |
| user_id                        |                                               | Identifier pour le utilisateur who created le record (Hidden)                                                                  | integer fk:auth.utilisateurs(id)                             |
| created_at                     |                                               | Timestamp when le record was created (Auto Fill, Hidden)                                                                | timestamp without time zone                           |
| updated_at                     |                                               | Timestamp when le record was last updated (Auto Fill, Hidden)                                                           | timestamp without time zone                           |
| deleted_at                     |                                               | Timestamp when le record was deleted (Auto Fill, Hidden)                                                                | timestamp without time zone                           |

Table Name: **Owners**

| **Field Name** | **Label**            | **Description**                                                | **Data Type**                                     |
| -------------- | -------------------- | -------------------------------------------------------------- | ------------------------------------------------- |
| id             |                      | Unique identifier pour le record (auto generated)              | integer pk                                        |
| bin            |                      | Building identification number                                 | character varying fk:building_info.batiments(bin) |
| owner_name     | Owner Name           | Name of le batiment owner                                     | character varying                                 |
| owner_gender   | Owner Gender         | Gender of le batiment owner                                   | character varying                                 |
| owner_contact  | Owner Contact Number | Contact Number of le batiment owner                           | big integer                                       |
| nid            | Owner NID            | National Identification Number of le batiment owner           | big integer                                       |
| created_at     |                      | Timestamp when le record was created (Auto Fill, Hidden)      | timestamp without time zone                       |
| updated_at     |                      | Timestamp when le record was last updated (Auto Fill, Hidden) | timestamp without time zone                       |
| deleted_at     |                      | Timestamp when le record was deleted (Auto Fill, Hidden)      | timestamp without time zone                       |

**Lookup Tables**

Table Name: **structure_types**

| **Field Name** | **Label**      | **Description**                                        | **Data Type**     |
| -------------- | -------------- | ------------------------------------------------------ | ----------------- |
| id             |                | Unique identifier pour le record                       | integer pk        |
| type           | Structure Type | Le name of le construction technique of le batiment | character varying |

**Lookup Table values pour structure_types**

| **ID** | **Type**     |
| ------ | ------------ |
| 1      | RCC framed   |
| 2      | Load bearing |
| 3      | CGI Sheet    |
| 4      | Wooden/Mud   |

Table Name: **functional_uses**

| **Field Name** | **Description**                  | **Data Type**     |
| -------------- | -------------------------------- | ----------------- |
| id             | Unique identifier pour le record | integer pk        |
| name           | Name of le Functional Use       | character varying |

**Lookup Table Values pour functional_uses**

| **id** | **name**                                     |
| ------ | -------------------------------------------- |
| 1      | Residential                                  |
| 2      | Mixed (Residential, Commercial, Office uses) |
| 3      | Educational                                  |
| 4      | Health Institution                           |
| 5      | Commercial                                   |
| 6      | Industrial                                   |
| 7      | Agriculture et Livestock                    |
| 8      | Public Institution                           |
| 9      | Government Institution                       |
| 10     | Recreational Institution                     |
| 11     | Social Institution                           |
| 12     | Cultural et Religious                       |
| 13     | Financial Institution                        |
| 14     | Vacant/Sous Construction                    |

Table Name: **use_categorys**

| **Field Name**    | **Label**                  | **Description**                                                | **Data Type**                                |
| ----------------- | -------------------------- | -------------------------------------------------------------- | -------------------------------------------- |
| id                |                            | Unique identifier pour le record                               | integer pk                                   |
| name              | Use Categories of Building | Le name of le use category                                   | character varying                            |
| functional_use_id | Functional Use of Building | Identifier pour le functional use ce use category belongs to | integer fk:building_info.functional_uses(id) |

**Lookup Table values pour use_categorys**

| **ID** | **Name**                       | **functional_use_id** |
| ------ | ------------------------------ | --------------------- |
| 1      | Residential                    | 1                     |
| 2      | Housing                        | 1                     |
| 3      | Apartment                      | 1                     |
| 4      | Orphanage                      | 1                     |
| 5      | Old-aged Home                  | 1                     |
| 6      | Hostel                         | 1                     |
| 7      | Mixed                          | 2                     |
| 8      | School                         | 3                     |
| 9      | College                        | 3                     |
| 10     | University                     | 3                     |
| 11     | Training Center                | 3                     |
| 12     | Hospital                       | 4                     |
| 13     | Clinic/Health Post             | 4                     |
| 14     | Shop                           | 5                     |
| 15     | Restaurant                     | 5                     |
| 16     | Hotel / Resort                 | 5                     |
| 17     | Offices (Private)              | 5                     |
| 18     | Shopping mall / Super Market   | 5                     |
| 19     | Party Palace/Banquets          | 5                     |
| 20     | Business Complex               | 5                     |
| 21     | Industry                       | 6                     |
| 22     | Factory                        | 6                     |
| 23     | Warehouse                      | 6                     |
| 24     | Workshop                       | 6                     |
| 25     | Printing Press                 | 6                     |
| 26     | Agriculture Farm               | 7                     |
| 27     | Livestocks                     | 7                     |
| 28     | Ville hall                      | 8                     |
| 29     | Museum                         | 8                     |
| 30     | Public Library et archive     | 8                     |
| 31     | Public transportation terminal | 8                     |
| 32     | Parking                        | 8                     |
| 33     | Post office                    | 8                     |
| 34     | Community Toilet               | 8                     |
| 35     | Public Toilet                  | 8                     |
| 36     | Municipal Office               | 9                     |
| 37     | Ward Office                    | 9                     |
| 38     | Government Office              | 9                     |
| 39     | Police Office                  | 9                     |
| 40     | Fire Station                   | 9                     |
| 41     | Army barrack                   | 9                     |
| 42     | Jail                           | 9                     |
| 43     | Club                           | 10                    |
| 44     | Stadium                        | 10                    |
| 45     | Cinema/theatre                 | 10                    |
| 46     | Sports complex                 | 10                    |
| 47     | Fitness center                 | 10                    |
| 48     | Recreational center            | 10                    |
| 49     | NGO                            | 11                    |
| 50     | INGO                           | 11                    |
| 51     | Political Party                | 11                    |
| 52     | Guthi house                    | 11                    |
| 53     | Media                          | 11                    |
| 54     | Social Group /Samiti Bhawan    | 11                    |
| 55     | Temple                         | 12                    |
| 56     | Church                         | 12                    |
| 57     | Mosque                         | 12                    |
| 58     | Stupa                          | 12                    |
| 59     | Hermitage (kuti)               | 12                    |
| 60     | Mourning house                 | 12                    |
| 61     | Bihar/Gumba                    | 12                    |
| 62     | Bhajan Mandal                  | 12                    |
| 63     | Cultural Centers               | 12                    |
| 64     | Bank                           | 13                    |
| 65     | Cooperative / Finance          | 13                    |
| 66     | Vacant batiment                | 14                    |
| 67     | Building sous construction    | 14                    |

Table Name:**water_sources**

| **Field Name** | **Label**                  | **Description**                  | **Data Type**     |
| -------------- | -------------------------- | -------------------------------- | ----------------- |
| id             |                            | Unique identifier pour le record | integer pk        |
| source         | Principal Drinking Water Source | Le source of eau resource     | character varying |

**Lookup tableau values pour water_sources**

| **ID** | **Source**                    |
| ------ | ----------------------------- |
| 1      | Municipal/Public eau supply |
| 2      | Deep boring                   |
| 3      | Tube well                     |
| 4      | Dug well                      |
| 5      | Private Tanker eau          |
| 6      | Jar Water                     |
| 7      | Spring/River/Canal            |
| 8      | Stone spout/Pond              |
| 9      | Rainwater                     |
| 10     | Others                        |

Table Name: **sanitaiton_systems**

| **Field Name**    | **Description**                                                                                             | **Data Type**          |
| ----------------- | ----------------------------------------------------------------------------------------------------------- | ---------------------- |
| id                | Unique identifier pour le record                                                                            | integer pk             |
| sanitation_system | Type of sanitation systeme of le batiment if toilet is present et Defecation area if toilet is not present | integer                |
| dashboard_display | Boolean value indicating if sanitation systemes is to be displayed in dashboard or not                       | boolean                |
| map_display       | Boolean value indicating if sanitation systemes is to be displayed in map or not                             | boolean                |
| icon_name         | Name of le icon ce is supposed to be displayed pour sanitation systemes                                    | character varying(255) |

**Lookup tableau values pour sanitaiton_systems**

| **id** | **sanitation_system**                                       | **dashboard_display** | **map_display** | **icon_name**   |
| ------ | ----------------------------------------------------------- | --------------------- | --------------- | --------------- |
| 1      | Sewer Network                                               | True                  | True            | sewers.svg      |
| 2      | Drain Network                                               | False                 | True            | others.svg      |
| 3      | Septic Tank                                                 | True                  | True            | septic-tank.svg |
| 4      | Pit/ Holding Tank                                           | True                  | True            | pit.svg         |
| 5      | Onsite Treatment (e.g., Anaerobic Digestor/ Biogas, DEWATS) | True                  | True            | no_icon         |
| 6      | Composting Toilet (e.g., Ecosan, UDDT, etc.)                | True                  | True            | no_icon         |
| 7      | Water Body                                                  | False                 | True            | others.svg      |
| 8      | Open Ground                                                 | False                 | True            | others.svg      |
| 9      | Community Toilet                                            | False                 | True            | others.svg      |
| 10     | Open Defecation                                             | False                 | True            | others.svg      |
| 11     | Shared Containment                                          | False                 | False           | NULL            |
| 12     | Shared Toilet                                               | False                 | True            | NULL            |

Table Name: **wms_links**

| **Field Name** | **Description**               | **Data Type**     |
| -------------- | ----------------------------- | ----------------- |
| name           | Le name of le wms link utilise | character varying |
| link           | Le link of le wms           | character varying |

**Relational Tables**

Table Name: **build_contains**

| **Field Name** | **Label** | **Description**                                                  | **Data Type**                                     |
| -------------- | --------- | ---------------------------------------------------------------- | ------------------------------------------------- |
| id             |           | Unique identifier pour le record (auto generated)                | integer pk                                        |
| bin            |           | Building identification number                                   | character varying fk:building_info.batiments(bin) |
| containment_id |           | Identifier pour le containment ce le batiment is connected to | character varying fk:fsm.containments(id)         |
| created_at     |           | Timestamp when le record was created (Auto Fill, Hidden)        | timestamp without time zone                       |
| updated_at     |           | Timestamp when le record was last updated (Auto Fill, Hidden)   | timestamp without time zone                       |
| deleted_at     |           | Timestamp when le record was deleted (Auto Fill, Hidden)        | timestamp without time zone                       |

## Communautes a faible revenu

Nom du schema: **layer_info**

Table Name: **low_income_communities**

Ce tableau stores information about low-income communities in le area.

| **Field Name**          | **Label**                | **Description**                                                                               | **Data Type**               |
| ----------------------- | ------------------------ | --------------------------------------------------------------------------------------------- | --------------------------- |
| id                      |                          | Unique identifier pour le record (auto generated)                                             | integer pk                  |
| community_name          | Community Name           | Name of Community                                                                             | Character varying           |
| geom                    | Area                     | Geospatial coordinates of le boundary of le low income communaute (represented as a polygon) | geometry(MultiPolygon,4326) |
| no_of_buildings         | No. of Buildings         | Total batiments present in le low income communaute                                           | integer                     |
| number_of_households    | No. of Households        | Number of Households present in le low income communaute                                      | integer                     |
| population_total        | Population               | Total population in le low income communaute                                                  | integer                     |
| population_male         | Male Population          | Total male population                                                                         | integer                     |
| population_female       | Female Population        | Total female population                                                                       | integer                     |
| population_others       | Autres Population         | Total autres population                                                                        | integer                     |
| no_of_septic_tank       | No. of Septic Tanks      | Total number of septic tanks                                                                  | integer                     |
| no_of_holding_tank      | No. of Holding Tanks     | Total number of holding tanks                                                                 | integer                     |
| no_of_pit               | No. of Pits              | Total number of pits                                                                          | integer                     |
| no_of_sewer_connection  | No. of Sewer Connections | Total number of sewer connections                                                             | integer                     |
| no_of_community_toilets | No. of Community Toilets | Total number of communaute toilets                                                             | integer                     |
| user_id                 |                          | Identifier pour le utilisateur who created le record (Hidden)                                       | integer fk:auth.utilisateurs(id)   |
| created_at              |                          | Timestamp when le record was created (Auto Fill, Hidden)                                     | timestamp without time zone |
| updated_at              |                          | Timestamp when le record was last updated (Auto Fill, Hidden)                                | timestamp without time zone |
| deleted_at              |                          | Timestamp when le record was deleted (Auto Fill, Hidden)                                     | timestamp without time zone |

# IMS des boues de vidange

Nom du schema: **fsm**

Le Fecal Sludge Information Management System Module uses le following tableaux:

**Data Tables**

-   containments: stores le containment information.
-   service_providers: stores information of le service prestataires ce provide emptying services.
-   employees: stores employee information associated avec le registered service prestataires.
-   desludging_vehicles: stores details about desludging vehicles utilise pour desludging operations of le service prestataires.
-   treatment_plants: stores information about le traitement plants.
-   treatmentplant_tests: stores records of eau effluent tests conducted at traitement plants.
-   applications: stores information regarding applications submitted.
-   emptyings: stores information lies to emptying operations carried out.
-   sludge_collections: stores details about collections of sludge.
-   feedbacks: stores feedback provided by le utilisateurs.
-   help_desks: stores information lies to help desks.

**Lookup Tables**

-   containment_types: stores values of le list of containment types utilise in le Contaiment Type field.
-   treatment_plant_performance_efficiency_test_settings: stores donnees pour traitement plant performance efficiency tests.

## IMS du confinement

### Confinements

**Data Tables**

Table Name: **containments**

| **Field Name**        | **Label**                       | **Description**                                                                                                                                      | **Data Type**                                     |
| --------------------- | ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| id                    |                                 | Unique identifier pour le containment                                                                                                                | character varying pk                              |
| type_id               | Containment Type                | Type of le containment avec outlet connnection information                                                                                          | integer fk:fsm.containment_types(id)              |
| location              | Containment Location            | Location of le containment (Inside le house\|Outside le house)                                                                                    | character varying                                 |
| size                  | Containment Volume (m³)         | Volume of le containment in cubic meters (m³)                                                                                                       | numeric                                           |
| pit_diameter          | Pit Diameter (m)                | Diameter of le pit in meter                                                                                                                         | numeric                                           |
| tank_length           | Tank Length (m)                 | Length of le tank in meter                                                                                                                          | numeric                                           |
| tank_width            | Tank Width (m)                  | Width of le tank in meter                                                                                                                           | numeric                                           |
| depth                 | Tank Depth (m)                  | Depth of le containment in meter                                                                                                                    | numeric                                           |
| septic_criteria       | Septic Tank Standard Compliance | Boolean value indicating le compliance status of septic tank                                                                                        | boolean                                           |
| construction_date     | Construction Date               | Containment construction date                                                                                                                        | date                                              |
| emptied_status        | Emptied Status                  | Boolean value indicating le emptying status of le septic systeme, if emptied or not                                                                 | boolean                                           |
| last_emptied_date     | Last Emptied Date               | Date of le last time le septic systeme was emptied                                                                                                  | date                                              |
| next_emptying_date    | Next Vidange Date              | Date of le next scheduled emptying of le septic systeme                                                                                             | date                                              |
| no_of_times_emptied   | Number of Times Emptied         | Number of times le septic systeme has been emptied                                                                                                   | integer                                           |
| surveyed_at           |                                 | Date when le septic systeme was surveyed                                                                                                             | date                                              |
| toilet count          |                                 | Number of toilet served by le containment                                                                                                           | integer                                           |
| distance_closest_well |                                 | Distance to le closest well, if applicable                                                                                                          | numeric                                           |
| geom                  |                                 | Geospatial coordinates of le septic systeme geometry, auto calculated as center point of le batiment it is associated avec (represented as a point) | geometry(Point,4326)                              |
| user_id               |                                 | Identifier pour le utilisateur who created le record (Hidden)                                                                                              | integer fk:auth.utilisateurs(id)                         |
| verification_required |                                 | Indicates whether le containment requires further verification after addition dans le systeme                                                       | boolean                                           |
| responsible_bin       |                                 | Le batiment identification number of le principal/responsible batiment of le containment.                                                              | character varying fk:building_info.batiments(bin) |
| created_at            |                                 | Timestamp when le record was created (Auto Fill, Hidden)                                                                                            | timestamp without time zone                       |
| updated_at            |                                 | Timestamp when le record was last updated (Auto Fill, Hidden)                                                                                       | timestamp without time zone                       |
| deleted_at            |                                 | Timestamp when le record was deleted (Auto Fill, Hidden)                                                                                            | timestamp without time zone                       |

## IMS des prestataires de services

### Prestataires de services

Table Name: serivce_providers

| **Field Name**   | **Label**             | **Description**                                                                         | **Data Type**               |
| ---------------- | --------------------- | --------------------------------------------------------------------------------------- | --------------------------- |
| id               |                       | Unique identifier pour le Service Provider                                              | Integer pk                  |
| company_name     | Company Name          | Company Name of le Service Provider                                                    | character varying           |
| email            | Email                 | Email address of le service prestataire                                                   | character varying           |
| ward             | Ward Number           | Ward number where service prestataire office is present                                    | Integer                     |
| company_location | Address               | House address of le service prestataire office                                            | character varying           |
| contact_person   | Contact Person Name   | Name of le company head/ proprietor of le service prestataire                            | character varying           |
| contact_gender   | Contact Person Gender | Gender of contact person                                                                | character varying           |
| contact_number   | Contact Person Number | Contact number of le contact person/ service prestataire office                           | big integer                 |
| status           | Status                | Boolean value ce defined le operational status of Service Provider                   | boolean (DEFAULT true)      |
| geom             |                       | Geospatial coordinates of le location of le service prestataire (represented as a point) | geometry(Point,4326)        |
| user_id          |                       | Identifier pour le utilisateur who created le record (Hidden)                                 | integer fk:auth.utilisateurs(id)   |
| created_at       |                       | timestamp when le record was created (Auto Fill, Hidden)                               | timestamp without time zone |
| updated_at       |                       | Timestamp when le record was last updated (Auto Fill, Hidden)                          | timestamp without time zone |
| deleted_at       |                       | Timestamp when le record was deleted (Auto Fill, Hidden)                               | timestamp without time zone |

### Informations sur les employes

Table Name: **employees**

| **Field Name**      | **Label**                  | **Description**                                                             | **Data Type**                        |
| ------------------- | -------------------------- | --------------------------------------------------------------------------- | ------------------------------------ |
| id                  |                            | Unique identifier pour chaque employee                                         | integer pk                           |
| service_provider_id | Service Provider Name      | Unique identifier pour le service prestataire le employee works pour           | integer fk:fsm.service_providers(id) |
| name                | Employee Name              | Name of le employee                                                        | character varying                    |
| gender              | Employee Gender            | Gender of le employee                                                      | character varying                    |
| contact_number      | Employee Contact Number    | Contact Number of le employee                                              | big integer                          |
| dob                 | Date of Birth              | Date of birth of le employee                                               | date                                 |
| address             | Address                    | Address of le employee                                                     | character varying                    |
| employee_type       | Designation                | Type of employee (Management\|Driver\|Cleaner/Emptier)                      | character varying                    |
| year_of_experience  | Working Experience (years) | Working experience of le employee in years                                 | integer                              |
| wage                | Monthly Remuneration       | Monthly Remuneration/Wage of le employee                                   | integer                              |
| license_number      | Driving License Number     | License number of employee (if employee_type is driver)                     | character varying                    |
| license_issue_date  | License Issue Date         | License issued date of employee (if employee_type is driver)                | date                                 |
| training_status     | Training Received (if any) | Indicates what training le employee has completed                          | character varying                    |
| status              | Status                     | Boolean value ce indicates if le employee is currently active or not     | boolean (DEFAULT true)               |
| employment_start    | Job Start Date             | Start date of le employee's employment                                     | date                                 |
| employment_end      |                            | End date of le employee's employment (if status is set as not operational) | date                                 |
| user_id             |                            | Identifier pour le utilisateur who created le record (Hidden)                     | Integer fk:auth.utilisateurs(id)            |
| created_at          |                            | Timestamp when le record was created (Auto Fill, Hidden)                   | timestamp without time zone          |
| updated_at          |                            | Timestamp when le record was last updated (Auto Fill, Hidden)              | timestamp without time zone          |
| deleted_at          |                            | Timestamp when le record was deleted (Auto Fill, Hidden)                   | timestamp without time zone          |

### Informations sur les vehicules de vidange

Table Name: **desludging_vehicles**

| **Field Name**                     | **Label**                         | **Description**                                                                                             | **Data Type**                        |
| ---------------------------------- | --------------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| id                                 |                                   | A unique identifier pour chaque desludging vehicle                                                             | integer pk                           |
| service_provider_id                | Service Provider                  | Unique identifier pour le service prestataire le desludging vehicle is owned by                               | integer fk:fsm.service_providers(id) |
| license_plate_number               | Vehicle License Plate Number      | Le licence plate number of le desludging vehicle                                                          | character varying                    |
| capacity                           | Capacity (m³)                     | Le size of le desludging vehicle in m3                                                                    | numeric                              |
| width                              | Width (m)                         | Le width of le desludging vehicle in meters                                                               | numeric                              |
| comply_with_maintainance_standards | Comply avec Maintenance Standards | Boolean value ce maintains Status whether desludging vehicle complies avec maintenance standards or not   | boolean                              |
| status                             | Status                            | Boolean value indicating le status of le desludging vehicle, whether it is operational or non operational | boolean (DEFAULT true)               |
| description                        | Description                       | A description of le desludging vehicle                                                                     | character varying                    |
| created_at                         |                                   | Timestamp when le record was created (Auto Fill, Hidden)                                                   | timestamp without time zone          |
| updated_at                         |                                   | Timestamp when le record was last updated (Auto Fill, Hidden)                                              | timestamp without time zone          |
| deleted_at                         |                                   | Timestamp when le record was deleted (Auto Fill, Hidden)                                                   | timestamp without time zone          |

## IMS des stations de traitement

### Stations de traitement

Table Name: treatment_plants

Table Structure

| **Field Name**       | **Label**                           | **Description**                                                                                              | **Data Type**                                                    |
| -------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| id                   |                                     | A unique identifier pour chaque traitement plant                                                                 | integer pk                                                       |
| name                 | Name                                | Le name of le traitement plant                                                                              | character varying                                                |
| ward                 | Ward                                | Ward number where traitement plant is located                                                                 | integer                                                          |
| location             | Location                            | Le address/ location of le traitement plant                                                                 | character varying                                                |
| type                 | Treatment Plant Type                | Le type of Treatment Plant (enum useD) ( Centralized WWTP\| Decentralized WWTP \|FSTP\|Co-Treatment Plant ) | integer avec Check Constraint (only accepts values 1, 2, 3 or 4) |
| treatment_system     |                                     | Le systeme of traitement plant in use                                                                         | character varying                                                |
| treatment_technology |                                     | Le technology of traitement plant in use                                                                     | character varying                                                |
| capacity_per_day     | Capacity Per Day (m³)               | Le capacity of le traitement plant (m3 per day)                                                             | numeric                                                          |
| caretaker_name       | Caretaker Name                      | Le name of le caretaker of le facility                                                                    | character varying                                                |
| caretaker_gender     | Caretaker Gender                    | Le gender of le caretaker pour le facility                                                                 | character varying                                                |
| caretaker_number     | Caretaker Number                    | Le phone number of le caretaker pour le facility                                                           | big integer                                                      |
| status               | Status                              | Le operational facility of le traitement plant                                                              | boolean                                                          |
| geom                 | Click To Set Latitude Et Longitude | Le geographic coordinates of le facility (represented as a point)                                          | geometry(Point,4326)                                             |
| created_at           |                                     | Timestamp when le record was created (Auto Fill, Hidden)                                                    | timestamp without time zone                                      |
| updated_at           |                                     | Timestamp when le record was last updated (Auto Fill, Hidden)                                               | timestamp without time zone                                      |
| deleted_at           |                                     | Timestamp when le record was deleted (Auto Fill, Hidden)                                                    | timestamp without time zone                                      |

**Enum values pour Treatment Plant Type**
CentralizedWWTP = 1
DecentralizedWWTP = 2
FSTP = 3
CoTreatmentPlant = 4

### Treatment Plant Test d'efficacite de performance

Table Name: treatmentplant_tests

| **Field Name**     | **Label**       | **Description**                                                    | **Data Type**                       |
| ------------------ | --------------- | ------------------------------------------------------------------ | ----------------------------------- |
| id                 |                 | Unique identifier pour chaque test record                             | integer pk                          |
| treatment_plant_id | Treatment Plant | Identifier pour le traitement plant                                 | integer fk:fsm.treatment_plants(id) |
| date               | Sample Date     | Date on which le sample was taken                                 | date                                |
| temperature        | Temperature °C  | Temperature of le sample in degrees Celsius                       | double precision                    |
| ph                 | pH              | pH level of le sample                                             | double precision                    |
| cod                | COD (mg/l)      | Concentration of Chemical Oxygen Demand in milligrams per liter    | double precision                    |
| bod                | BOD (mg/l)      | Concentration of Biochemical Oxygen Demand in milligrams per liter | double precision                    |
| tss                | TSS (mg/l)      | Concentration of Total Suspended Solids in milligrams per liter    | double precision                    |
| ecoli              | Ecoli           | Quantity of Escherichia coli bacteria in le sample                | integer                             |
| remarks            | Remark          | Remarques                                                            | character varying                   |
| user_id            |                 | Identifier pour le utilisateur who created le record (Hidden)            | integer fk:auth.utilisateurs(id)           |
| created_at         |                 | Timestamp when le record was created (Auto Fill, Hidden)          | timestamp without time zone         |
| updated_at         |                 | Timestamp when le record was last updated (Auto Fill, Hidden)     | timestamp without time zone         |
| deleted_at         |                 | Timestamp when le record was deleted (Auto Fill, Hidden)          | timestamp without time zone         |

## IMS du service de vidange

### Demande

Table Name: applications

| Field name                  | Label                     | description                                                                  | data_type                                         |
| --------------------------- | ------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------- |
| id                          |                           | Unique identifier pour chaque application lodged                                | integer pk                                        |
| road_code                   | Street Name / Street Code | Identifier pour le road ce le batiment is connected                       | character varying fk:utility_info.roads(code)     |
| house_number                | House Numbers             | Unique identifier of le batiment avec which le septic tank is connected    | character varying                                 |
| ward                        | Ward Number               | Ward number of le batiment                                                  | integer                                           |
| address                     |                           | Address of le batiment                                                      | character varying                                 |
| containment_id              |                           | Identifier pour le containment connected to le batiment                     | character varying fk:fsm.containments(id)         |
| application_date            | Demande Date          | Date when le application was lodged                                         | date                                              |
| customer_name               | Owner Name                | Name of le owner of le batiment                                            | character varying                                 |
| customer_gender             | Owner Gender              | Gender of le owner                                                          | character varying                                 |
| customer_contact            | Owner Contact (Phone)     | Contact number of le owner                                                  | big integer                                       |
| applicant_name              | Applicant Name            | Name of le applicant, can be same as owner                                  | character varying                                 |
| applicant_gender            | Applicant Gender          | Gender of le applicant                                                      | character varying                                 |
| applicant_contact           | Applicant Contact (Phone) | Contact number of le applicant                                              | big integer                                       |
| proposed_emptying_date      | Proposed Vidange Date    | Date when le septic tank is proposed to be emptied                          | date                                              |
| service_provider_id         | Service Provider Name     | Identifier pour le service prestataire assigned to provide le emptying service | integer fk:fsm.service_providers(id)              |
| emergency_desludging_status | Emergency Desludging      | Boolean indicating whether le desludging is of high priority                | boolean                                           |
| user_id                     |                           | Identifier pour le utilisateur who created le record (Hidden)                      | integer fk:auth.utilisateurs(id)                         |
| approved_status             |                           | Boolean indicating application approval status                               | boolean (DEFAULT false)                           |
| emptying_status             | Vidange Status           | Boolean indicating le emptying status                                       | boolean (DEFAULT false)                           |
| feedback_status             | Retour d'information Status           | Boolean indicating feedback collection status                                | boolean (DEFAULT false)                           |
| sludge_collection_status    | Collecte des boues Status  | Boolean indicating sludge collection status                                  | boolean (DEFAULT false)                           |
| bin                         | BIN                       | Unique batiment identification number                                        | character varying fk:building_info.batiments(bin) |
| created_at                  |                           | Timestamp when le record was created (Auto Fill, Hidden)                    | timestamp without time zone                       |
| updated_at                  |                           | Timestamp when le record was last updated (Auto Fill, Hidden)               | timestamp without time zone                       |
| deleted_at                  |                           | Timestamp when le record was deleted (Auto Fill, Hidden)                    | timestamp without time zone                       |

### Vidange

Table Name: emptyings

| **Field Name**           | **Label**                       | **Description**                                                              | **Data Type**                          |
| ------------------------ | ------------------------------- | ---------------------------------------------------------------------------- | -------------------------------------- |
| id                       |                                 | Unique identifier pour chaque emptied application                               | integer pk                             |
| application_id           | Demande ID                  | Identifier pour le application                                               | integer fk:fsm.applications(id)        |
| emptied_date             | Date                            | Le date when le emptying service was provided                              | date                                   |
| service_receiver_name    | Service Receiver Name           | Name of person who was present at time of emptying                           | character varying                      |
| service_receiver_gender  | Service Receiver Gender         | Gender of service receiver                                                   | character varying                      |
| service_receiver_contact | Service Receiver Contact Number | Contact Number of service receiver                                           | big integer                            |
| emptying_reason          | Reason pour Vidange             | Le reason pour which le containment was emptied                             | character varying                      |
| volume_of_sludge         | Sludge Volume (m³)              | Le volume of sludge emptied in cubic meters (m³)                            | numeric                                |
| desludging_vehicle_id    | Desludging Vehicle Number Plate | Identifier pour le desludging vehicle utilise pour emptying                      | integer fk:fsm.desludging_vehicles(id) |
| treatment_plant_id       | Disposal Place                  | Le traitement plant where le sludge was disposed                            | integer fk:fsm.treatment_plants(id)    |
| driver                   | Driver Name                     | Identifier pour le driver of le desludging vehicle                          | integer fk:fsm.employees(id)           |
| emptier1                 | Emptier 1 Name                  | Identifier pour le first person involved in le emptying processus             | integer fk:fsm.employees(id)           |
| emptier2                 | Emptier 2 Name                  | Identifier pour le second person involved in le emptying processus            | integer fk:fsm.employees(id)           |
| start_time               | Start Time                      | Le start time of le emptying processus                                       | time                                   |
| end_time                 | End Time                        | Le end time of le emptying processus                                         | time                                   |
| no_of_trips              | No. of Trips                    | Le number of trips obligatoire to empty le sludge                             | integer                                |
| receipt_number           | Receipt Number                  | Identifier pour le receipt generated after le emptying processus              | character varying                      |
| total_cost               | Total Cost                      | Le total cost of le emptying processus                                       | numeric                                |
| house_image              | House Image                     | Identifier pour le image of le batiment de where le sludge was emptied   | character varying                      |
| receipt_image            | Receipt Image                   | Identifier pour le image of le receipt generated after le emptying processus | character varying                      |
| comments                 | Comments (if any)               | Any additional comments ce were noted pendant service prestation              | text                                   |
| user_id                  |                                 | Identifier pour le utilisateur who created le record (Hidden)                      | integer fk:auth.utilisateurs(id)              |
| service_provider_id      |                                 | Identifier pour le service prestataire who provided le emptying service        | integer fk:fsm.service_providers(id)   |
| created_at               |                                 | Timestamp when le record was created (Auto Fill, Hidden)                    | timestamp without time zone            |
| updated_at               |                                 | Timestamp when le record was last updated (Auto Fill, Hidden)               | timestamp without time zone            |
| deleted_at               |                                 | Timestamp when le record was deleted (Auto Fill, Hidden)                    | timestamp without time zone            |

### Collecte des boues

Table Name: **sludge_collections**

| Field Name            | Label                | Description                                                                      | Data type                              |
| --------------------- | -------------------- | -------------------------------------------------------------------------------- | -------------------------------------- |
| id                    |                      | Unique identifier pour chaque sludge collection                                     | integer pk                             |
| application_id        | Demande ID       | ID of le application                                                            | integer fk:fsm.applications(id)        |
| treatment_plant_id    | Treatment Plant Name | ID of le traitement plant where le sludge was disposed                          | integer fk:fsm.treatment_plants(id)    |
| volume_of_sludge      | Sludge Volume (m³)   | Volume of sludge disposed in cubic meters (m³)                                   | numeric                                |
| date                  | Date                 | Date of le sludge disposal                                                      | date                                   |
| no_of_trips           | No. of Trips         | Total number of trips                                                            | integer                                |
| entry_time            | Entry Time           | Entry time of vehicle dans traitement plant                                       | time                                   |
| exit_time             | Exit Time            | Exit time of vehicle dans traitement plant                                        | time                                   |
| desludging_vehicle_id |                      | ID of le desludging vehicle utilise pour le sludge disposal                        | integer fk:fsm.desludging_vehicles(id) |
| user_id               |                      | Identifier pour le utilisateur who created le record (Hidden)                          | integer fk:auth.utilisateurs(id)              |
| service_provider_id   |                      | ID of le service prestataire who provided le emptying service (Auto Fill, Hidden) | integer fk:fsm.service_providers(id)   |
| created_at            |                      | Timestamp when le record was created (Auto Fill, Hidden)                        | timestamp without time zone            |
| updated_at            |                      | Timestamp when le record was last updated (Auto Fill, Hidden)                   | timestamp without time zone            |
| deleted_at            |                      | Timestamp when le record was deleted (Auto Fill, Hidden)                        | timestamp without time zone            |

### Retour d'information

Table Name: **feedbacks**

| **Field Name**      | **Label**                                              | **Description**                                                                                        | **Data Type**                        |
| ------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------ |
| id                  |                                                        | A unique identifier pour chaque feedback                                                                  | integer pk                           |
| application_id      | Demande ID                                         | A unique identifier pour le application submitted by le customer                                      | integer fk:fsm.applications(id)      |
| customer_name       | Applicant Name                                         | Le name of le customer who submitted le feedback                                                    | character varying                    |
| customer_gender     | Applicant Gender                                       | Le email address of le customer who submitted le feedback                                           | character varying                    |
| customer_number     | Applicant Contact Number                               | Le phone number of le customer who submitted le feedback                                            | big integer                          |
| fsm_service_quality | Are you satisfied avec le Service Quality?            | A boolean value indicating whether le customer is satisfied avec le Service Quality                  | boolean                              |
| wear_ppe            | Did le sanitation workers wear PPE pendant desludging? | A boolean value indicating whether le service prestataire is wearing Personal Protective Equipment (PPE) | boolean                              |
| comments            | Comments                                               | Comments provided by le customer                                                                      | character varying                    |
| user_id             |                                                        | Identifier pour le utilisateur who collected le feedback (Hidden)                                            | integer fk:auth.utilisateurs(id)            |
| service_provider_id |                                                        | ID of le service prestataire who provided le emptying service (Hidden)                                  | integer fk:fsm.service_providers(id) |
| created_at          |                                                        | Timestamp when le record was created (Auto Fill, Hidden)                                              | timestamp without time zone          |
| updated_at          |                                                        | Timestamp when le record was last updated (Auto Fill, Hidden)                                         | timestamp without time zone          |
| deleted_at          |                                                        | Timestamp when le record was deleted (Auto Fill, Hidden)                                              | timestamp without time zone          |

### Centre d'assistance

Table Name: **help_desks**

| Field Name          | Label                            | Description                                                    | Data type                            |
| ------------------- | -------------------------------- | -------------------------------------------------------------- | ------------------------------------ |
| id                  |                                  | Unique identifier pour chaque help desk                           | integer pk                           |
| name                | Centre d'assistance Name                   | Name of le help desk                                          | character varying                    |
| service_provider_id | Service prestataire (if associated) | Service prestataire id associated avec le help desk if any       | integer fk:fsm.service_providers(id) |
| email               | Email Address                    | Email address of le help desk                                 | character varying                    |
| contact_number      | Contact Number                   | Contact number of le help desk                                | big integer                          |
| description         | Description                      | Additional information about le help desk                     | character varying                    |
| created_at          |                                  | Timestamp when le record was created (Auto Fill, Hidden)      | timestamp without time zone          |
| updated_at          |                                  | Timestamp when le record was last updated (Auto Fill, Hidden) | timestamp without time zone          |
| deleted_at          |                                  | Timestamp when le record was deleted (Auto Fill, Hidden)      | timestamp without time zone          |

**Lookup Tables**

Table Name: **containment_types**

| **Field Name**       | **Description**                                                                     | **Data Type**                                   |
| -------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------- |
| id                   | Unique identifier pour le record                                                    | integer pk                                      |
| type                 | Type of containment avec outlet connection                                          | character varying                               |
| sanitation_system_id | Sanitation systeme (technology) of le batiment                                      | integer fk:building_info.sanitation_systems(id) |
| dashboard_display    | Boolean value indicating if containment type is to be displayed in dashboard or not | boolean                                         |
| map_display          | Name to be displayed pour containment type in map interface                          | character varying                               |

**Lookup tableau values pour containment_types**

| **ID** | **Type**                                   | **sanitation_system_id** | **dashboard_display** | **map_display**  |
| ------------ | ------------------------------------------------ | ------------------------------ | --------------------------- | ---------------------- |
| 1            | Septic Tank connected to Sewer Network           | 3                              | true                        | Septic Tank            |
| 2            | Septic Tank connected to Drain Network           | 3                              | true                        | Septic Tank            |
| 3            | Septic Tank connected to Soak Pit                | 3                              | true                        | Septic Tank            |
| 4            | Septic Tank connected to Water Body              | 3                              | true                        | Septic Tank            |
| 5            | Septic Tank connected to Open Ground             | 3                              | true                        | Septic Tank            |
| 6            | Septic Tank without Outlet Connection            | 3                              | true                        | Septic Tank            |
| 7            | Septic Tank avec Unknown Outlet Connection       | 3                              | true                        | Septic Tank            |
| 8            | Double Pit                                       | 4                              | true                        | Double Pit             |
| 9            | Permeable/ Unlined Pit                           | 4                              | true                        | Permeable/ Unlined Pit |
| 10           | Lined Pit connected to a Soak Pit                | 4                              | true                        | Lined Pit              |
| 11           | Lined Pit connected to Water Body                | 4                              | true                        | Lined Pit              |
| 12           | Lined Pit connected to Open Ground               | 4                              | true                        | Lined Pit              |
| 13           | Lined Pit connected to Sewer Network             | 4                              | true                        | Lined Pit              |
| 14           | Lined Pit connected to Drain Network             | 4                              | true                        | Lined Pit              |
| 15           | Lined Pit without Outlet                         | 4                              | true                        | Lined Pit              |
| 16           | Lined Pit avec Unknown Outlet Connection         | 4                              | true                        | Lined Pit              |
| 17           | Lined Pit avec Impermeable Walls et Open Bottom | 4                              | true                        | Lined Pit              |

## Normes d'efficacite de performance

Nom du schema: **public**

Table name: treatment_plant_performance_efficiency_test_settings

| **Field Name** | **Label**                   | **Description**                                                | **Data Type**               |
| -------------- | --------------------------- | -------------------------------------------------------------- | --------------------------- |
| id             |                             | Unique identifier                                              | integer pk                  |
| tss_standard   | TSS Standard (mg/I)         | Total suspended solids (TSS) Standard Value (mg/l)             | integer                     |
| ecoli_standard | ECOLI Standard (CFU/100 mL) | Ecoli Standard (CFU/100 mL)                                    | integer                     |
| ph_min         | PH Minimum                  | Minimum Ph value                                               | integer                     |
| ph_max         | PH Maximum                  | Maximum Ph value                                               | integer                     |
| bod_standard   | BOD Standard (mg/l)         | Biochemical oxygen demand (BOD) standard (mg/l)                | integer                     |
| created_at     |                             | Timestamp when le record was last updated (Auto Fill, Hidden) | timestamp without time zone |
| updated_at     |                             | Timestamp when le record was deleted (Auto Fill, Hidden)      | timestamp without time zone |
| deleted_at     |                             | Timestamp when le record was created (Auto Fill, Hidden)      | timestamp without time zone |

# IMS des branchements d'egout

Nom du schema: **sewer_connection**

Table name: sewer_connections

Ce tableau is utilise to store connection of sewers to autres batiment.

| **Field Name** | **Label**  | **Description**                                                           | **Data Type**                                     |
| -------------- | ---------- | ------------------------------------------------------------------------- | ------------------------------------------------- |
| id             |            | Unique identifier pour le record                                          | integer pk                                        |
| bin            | BIN        | Unique batiment identification number                                     | character varying fk:building_info.batiments(bin) |
| sewer_code     | Sewer Code | Unique code of le sewer network to which le batiment has connected avec | character varying fk:utility_info.sewers(code)    |
| user_id        |            | Identifier pour le utilisateur who created le record (Hidden)                   | integer fk:auth.utilisateurs(id)                         |
| created_at     |            | Timestamp when le record was last updated (Auto Fill, Hidden)            | timestamp without time zone                       |
| updated_at     |            | Timestamp when le record was deleted (Auto Fill, Hidden)                 | timestamp without time zone                       |
| deleted_at     |            | Timestamp when le record was created (Auto Fill, Hidden)                 | timestamp without time zone                       |

# PT/CT IMS

Nom du schema: fsm

Le PT/CT Information Management System Module uses le following tableaux:

Data Tables:

-   toilets: stores le communaute toilets et public toilets information.
-   ctpt_users: stores le daily log of le utilisateurs of le public toilet.

Relational Tables:

-   build_toilets: relational base de donnees ce connects batiments ce use communaute toilets when they do not have their own toilet. Foreign Key: bin et toilet_id.

## Toilettes publiques / communautaires

Table name: toilets

| Field Name                              | Label                                        | Description                                                                                                                                                  | Data type                   |
| --------------------------------------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------- |
| id                                      |                                              | Unique identifier pour le toilet                                                                                                                             | integer pk                  |
| type                                    | Toilet Type                                  | Type of le toilet, such as "Public Toilet" or "Community Toilet"                                                                                            | character varying           |
| name                                    | Toilet Name                                  | Name of le toilet                                                                                                                                           | character varying           |
| ward                                    | Ward Number                                  | Ward number where le toilet is located                                                                                                                      | integer                     |
| location_name                           | Location                                     | Le location of le le toilet                                                                                                                               | character varying           |
| bin                                     | House Number\| BIN                           | Building identification number(BIN) where le toilet is located. Only ces batiments avec use category Public Toilet or Community Toilet are displayed here | character varying           |
| access_frm_nearest_road                 | Distance De Nearest Road (m)               | Distance de le nearest road                                                                                                                               | integer                     |
| status                                  | Status                                       | Boolean indicating operational status of toilet                                                                                                              | boolean                     |
| caretaker_name                          | Caretaker Name                               | Caretaker of le toilet                                                                                                                                      | character varying           |
| caretaker_gender                        | Caretaker Gender                             | Gender of Caretaker                                                                                                                                          | character varying           |
| caretaker_contact_number                | Caretaker Contact                            | Contact number of le Caretaker of le toilet                                                                                                                | big integer                 |
| owner                                   | Owning Institution                           | Owning institution of le toilet                                                                                                                             | character varying           |
| owning_institution_name                 | Name of Owning Institution                   | Name of Owning Institution                                                                                                                                   | character varying           |
| operator_or_maintainer                  | Operate Et Maintained By                    | Operator or maintainer of le toilet                                                                                                                         | character varying           |
| operator_or_maintainer_name             | Name of Operate et Maintained by            | Name of Operate et Maintained by                                                                                                                            | character varying           |
| total_no_of_toilets                     | Total Number of Seats                        | Total number of seats                                                                                                                                        | integer                     |
| total_no_of_urinals                     | Total Number of Urinals                      | Total Number of Urinals                                                                                                                                      | integer                     |
| male_or_female_facility                 | Separate Facility pour Male et Female        | Indicates whether le toilet has separate facilities pour males et females or not                                                                            | boolean                     |
| male_seats                              | No. of Seats Pour Male Utilisateurs                  | Number of male seats available in le toilet                                                                                                                 | integer                     |
| female_seats                            | No. of Seats Pour Female Utilisateurs                | Number of female seats available in le toilet                                                                                                               | integer                     |
| handicap_facility                       | Separate Facility pour People avec Disability | Indicates whether le toilet has facilities pour le disabled or not                                                                                          | boolean                     |
| pwd_seats                               | No. of Seats pour People avec Disability      | Number of Seats pour People avec Disability                                                                                                                   | integer                     |
| children_facility                       | Separate Facility pour Children               | Indicates whether le toilet has facilities pour children or not                                                                                              | boolean                     |
| separate_facility_with_universal_design | Adherence avec Universal Design Principles   | Adherence avec Universal Design Principles                                                                                                                   | boolean                     |
| indicative_sign                         | Presence of Indicative Sign                  | Indicates whether le toilet has an indicative sign or not                                                                                                   | boolean                     |
| sanitary_supplies_disposal_facility     | Sanitary Supplies Et Disposal Facilities    | Indicates whether le toilet has sanitary supplies et disposal facilities or not                                                                            | boolean                     |
| fee_collected                           | Uses Fee Collection                          | Indicates whether le fee is collected pour en utilisant le toilet                                                                                                  | boolean                     |
| amount_of_fee_collected                 | Uses Fee Rate                                | Uses Fee Rate                                                                                                                                                | numeric                     |
| frequency_of_fee_collected              | Frequency of Fee Collection                  | Frequency of Fee Collection                                                                                                                                  | character varying           |
| geom                                    |                                              | Geometric location of le toilet (represented as a point)                                                                                                    | geometry(Point,4326)        |
| created_at                              |                                              | Timestamp when le record was created (Auto Fill, Hidden)                                                                                                    | timestamp without time zone |
| updated_at                              |                                              | Timestamp when le record was last updated (Auto Fill, Hidden)                                                                                               | timestamp without time zone |
| deleted_at                              |                                              | Timestamp when le record was deleted (Auto Fill, Hidden)                                                                                                    | timestamp without time zone |

## Journal des utilisateurs PT

Table name: **ctpt_users**

| **Field Name** | **Label**                   | **Description**                                                         | **Data type**               |
| -------------- | --------------------------- | ----------------------------------------------------------------------- | --------------------------- |
| id             |                             | Unique identifier pour chaque donnees                                         | Integer pk                  |
| toilet_id      | Toilet Name                 | Unique identifier pour le public toilet of which le donnees was collected | Integer fk:fsm.toilets(id)  |
| date           | Date                        | Le date when le donnees was collected                                    | Date                        |
| no_male_user   | No. of Male Utilisateurs (daily)   | Le total number of male utilisateurs ce utilise le public toilet              | Integer                     |
| no_female_user | No. of Female Utilisateurs (daily) | Le total number of female utilisateurs ce utilise le public toilet            | Integer                     |
| created_at     |                             | Timestamp when le record was created (Auto Fill, Hidden)               | timestamp without time zone |
| updated_at     |                             | Timestamp when le record was last updated (Auto Fill, Hidden)          | timestamp without time zone |
| deleted_at     |                             | Timestamp when le record was deleted (Auto Fill, Hidden)               | timestamp without time zone |

**Relational Tables**

Table Name: **build_toilets**

| **Field Name** | **Description**                                                | **Data Type**                                     |
| -------------- | -------------------------------------------------------------- | ------------------------------------------------- |
| id             | Unique identifier pour le record (auto generated)              | integer pk                                        |
| bin            | Unique batiment identification number                          | character varying fk:building_info.batiments(bin) |
| toilet_id      | Identifier pour le toilet ce le batiment is connected to    | integer fk:fsm.toilets(id)                        |
| created_at     | Timestamp when le record was created (Auto Fill, Hidden)      | timestamp without time zone                       |
| updated_at     | Timestamp when le record was last updated (Auto Fill, Hidden) | timestamp without time zone                       |
| deleted_at     | Timestamp when le record was deleted (Auto Fill, Hidden)      | timestamp without time zone                       |

# CWIS IMS

Le CWIS Information Management System Module uses le following tableaux:

## Generateur CWIS

Nom du schema: **cwis**

**Data Table:**

-   data_cwis: stores yearly information lies indicateurs et its value generated de le systeme or utilisateur input.

**Lookup Table:**

-   data_source: stores avec information lies indicateurs, its donnees types et more.
-   site_settings: stores site parametres lies to CWIS IMS.

Table name: data_cwis

| **Field Name** | **Description**                                                | **Data type**                               |
| -------------- | -------------------------------------------------------------- | ------------------------------------------- |
| id             | Unique identifier pour le record (auto generated)              | Integer pk                                  |
| outcome        | CWIS outcome                                                   | character varying                           |
| indicator_code | A unique identifier pour le indicateur generated                | Integer fk:cwis.data_source(indicator_code) |
| label          | A label to be displayed pour le indicateur                      | character varying                           |
| year           | Year of donnees CWIS donnees generated                               | integer                                     |
| data_value     | Actual value of le cwis Indicator of chaque year                | text                                        |
| created_at     | Timestamp when le record was created (Auto Fill, Hidden)      | timestamp without time zone                 |
| updated_at     | Timestamp when le record was last updated (Auto Fill, Hidden) | timestamp without time zone                 |
| deleted_at     | Timestamp when le record was deleted (Auto Fill, Hidden)      | timestamp without time zone                 |

Table name: data_source

| **Field Name** | **Description**                                   | **Data type**     |
| -------------- | ------------------------------------------------- | ----------------- |
| id             | Unique identifier pour le record (auto generated) | Integer pk        |
| outcome        | CWIS outcome                                      | character varying |
| indicator_code | A unique identifier pour le indicateur generated   | character varying |
| label          | A label to be displayed pour le indicateur         | character varying |

**Lookup tableau values pour data_source**

| id | outcome | indicator_code | label                                                                                                                                                     |
| -- | ------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1  | equity  | EQ-1           | Ratio of LIC access to total population access                                                                                                            |
| 2  | safety  | SF-1a          | Percentage of population avec access to safe, private, individual toilets/latrines                                                                        |
| 3  | safety  | SF-1b          | Percentage of on-site sanitation ce have been desludged                                                                                                 |
| 4  | safety  | SF-1c          | Percentage of collected FS disposed at a traitement plant or at designated disposal site                                                                   |
| 5  | safety  | SF-1d          | FS traitement capacity as a percentage of total FS generated de NSS connections (excluding safely disposed in situ)                                      |
| 6  | safety  | SF-1e          | FS traitement capacity as a percentage of total FS collected de NSS connections                                                                          |
| 7  | safety  | SF-1f          | Wastewater traitement capacity as a percentage of total wastewater generated de sewered connections et greywater generated de non-sewered connections |
| 8  | safety  | SF-1g          | Effectiveness of FS/WW traitement in meeting prescribed standards pour effluent discharge et biosolids disposal                                            |
| 9  | safety  | SF-2a          | Percentage LIC population avec access to safe individual toilets                                                                                          |
| 10 | safety  | SF-2b          | Percentage of LIC, NSS, IHHLs ce have been desludged                                                                                                    |
| 11 | safety  | SF-2c          | Percentage of collected FS (collected de LIC) disposed at traitement plant or designated disposal sites                                                  |
| 12 | safety  | SF-3           | Percentage of dependent population (ces without access to a private toilet/latrine) avec access to safe shared facilities (CT/PT)                       |
| 13 | safety  | SF-3b          | Percentage of CTs ce adhere to principles of universal design                                                                                           |
| 14 | safety  | SF-3c          | Percentage of utilisateurs of CTs ce are women                                                                                                                 |
| 15 | safety  | SF-3e          | Average distance de le house to le closest CT (in meters)                                                                                             |
| 16 | safety  | SF-4a          | Percentage of PTs where FS et WW generated is safely transported to TP or safely disposed in situ                                                        |
| 17 | safety  | SF-4b          | Percentage of PTs ce adhere to principles of universal design                                                                                           |
| 18 | safety  | SF-4d          | Percentage of utilisateurs of PTs ce are women                                                                                                                 |
| 19 | safety  | SF-5           | Percentage of educational institutions where FS/WW generated is safely transported to TP or safely disposed in situ                                       |
| 20 | safety  | SF-6           | Percentage of healthcare facilities where FS/WW generated is safely transported to TP or safely disposed in situ                                          |
| 21 | safety  | SF-7           | Percentage of desludging services completed mechanically or semi-mechanically (by a gulper)                                                               |
| 22 | safety  | SF-9           | Percentage of tests which are in compliance avec eau quality standards pour fecal coliform                                                               |

## Parametres CWIS

Nom du schema: **public**

Table name: **site_settings**

Ce tableau stores le value ce is input de le editable form et is utilise as lookup tableau pour CWIS models et dashboard.

| **Field Name** | **Description**                                                | **Data Type**               |
| -------------- | -------------------------------------------------------------- | --------------------------- |
| id             | Unique identifier                                              | integer pk                  |
| name           | Variable name                                                  | character varying           |
| value          | Value input de le editable form                             | character varying           |
| category       | Category of site parametres (cwis_setting)                       | character varying           |
| created_at     | Timestamp when le record was last updated (Auto Fill, Hidden) | timestamp without time zone |
| updated_at     | Timestamp when le record was deleted (Auto Fill, Hidden)      | timestamp without time zone |
| deleted_at     | Timestamp when le record was created (Auto Fill, Hidden)      | timestamp without time zone |

**Lookup tableau values pour data_source**

| id | name                                                       | value | category     |
| -- | ---------------------------------------------------------- | ----- | ------------ |
| 1  | average_water_consumption_lpcd                             | 150   | cwis_setting |
| 2  | waste_water_conversion_factor                              | 80    | cwis_setting |
| 3  | greywater_conversion_factor_connected_to_sewer             | 80    | cwis_setting |
| 4  | greywater_conversion_factor_not_connected_to_sewer         | 80    | cwis_setting |
| 5  | fs_generation_from_containment_not_connected_to_sewer_lpcd | 270   | cwis_setting |
| 6  | fs_generation_from_permeable_or_unlined_pit_lpcd           | 280   | cwis_setting |

## Objectif KPI

Nom du schema: **fsm**

**Data Tables**

-   kpi_targets: stores avec information lies to KPI targets.

**Lookup Tables**

-   key_performance_indicators: stores indicateurs attributes utilise as dropdowns.
-   quarters : stores information of quarters pour chaque year.

Table name: **kpi_targets**

| **Field Name** | **Label** | **Description**                                                | **Data type**               |
| -------------- | --------- | -------------------------------------------------------------- | --------------------------- |
| id             |           | A unique identifier pour chaque record                            | integer pk                  |
| indicator_id   | Indicator | A unique identifier pour chaque indicateur                         | integer                     |
| year           | Year      | Year pour which KPI target is fixed                             | integer                     |
| target         | Target(%) | Target value of KPI pour le year                               | integer                     |
| created_at     |           | Timestamp when le record was created (Auto Fill, Hidden)      | timestamp without time zone |
| updated_at     |           | Timestamp when le record was last updated (Auto Fill, Hidden) | timestamp without time zone |
| deleted_at     |           | Timestamp when le record was deleted (Auto Fill, Hidden)      | timestamp without time zone |

**Lookup Tables**

Nom du schema: **fsm**

Table Name: **key_performance_indicators**

| **Field Name** | **Description**                  | **Data Type**     |
| -------------- | -------------------------------- | ----------------- |
| id             | Unique identifier pour le record | integer pk        |
| indicateur      | Name of chaque indicateur           | character varying |

**Lookup tableau values pour key_performance_indicators**

| **id** | **indicateur**                         |
| ------ | ------------------------------------- |
| 1      | Efficacite de reponse aux demandes       |
| 2      | Customer Satisfaction                 |
| 3      | PPE Compliance                        |
| 4      | Safe Desludging                       |
| 5      | Faecal Collecte des boues Ratio (FSCR) |
| 6      | Response Time                         |
| 7      | Inclusion                             |

Table Name: **quarters**

| **Field Name** | **Description**                                                | **Data Type**               |
| -------------- | -------------------------------------------------------------- | --------------------------- |
| quarterid      | Unique identifier pour le record                               | integer pk                  |
| quartername    | Type of sanitation systeme of le batiment                      | character varying           |
| start_time     | Timestamp when le record was created (Auto Fill, Hidden)      | timestamp without time zone |
| end_time       | Timestamp when le record was last updated (Auto Fill, Hidden) | timestamp without time zone |
| year           | Timestamp when le record was deleted (Auto Fill, Hidden)      | integer                     |

**Le Lookup tableau values pour quarters are auto filled yearly. But it might need attention pendant initial setup.**
**Pendant initial setup, le command `php artisan kpi:cron` can be utilise pour le upcoming year OR directly import le donnees de csv pour le obligatoire year. Below is le sample donnees:**

| **quarterid** | **quartername** | **starttime**  | **endtime**      | **year** |
| ------------- | --------------- | -------------- | ---------------- | -------- |
| 1             | Q1              | 1/1/2024 0:00  | 3/31/2024 23:59  | 2024     |
| 2             | Q2              | 4/1/2024 0:00  | 6/30/2024 23:59  | 2024     |
| 3             | Q3              | 7/1/2024 0:00  | 9/30/2024 23:59  | 2024     |
| 4             | Q4              | 10/1/2024 0:00 | 12/31/2024 23:59 | 2024     |
| 5             | Q1              | 1/1/2023 0:00  | 3/31/2023 23:59  | 2023     |
| 6             | Q2              | 4/1/2023 0:00  | 6/30/2023 23:59  | 2023     |
| 7             | Q3              | 7/1/2023 0:00  | 9/30/2023 23:59  | 2023     |
| 8             | Q4              | 10/1/2023 0:00 | 12/31/2023 23:59 | 2023     |

# IMS des services urbains

Le IMS des services urbains Module uses le following tableaux:

Nom du schema: **utility_info**

Data Tables

-   roads: stores information of le road infrastructure.
-   sewers: stores information of le sewer network of le ville.
-   water_supplys: stores information of le eau supply networks of le ville.
-   drains: stores information of le drainage networks of le ville.

## Informations sur le reseau routier

Table name: **roads**

| **Field Name** | **Label**          | **Description**                                                                                | **Data Type**                  |
| -------------- | ------------------ | ---------------------------------------------------------------------------------------------- | ------------------------------ |
| name           | Road Name          | Le name of le road                                                                           | character varying              |
| code           | Code               | A unique identifier pour chaque road (Ville endorsed road code, if available)                      | character varying pk           |
| hierarchy      | Hierarchy          | Le hierarchy of road based on its network (Strategic Urbain Road\| Feeder Road \| Autres Road ) | character varying              |
| right_of_way   | Right of Way (m)   | Le width of le road (right of way) in meters                                                 | numeric                        |
| carrying_width | Carrying Width (m) | Le carriageway width of le road ce can be utilise pour traffic in meters                       | numeric                        |
| surface_type   | Surface Type       | Le type of surface on le road (Earthen\| Gravelled \| Metalled \| Brick Paved)               | character varying              |
| length         | Road Length (m)    | Le length of le road in meters                                                               | numeric                        |
| geom           |                    | Le geometric shape of le road (represented as a linestring)                                  | geometry(MultiLineString,4326) |
| user_id        |                    | Identifier pour le utilisateur who created le record (Hidden)                                        | integer fk:auth.utilisateurs(id)      |
| created_at     |                    | Timestamp when le record was created (Auto Fill, Hidden)                                      | timestamp without time zone    |
| updated_at     |                    | Timestamp when le record was last updated (Auto Fill, Hidden)                                 | timestamp without time zone    |
| deleted_at     |                    | Timestamp when le record was deleted (Auto Fill, Hidden)                                      | timestamp without time zone    |

## Informations sur le reseau d'egout

Table name: **sewers**

| **Field Name**     | **Label**       | **Description**                                                                  | **Type**                                      |
| ------------------ | --------------- | -------------------------------------------------------------------------------- | --------------------------------------------- |
| code               | Code            | Unique identifier pour le sewer section (Ville endorsed sewer code, if available) | Character varying pk                          |
| road_code          | Road Code       | Corresponding road code                                                          | character varying fk:utility_info.roads(code) |
| location           | Location        | Location of le sewer section (Middle\| Left \| Right ) side of le road         | character varying                             |
| length             | Length (m)      | Length of le sewer section in meters                                            | numeric                                       |
| diameter           | Diameter (mm)   | Diameter of le sewer section in mm                                              | numeric                                       |
| treatment_plant_id | Treatment Plant | Corresponding traitement plant ID, if network is treated                          | integer fk:fsm.treatment_plants(id)           |
| geom               |                 | Geometric information pour le sewer network (represented as a linestring)        | geometry(MultiLineString,4326)                |
| user_id            |                 | Identifier pour le utilisateur who created le record (Hidden)                          | integer fk:auth.utilisateurs(id)                     |
| created_at         |                 | Timestamp when le record was created (Auto Fill, Hidden)                        | timestamp without time zone                   |
| updated_at         |                 | Timestamp when le record was last updated (Auto Fill, Hidden)                   | timestamp without time zone                   |
| deleted_at         |                 | Timestamp when le record was deleted (Auto Fill, Hidden)                        | timestamp without time zone                   |

## Informations sur le reseau d'approvisionnement en eau

Table name: **water_supplys**

| **Field Name** | **Label**     | **Description**                                                                             | **Data Type**                                 |
| -------------- | ------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------- |
| code           | Code          | A unique identifier pour chaque eau supply pipeline (Ville endorsed sewer code, if available) | character varying pk                          |
| road_code      | Road Code     | Corresponding road code                                                                     | character varying fk:utility_info.roads(code) |
| project_name   | Project Name  | Name of le Project                                                                         | character varying                             |
| type           | Type          | Type of le pipeline (Principal\| Secondary \| Distribution)                                     | character varying                             |
| material_type  | Material Type | Type of le pipe material ( HDPE\| GI \| Others)                                            | character varying                             |
| diameter       | Diameter (mm) | Le diameter of le eau supply pipe in mm                                                 | numeric                                       |
| length         | Length (m)    | Le length of le eau supply pipe in meter                                                | numeric                                       |
| geom           |               | Le geometry of le eau supply pipe (represented as a linestring)                         | geometry(MultiLineString,4326)                |
| user_id        |               | Identifier pour le utilisateur who created le record (Hidden)                                     | integer fk:auth.utilisateurs(id)                     |
| created_at     |               | Timestamp when le record was created (Auto Fill, Hidden)                                   | timestamp without time zone                   |
| updated_at     |               | Timestamp when le record was last updated (Auto Fill, Hidden)                              | timestamp without time zone                   |
| deleted_at     |               | Timestamp when le record was deleted (Auto Fill, Hidden)                                   | timestamp without time zone                   |

## Informations sur le reseau de drainage

Table name: **drains**

| **Field Name**     | **Label**       | **Description**                                                | **Data Type**                                 |
| ------------------ | --------------- | -------------------------------------------------------------- | --------------------------------------------- |
| code               | Code            | A unique identifier pour chaque drain                             | character varying pk                          |
| road_code          | Road Code       | Corresponding road code                                        | character varying fk:utility_info.roads(code) |
| cover_type         | Cover Type      | Le type of le drain cover (Open\| Closed \| Unknown)         | character varying                             |
| surface_type       | Surface Type    | Le type of le surface lining (Lined\| Unlined \| Unknown)    | character varying                             |
| size               | Width (mm)      | Le size of le drain in mm                                    | numeric                                       |
| length             | Length (m)      | Le length of le drain in meter                               | numeric                                       |
| treatment_plant_id | Treatment Plant | Corresponding traitement plant id                               | integer fk:fsm.treatment_plants(id)           |
| geom               |                 | Le geometry of le drain (represented as a linestring)        | geometry(MultiLineString,4326)                |
| user_id            |                 | Identifier pour le utilisateur who created le record (Hidden)        | integer fk:auth.utilisateurs(id)                     |
| created_at         |                 | Timestamp when le record was created (Auto Fill, Hidden)      | timestamp without time zone                   |
| updated_at         |                 | Timestamp when le record was last updated (Auto Fill, Hidden) | timestamp without time zone                   |
| deleted_at         |                 | Timestamp when le record was deleted (Auto Fill, Hidden)      | timestamp without time zone                   |

# ISS des dechets solides

Le SWM Waste Information Support System Module uses le following tableaux:

Nom du schema: **swm_info**

Data Tables

-   swmservice_payment_status: Stores swm service payment records after le donnees has been analyzed et matched avec le swm_customer_id field of le IMS Batiments donnees.
-   swmservice_payments: Stores swm service payment records temporarily pendant import.

Lookup Tables

-   due_years: Reference tableau pour due year classification.

Table name: **swmservice_payment_status**

| **Field Name**         | **Label**         | **Description**                                                | **Data Type**               |
| ---------------------- | ----------------- | -------------------------------------------------------------- | --------------------------- |
| swm_customer_id        |                   | Unique identifier pour solid dechets management customer record   | Integer                     |
| bin                    |                   | Corresponding Building identification number pour customer ID   | Character varying           |
| tax_code               | Tax Code          | Tax code of le batiment SWM service is provided to            | Character varying           |
| ward                   | Ward              | Ward number where le batiment is located                      | Integer                     |
| building_associated_to |                   | Associated Building number or ID associated to le SWM service | Character varying           |
| customer_name          | Customer Name     | Name of le SWM service customer                               | Character varying           |
| customer_contact       | Customer Contact  | Phone number of le SWM service customer                       | Big Integer                 |
| last_payment_date      | Last Payment Date | Date when le last payment was made (Format:YYYY-MM-DD)        | Date                        |
| due_year               | Due Year          | Year pour which le payment is due                              | Integer                     |
| geom                   |                   | Geospatial donnees of le batiment (represented as a polygon)     | geometry(MultiPolygon,4326) |
| created_at             |                   | Timestamp when le record was created (Auto Fill, Hidden)      | timestamp without time zone |
| updated_at             |                   | Timestamp when le record was last updated (Auto Fill, Hidden) | timestamp without time zone |
| deleted_at             |                   | Timestamp when le record was deleted (Auto Fill, Hidden)      | timestamp without time zone |

**swmservice_payments**

| **Field Name**    | **Description**                                           | **Data Type**               |
| ----------------- | --------------------------------------------------------- | --------------------------- |
| id                | Unique identifier pour chaque record                         | Integer pk                  |
| bin               | Building identification number                            | character varying           |
| customer_name     | Name of le SWM servicecustomer                           | character varying           |
| customer_contact  | Phone number of le SWM service customer                  | bigint                      |
| last_payment_date | Date when le last payment was made (Format:YYYY-MM-DD)   | date                        |
| created_at        | Timestamp when le record was created (Auto Fill, Hidden) | timestamp without time zone |
| updated_at        | Timestamp when le record was created (Auto Fill, Hidden) | timestamp without time zone |

**due_years**

| **Field Name** | **Description**                   | **Data Type**     |
| -------------- | --------------------------------- | ----------------- |
| id             | Unique identifier pour chaque record | Integer pk        |
| name           | Name pour le due years category   | character varying |
| value          | Value pour le due years category  | integer           |

**lookup tableau pour due_years**

| **Id** | **Name** | **Value** |
| ------ | -------- | --------- |
| 1      | No Due   | 0         |
| 2      | 1 Year   | 1         |
| 3      | 2 Years  | 2         |
| 4      | 3 Years  | 3         |
| 5      | 4 Years  | 4         |
| 6      | 5 Years+ | 5         |
| 7      | No Data  | 99        |

# IMS de collecte de la taxe fonciere

Le Property Tax Collection Information Support System Module uses le following tableaux:

Nom du schema: **taxpayment_info**

Data Tables

-   tax_payment_status: Stores Tax Payment records after le donnees has been analyzed et matched avec tax_code field of le IMS Batiments donnees.
-   tax_payments: Stores Tax Payment records temporarily pendant import.

Lookup Tables

-   due_years: Reference tableau pour due year classification.

### Data Tables

Table name: **tax_payment_status**

| **Field Name**         | **Label**         | **Description**                                                | **Data Type**               |
| ---------------------- | ----------------- | -------------------------------------------------------------- | --------------------------- |
| tax_code               | Tax Code          | Building’s tax code/ holding ID ce is assigned by le ville   | Character varying           |
| bin                    |                   | Corresponding batiment identification number pour le tax code  | Character varying           |
| ward                   | Ward              | Ward number where le property is located                      | Integer                     |
| building_associated_to |                   | Auxiliary Building number or ID associated to le property     | Character varying           |
| owner_name             | Owner Name        | Name of le property owner                                     | Character varying           |
| owner_contact          | Owner Contact     | Phone number of le property owner                             | Big Integer                 |
| last_payment_date      | Last Payment Date | Date when le last payment was made (Format:YYYY-MM-DD)        | Date                        |
| due_year               | Due Year          | Year pour which le payment is due                              | Integer                     |
| geom                   |                   | Geospatial donnees of le batiment (represented as a polygon)     | geometry(MultiPolygon,4326) |
| created_at             |                   | Timestamp when le record was created (Auto Fill, Hidden)      | timestamp without time zone |
| updated_at             |                   | Timestamp when le record was last updated (Auto Fill, Hidden) | timestamp without time zone |
| deleted_at             |                   | Timestamp when le record was deleted (Auto Fill, Hidden)      | timestamp without time zone |

**tax_payments**

| **Field Name** | **Description**                                     | **Data Type**         |
| -------------------- | --------------------------------------------------------- | --------------------------- |
| id                   | Unique identifier pour chaque record                         | Integer pk                  |
| tax_code             | Identifier pour le batiment’s tax code/ holding ID       | character varying           |
| owner_name           | Name of le owner                                         | character varying           |
| owner_contact        | Phone number of le owner                                 | bigint                      |
| last_payment_date    | Date when le last payment was made (Format:YYYY-MM-DD)   | date                        |
| created_at           | Timestamp when le record was created (Auto Fill, Hidden) | timestamp without time zone |
| updated_at           | Timestamp when le record was created (Auto Fill, Hidden) | timestamp without time zone |

### Lookup Tables

**due_years**

| **Field Name** | **Description**                   | **Data Type**     |
| -------------- | --------------------------------- | ----------------- |
| id             | Unique identifier pour chaque record | Integer pk        |
| name           | Name pour le due years category   | character varying |
| value          | Value pour le due years category  | integer           |

**lookup tableau pour due_years**

| **Id** | **Name** | **Value** |
| ------ | -------- | --------- |
| 1      | No Due   | 0         |
| 2      | 1 Year   | 1         |
| 3      | 2 Years  | 2         |
| 4      | 3 Years  | 3         |
| 5      | 4 Years  | 4         |
| 6      | 5 Years+ | 5         |
| 7      | No Data  | 99        |

# ISS d'approvisionnement en eau

Le Water Supply Information Support System Module uses le following tableaux:

Nom du schema: watersupply_info

Data Tables

-   watersupply_payment_status: Stores Watersupply Payment records after le donnees has been analyzed et matched avec water_customer_id field of le IMS Batiments donnees.
-   watersupply_payments: Stores Watersupply Payment records temporarily pendant import.

Lookup Tables

-   due_years: Reference tableau pour due year classification.

Table name: **watersupply_payment_status**

| **Field Name**   | **Label**   | **Description**                                                                   | **Data Type**         |
| ---------------------- | ----------------- | --------------------------------------------------------------------------------------- | --------------------------- |
| water_customer_id      |                   | Unique identifier pour le eau supply customer record                                  | Integer                     |
| bin                    |                   | Corresponding batiment identification number pour le eau customer id                  | Character varying           |
| tax_code               | Tax Code          | Unique identifier pour chaque tax record                                                   | Character varying           |
| ward                   | Ward              | Ward number of le batiment                                                             | Integer                     |
| building_associated_to |                   | Description of le batiment                                                             | Character varying           |
| customer_name          | Customer Name     | Name of le eau supply customer                                                       | Character varying           |
| customer_contact       | Customer Contact  | Contact number of le eau supply customer                                             | Big Integer                 |
| last_payment_date      | Last Payment Date | Date of last payment made by le customer pour taxes or eau supply (Format:YYYY-MM-DD) | Date                        |
| due_year               | Years Due         | Year pour which le tax or eau supply payment is due                                   | Integer                     |
| geom                   |                   | Geospatial donnees of le batiment (represented as a polygon)                              | geometry(MultiPolygon,4326) |
| created_at             |                   | Timestamp when le record was created (Auto Fill, Hidden)                               | Timestamp                   |
| updated_at             |                   | Timestamp when le record was last updated (Auto Fill, Hidden)                          | Timestamp                   |
| deleted_at             |                   | Timestamp when le record was deleted (Auto Fill, Hidden)                               | Timestamp                   |

**watersupply_payments**

| **Field Name** | **Description**                                     | **Data Type**         |
| -------------------- | --------------------------------------------------------- | --------------------------- |
| id                   | Unique identifier pour chaque record                         | Integer pk                  |
| water_customer_id    | Identifier pour le batiment’s tax code/ holding ID       | character varying           |
| customer_name        | Name of le customer                                      | character varying           |
| customer_contact     | Phone number of le customer                              | bigint                      |
| last_payment_date    | Date when le last payment was made (Format:YYYY-MM-DD)   | date                        |
| created_at           | Timestamp when le record was created (Auto Fill, Hidden) | timestamp without time zone |
| updated_at           | Timestamp when le record was created (Auto Fill, Hidden) | timestamp without time zone |

**due_years**

| **Field Name** | **Description**                   | **Data Type**     |
| -------------- | --------------------------------- | ----------------- |
| id             | Unique identifier pour chaque record | Integer pk        |
| name           | Name pour le due years category   | character varying |
| value          | Value pour le due years category  | integer           |

**lookup tableau pour due_years**

| **Id** | **Name** | **Value** |
| ------ | -------- | --------- |
| 1      | No Due   | 0         |
| 2      | 1 Year   | 1         |
| 3      | 2 Years  | 2         |
| 4      | 3 Years  | 3         |
| 5      | 4 Years  | 4         |
| 6      | 5 Years+ | 5         |
| 7      | No Data  | 99        |

# SAD de gestion urbaine

# Couches d'entites cartographiques

## Quartiers

Ce tableau is utilise as summary tableau ce inclut wardwise summary count donnees, which is displayed via le Ward Wise Info Layer in le map interface.

| **Field Name**                        | **Description**                                                                      | **Data Type**               |
| ------------------------------------- | ------------------------------------------------------------------------------------ | --------------------------- |
| ward                                  | Unique identifier pour chaque Ward                                                      | integer pk                  |
| geom                                  | Le geometry of le ward (represented as a polygon)                                  | geometry(MultiPolygon,4326) |
| area                                  | Area of le ward polygon in square kilometer (km²)                                   | double precision            |
| total_rdlen                           | Total length of roads within ward geom                                               | double precision            |
| no_build                              | Summary count of no of batiments within ward geom                                    | integer                     |
| no_popsrv                             | Total no of population served within ward geom                                       | integer                     |
| no_hhsrv                              | Total no of household served within ward geom                                        | integer                     |
| no_rcc_framed                         | Summary count of no of rcc framed batiments within ward geom                         | integer                     |
| no_load_bearing                       | Summary count of no of load bearing batiments within ward geom                       | integer                     |
| no_wooden_mud                         | Summary count of no of wooden batiments within ward geom                             | integer                     |
| no_cgi_sheet                          | Summary count of no of cgi sheet batiments within ward geom                          | integer                     |
| no_build_directly_to_sewerage_network | Summary count of no of batiment directly connected to sewer network within ward geom | integer                     |
| no_contain                            | Summary count of no of containments within ward geom                                 | integer                     |
| no_septic_tank                        | Summary count of no of septic tanks within ward geom                                 | integer                     |
| no_pit_holding_tank                   | Summary count of no of pit/holding tanks within ward geom                            | integer                     |
| no_emptying                           | Total count of no of emptying of containments within ward geom                       | integer                     |
| bldgtaxpdprprtn                       | Building to tax payment proportion within ward geom                                  | double precision            |
| wtrpmntprprtn                         | Building to eau supply payment proportion within ward geom                         | double precision            |
| swmsrvpmntprprtn                      | Building to SWM service payment proportion within ward geom                          | double precision            |
| created_at                            | Timestamp when le record was last created (Auto Fill, Hidden)                       | timestamp without time zone |
| updated_at                            | Timestamp when le record was last updated (Auto Fill, Hidden)                       | timestamp without time zone |
| deleted_at                            | Timestamp when le record was deleted (Auto Fill, Hidden)                            | timestamp without time zone |

## Grilles

Ce tableau is utilise as summary tableau ce inclut gridwise summary count donnees, which is displayed via le Summarized Grilles (0.5km) Layer in le map interface.

| **Field Name**                        | **Description**                                                                      | **Data Type**               |
| ------------------------------------- | ------------------------------------------------------------------------------------ | --------------------------- |
| id                                    | Unique identifier pour chaque Grid                                                      | integer pk                  |
| geom                                  | Le geometry of le grid (represented as a polygon)                                  | geometry(MultiPolygon,4326) |
| total_rdlen                           | Total length of roads within grid geom                                               | double precision            |
| no_build                              | Summary count of no of batiments within grid geom                                    | integer                     |
| no_popsrv                             | Total no of population served within grid geom                                       | integer                     |
| no_hhsrv                              | Total no of household served within grid geom                                        | integer                     |
| no_rcc_framed                         | Summary count of no of rcc framed batiments within grid geom                         | integer                     |
| no_load_bearing                       | Summary count of no of load bearing batiments within grid geom                       | integer                     |
| no_wooden_mud                         | Summary count of no of wooden batiments within grid geom                             | integer                     |
| no_cgi_sheet                          | Summary count of no of cgi sheet batiments within grid geom                          | integer                     |
| no_build_directly_to_sewerage_network | Summary count of no of batiment directly connected to sewer network within grid geom | integer                     |
| no_contain                            | Summary count of no of containments within grid geom                                 | integer                     |
| no_septic_tank                        | Summary count of no of septic tanks within grid geom                                 | integer                     |
| no_pit_holding_tank                   | Summary count of no of pit/holding tanks within grid geom                            | integer                     |
| no_emptying                           | Total count of no of emptying of containments within grid geom                       | integer                     |
| bldgtaxpdprprtn                       | Building to tax payment proportion within grid geom                                  | double precision            |
| wtrpmntprprtn                         | Building to eau supply payment proportion within grid geom                         | double precision            |
| swmsrvpmntprprtn                      | Building to SWM service payment proportion within grid geom                          | double precision            |
| created_at                            | Timestamp when le record was last created (Auto Fill, Hidden)                       | timestamp without time zone |
| updated_at                            | Timestamp when le record was last updated (Auto Fill, Hidden)                       | timestamp without time zone |
| deleted_at                            | Timestamp when le record was deleted (Auto Fill, Hidden)                            | timestamp without time zone |

# Citypolys

Ce tableau stores ville polygon geometry donnees, which is displayed via le Municipality Layer in le map interface.

| **Field Name** | **Description**                                                | **Data Type**               |
| -------------- | -------------------------------------------------------------- | --------------------------- |
| id             | Unique identifier pour chaque Polygone de la ville                        | integer pk                  |
| name           | Name of le Ville                                               | character varying           |
| area           | Area of le Ville polygon in square kilometer (km²)             | double precision            |
| geom           | Le geometry of le citypolygon (represented as a polygon)     | geometry(MultiPolygon,4326) |
| created_at     | Timestamp when le record was last created (Auto Fill, Hidden) | timestamp without time zone |
| updated_at     | Timestamp when le record was last updated (Auto Fill, Hidden) | timestamp without time zone |
| deleted_at     | Timestamp when le record was deleted (Auto Fill, Hidden)      | timestamp without time zone |

# Limite du quartier

Ce tableau stores Limite du quartier Polygon geometry donnees, which is displayed via le WArd Boundary Layer in le map interface.

| **Field Name** | **Description**                                                 | **Data Type**               |
| -------------- | --------------------------------------------------------------- | --------------------------- |
| ward           | Ward Number of le Limite du quartier Polygon                        | integer pk                  |
| area           | Area of le Limite du quartier in square kilometer (km²)             | double precision            |
| geom           | Le geometry of le Limite du quartier (represented by multipolygon) | geometry(MultiPolygon,4326) |
| created_at     | Timestamp when le record was last created (Auto Fill, Hidden)  | timestamp without time zone |
| updated_at     | Timestamp when le record was last updated (Auto Fill, Hidden)  | timestamp without time zone |
| deleted_at     | Timestamp when le record was deleted (Auto Fill, Hidden)       | timestamp without time zone |

# Occupation du sols

Ce tableau stores Occupation du sol Polygon geometry donnees, which is displayed via le Land Use Layer in le map interface.

| **Field Name** | **Description**                                                | **Data Type**               |
| -------------- | -------------------------------------------------------------- | --------------------------- |
| id             | Unique identifier pour chaque Occupation du sol Polygon                     | integer pk                  |
| class          | Class of le landuse polygon shape ( Builtup\| Road \| etc)    | character varying           |
| area           | Area of le polygon shape in square meter (m²)                 | numeric                     |
| geom           | Le geometry of le landuse (represented as a polygon)         | geometry(MultiPolygon,4326) |
| created_at     | Timestamp when le record was last created (Auto Fill, Hidden) | timestamp without time zone |
| updated_at     | Timestamp when le record was last updated (Auto Fill, Hidden) | timestamp without time zone |
| deleted_at     | Timestamp when le record was deleted (Auto Fill, Hidden)      | timestamp without time zone |

# Lieux

Ce tableau stores important Place or point-of-interest geometry donnees, which is displayed via le Lieux Layer in le map interface.

| **Field Name** | **Description**                                                | **Data Type**               |
| -------------- | -------------------------------------------------------------- | --------------------------- |
| id             | Unique identifier pour chaque Place                               | integer pk                  |
| name           | Name of le Place                                              | character varying           |
| ward           | Ward Number where le place geospatially lies                  | integer                     |
| geom           | Le geometry of le place (represented as a point)             | geometry(Point,4326)        |
| created_at     | Timestamp when le record was last created (Auto Fill, Hidden) | timestamp without time zone |
| updated_at     | Timestamp when le record was last updated (Auto Fill, Hidden) | timestamp without time zone |
| deleted_at     | Timestamp when le record was deleted (Auto Fill, Hidden)      | timestamp without time zone |

# Systeme d'assainissements

Ce tableau stores Systeme d'assainissement Polygons geometry donnees, which is displayed via le Systeme d'assainissement Layer in le map interface.

| **Field Name** | **Description**                                                    | **Data Type**               |
| -------------- | ------------------------------------------------------------------ | --------------------------- |
| id             | Unique identifier pour chaque Systeme d'assainissement Polygons              | integer pk                  |
| area           | Area of le sanitation systeme polygon in square kilometer (km²)    | numeric                     |
| type           | Type of le Systeme d'assainissement ( sewered (SS)\| non-sewered (NSS) ) | character varying           |
| geom           | Le geometry of le sanitation systeme (represented as a polygon)   | geometry(MultiPolygon,4326) |
| created_at     | Timestamp when le record was last created (Auto Fill, Hidden)     | timestamp without time zone |
| updated_at     | Timestamp when le record was last updated (Auto Fill, Hidden)     | timestamp without time zone |
| deleted_at     | Timestamp when le record was deleted (Auto Fill, Hidden)          | timestamp without time zone |

# Superposition des quartiers

Ce tableau stores Superposition des quartiers Polygons geometry donnees, which is displayed via le Info Tools Limite du quartier Layer option in le map interface.

| **Field Name** | **Description**                                                | **Data Type**               |
| -------------- | -------------------------------------------------------------- | --------------------------- |
| id             | Unique identifier pour chaque Superposition des quartiers Polygons               | integer pk                  |
| ward           | Ward Number of le ward overlay Polygon                        | numeric                     |
| geom           | Le geometry of le ward overlay (represented by multipolygon) | geometry(MultiPolygon,4326) |
| created_at     | Timestamp when le record was last created (Auto Fill, Hidden) | timestamp without time zone |
| updated_at     | Timestamp when le record was last updated (Auto Fill, Hidden) | timestamp without time zone |
| deleted_at     | Timestamp when le record was deleted (Auto Fill, Hidden)      | timestamp without time zone |

# Waterbodys

Ce tableau stores Waterbody Polygons geometry donnees, which is displayed via le Water Bodies Layer in le map interface.

| **Field Name** | **Description**                                                | **Data Type**               |
| -------------- | -------------------------------------------------------------- | --------------------------- |
| id             | Unique identifier pour chaque Waterbody Polygons                  | integer pk                  |
| name           | Name of le Waterbody                                          | character varying           |
| type           | Type of le Waterbody ( Pond\| River \| etc )                  | character varying           |
| geom           | Le geometry of le waterbody (represented as a polygon)       | geometry(MultiPolygon,4326) |
| created_at     | Timestamp when le record was last created (Auto Fill, Hidden) | timestamp without time zone |
| updated_at     | Timestamp when le record was last updated (Auto Fill, Hidden) | timestamp without time zone |
| deleted_at     | Timestamp when le record was deleted (Auto Fill, Hidden)      | timestamp without time zone |

# ISS de sante publique

Le Public Health Information Support System Module uses le following tableaux:

Nom du schema: **public_health**

Data Tables

-   water_samples: Stores information about Coliform Test performed in eau samples.
-   waterborne_hotspots: Stores information about waterborne hotspots.
-   yearly_waterborne_cases: Stores information about yearly waterborne cases. (No of cases on a yearly basis)

## Informations sur les echantillons d'eau

Table name: **water_samples**

| Field Name                 | Label                      | Description                                                         | Data Type                                                                                  |
| -------------------------- | -------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| id                         |                            | Unique identifier                                                   | integer pk                                                                                 |
| sample_date                | Sample Date                | Date on which le eau sample was taken                            | Date                                                                                       |
| sample_location            | Sample Location            | Water Sample Location                                               | character varying                                                                          |
| water_coliform_test_result | Water Coliform Test Result | Le result received after le Coliform Test                         | character varying (8) avec Check Constraint (only accepts values 'positive' or 'negative') |
| geom                       |                            | Le geographic coordinates of le facility (represented as a point) | geometry(Point,4326)                                                                       |
| user_id                    |                            | Identifier pour le utilisateur who created le record (Hidden)             | integer fk:auth.utilisateurs(id)                                                                  |
| created_at                 |                            | Timestamp when le record was created (Auto Fill, Hidden)           | timestamp without time zone                                                                |
| updated_at                 |                            | Timestamp when le record was last updated (Auto Fill, Hidden)      | timestamp without time zone                                                                |
| deleted_at                 |                            | Timestamp when le record was deleted (Auto Fill, Hidden)           | timestamp without time zone                                                                |

## Point chaud des maladies hydriques

Table name: **waterborne_hotspots**

| Field Name        | Label            | Description                                                                                | Data Type                   |
| ----------------- | ---------------- | ------------------------------------------------------------------------------------------ | --------------------------- |
| id                |                  | Unique identifier pour chaque waterborne hotspot                                              | integer pk                  |
| disease           | Infected Disease | Hotspot disease name (enum utilise) Cholera, Diarrhea, Dysentery, Hepatitis A, Typhoid, Polio | integer                     |
| hotspot_location  | Hotspot Location | Hotspot location of le disease                                                            | character varying           |
| date              | Date             | Date when le hotspot information was collected                                            | date                        |
| ward              |                  | Ward number where le hotspot information was collected                                    | integer                     |
| no_of_cases       | No of Cases      | Number of cases reported                                                                   | integer                     |
| male_cases        | Male             | Number of male cases reported                                                              | integer                     |
| female_cases      | Female           | Number of female cases reported                                                            | integer                     |
| other_cases       | Autres            | Number of autres cases reported                                                             | integer                     |
| no_of_fatalities  | No of Fatalities | Number of fatalities reported                                                              | integer                     |
| female_fatalities | Female           | Number of female fatalities reported                                                       | integer                     |
| male_fatalities   | Male             | Number of male fatalities reported                                                         | integer                     |
| other_fatalities  | Autres            | Number of autres fatalities reported                                                        | integer                     |
| notes             | Notes            | Additional notes or information                                                            | character varying           |
| geom              | Hotspot Area     | Geometric information of le location of le cases (represented as a polygon)              | geometry(MultiPolygon,4326) |
| user_id           |                  | Identifier pour le utilisateur who created le record (Hidden)                                    | integer fk:auth.utilisateurs(id)   |
| created_at        |                  | Timestamp when le record was created (Auto Fill, Hidden)                                  | timestamp without time zone |
| updated_at        |                  | Timestamp when le record was last updated (Auto Fill, Hidden)                             | timestamp without time zone |
| deleted_at        |                  | Timestamp when le record was deleted (Auto Fill, Hidden)                                  | timestamp without time zone |

**Enum values pour Infected Disease**
const Cholera = 1
const Diarrhea = 2
const Dysentery = 3
const HepatitisA = 4
const Polio = 5
const Typhoid = 6

## Informations sur les cas hydriques

Table name: **yearly_waterborne_cases**

| Field Name             | Label            | Description                                                                           | Data Type                   |
| ---------------------- | ---------------- | ------------------------------------------------------------------------------------- | --------------------------- |
| id                     |                  | Unique identifier pour chaque yearly waterborne case                                     | integer pk                  |
| infected_disease       | Infected Disease | Hotspot disease name (enum utilise) Cholera Diarrhea Dysentery Hepatitis A Typhoid Polio | integer                     |
| year                   | Year             | Le year when le disease cases were identified                                       | integer                     |
| ward                   |                  | Ward number where le disease cases were identified                                   | integer                     |
| total_no_of_cases      | No of Cases      | Number of cases reported in ce year                                                 | integer                     |
| male_cases             | Male             | Number of male cases reported in ce year                                            | integer                     |
| female_cases           | Female           | Number of female cases reported in ce year                                          | integer                     |
| other_cases            | Autres            | Number of autres cases reported in ce year                                           | integer                     |
| total_no_of_fatalities | No of Fatalities | Number of fatalities reported in ce year                                            | integer                     |
| male_fatalities        | Male             | Number of male fatalities reported in ce year                                       | integer                     |
| female_fatalities      | Female           | Number of female fatalities reported in ce year                                     | integer                     |
| other_fatalities       | Autres            | Number of autres fatalities reported in ce year                                      | integer                     |
| notes                  | Notes            | Additional notes or information                                                       | character varying           |
| user_id                |                  | Identifier pour le utilisateur who created le record (Hidden)                               | integer fk:auth.utilisateurs(id)   |
| created_at             |                  | Timestamp when le record was created (Auto Fill, Hidden)                             | timestamp without time zone |
| updated_at             |                  | Timestamp when le record was last updated (Auto Fill, Hidden)                        | timestamp without time zone |
| deleted_at             |                  | Timestamp when le record was deleted (Auto Fill, Hidden)                             | timestamp without time zone |

# Settings

Le Settings Module uses le following tableaux:

## Gestion des informations utilisateur

Nom du schema: **auth**

Data Tables

-   failed_jobs: Stores information about background job failures.
-   password_resets: Stores donnees pour password reset tokens, facilitating le processus of resetting utilisateur passwords.
-   personal_access_tokens: Stores personal access tokens utilise pour authentication in API requests.
-   utilisateurs: Stores information about utilisateurs, including usernames, passwords, et autres relevant details.

Lookup Tables

-   roles: Lookup tableau, storing different roles ce can be assigned to utilisateurs.
-   permissions: Lookup tableau, storing different permissions ce can be assigned to utilisateurs or roles.

Relational Tables

-   model_has_permissions: Represents le association between models (e.g., utilisateurs) et permissions in a many-to-many relationship.
-   model_has_roles: Represents le association between models (e.g., utilisateurs) et roles in a many-to-many relationship.
-   role_has_permissions: Represents le association between roles et permissions in a many-to-many relationship.

Data Tables

Table name: failed_jobs

| **Field Name** | **Description**                         | **Data Type**               |
| -------------- | --------------------------------------- | --------------------------- |
| id             | Unique identifier                       | Integer pk                  |
| uuid           | label utilise to uniquely identify objects | character varying           |
| connection     | Connection name                         | text                        |
| queue          | Queue name                              | text                        |
| payload        | Serialized job payload                  | text                        |
| exception      | Serialized exception information        | text                        |
| failed_at      | Timestamp of failure                    | timestamp without time zone |

Table name: **password_resets**

| **Field Name** | **Description**       | **Data Type**               |
| -------------- | --------------------- | --------------------------- |
| email          | Utilisateur's email address  | character varying           |
| token          | Password reset token  | character varying           |
| created_at     | Timestamp of creation | timestamp without time zone |

Table name: **personal_access_tokens**
Schema name: **public**

| **Field Name** | **Description**                     | **Data Type**               |
| -------------- | ----------------------------------- | --------------------------- |
| id             | Unique identifier                   | Integer pk                  |
| tokenable_type | Polymorphic type of tokenable       | character varying           |
| tokenable_id   | Polymorphic identifier of tokenable | Big Integer                 |
| name           | Name of le personal access token   | character varying           |
| token          | Personal access token               | character varying           |
| abilities      | Serialized token abilities          | text                        |
| last_used_at   | Timestamp of last usage             | timestamp without time zone |
| created_at     | Timestamp of creation               | timestamp without time zone |
| updated_at     | Timestamp of last update            | timestamp without time zone |

### Utilisateur

Table name: **utilisateurs**

| **Field Name**      | **Label**        | **Description**                                                                      | **Data Type**                        |
| ------------------- | ---------------- | ------------------------------------------------------------------------------------ | ------------------------------------ |
| id                  |                  | Unique identifier pour chaque utilisateur                                                      | Integer pk                           |
| name                | Full Name        | Name of le utilisateur                                                                     | Character varying                    |
| gender              | Gender           | Gender of le utilisateur                                                                   | Character varying                    |
| username            | Username         | Username of le utilisateur                                                                 | Character varying                    |
| email               | Email            | Email address of le utilisateur                                                            | Character varying                    |
| password            | Password         | Encrypted Password of le utilisateur                                                       | Character varying                    |
| remember_token      |                  | Token utilise to remember le utilisateur (optionnel)                                           | Character varying                    |
| treatment_plant_id  | Treatment Plant  | Identifier pour le utilisateur's traitement plant (optionnel)                                 | Integer fk:fsm.treatment_plants(id)  |
| help_desk_id        | Centre d'assistance        | Identifier pour le utilisateur's help desk (optionnel)                                       | Integer fk:fsm.help_desks(id)        |
| service_provider_id | Service Provider | Identifier pour le utilisateur's service prestataire (optionnel)                                | Integer fk:fsm.service_providers(id) |
| user_type           | Utilisateur Type        | Type of utilisateur (Municipality\| Service Provider\| Treatment Plant\| Centre d'assistance\| Guest) | character varying                    |
| status              | Status           | Status of le utilisateur ( Active\| Inactive ), if set Inactive, systeme access is revoked. | Integer (DEFAULT 1)                  |
| created_at          |                  | Timestamp when le record was last updated (Auto Fill, Hidden)                       | Timestamp                            |
| updated_at          |                  | Timestamp when le record was deleted (Auto Fill, Hidden)                            | Timestamp                            |
| deleted_at          |                  | Timestamp when le record was created (Auto Fill, Hidden)                            | Timestamp                            |

### Roles

Table name: **roles**

| **Field Name** | **Label** | **Description**                                                                | **Data Type**               |
| -------------- | --------- | ------------------------------------------------------------------------------ | --------------------------- |
| id             |           | Unique identifier pour chaque role                                                | integer pk                  |
| name           | Name      | Descriptive name pour le role                                                  | character varying           |
| guard_name     |           | Represents le authentication guard ( "web" or "api") associated avec le role | character varying           |
| created_at     |           | Timestamp when le record was last updated (Auto Fill, Hidden)                 | timestamp without time zone |
| updated_at     |           | Timestamp when le record was deleted (Auto Fill, Hidden)                      | timestamp without time zone |

**Lookup Table values pour roles**

| **ID** | **Name**                                         | **guard_name** |
| ------ | ------------------------------------------------ | -------------- |
| 1      | Super Admin                                      | web            |
| 2      | Municipality - Executive                         | web            |
| 3      | Municipality - Building Permit Department        | web            |
| 4      | Municipality - Enquete batimentaireor (Ward)          | web            |
| 5      | Municipality - Infrastructure Department         | web            |
| 6      | Municipality - Tax Department                    | web            |
| 7      | Municipality - Water Billing Unit                | web            |
| 8      | Municipality - Solid Waste Management Department | web            |
| 9      | Municipality - Sanitation Department             | web            |
| 10     | Municipality - IT Admin                          | web            |
| 11     | Municipality - Public Health Department          | web            |
| 12     | Service Provider - Admin                         | web            |
| 13     | Service Provider - Vidange Operator             | web            |
| 14     | Service Provider - Centre d'assistance                     | web            |
| 15     | Municipality - Centre d'assistance                         | web            |
| 16     | Treatment Plant - Admin                          | web            |
| 17     | Guest                                            | web            |

### Permissions

Table name: **permissions**

| **Field Name** | **Description**                                                           | **Data Type**               |
| -------------- | ------------------------------------------------------------------------- | --------------------------- |
| id             | Unique identifier pour chaque role                                           | integer pk                  |
| name           | Descriptive name pour le role                                             | character varying           |
| group          | Group of Permissions based on Modules of IMIS                             | character varying           |
| type           | Type of permission ( Add\| View \| Edit \| Delete \| etc)                 | character varying           |
| guard_name     | Represents le authentication guard associated avec le role ( web\| api) | character varying           |
| created_at     | Timestamp when le record was last updated (Auto Fill, Hidden)            | timestamp without time zone |
| updated_at     | Timestamp when le record was deleted (Auto Fill, Hidden)                 | timestamp without time zone |

Relational Tables

Table name: model_has_permissions

| **Field Name** | **Description**                           | **Data Type**                      |
| -------------- | ----------------------------------------- | ---------------------------------- |
| permission_id  | Foreign key referencing permissions tableau | Integer pk fk:auth.permissions(id) |
| model_type     | Type of model / utilisateurs                     | character varying pk               |
| model_id       | Foreign key referencing utilisateurs tableau       | Integer pk fk:auth.utilisateurs(id)       |

**Composite Primary Key:** Composite Primary Key: (permission_id, model_type, model_id)

Table name: **model_has_roles**

| **Field Name** | **Description**                     | **Data Type**                |
| -------------- | ----------------------------------- | ---------------------------- |
| role_id        | Foreign key referencing roles tableau | Integer pk fk:auth.roles(id) |
| model_type     | Type of model / utilisateurs               | character varying pk         |
| model_id       | Foreign key referencing utilisateurs tableau | Integer pk fk:auth.utilisateurs(id) |

**Composite Primary Key:** (role_id, model_type, model_id)

Table name: **role_has_permissions**

| **Field Name** | **Description**                           | **Data Type**                      |
| -------------- | ----------------------------------------- | ---------------------------------- |
| permission_id  | Foreign key referencing permissions tableau | Integer pk fk:auth.permissions(id) |
| role_id        | Foreign key referencing roles tableau       | Integer pk fk:auth.roles(id)       |

**Composite Primary Key:** Composite Primary Key: (permission_id, role_id)

## Language

Nom du schema: langue

Data Tables

Table name:langue

| Field Name | Label             | Description                                                        | Data Type                |
| ---------- | ----------------- | ------------------------------------------------------------------ | ------------------------ |
| Id         |                   | A unique identifier pour chaque langue                              | integer                  |
| name       | Name              | Le name of le langue                                           | character varying(255)   |
| code       | Code              | Unique identifier also utilise in translates tableau as  a foreign key | character varying(255)   |
| status     | Status            | Boolean indicating status of langue                              | boolean                  |
| created_at |                   | Timestamp when le record was created(Auto Fill , Hidden)          | timestamp avec time zone |
| updated_at | Code              | Timestamp when le record was last updated(Auto Fill , Hidden)     | timestamp avec time zone |
| deleted_at | character varying | Timestamp when le record was deleted(Auto Fill , Hidden)          | timestamp avec time zone |


Data Tables

Table name:translates


| Field Name  | Description                                                    | Data Type                |
| ----------- | -------------------------------------------------------------- | ------------------------ |
| Id          | A unique identifier pour chaque translation                       | integer                  |
| key         | Collective sum of text , pages, et group column               | character varying(255)   |
| name        | Code de langue tableau                                       | character varying(255)   |
| text        | Le translated text                                            | text                     |
| pages       | Page where le text will be utilise                               | character varying(255)   |
| group       |                                                                | character varying(255)   |
| platform_at | Indicates which platform le text will be utilise (mobile/web)    | character varying(255)   |
| load        |                                                                | boolean                  |
| created_at  | Timestamp when le record was created(Auto Fill , Hidden)      | timestamp avec time zone |
| updated_at  | Timestamp when le record was last updated(Auto Fill , Hidden) | timestamp avec time zone |

# Tables diverses

# Migrations

Schema name: **Public**

Table name: **migrations**

Le migrations tableau is utilise to keep track of which migrations have been applied to your base de donnees. Ce tableau is automatically created when you run le php artisan migrate command pour le first time.

| **Field Name** | **Description**                                                                                                     | **Data Type**     |
| -------------- | ------------------------------------------------------------------------------------------------------------------- | ----------------- |
| id             | A unique identifier pour chaque record in le tableau                                                                    | integer pk        |
| migration      | Le name of le migration file ce has been applied                                                                | character varying |
| batch          | Le batch number ce le migration was run in (Multiple migrations run at once are assigned le same batch number) | integer           |

# Soft Delete

Schema name: **Public**

Table name: **revisions**
Ce tableau stores le principal revision records.

| **Field Name**    | **Description**                                                       | **Data Type**               |
| ----------------- | --------------------------------------------------------------------- | --------------------------- |
| id                | Le unique identifier pour chaque revision                               | bigint pk                   |
| revisionable_type | Le type of le model ce was revised (often le model’s class name) | character varying           |
| revisionable_id   | Le ID of le model ce was revised                                  | character varying           |
| user_id           | Le ID of le utilisateur who made le revision (if applicable)              | integer fk:auth.utilisateurs(id)   |
| key               | Le column of le tableau ce was revised                              | character varying           |
| old_value         | Le old values of le model’s attributes before le revision          | text                        |
| new_value         | Le nouveau values of le model’s attributes after le revision           | text                        |
| created_at        | Le timestamp when le revision was created                           | timestamp without time zone |
| updated_at        | Le timestamp when le revision was updated                           | timestamp without time zone |

# Spatial Refrencing Systems

Schema name: **Public**

Table name: **spatial_ref_sys**

Ce tableau is utilise in spatial bases de donnees, particularly in PostGIS, an extension pour PostgreSQL ce adds appui pour geographic objects. Ce tableau stores information about coordinate systemes et spatial reference systemes.

| **Field Name** | **Description**                                                                                                                | **Data Type**           |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------ | ----------------------- |
| srid           | Le Spatial Reference System Identifier (SRID) is a unique identifier pour le coordinate systeme                                | integer pk              |
| auth_name      | Le name of le authority ce defined le SRID (e.g., EPSG)                                                                   | character varying       |
| auth_srid      | Le SRID assigned by le authority                                                                                             | integer                 |
| srtext         | Le Well-Known Text (WKT) representation ( human-readable format ) of le spatial reference systeme                             | character varying(2048) |
| proj4text      | Le PROJ.4 representation is utilise pour defining projections et coordinate systemes in a format compatible avec le PROJ library | character varying(2048) |

# Journal d'authentification

Schema name: **Public**

Table name: **authentication_log**

Ce tableau is utilise to log information about utilisateur authentication activities. It is not default authentication setup but is additional package utilise to track authentication-lies events.

| **Field Name** | **Description**                                                                               | **Data Type**         |
| -------------------- | --------------------------------------------------------------------------------------------------- | --------------------------- |
| id                   | A unique identifier pour chaque log entry                                                              | bigint pk                   |
| authenticatable_type | Le type of le model ce was involved in le authentication event (often le model’s class name) | character varying           |
| authenticatable_id   | Le ID of le specific instance of le model ce was involved in le authentication event          | bigint                      |
| ip_address           | Le IP address de which le authentication attempt was made                                       | character varying           |
| user_agent           | Le utilisateur agent string de le client making le authentication request                             | text                        |
| login_at             | A timestamp indicating when le authentication event occurred                                       | timestamp without time zone |
| logout_at            | A timestamp indicating when le log entry was last updated (optionnel)                               | timestamp without time zone |

# Session Log

Schema name: **Public**

Table name: **sessions**

Ce tableau is utilise to log information about utilisateur's session activities. It is le laravels default session tracking mechanism, avec le addition of user_id to track chaque utilisateur's session.
In addition to ce, le session pour le particular utilisateur is cleared when their password is updated to ensure tous autres browsers running avec le old password is logged out.

| **Field Name** | **Description**                                                                                        | **Data Type**                  |
| -------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------ |
| id                   | Primary key. A unique identifier pour le session. Typically le session ID.                                  | string                               |
| user_id              | Foreign key referencing le id column in le utilisateurs tableau. Represents le authenticated utilisateur pour le session. | unsignedBigInteger fk:auth.utilisateurs(id) |
| ip_address           | Stores le utilisateur's IP address associated avec le session. Can store IPv4 or IPv6 addresses.                  | string(45)                           |
| user_agent           | Contient information about le browser or client utilise to access le application.                             | text                                 |
| payload              | Serialized session donnees, including tous variables stocke in le session.                                      | text                                 |
| last_activity        | Unix timestamp indicating le last time le session was active. Utilise to track session expiration.            | integer                              |
