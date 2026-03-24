Version : V1.0.0

# Documentation API

APIs are logically grouped et stocke within multiple controllers to ensure a clear separation of concerns et maintainability. Chaque controller is responsible pour managing a specific set of lies endpoints, providing a structured approche to API developpement.

## AuthController

### App Login

| URL          | {Base_URL}/api/login              |          |                   |
| ------------ | --------------------------------- | -------- | ----------------- |
| Methode       | POST                              |          |                   |
| En-tetes      | Header                            | Type     | Obligatoire/Optionnel |
| Content-Type | application/x-www-form-urlencoded | obligatoire |                   |
| Accept       | application/json                  |          |                   |

Parametres POST

| Parametre | Type   | Obligatoire/Optionnel |
| --------- | ------ | ----------------- |
| email     | string | obligatoire          |
| password  | string | obligatoire          |

Reponse en cas de succes

{

"status": true,

"message": "User Logged In Successfully.",

"token": "",

"data": {

"name": "",

"gender": "",

"treatment_plant": "",

"help_desk": "",

"service_provider": "",

"permissions": {

"building-survey": ,

"save-emptying-service":

}

}

}

Reponse en cas d'erreur

{

"status": false,

"message": "Email & Password does not match with our records."

}

### App Logout

| URL           | {Base_URL}/api/logout             |          |                   |
| ------------- | --------------------------------- | -------- | ----------------- |
| Methode        | POST                              |          |                   |
| En-tetes       | Header                            | Type     | Obligatoire/Optionnel |
| Authorization | Bearer {access_token}             | obligatoire |                   |
| Content-Type  | application/x-www-form-urlencoded | obligatoire |                   |
| Accept        | application/json                  | obligatoire |                   |

Parametres POST

Reponse en cas de succes

{

"success": true,

"message": "Logged out Successfully."

}

## ApiServiceController

### GET application info de application ID

| URL           | {Base_URL}/api/application/{application_id} |          |                   |
| ------------- | ------------------------------------------- | -------- | ----------------- |
| Methode        | GET                                         |          |                   |
| En-tetes       | Header                                      | Type     | Obligatoire/Optionnel |
| Authorization | Bearer {access_token}                       | obligatoire |                   |
| Content-Type  | application/x-www-form-urlencoded           | obligatoire |                   |
| Accept        | application/json                            | obligatoire |                   |

Parametres GET

{application_id}

Reponse en cas de succes

{

"success": true,

"data": {

"id": ,

"application_date": "",

"road_code": "",

"containment_id": "",

"approved_status": ,

"emptying_status": ,

"feedback_status": ,

"customer_name": "",

"ward": ,

"address": ,

"customer_contact": ,

"applicant_name": "",

"user_id": ,

"service_provider_id": ,

"customer_gender": "",

"applicant_gender": "",

"created_at": "",

"updated_at": ,

"deleted_at": ,

"proposed_emptying_date": "",

"house_number": "",

"applicant_contact": ,

"sludge_collection_status": ,

"emergency_desludging_status": ,

"buildings": {

"bin": "",

"ward": ,

"road_code": "",

"address": ,

"structure_type_id": ,

"estimated_area": "",

"floor_count": ,

"household_served": ,

"population_served": ,

"functional_use_id": ,

"use_category_id": ,

"office_business_name": ,

"building_associated_to": ,

"water_source_id": ,

"well_presence_status": "",

"toilet_status": "",

"toilet_count": ,

"sewer_code": ,

"drain_code": ,

"surveyed_status": ,

"surveyed_date": ,

"verification_required": ,

"geom": "",

"tax_code": "",

"user_id": ,

"created_at": "",

"updated_at": "",

"deleted_at": ,

"house_number": "",

"desludging_vehicle_accessible": ,

"water_customer_id": ,

"swm_customer_id": ,

"sanitation_system_type_id": ,

"sanitation_system_technology_id": ,

"construction_year": ,

"distance_from_well": ,

"no_of_ihhl_yes": ,

"no_of_ihhl_no": ,

"mapped_functional_use_id": ,

"lic_id": ,

"structure_type": {

"id": ,

"type": "",

"created_at": "",

"updated_at": "",

"deleted_at":

},

"functional_use": {

"id": ,

"name": "",

"created_at": "",

"updated_at": "",

"deleted_at":

},

"sanitation_system_types": {

"id": ,

"type": "",

"created_at": ,

"updated_at": ,

"deleted_at":

},

"owners": {

"id": ,

"bin": "",

"owner_name": "",

"owner_gender": "",

"owner_contact": ,

"created_at": ,

"updated_at": ,

"deleted_at": ,

"tax_code": ""

}

},

"service_provider": {

"id": ,

"company_name": "",

"ward": ,

"company_location": "",

"email": "",

"contact_person": "",

"contact_number": ,

"geom": ,

"created_at": "",

"updated_at": "",

"deleted_at": ,

"total_trips": ,

"contact_gender": "",

"status":

},

"feedback": {

"id": ,

"application_id": ,

"comments": "",

"fsm_service_quality": ,

"customer_name": "",

"customer_number": ,

"customer_gender": "",

"wear_ppe": ,

"user_id": ,

"created_at": ,

"updated_at": ,

"deleted_at": ,

"service_provider_id":

}

},

"message": "Application Details."

}

Reponse en cas d'erreur

{

"status": false,

"message": "No Application found for ID 9999."

}

### GET containment(s) info de application ID

| URL           | {Base_URL}/api/containment/{application_id} |          |                   |
| ------------- | ------------------------------------------- | -------- | ----------------- |
| Methode        | GET                                         |          |                   |
| En-tetes       | Header                                      | Type     | Obligatoire/Optionnel |
| Authorization | Bearer {access_token}                       | obligatoire |                   |
| Content-Type  | application/x-www-form-urlencoded           | obligatoire |                   |
| Accept        | application/json                            | obligatoire |                   |

Parametres GET

{application_id}

Reponse en cas de succes

{

"success": true,

"data": [

{

"id": "",

"location": "",

"size": "",

"pit_number": ,

"pit_diameter": ,

"tank_length": ,

"tank_width": ,

"depth": ,

"septic_criteria": ,

"construction_date": "",

"buildings_served": ,

"emptied_status": ,

"last_emptied_date": "",

"next_emptying_date": "",

"no_of_times_emptied": ,

"geom": "",

"surveyed_at": ,

"verification_required": ,

"user_id": ,

"created_at": ,

"updated_at": ,

"deleted_at": ,

"type": "",

"population_served": ,

"household_served": ,

"toilet_count": ,

"distance_closest_well":

}

],

"message": "Containment details for application 1"

}

Reponse en cas d'erreur

{

"status": false,

"message": "No containment found or application with ID 9999 doesn't exist."

}

### GET service prestataires

| URL           | {Base_URL}api/service-prestataires   |          |                   |
| ------------- | --------------------------------- | -------- | ----------------- |
| Methode        | GET                               |          |                   |
| En-tetes       | Header                            | Type     | Obligatoire/Optionnel |
| Authorization | Bearer {access_token}             | obligatoire |                   |
| Content-Type  | application/x-www-form-urlencoded | obligatoire |                   |
| Accept        | application/json                  | obligatoire |                   |

Reponse en cas de succes

{

"success": true,

"data": {

"1": "Cleaning Services PVT.LTD"

},

"message": "Service Providers."

}

Reponse en cas d'erreur

## BuildingSurveyController

### GET WMS layer of batiments

| URL           | {Base_URL}/api/wms/batiments      |          |                   |
| ------------- | --------------------------------- | -------- | ----------------- |
| Methode        | GET                               |          |                   |
| En-tetes       | Header                            | Type     | Obligatoire/Optionnel |
| Authorization | Bearer {access_token}             | obligatoire |                   |
| Content-Type  | application/x-www-form-urlencoded | obligatoire |                   |
| Accept        | application/json                  | obligatoire |                   |

Reponse en cas de succes

{

"success": true,

"baseUrl": "{base_url:8080}/geoserver/{workspace}/",

"data": {

"buildings": "wms?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&FORMAT=image/png&TRANSPARENT=true&LAYERS={workspace}:{layer_name}&TILED=true&STYLES={workspace}:{style_name}&FORMAT_OPTIONS=dpi:113&WIDTH={width}&HEIGHT={height}&srs=EPSG:900913&BBOX={minX},{minY},{maxX},{maxY}"

},

"message": "WMS layer for buildings."

}

### GET WMS layer of containments

| URL           | {Base_URL}/api/wms/containments   |          |                   |
| ------------- | --------------------------------- | -------- | ----------------- |
| Methode        | GET                               |          |                   |
| En-tetes       | Header                            | Type     | Obligatoire/Optionnel |
| Authorization | Bearer {access_token}             | obligatoire |                   |
| Content-Type  | application/x-www-form-urlencoded | obligatoire |                   |
| Accept        | application/json                  | obligatoire |                   |

Reponse en cas de succes

{

"success": true,

"baseUrl": "{base_url:8080}/geoserver/{workspace}/",

"data": {

"containments": "wms?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&FORMAT=image/png&TRANSPARENT=true&LAYERS={workspace}:{layer_name}&TILED=true&STYLES={workspace}:{style_name}&FORMAT_OPTIONS=dpi:113&WIDTH={width}&HEIGHT={height}&srs=EPSG:900913&BBOX={minX},{minY},{maxX},{maxY}"

},

"message": "WMS layer for containments."

}

### GET WMS layer of wards

| URL           | {Base_URL}/api/wms/wards          |          |                   |
| ------------- | --------------------------------- | -------- | ----------------- |
| Methode        | GET                               |          |                   |
| En-tetes       | Header                            | Type     | Obligatoire/Optionnel |
| Authorization | Bearer {access_token}             | obligatoire |                   |
| Content-Type  | application/x-www-form-urlencoded | obligatoire |                   |
| Accept        | application/json                  | obligatoire |                   |

Reponse en cas de succes

{

"success": true,

"baseUrl": "{base_url:8080}/geoserver/{workspace}/",

"data": {

"wards": "wms?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&FORMAT=image/png&TRANSPARENT=true&LAYERS={workspace}:{layer_name}&TILED=true&STYLES={workspace}:{style_name}&FORMAT_OPTIONS=dpi:113&WIDTH={width}&HEIGHT={height}&srs=EPSG:900913&BBOX={minX},{minY},{maxX},{maxY}"

},

"message": "WMS layer for wards."

}

### GET WMS layer of roads

| **URL**     | {Base_URL}/api/wms/roads          |                |                             |
| ----------------- | --------------------------------- | -------------- | --------------------------- |
| **Methode**  | GET                               |                |                             |
| **En-tetes** | **Header**                  | **Type** | **Obligatoire/Optionnel** |
| Authorization     | Bearer {access_token}             | obligatoire       |                             |
| Content-Type      | application/x-www-form-urlencoded | obligatoire       |                             |
| Accept            | application/json                  | obligatoire       |                             |

**Reponse en cas de succes**

{

"success": true,

"baseUrl": "{base_url:8080}/geoserver/{workspace}/",

"data": {

"roads": "wms?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&FORMAT=image/png&TRANSPARENT=true&LAYERS={workspace}:{layer_name}&TILED=true&STYLES={workspace}:{style_name}&FORMAT_OPTIONS=dpi:113&WIDTH={width}&HEIGHT={height}&srs=EPSG:900913&BBOX={minX},{minY},{maxX},{maxY}"

},

"message": "WMS layer for roads."

}

### POST Save batiment enquete

| URL           | {Base_URL}/api/save-batiment      |          |                   |
| ------------- | --------------------------------- | -------- | ----------------- |
| Methode        | POST                              |          |                   |
| En-tetes       | Header                            | Type     | Obligatoire/Optionnel |
| Authorization | Bearer {access_token}             | obligatoire |                   |
| Content-Type  | application/x-www-form-urlencoded | obligatoire |                   |
| Accept        | application/json                  | obligatoire |                   |

Parametres POST

| Parametre      | Type        | Required? |
| -------------- | ----------- | --------- |
| bin            | varchar     | Yes       |
| tax_code       | varchar     | Yes       |
| collected_date | Date(Y-m-d) | Yes       |
| kml            | .kml File   | Yes       |

Reponse en cas de succes

{

"status": true,

"message": "Building Survey is uploaded successfully."

}

## VidangeServiceController

### GET assessed applications (pour emptying service)

| URL           | {Base_URL}/api/assessed-applications |          |                   |
| ------------- | ------------------------------------ | -------- | ----------------- |
| Methode        | GET                                  |          |                   |
| En-tetes       | Header                               | Type     | Obligatoire/Optionnel |
| Authorization | Bearer {access_token}                | obligatoire |                   |
| Content-Type  | application/x-www-form-urlencoded    | obligatoire |                   |
| Accept        | application/json                     | obligatoire |                   |

Reponse en cas de succes

{

"success": true,

"data": {

"applications": []

},

"message": "Applications"

}

### GET traitement plants (place of disposal)

| URL           | {Base_URL}api/traitement-plants    |          |                   |
| ------------- | --------------------------------- | -------- | ----------------- |
| Methode        | GET                               |          |                   |
| En-tetes       | Header                            | Type     | Obligatoire/Optionnel |
| Authorization | Bearer {access_token}             | obligatoire |                   |
| Content-Type  | application/x-www-form-urlencoded | obligatoire |                   |
| Accept        | application/json                  | obligatoire |                   |

Reponse en cas de succes

{

"success": true,

"data": {

"treatment-plants": [

{

"id": ,

"name": ""

}

]

},

"message": "Treatment Plants"

}

### GET vacutugs

| URL           | {Base_URL}/api/vacutugs           |          |                   |
| ------------- | --------------------------------- | -------- | ----------------- |
| Methode        | GET                               |          |                   |
| En-tetes       | Header                            | Type     | Obligatoire/Optionnel |
| Authorization | Bearer {access_token}             | obligatoire |                   |
| Content-Type  | application/x-www-form-urlencoded | obligatoire |                   |
| Accept        | application/json                  | obligatoire |                   |

Reponse en cas de succes

{

"success": true,

"data": [],

"message": "Vacutugs"

}

### GET drivers

| URL           | {Base_URL}/api/drivers            |          |                   |
| ------------- | --------------------------------- | -------- | ----------------- |
| Methode        | GET                               |          |                   |
| En-tetes       | Header                            | Type     | Obligatoire/Optionnel |
| Authorization | Bearer {access_token}             | obligatoire |                   |
| Content-Type  | application/x-www-form-urlencoded | obligatoire |                   |
| Accept        | application/json                  | obligatoire |                   |

Reponse en cas de succes

{

"success": true,

"data": [],

"message": "Drivers."

}

### GET emptiers

| URL           | {Base_URL}/api/emptiers           |          |                   |
| ------------- | --------------------------------- | -------- | ----------------- |
| Methode        | GET                               |          |                   |
| En-tetes       | Header                            | Type     | Obligatoire/Optionnel |
| Authorization | Bearer {access_token}             | obligatoire |                   |
| Content-Type  | application/x-www-form-urlencoded | obligatoire |                   |
| Accept        | application/json                  | obligatoire |                   |

Reponse en cas de succes

{

"success": true,

"data": [],

"message": "Emptiers."

}

### POST Save emptying service

| URL           | {Base_URL}/api/save-emptying      |          |                   |
| ------------- | --------------------------------- | -------- | ----------------- |
| Methode        | POST                              |          |                   |
| En-tetes       | Header                            | Type     | Obligatoire/Optionnel |
| Authorization | Bearer {access_token}             | obligatoire |                   |
| Content-Type  | application/x-www-form-urlencoded | obligatoire |                   |
| Accept        | application/json                  | obligatoire |                   |

Parametres POST

| Parametre         | Type             | Required? |
| ----------------- | ---------------- | --------- |
| volume_of_sludge  | Double precision | Yes       |
| vacutug_id        | integer          | Yes       |
| place_of_disposal | integer          | Yes       |
| driver            | varchar          | Yes       |
| emptier1          | varchar          | Yes       |
| emptier1          | varchar          | No        |
| start_time        | Time (HⓂ️s)    | Yes       |
| end_time          | Time (HⓂ️s)    | Yes       |
| no_of_trips       | Double precision | Yes       |
| receipt_number    | varchar          | Yes       |
| total_cost        | numeric          | Yes       |
| application_id    | integer          | Yes       |
| house_image       | Image file       | Yes       |
| receipt_image     | Image file       | Yes       |

Reponse en cas de succes

{

"success": true,

"message": "Emptying service saved successfully."

}
