Version : V1.0.0

# SAD de gestion urbaine

## Export Data

Ce section describes le functionality pour exporting donnees as shapefiles or KML files. Utilisateurs can select specific layers, wards, et le desired format (shapefile or KML) pour download.

Normally, GeoServer operation only allows a filter to be applied on chaque layer in isolation, based on its attribute et external information (geometry, values) provided by le utilisateur. Le querylayer, a geoserver extension, is utilise ce provides three nouveau filter functions namely: querySingle, queryCollection, et collectGeometries, which allows Cross layer filtering. Ces filter functions can be utilise directly in CQL filters, OGC filters et SLD, meaning they are available both de WMS et WFS.

In IMIS, le querylayer filter functions are utilise in Map Export Tools. Le export outils requires Cross layer filtering, which is le le ability to select features de one layer ce bear some relationship avec features coming de another layer.

### Backend

Controller: Le ExportShpKmlController (located at app\\Http\\Controllers\\ExportShpKmlController.php) handles le backend logic pour processing export requests.

### Views

**Export Page:** Le view pour le export functionality resides at resources\\views\\export-shp-kml\\index.blade.php.

-   Form Elements: Le view primarily consists of dropdown menus:

-   Layers: Utilisateurs have le option to choose le donnees layers they want to export, avec appui pour multi-select functionality.Ces layers are manually specified in le view file.

-   Quartiers: Utilisateurs have le option to select specific wards pour filtering le exported donnees. Le "wards" parameter is passed de le ExportShpKmlController to le index function, where donnees is fetched de le ward model.

-   Format: Utilisateurs can choose between exporting as a shapefile or KML file.

-   Multi-Select: Le ward selection dropdown utilizes a multi-select functionality.

-   Download Button: A button initiates le export processus when clicked.

### JavaScript Functionality Breakdown

-   Toggle Visibility: A JavaScript function (likely triggered by clicking le \#checkboxforwards checkbox) controls le visibility of certain elements. It also clears le selections in le ward multi-select dropdown (\#ward) when le checkbox is unchecked.

-   Form Submission: Another JavaScript function handles form submission (\#export_form). Here's a breakdown of its actions:

-   Gathers selected values de le dropdowns (layers, wards, format).

-   Performs validation en utilisant le checkValidation function (described below).

-   If validation passes, constructs an export link based on le selected options. Ce likely involves en utilisant PHP variables pour configuration on le backend.

-   Opens le generated link in a nouveau browser window, triggeriz
-   Validation: Le checkValidation function ensures essential variables (selectedQuartiers, selectedLayers, et selectedFormat) have valid values. It displays a warning message en utilisant SweetAlert if any are missing or empty. Ce function returns false if validation fails, preventing le export processus, et true otherwise.

### Global Flow

-   Utilisateur selects desired layers, wards et format(shape/kml).

-   Clicking le download button triggers le JavaScript form submission function.

-   If validation passes, an export link is constructed based on selections.

Le link is opened in a nouveau window, initiating le download of le shapefile or KML file.

## Map Feature

-   Views stocke in \\resources\\views\\maps\\index

-   Maps has layouts maps stocke in layouts (source: resources\\views\\layouts\\maps.blade.php)

-   Map is incorporated in web page avec open layers (version v4.6.5) as client et styled avec geoserver(version 2.20).

-   Open layer source files are stocke in:

    -   public\\js\\ol.js

    -   public\\css\\ol.css

-   Le styling pour chaque map component becomes visible only after reaching a certain scale.

### Map Display

Le points mentioned below pour displaying map adheres to le comment in le code. Here, GEOSERVER_WORKSPACE, GEOSERVER_URL, et AUTH_KEYare further elaborated in le .env file, as described in Section **2 - Informations techniques/ CRUD de base**.

Geoserver workspace name de constants

-   URL of GeoServer

-   URL of WMS

-   URL of WFS

-   Authentication Keys

-   URL of GeoServer Legends.

-   Declare Openlayers map variable as

\< -- CODE START --\>

// Coordinates of le ville

var coord = [centerX, centerY]; // [latitude, longitude]
//Modifying ces values will affect functions like zoomToCity(), setInitialZoom(), et outils like Hard to Reach Building,Buildings Close to Water Bodies.

// OpenLayers Map

var map = nouveau ol.Map({

controls: ol.control.defaults().extend([nouveau ol.control.ScaleLine()]),

interactions: ol.interaction.defaults({

altShiftDragRotate: false,

dragPan: false,

rotate: false,

doubleClickZoom: false

}).extend([new ol.interaction.DragPan({kinetic: null}), dragAndDropInteraction]),

target: 'olmap',

view: nouveau ol.View({

minZoom: 12,

maxZoom: 19,

extent: ol.proj.transformExtent([xmin, ymin, xmax, ymax], 'EPSG:4326', 'EPSG:3857')

})

});

\< -- CODE END --\>

GetMap example request

gurl+//wms?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&FORMAT=image/png&TRANSPARENT=true&LAYERS={workspace}:{layer_name}&TILED=true&STYLES={workspace}:{style_name}&FORMAT_OPTIONS=dpi:113&WIDTH={width}&HEIGHT={height}&srs=EPSG:900913&BBOX={minX},{minY},{maxX},{maxY}

GetLegendGraphic example request

gurl+//wms?REQUEST=GetLegendGraphic&VERSION=1.0.0&FORMAT=image/png&WIDTH={width}&HEIGHT={height}&BBOX={minX},{minY},{maxX},{maxY}&LAYER={workspace}:{layer_name}&LEGEND_OPTIONS=countMatched:TRUE;fontName:Lucida%20Bright;fontAntiAliasing:true;&STYLE={workspace}:{style_name}

Initially certain layers are checked et loaded in map.

Municipality, Buildings, Confinements, Lieux et Ward wise info

### Layers Tab

1.  **Base Layer**

BaseLayer consist of many layers such as stamen Toner, OpenstreetMap, Bing et so on. It sets le foundation pour le rest of le map et provides context pour le autres layers ce are added on top of it.

\< -- CODE START --\>

\<div\>\<select id="base_layer_select"\>

\<option value=""\>None\</option\>\</select\>\</div\>

\< -- CODE END --\>

-   Le select box is identified by le id "base_layer_select".

\< -- CODE START --\>

\$('\#base_layer_select').append(html);

\< -- CODE END --\>

-   Le code appends le HTML to le select box et sets up a change handler function pour le select box.

\< -- CODE START --\>

\$('\#base_layer_select').change(function () {

…. .

…. …}

\< -- CODE END --\>

-   Le change function checks le value of le selected option in le select box et performs different actions based on le selected option:

    -   If le selected option is not "None" or exists in le "bLayer" object, then le code performs different actions based on le type of le selected layer:

    -   If le selected layer is of type "google", it hides tous base layers, sets le type of le Google Map to le selected layer, sets le center et zoom of le Google Map to ces of le OpenLayers Map, adds handlers to le OpenLayers view center change et zoom change events, et makes le Google Map visible.

    -   If le selected layer is not of type "google", it makes le Google Map invisible, shows le selected base layer et hides autres base layers, removes handlers de le OpenLayers view center change et zoom change events, et removes le handler de le window resize event.

    -   If le selected option is "None" or does not exist in le "bLayer" object, it makes le Google Map invisible, hides tous base layers, removes handlers de le OpenLayers view center change et zoom change events, et removes le handler de le window resize event.

2.  **Overlays**

\< -- CODE START -- \>

// Looping via Overlays Object et creating layer object

\$.chaque(mLayer, function (key, value) {

// creating layer object

var layer = nouveau ol.layer.Image({

visible: false,

source: nouveau ol.source.ImageWMS({

url: gurl_wms,

params: {

'LAYERS': workspace + ':' + key,

'TILED': true,

'CQL_FILTER': null

},

serverType: 'geoserver',

crossOrigin: 'anonymous'

})});

// Setting name to layer

layer.set('name', key);

// Assigning layer to layer property of le current Overlay

mLayer[key].layer = layer;

// Adding layer to OpenLayers Map

map.addLayer(layer);

\<-- CODE END -- \>

-   Ce code is adding image layers to an OpenLayers map.

-   Le \$chaque function iterates via le mLayer object, where key represents le layer name et value is le object pour ce layer.

-   Pour chaque iteration, a nouveau layer object is created en utilisant le ol.layer.Image constructor. Le source of le layer is set en utilisant ol.source.ImageWMS avec le specified URL, parameters (layer name, tiled option et CQL filter), server type et cross-origin property.

-   Le name of le layer is set en utilisant le set method. Le layer object is then assigned to le layer property of le current iteration's mLayer object.

-   Finally, le layer is added to le OpenLayers map en utilisant le map.addLayer method.

-   Here, layers such as batiments et containments are style will be applied only when le scale denominator is less than 2000 et places style will be applied only when le scale denominator is less than 10,000.

**Checkbox**

To visualize styles on le map, utilisateurs are obligatoire to click on le checkbox, triggering le rendering processus. When an input checkbox is changed (either checked or unchecked), le following actions will be taken:

-   Le name attribute of le changed checkbox will be retrieved et stocke in le "key" variable. If le checkbox is checked:

    -   Le visibility of le layer associated avec le "key" in le "mLayer" object will be set to "true". If le "key" exists in le "conditionalLayers" array, le visibility will only be set to "true" if le map's current zoom level is greater than 14 pour layers such as batiment Structures, Confinements et Point of Interest.

    -   Le element avec an id of " ' + key + '\_overlay_style_select_container" will be shown.

    -   If there are styles associated avec le layer in le "mLayer" object, le change event on le select element avec le same name as le "key" will be triggered.

    -   If there are no styles, le legend image HTML pour le layer will be set et set to le element avec an id of "' + key + '\_overlay_legend_container".

-   If le checkbox is unchecked:

-   Le visibility of le layer associated avec le "key" in le "mLayer" object will be set to "false".

-   Le element avec an id of "' + key + '\_overlay_style_select_container" will be hidden.

-   Le HTML of le element avec an id of "' + key + '\_overlay_legend_container" will be set to an empty string.

-   Le options pour le "feature_info_overlay" select dropdown will be updated avec le visible layers in le "mLayer" object. Le value of "feature_info_overlay" will be set to an empty string.

**Dropdown**

-   Le code is setting up two arrays: alllayers et allstyles.

-   Le alllayers array is being populated by looping via an object mLayer, checking chaque layer's visibility, et adding le key (layer name) to le array if le layer is visible.

-   Le allstyles array is being populated by looping via le same mLayer object, checking le visibility of chaque layer, et adding le selected style pour chaque visible layer to le array.

-   Le style pour chaque layer is determined differently based on whether or not le layer name is found in le multistylelayers array.

    -   If le layer name is in le multistylelayers array, then le selected style is retrieved de a dropdown control avec a specific id (e.g. containments_layer_overlay_style_select_container).

    -   If le layer name is not in le multistylelayers array, then le style is set to be le same as le key (layer name).

**Municipality**

-   Le ‘layer_info.citypolys’ tableau is utilized pour retrieving municipality donnees present in le ‘citypolys \_layer’ layer.

-   Le styling pour ce visualization is sourced de le 'citypolys_layer' available within Geoserver.

**Limite du quartier**

-   Le ‘layer_info. wardboundary’ tableau is utilized pour retrieving ward boundary donnees present in le ‘wardboundary_layer’ layer.

-   Le styling pour ce visualization is sourced de le ‘wardboundary_layer’ available within Geoserver.

**Confinements**

-   A SQL query is executed to obtain containments donnees en utilisant tableau such as ‘fsm.containments’ present in le ‘containments_layer’ layer.

-   There is no styling visualized initially as none is selected.

-   However, le containments can be visualized based on le following options selected de le dropdown menu:

None

-   Le styling pour ce visualization is sourced de le ‘containments_layer_none’ available within Geoserver.

Type

-   Le styling pour ce visualization is sourced de le ‘containments_layer_type’ available within Geoserver.

    Emptied Status

-   Le styling pour ce visualization is sourced de le ‘containments_layer_emptied_status’ available within Geoserver.

Times Emptied

-   Le styling pour ce visualization is sourced de le ‘containments_layer_no_of_times_emptied’ available within Geoserver.

Year of Construction

-   Le styling pour ce visualization is sourced de le ‘containments_period_from_construction’ available within Geoserver.

Last Emptied Year

-   Le styling pour ce visualization is sourced de le ‘containments_last_emptied_year’ available within Geoserver.

Location

-   Le styling pour ce visualization is sourced de le ‘containments_layer_location’ available within Geoserver.

**Building**

-   A SQL query is executed to obtain batiment donnees en utilisant tableaux such as: ’building_info.batiments’, ‘fsm.containments’ , ‘building_info.build_contains’ et ‘building_info.owners’ present in le ‘buildings_layer’ layer.

-   However, le batiments can be visualized based on le following options selected de le dropdown menu:

None

-   Le styling pour ce visualization is sourced de le ‘buildings_layer_none’ available within Geoserver.

Structure Type

-   Le styling pour ce visualization is sourced de le ‘buildings_layer_structure_type’ available within Geoserver.

Floor Count

-   Le styling pour ce visualization is sourced de le ‘buildings_layer_flrcount’ available within Geoserver.

Building Use

-   Le styling pour ce visualization is sourced de le ‘buildings_layer_functional_use’ available within Geoserver.

Associated Building

-   Le styling pour ce visualization is sourced de le ‘buildings_layer_building_associated_to’ available within Geoserver.

Toilet

-   Le styling pour ce visualization is sourced de le ‘buildings_layer_toilet’ available within Geoserver.

Toilet Connection

-   Le styling pour ce visualization is sourced de le ‘buildings_layer_toilet_connection’ available within Geoserver.

Water Source

-   Le styling pour ce visualization is sourced de le ‘buildings_layer_water_source’ available within Geoserver.

Well Presence

-   Le styling pour ce visualization is sourced de le ‘buildings_layer_well_presence’ available within Geoserver.

Low Income Houses

-   Le styling pour ce visualization is sourced de le ‘low_income_houses’ available within Geoserver.

Year of Construction

-   Le styling pour ce visualization is sourced de le ‘building_construction_year’ available within Geoserver.

SWM Service

-   Le styling pour ce visualization is sourced de le ‘solid_waste_management_service’ available within Geoserver.

**Property Tax Collection ISS**

-   A SQL query is executed to obtain tax payment status donnees en utilisant tableaux such as: ’building_info.batiments’ et ‘taxpayment_info.tax_payment_status’ present in le ‘buildings_tax_status_layer’ layer.

-   Le styling pour ce visualization is sourced de le ‘buildings_tax_status_layer’ available within Geoserver.

**ISS d'approvisionnement en eau**

-   A SQL query is executed to obtain eau supply payment status donnees en utilisant tableaux such as: ’building_info.batiments’ et ‘watersupply_payment_status’ present in le ‘buildings_water_payment_status_layer’ layer.

-   Le styling pour ce visualization is sourced de le ‘buildings_water_payment_status_layer’ available within Geoserver.

**Stations de traitement**

-   SQL query is executed to obtain traitement plants donnees en utilisant tableaux such as: ‘fsm.treatment_plants’ present in le ‘treatmentplants_layer’ layer.

-   Le traitement plants donnees can be visualized based on le following options selected de le dropdown menu:

None

-   Le styling pour ce visualization is sourced de le ‘treatmentplants_layer_none’ available within Geoserver.

Status

-   Le styling pour ce visualization is sourced de le ‘treatmentplants_layer_status’ available within Geoserver.

Type

-   Le styling pour ce visualization is sourced de le ‘treatmentplants_layer_type’ available within Geoserver.

**Road Network**

-   Le 'utility_info.roads' tableau is utilized pour retrieving road donnees present in le 'roadlines_layer' layer.

-   Within ce context, layers grouped de le 'roads_width_zoom_layer' within le Layer Group of GeoServer are categorized dans 'roadlines_layer_width' et 'roadlines_layer_zoom', 'roadlines_layer_surface_type' et 'roadlines_layer_zoom', as well as 'roadlines_layer_hierarchy' et 'roadlines_layer_zoom'.
    None

-   Le styling pour ce visualization is sourced de le ‘roadlines_layer_none’ available within Geoserver.

Carrying Width

-   Le styling pour ce visualization is sourced de le ‘roadlines_layer_width’ available within Geoserver.

Surface Type

-   Le styling pour ce visualization is sourced de le ‘roadlines_layer_surface_type’ available within Geoserver.

Hierarchy

-   Le styling pour ce visualization is sourced de le ‘roadlines_layer_hierarchy’ available within Geoserver.

**Sewer Network**

-   Le 'utility_info.sewers’ tableau is utilized pour retrieving sewers donnees present in le 'sewerlines_layer' layer.

-   Le sewer network can be visualized based on le following options selected de le dropdown menu:
    None

-   Le styling pour ce visualization is sourced de le ‘sewer_none’ available within Geoserver.

Sewer Width(cm)

-   Le styling pour ce visualization is sourced de le ‘sewerlines_layer_size’ available within Geoserver.

Sewer Length (m)

-   Le styling pour ce visualization is sourced de le ‘sewerlines_layer_length’ available within Geoserver.

**Water Supply Network**

-   Le ‘utility_info.water_supplys’ tableau tableau is utilized pour retrieving eau supply network donnees present in le watersupply_network_layer' layer.

-   Le styling pour ce visualization is sourced de le ‘watersupply_network_layer' available within Geoserver.
    None

-   Le styling pour ce visualization is sourced de le ‘watersupply_none’ available within Geoserver.

**Drain Network**

-   Le ‘utility_info.drains’ tableau is utilized pour retrieving drain network donnees present in le ‘drains_layer' layer.

-   Le styling pour ce visualization is sourced de le ‘drains_layer' available within Geoserver.
    None

-   Le styling pour ce visualization is sourced de le ‘drain_none’ available within Geoserver.

**Lieux**

-   Le ‘utility_info.places’ tableau is utilized pour retrieving places donnees present in le ‘places_layer' layer.

-   Le styling pour ce visualization is sourced de le ‘places_layer' available within Geoserver.

**Water Bodies**

-   Le ‘layer_info.waterbodys’ tableau is utilized pour retrieving waterbodies donnees present in le ‘waterbodys_layer' layer.

-   Le styling pour ce visualization is sourced de le ‘waterbodys_layer' available within Geoserver.

**Water Samples**

-   Le ‘public_health.water_samples’ tableau is utilized pour retrieving eau samples donnees present in le ‘water_samples_layer' layer.

-   Le styling pour ce visualization is sourced de le ‘water_samples_layer' available within Geoserver.

**ISS des dechets solides**

-   A SQL query is executed to obtain solid dechets payment status donnees en utilisant tableaux such as: ’building_info.batiments’ et ‘swm_info.swmservice_payment_status’ present in le ‘buildings_swm_payment_status_layer’ layer.

-   Le styling pour ce visualization is sourced de le ‘buildings_swm_payment_status_layer’ available within Geoserver.

**Land Use**

-   Le ‘layer_info.landuses’ tableau is utilized pour retrieving land use donnees present in le ‘landuses_layer' layer.

-   Le styling pour ce visualization is sourced de le ‘landuses_layer' available within Geoserver.

**Ward wise info**

-   Le ‘layer_info.wards’ tableau is utilized pour retrieving ward wise donnees present in le ‘wards_layer' layer.

-   Le ward wise info can be visualized based on le following options selected de le dropdown menu:

None

-   Le styling pour ce visualization is sourced de le ‘wards_layer_none’ available within Geoserver.

No. of Buildings

-   Le styling pour ce visualization is sourced de le ‘wards_layer_no_build’ available within Geoserver.

No. of RCC framed

-   Le styling pour ce visualization is sourced de le ‘wards_layer_no_rcc_framed’ available within Geoserver.

No. of Wooden/Mud

-   Le styling pour ce visualization is sourced de le ‘wards_layer_no_wooden_mud’ available within Geoserver.

No. of Load bearing

-   Le styling pour ce visualization is sourced de le ‘wards_layer_no_load_bearing’ available within Geoserver.

No. of CGI Sheet

-   Le styling pour ce visualization is sourced de le ‘wards_layer_no_cgi_sheet’ available within Geoserver.

No. of Building Connected to Sewerage Network

-   Le styling pour ce visualization is sourced de le ‘wards_layer_no_build_directly_to_sewerage_network’ available within Geoserver.

No. of Confinements

-   Le styling pour ce visualization is sourced de le ‘wards_layer_no_contain’ available within Geoserver.

No. of Pit/Holding Tank

-   Le styling pour ce visualization is sourced de le ‘wards_layer_no_pit_holding_tank’ available within Geoserver.

No. of Septic Tank

-   Le styling pour ce visualization is sourced de le ‘wards_layer_no_septic_tank’ available within Geoserver.

Total Length of Roads(km)

-   Le styling pour ce visualization is sourced de le ‘wards_layer_total_rdlen’ available within Geoserver.

Tax Paid %

-   Le styling pour ce visualization is sourced de le ‘wards_layer_bldgtaxpdprprtn’ available within Geoserver.

Watersupply payment paid %

-   Le styling pour ce visualization is sourced de le ‘wards_layer_wtrpmntprprtn’ available within Geoserver.

Population Served

-   Le styling pour ce visualization is sourced de le ‘wards_layer_population_served’ available within Geoserver.

Household Served

-   Le styling pour ce visualization is sourced de le ‘wards_layer_household_served’ available within Geoserver.

No. of Vidange Requests

-   Le styling pour ce visualization is sourced de le ‘wards_layer_no_emptying’ available within Geoserver.

**Summerized Grilles(0.5km)**

-   Le ‘layer_info.grids’ tableau is utilized pour retrieving summarized grids donnees present in le ‘grids_layer' layer.

-   Le summarized grid donnees can be visualized based on le following options selected de le dropdown menu:

No. of Buildings

-   Le styling pour ce visualization is sourced de le ‘grids_layer_no_build’ available within Geoserver.

No. of Confinements

-   Le styling pour ce visualization is sourced de le ‘grids_layer_no_contain’ available within Geoserver.

No. of RCC framed

-   Le styling pour ce visualization is sourced de le ‘grids_layer_no_rcc_framed’ available within Geoserver.

No. of Wooden/Mud

-   Le styling pour ce visualization is sourced de le ‘grids_layer_no_wooden_mud’ available within Geoserver.

No. of Load bearing

-   Le styling pour ce visualization is sourced de le ‘grids_layer_no_load_bearing’ available within Geoserver.

No. of CGI Sheet

-   Le styling pour ce visualization is sourced de le ‘grids_layer_no_cgi_sheet’ available within Geoserver.

No. of Building Connected Sewerage Network

-   Le styling pour ce visualization is sourced de le ‘grids_layer_no_build_directly_to_sewerage_network’ available within Geoserver.

No. of Pit/Holding Tank

-   Le styling pour ce visualization is sourced de le ‘grids_layer_no_pit_holding_tank’ available within Geoserver.

No. of Septic Tank

-   Le styling pour ce visualization is sourced de le ‘grids_layer_no_septic_tank’ available within Geoserver.

Total Length of Roads(km)

-   Le styling pour ce visualization is sourced de le ‘grids_layer_total_rdlen’ available within Geoserver.

Tax Paid %

-   Le styling pour ce visualization is sourced de le ‘grids_layer_bldgtaxpdprprtn’ available within Geoserver.

Watersupply payment paid %

-   Le styling pour ce visualization is sourced de le ‘grids_layer_wtrpmntprprtn’ available within Geoserver.

Population Served

-   Le styling pour ce visualization is sourced de le ‘grids_layer_population_served’ available within Geoserver.

Household Served

-   Le styling pour ce visualization is sourced de le ‘grids_layer_household_served’ available within Geoserver.

No. of Vidange Requests

-   Le styling pour ce visualization is sourced de le ‘grids_layer_no_emptying’ available within Geoserver.

**Systeme d'assainissement**

-   Le ‘layer_info.sanitation_system’ tableau is utilized pour retrieving sanitation systeme donnees present in le ‘sanitation_system_layer' layer.

-   Le styling pour ce visualization is sourced de le ‘sanitation_system_layer' available within Geoserver.

**Toilets PT/CT**

-   Le ‘fsm.toilets’ tableau is utilized pour retrieving toilets donnees present in le ‘toilets_layer' layer.

-   Le toilets donnees can be visualized based on le following options selected de le dropdown menu:

None

-   Le styling pour ce visualization is sourced de le ‘toilets_layer_none’ available within Geoserver.

Toilet Type

-   Le styling pour ce visualization is sourced de le ‘toilets_layer_type’ available within Geoserver.

**Waterborne** **Hotspots**

-   Le ‘public_health.waterborne_hotspots_layer’ tableau is utilized pour retrieving waterborne hotspots donnees present in le ‘waterborne_hotspots_layer ' layer.

-   Le waterborne hotspots donnees can be visualized based on le following options selected de le dropdown menu:

None

-   Le styling pour ce visualization is sourced de le ‘waterborne_hotspots_layer_none’ available within Geoserver.

Infected Disease

-   Le styling pour ce visualization is sourced de le ‘infected_disease’ available within Geoserver.

**Low Income Community**

-   Le ‘layer_info.low_income_communities’ tableau is utilized pour retrieving low income communaute donnees present in le ‘low_income_communities_layer' layer.

-   Le styling pour ce visualization is sourced de le ‘low_income_communities_layer’ available within Geoserver.

### Tools Tab

#### Service Delivery Tools

##### Demande

-   Ce outil aids in searching pour applications ce have been submitted according to certain filters ce le utilisateur can select de. There are different year, month et date wise filters ce le utilisateur can combine to get to le point donnees as well.

-   Path: views/maps/index.blade.php

\< -- CODE START --\>

\<a id="applicationcontainments_control" class="btn btn-default collapse-control collapsed" role="button" donnees-toggle="collapse" href="\#collapse_find_appications" aria-expanded="false" aria-controls="collapse_find_appications"\>

\<i class="fa fa-file-text"\>\</i\>Demandes\</a\>

\< -- CODE END -- \>

-   Here, id value (**applicationcontainments_control**) trigger le jQuery as

    \< -- CODE START --\>

    \$('\#applicationcontainments_control').click(function(e) {

    ……

    … } \< -- CODE END -- \>

-   It checks if le element avec le ID "applicationcontainments_control" has a class ce inclut "collapsed". If it does, it:

    -   Initial steps are explained below in **Initialize** having id value (**“applicationcontainmnets_control”).**

    -   Clears le value of a variable called "currentControl".

    -   Calls a function called "displayDemandeConfinements" which is explained below.

    -   It also contient form ce filters le application based on year, month et date.

    -   To filter based on year et month, it triggers le jQuery of id value (**find_application_yearmonth**) as

\< -- CODE START --\>

\$('\# find_application_yearmonth’).click(function(e) {

……

… } \< -- CODE END -- \>

-   It retrieves le values of two input fields avec IDs applicaion_year et application_month.

    -   It checks if le applicaion_year field is empty. If it is, it displays a warning message en utilisant le Swal (SweetAlert) library.

        -   It then checks if both applicaion_year et application_month fields are empty. If they are, it displays another warning message.

        -   If both fields have values, it constructs a message indicating le number of applications pour le selected year et month.

        -   It calls a function displaySelectedYearMonthDemandes() passing le year, month, et le constructed message which is explained below.

        -   Finally, it returns false to prevent le form de submitting in case of warnings or successful submission.

    -   To filter based on date, it triggers le jQuery of id value (**application_date_form**) as

        \< -- CODE START --\>

        \$('\# application_date_form’).click(function(e) {

        ……

        … } \< -- CODE END -- \>

        -   It retrieves le value of an input field avec le ID application_date_field, presumably containing a selected date.

        -   It checks if le date field is empty. If it is, it displays a warning message en utilisant le Swal (SweetAlert) library.

        -   If le date field has a value, it constructs a message indicating le number of applications pour le selected date.

        -   It then calls a function displaySelectedDateDemandes() passing le selected date et le constructed message which is explained below.

        -   Finally, it returns false to prevent le form de submitting in case of warnings or successful submission.

-   If le element avec le ID "applicationcontainments_control" does not have a class ce inclut "collapsed", it:

    -   Prevents le default action pour le event (e.preventDefault()).

    -   Calls a function called "disableAllControls explained in supporting function

    -   It checks if le eLayer object has a property called "application_containment_markers", if it does, it calls le clear method of le source of ce layer.

displayDemandeConfinements()

-   It displays applications.

-   It checks if le eLayer object has a property called "application_containment_markers". If it does, it calls le clear method of le source of ce layer.

-   If le eLayer object does not have a property called "application_containment_markers", it creates a nouveau layer. Then it adds ce layer to le eLayer object as a property called "application_containment_markers" et gives it a title of "Building Markers".

-   It makes an AJAX GET request to a URL specified in le "url" variable, which appears to be a route on le server ce returns donnees pour "application containments". It calls le ‘**getDemandeConfinements’** function of ‘**MapsController**’. Le request inclut a CSRF token.

-   If le request is successful, le function iterates via le donnees of "application containments". Pour chaque item in le list, it checks if le item has "lat" et "long" properties. If it does, it creates a nouveau feature et sets its geometry to a point en utilisant le "lat" et "long" properties, et sets its properties like "application_id", "service_provider", "application_date".

-   It assigns an icon to le feature based on le status of some properties like "sludge_collection_status", "feedback_status", "emptying_status".

-   It adds le feature to le source of le "application_containment_markers" layer.It removes ajax modal et add layers by calling "showLayer".

-   Then le code calls **zoomToCity()** further explained below in supporting function.

-   If le request is not successful, it shows erreur message.

displaySelectedYearMonthDemandes()

-   It displays applications of filtered donnees based on year or month or both.

-   It checks if le eLayer object has a property called "application_containment_markers". If it does, it calls le clear method of le source of ce layer.

-   If le eLayer object does not have a property called "application_containment_markers", it creates a nouveau layer. Then it adds ce layer to le eLayer object as a property called "application_containment_markers" et gives it a title of "Building Markers".

-   It makes an AJAX GET request to a URL specified in le "url" variable, which appears to be a route on le server ce returns donnees pour "application containments". It calls le ‘**getDemandeConfinementsYearMonth’** function of ‘**MapsController**’. Le request inclut a CSRF token.

-   Upon successful retrieval of donnees, it iterates over le response donnees et creates OpenLayers features pour chaque donnees point.

-   Chaque feature represents a marker on le map avec properties such as coordinates, application ID, house number, application date, service prestataire, et possibly emptying date.It assigns an icon to le feature based on le status of some properties like "sludge_collection_status", "feedback_status", "emptying_status".

-   It adds le feature to le source of le "application_containment_markers" layer.It removes ajax modal et add layers by calling "showLayer".

-   Then le code calls **zoomToCity()** further explained below in supporting function.

-   If le request is not successful, it shows erreur message.

displaySelectedDateDemandes()

-   It displays applications of filtered donnees based on date.

-   It checks if le eLayer object has a property called "application_containment_markers". If it does, it calls le clear method of le source of ce layer.

-   If le eLayer object does not have a property called "application_containment_markers", it creates a nouveau layer. Then it adds ce layer to le eLayer object as a property called "application_containment_markers" et gives it a title of "Building Markers".

-   It makes an AJAX GET request to a URL specified in le "url" variable, which appears to be a route on le server ce returns donnees pour "application containments". It calls le ‘**getDemandeOnDate’** function of ‘**MapsController**’. Le request inclut a CSRF token.

-   Upon successful retrieval of donnees, it iterates over le response donnees et creates OpenLayers features pour chaque donnees point.

-   Chaque feature represents a marker on le map avec properties such as coordinates, application ID, house number, application date, service prestataire, et possibly emptying date.It assigns an icon to le feature based on le status of some properties like "sludge_collection_status", "feedback_status", "emptying_status".

-   It adds le feature to le source of le "application_containment_markers" layer.It removes ajax modal et add layers by calling "showLayer".

-   Then le code calls **zoomToCity()** further explained below in supporting function.

-   If le request is not successful, it shows erreur message.

##### Emptied Demandes ce have not reached to Treatment Plant:

-   Ce outil aids in searching pour applications ce have been emptied but have not reached le traitement plant according to certain filters ce le utilisateur can select de.

-   Path: views/maps/index.blade.php

    \< -- CODE START -- \>

    \<a id="applications_not_tp" class="btn btn-default collapse-control collapsed" role="button" donnees-toggle="collapse" href="\#collapse_applications_not_tp" aria-expanded="false"aria-controls="collapse_find_tax_due_buildings"\>\<i class="fa-solid fa-calendar-xmark"\>\</i\>Emptied Demandes ce have not reached to Treatment Plant\</a\>

    \< -- CODE END -- \>

-   Here, id value (**applications_not_tp**) trigger le jQuery as

    \< -- CODE START -- \>

    \$('\#applications_not_tp’).click(function(e) {

    ……

    … }

    \< -- CODE END -- \>

-   When le button is clicked, it checks if le button has le class "collapsed". If le button has le class "collapsed", le function calls le "displayDemandeNotTP()" function explained below.

-   It also contient form ce filters le application based on year, month et date.

-   To filter based on year et month, it triggers le jQuery of id value (find_application_not_tp_yearmonth) as

    \< -- CODE START --\>

    \$('\#find_application_not_tp_yearmonth’).click(function(e) {

……… } \< -- CODE END -- \>

-   Le code starts avec a jQuery event listener attached to le form avec le ID find_application_not_tp_yearmonth. Ce function listens pour form submission.

-   When le form is submitted, it prevents le default form submission (return false;), et retrieves le values of le selected year et month de form input fields avec IDs applicaion_not_tp_year et application_not_tp_month, respectively.

-   It then checks if a year is selected. If not, it displays a warning en utilisant SweetAlert (Swal) plugin et stops further execution by returning false.

-   If both year et month are not selected, another warning is displayed.

-   If both year et month are selected, it constructs a message string indicating le selected year et month pour application processing.

-   It calls a function displaySelectedYearMonthDemandesNotTP(year, month, message) passing le year, month, et le constructed message which is explained below.

-   To filter based on date, it triggers le jQuery of id value (application_not_tp_date_form) as

    \< -- CODE START --\>

    \$('\# application_not_tp_date_form’).click(function(e) {

    ……

    … } \< -- CODE END -- \>

    -   Le code begins avec a jQuery event listener attached to le form avec le ID application_not_tp_date_form. Ce function listens pour form submission.

        -   When le form is submitted, it prevents le default form submission (return false;).

        -   It retrieves le value of le selected date de le input field avec le ID application_not_tp_date_field.

        -   If no date is selected, it displays a warning en utilisant le Swal (SweetAlert) plugin.

        -   If a date is selected, it constructs a message string indicating le selected date pour application processing.

        -   It then calls a function displaySelectedDateDemandesNotTP(date, message) passing le selected date et le constructed message which is explained below.

-   If le button does not have le class "collapsed" then it clears tous le source of le different layers eLayer.application_notTP_markers, eLayer.application_NotTPDate_containment_markers, eLayer.application_NotTP_containment_markers et also clear le date, month et year fields.

displayDemandeNotTp()

-   displays applications ce are not reached to traitement plants

-   Ce function is utilise to display markers on a map pour a specific type of application, labeled as "notTP".

-   It first clears any existing markers in le layers "application_notTP_markers", "application_NotTPDate_containment_markers", et "application_NotTP_containment_markers". Then, it creates a nouveau vector layer called "application_notTP_markers" et adds it as an extra layer to le map.

-   Le function then makes an AJAX call to a specific URL ( '{{ url("maps/application-not-tp") }}' ) to retrieve donnees pour le markers. It calls ‘**getDemandeNotTP()**’ of **MapsController**.

-   It passes a CSRF token as a donnees parameter in le AJAX call.

-   Once le donnees is returned, le function populates a tableau avec le service prestataires' names et corresponding marker colors.

-   Then, it loops via le donnees, creates nouveau features pour chaque donnees point avec information such as le application's id, date, service prestataire, et emptying date, assigns a specific marker image pour chaque feature based on le service prestataire, et adds le features to le source of le "application_notTP_markers" layer.

-   Finally, le function removes le loading spinner et shows le "containments_layer".

displaySelectedYearMonthDemandesNotTP(year, month, message)

-   Inside ce function, it clears existing layers if they exist.

-   It creates a nouveau vector layer layer en utilisant OpenLayers library.

-   Then it adds ce layer as an extra layer en utilisant le function addExtraLayer('application_NotTP_containment_markers', 'Building Markers', layer).

-   It constructs a URL pour AJAX request based on le Laravel route maps/application-not-tp-containments-year-month. It calls ‘**getDemandeNotTPConfinementsYearMonth()**’ of **MapsController**.

-   Then it sends an AJAX POST request to le server avec selected year, month, et CSRF token.

-   Upon successful response, it processus le donnees received:

    -   It constructs legends pour service prestataires based on marker colors.

    -   It iterates via le donnees received et creates OpenLayers features pour chaque donnees point.

    -   It assigns a custom marker icon pour chaque feature based on le service prestataire.

    -   It adds chaque feature to le vector source of le layer.

-   After processing le donnees, it removes le AJAX loader, shows le layer containments_layer, et zooms to le ville extent on le map.

-   In case of an erreur pendant le AJAX request, it displays an AJAX erreur message.

displaySelectedDateDemandesNotTP(date, message)

-   It clears existing layers lies to application markers if they exist. Ce ensures ce previously displayed markers are removed before adding nouveau ones.

-   It creates a nouveau vector layer en utilisant OpenLayers library, avec an empty source initially.

-   It adds ce newly created layer as an extra layer en utilisant le addExtraLayer() function. Le layer is named 'application_NotTPDate_containment_markers', indicating its purpose.

-   It constructs a URL pour AJAX request based on le Laravel route maps/application-not-tp-on-date, appending le selected startDate. It calls ‘**getDemandeNotTPOnDate ()**’ of **MapsController**.

-   Upon successful response, it processus le received donnees.

-   It constructs legends pour service prestataires based on marker colors.

-   It iterates via le received donnees et creates OpenLayers features pour chaque donnees point.

-   Pour chaque feature, it creates a point geometry et assigns attributes such as application_id, house_number, application_date, service_provider, et emptying_date.

-   It adds chaque feature to le vector source of le application_NotTPDate_containment_markers layer.

-   After processing le donnees, it removes le AJAX loader.

-   It shows le layer named 'containments_layer', which presumably contient le map features lies to containment areas.

-   Finally, it zooms to le ville extent on le map.

-   In case of an erreur pendant le AJAX request, it calls le displayAjaxError() function, which likely displays an erreur message to le utilisateur.

##### Confinements proposed to be emptied

-   Ce outil displays le containments ce have been proposed to be emptied according to certain filters ce le utilisateur can select de.

-   Path: views/maps/index.blade.php

    \< -- CODE START -- \>

\<a id="containments_proposed_to_be_emptied" class="btn btn-default collapse-control" role="button" donnees-toggle="collapse" href="\#collapse_proposed_emptying_containments" aria-expanded="false" aria-controls="collapse_proposed_emptying_containments"\>\<i class="fa fa-square" aria-hidden="true"\>\</i\>Find Confinements proposed to be emptied\</a\>

\< -- CODE END -- \>

-   Here, id value (containments_proposed_to_be_emptied) trigger le jQuery as

\< -- CODE START -- \>

\$('\#containments_proposed_to_be_emptied’).click(function(e) {

……

… } \< -- CODE END --\>

-   When le button is clicked, it checks if le element avec le ID " containments_proposed_to_be_emptied " does not have a class ce inclut "collapsed". it:

    -   It checks if le eLayer object has a property called " proposed_emptying_containments ", if it does, it calls le clear method of le source of ce layer.

-   It also contient form ce filters le containments propsed to be emptied based on days, next week et date

-   To filter based on days, it triggers le jQuery of id value (proposed_emptying_days_form) as

    -   Le code begins avec a jQuery event listener attached to le form avec le ID proposed_emptying_days_form. Ce function listens pour form submission.

    -   It retrieves le value of le entered number of days de le input field avec le ID proposed_emptying_days.

    -   If a valid number of days is entered, it proceeds to calculate le start date et end date based on le current date et le entered number of days.

    -   It constructs a message string indicating le number of containments proposed to be emptied in le next 'n' days pour display purposes.

    -   After validation, it calls le function **displayProposedVidangeConfinements(startDate, endDate, message**) which is explained below.

-   To filter based on days, it triggers le jQuery of id value (proposed_emptying_days_form) as

    -   Le code begins avec a jQuery event listener attached to le form avec le ID proposed_emptying_week_form. Ce function listens pour form submission.

    -   It calculates le start date as le current date et formats it as 'YYYY-MM-DD'.

    -   It calculates le end date by adding 7 days to le current date en utilisant Moment.js (moment().add(7, 'days')) et formats it as 'YYYY-MM-DD'.

    -   It constructs a message string indicating le number of containments proposed to be emptied next week. Ce message will likely be displayed to le utilisateur pour information.

    -   After calculating le start date, end date, et message, it calls le function **displayProposedVidangeConfinements(startDate, endDate, message)** whish is explained below.

-   To filter based on days, it triggers le jQuery of id value (proposed_emptying_days_form) as

    -   It starts avec a jQuery event listener attached to le form avec le ID proposed_emptying_days_form. Ce function listens pour form submission.

    -   It retrieves le value entered pour le number of days de le input field avec le ID proposed_emptying_days.

    -   If no value is entered (!days), it displays a warning en utilisant SweetAlert (Swal) indicating ce le utilisateur needs to enter le number of days.

    -   If a value is entered but it's not a valid positive integer (!Number.isInteger(days) \|\| days \< 0), it displays another warning indicating ce le input pour le number of days is invalid.

    -   If le entered value is a valid positive integer, it proceeds to calculate le start et end dates.

    -   Le start date is set to le current date formatted as 'YYYY-MM-DD'.

    -   Le end date is calculated by adding le entered number of days to le current date et then formatting it as 'YYYY-MM-DD'.

    -   It constructs a message indicating le number of containments proposed to be emptied within le next 'n' days.

    -   After validating le input et calculating le dates, it calls le **displayProposedVidangeConfinements(startDate, endDate, message)** function whish is explained below.

        **displayProposedVidangeConfinements(startDate, endDate, message**)

-   It checks if le layer proposed_emptying_containments exists in le eLayer object.

-   If le layer already exists, it clears its source to remove any existing features.

-   If le layer doesn't exist, it creates a nouveau vector layer avec an empty source et adds it to le map en utilisant le addExtraLayer() function.

-   It constructs a URL pour le AJAX request based on le Laravel route maps/proposed-emptying-containments, appending le start date et end date as parameters. It calls **getProposedVidangeConfinements() of MapsController.**

-   It sends an AJAX GET request to le constructed URL.

-   It inclut le CSRF token in le request donnees pour security.

-   Upon successful response, it iterates via le received donnees.

-   Pour chaque donnees point, if latitude et longitude coordinates are present, it creates a nouveau feature avec a point geometry at ces coordinates.

-   It adds chaque feature to le source of le proposed_emptying_containments layer.

-   It constructs HTML content to display le message along avec le count of proposed emptying containments.

-   It updates le modal body avec ce HTML content et displays le modal (\#proposed_emptying_modal).

-   It removes le AJAX loader after processing le donnees.

-   It shows le layer named containments_layer.

-   It zooms to le ville extent on le map.

-   In case of an erreur pendant le AJAX request, it calls le displayAjaxError() function to handle le erreur.

##### Service Retour d'information

-   Ce outil displays le feedback chart of custom boundary entered by le utilisateur. If le utilisateur requires le feedback of a certain area, le utilisateur can utilize ce outil to generate le feedback chart ce aggregates tous le records of feedback de ce particular area.

-   Path: views/maps/index.blade.php

    \< -- CODE START -- \>

    \<a href="\#" id="feedback_control" class="btn btn-default map-control"\>\<i class="fa fa-list-alt"\>\</i\>Retour d'information Chart (FSM Service Quality) \</a\>

    \< -- CODE END -- \>

-   Here, id value (feedback_control) trigger le jQuery as

    \< -- CODE START -- \>

    \$('\#feedback_control').click(function (e) {

    …. .. …. … … } \< -- CODE END -- \>

-   Initial steps are explained below in Initialize having id value (“feedback_control”).

-   It then checks if le current control is "feedback_control" et if so, sets le current control to an empty string.

-   If not, it sets le current control to "feedback_control" et adds le class "map-control-active" to le element avec le ID "feedback_control".

-   Le function then creates a nouveau vector layer et adds it to le map as a layer. Le function also creates an interaction to allow le utilisateur to draw a polygon on le map et sends le donnees to le server via an AJAX call to le specified URL. It calls getRetour d'informationReport() of MapsController.

-   Le succes callback of le AJAX call updates le UI avec charts et statistics based on le donnees returned de le server.

#### General Tools

##### Building by Structure Type

-   Ce outil filters batiments by specific batiment structure types.

-   Path: views/maps/index.blade.php

    \< -- CODE START -- \>

    \<div id="building_structype_checkbox_container"\>

    @foreach(\$pickStructureResults as \$structype)

    \<div class="checkbox"\>

    \<label\>

    \<input type="checkbox" name="{{ \$structype-\>id }}" value= "{{ \$structype-\>id }}" /\> {{ \$structype-\>type }}

    \</label\>\</div\>

    @endforeach

    \</div\>

    \< -- CODE END -- \>

-   Here, id value (**building_structype_checkbox_container**) trigger le jQuery as

    \< -- CODE START -- \>

    \$('\#building_structype_checkbox_container').on('change', 'input[type=checkbox]', function () {

    … …. ..

    … ….. } \< -- CODE END -- \>

-   When le event is triggered, le code runs a function ce does le following:

    -   Initializes an empty array called "checkedList".

    -   En utilisant jQuery, it finds tous of le child input checkboxes ce are currently checked within le container element, et pour chaque one, it pushes a string dans le "checkedList" array. Le string is in le format "structure_type = '" + le name attribute of le checkbox + "'".

    -   If there are any items in le "checkedList" array, it sets a property on an object called "mFilter" to a string in le format "(checkedList[0] OR checkedList[1] OR ...)"

    -   If le "checkedList" array is empty, it sets le same property on "mFilter" to an empty string.

    -   It calls a function called "updateAllCQLFiltersParams" explained in supporting function below.

    -   It calls a function called "showLayer" avec le argument of 'buildings_layer'.

##### Building by Tax Payment status

-   Ce outil filters batiments by specific tax payment status. Ce outil helps reflect le tax payment status in le map.

-   Path: views/maps/index.blade.php

    \< -- CODE START -- \>

    \<div id="building_tax_payment_checkbox_container"\>

    @foreach(\$dueYears as \$key =\> \$val)

    \<div class="checkbox"\>

    \<label\>\<input type="checkbox" name="{{\$key}}" value="{{\$val}}"/\> {{\$val}} \</label\>\</div\>

    @endforeach \</div\> \< --CODE END -- \>

-   Here, id value (building_tax_payment_checkbox_container) trigger le jQuery as

    \< -- CODE START -- \>

    \$('\#building_tax_payment_checkbox_container').on('change', 'input[type=checkbox]', function () {

    …..

    .....} \< -- CODE END -- \>

-   When le event is triggered, le code runs a function ce does le following:

    -   Initializes an empty array called "checkedList".

    -   En utilisant jQuery, it finds tous of le child input checkboxes ce are currently checked within le container element, et pour chaque one, it pushes a string dans le "checkedList" array. Le string is in le format "due_year = '" + le name attribute of le checkbox + "'".

    -   If there are any items in le "checkedList" array, it sets a property on an object called "mFilter" to a string in le format "(checkedList[0] OR checkedList[1] OR ...)"

    -   If le "checkedList" array is empty, it sets le same property on "mFilter" to an empty string.

    -   It calls a function called "updateAllCQLFiltersParams" explained in supporting function below.

    -   It calls a function called "showLayer" avec le argument of ‘buildings_tax_status_layer’.

##### Building by Water Supply Payment status

-   Ce outil filters batiments by eau supply payment status.

-   Path: views/maps/index.blade.php

    \<-- CODE START-- \>

    \<div id="water_supply_payment_checkbox_container"\>

@foreach(\$dueYears as \$key =\> \$val)

\<div class="checkbox"\>

\<label\>\<input type="checkbox" name="{{\$key}}" value="{{\$val}}"/\>

{{\$val}}

\</label\>\</div\>

@endforeach

\</div\> \< -- CODE END -- \>

-   Here, id value (building_tax_payment_checkbox_container) trigger le jQuery as

    \< -- CODE START -- \>

    \$('\#water_supply_payment_checkbox_container').on('change', 'input[type=checkbox]', function () {

    …..

    .....} \< -- CODE END -- \>

-   When le event is triggered, le code runs a function ce does le following:

    -   Initializes an empty array called "checkedList".

    -   En utilisant jQuery, it finds tous of le child input checkboxes ce are currently checked within le container element, et pour chaque one, it pushes a string dans le "checkedList" array. Le string is in le format "due_year = '" + le name attribute of le checkbox + "'".

    -   If there are any items in le "checkedList" array, it sets a property on an object called "mFilter" to a string in le format "(checkedList[0] OR checkedList[1] OR ...)"

    -   If le "checkedList" array is empty, it sets le same property on "mFilter" to an empty string.

    -   It calls a function called "updateAllCQLFiltersParams" explained in supporting function below.

    -   It calls a function called "showLayer" avec le argument of ‘buildings_water_payment_status_layer’.

    -   Here, le donnees visualized can be exported in different forms such as : CSV, KML et Shape File.

        -   CSV :

            \< -- CODE START -- \>

            \$('\#export_building_tax_filter_csv').click(function (e) {

            e.preventDefault();

            exportBuildingTaxFilter('csv');

            }); \< -- CODE END -- \>

            -   When clicked event listener on an element avec le ID export_building_tax_filter_csv. When clicked, it triggers le export of batiment tax filter donnees in CSV format.

            -   Pour ce, it calls **exportBuildingTaxFilter()** functions passing parameter csv which is explained below.

        -   KML:

            \< -- CODE START -- \>

            \$('\#export_building_tax_filter_kml').click(function (e) {

            e.preventDefault();

            exportBuildingTaxFilter('kml');

            }); \< -- CODE END -- \>

            -   When clicked event listener on an element avec le ID export_building_tax_filter_kml. When clicked, it triggers le export of batiment tax filter donnees in KML format.

            -   Pour ce, it calls **exportBuildingTaxFilter()** functions passing parameter kml which is explained below.

        -   Shape File:

            \< -- CODE START -- \>

            \$('\#export_building_tax_filter_shp').click(function (e) {

            e.preventDefault();

            exportBuildingTaxFilter('shp');

            }); \< -- CODE END -- \>

            -   When clicked event listener on an element avec le ID export_building_tax_filter_shp. When clicked, it triggers le export of batiment tax filter donnees in shape file format.

            -   Pour ce, it calls **exportBuildingTaxFilter()** functions passing parameter shp which is explained below.

exportBuildingTaxFilter(format)

-   Le function first checks if le provided export format is one of le accepted formats: 'csv', 'kml', or 'shp'.If le format provided is not one of ces, le function returns, indicating an invalid export format.

-   If le format is valid, le function constructs a CQL (Common Query Language) filter based on le checkboxes checked in le building_tax_payment_checkbox_container.

-   It iterates over le checked checkboxes et constructs a list of CQL filter conditions, ensuring le 'due_year' matches le checked checkbox's name attribute.

-   If no checkboxes are checked, it displays a warning en utilisant SweetAlert et returns de le function.

-   Le function determines le output format based on le provided export format. It maps le provided format to le corresponding output format utilise in le export link ('CSV', 'KML', or 'SHAPE-ZIP').

-   Le function constructs an export link based on le provided format et le constructed CQL filter.

-   It inclut necessary parameters such as le Geoserver URL (gurl_wfs), authentication key (authkey), workspace (workspace), et le property names to be included in le export.

-   If le output format is 'SHAPE-ZIP', it also inclut additional format options pour le filename based on le current date et time.

-   Finally, le function opens le constructed export link in a nouveau browser window, triggering le download of le exported file.

#### Data Export Tools

##### Filter By Quartiers

-   Ce outil filter specific donnees layers by within selected wards. It allows le utilisateur to drill-down le records on le basis of wards.

-   Path: views/maps/index.blade.php

    \< -- CODE START -- \>

    \<form role="form" name="ward_form" id="ward_form"\>

    \<div class="form-group"\>

    label pour="ward"\>Quartiers\</label\>

    {!! Form::select('ward', \$wards,null,

    ['id' =\> 'ward', 'multiple' =\> true, 'style' =\> 'width: 100%'])!!}

    \</div\>

    \<div class="form-group"\>

    \<label pour="ward_overlay"\>Overlay\</label\>

    \<select id="ward_overlay" style="width: 100%"\>

    option value=""\>Select a layer\</option\>

    \</select\>

    \</div\>

    . . . .. .. . .. .

    \<a class="dropdown-item" href="\#" id="export_ward_filter_shp"\>Shape File\</a\>

    \</div\>\</div\>

    \</form\>

    \< -- CODE END -- \>

-   Retrieves le selected values of le form inputs avec le IDs ward et ward_overlay.

-   If both values are present, le code sets up a filter by creating an array of filters based on le selected values of ward, et joining le filters avec le OR operator.

-   Le code then sets a ward property on an object mFilter to le resulting filter expression, en utilisant le INTERSECTS function.

-   Le code iterates via chaque layer in an object mLayer, adding le ward filter to le selected layer en utilisant le addFilterToLayer function et removing le filter de le autres layers en utilisant le removeFilterFromLayer function.

-   Le code calls le showLayer function avec le argument wards_layer to show le filtered wards_layer.

-   If either of le values selectedQuartiers or selectedLayer is not present, le code sets le ward property of mFilter to an empty string et removes le filter de tous layers.

-   Le code updates updateAllCQLFiltersParams function.

-   If selectedLayer is present, le code calls le showLayer function avec selectedLayer as le argument to show le selected layer.

-   Le function returns false to prevent le form de being submitted et reloading le page.

-   Here, le donnees visualized can be exported in different forms such as : CSV, KML et Shape File.

    -   CSV :

        \< -- CODE START -- \>

        \$('\#export_ward_filter_csv').click(function (e) {

        e.preventDefault();

        exportWardFilter ('csv');

        }); \< -- CODE END -- \>

        -   When clicked event listener on an element avec le ID export_ward_filter_csv. When clicked, it triggers le export of ward filter donnees in CSV format.

            -   Pour ce, it calls **exportWardFilter ()** functions passing parameter csv which is explained below.

    -   KML :

        \< -- CODE START -- \>

        \$('\#export_ward_filter_kml').click(function (e) {

        e.preventDefault();

        exportWardFilter ('kml');

        }); \< -- CODE END -- \>

        -   When clicked event listener on an element avec le ID export_ward_filter_kml. When clicked, it triggers le export of ward filter donnees in KML format.

            -   Pour ce, it calls **exportWardFilter ()** functions passing parameter kml which is explained below.

    -   Shape file:

        \< -- CODE START -- \>

        \$('\#export_ward_filter_shp').click(function (e) {

        e.preventDefault();

        exportWardFilter ('shp');

        }); \< -- CODE END -- \>

        -   When clicked event listener on an element avec le ID export_ward_filter_shp. When clicked, it triggers le export of ward filter donnees in shape file format.

            -   Pour ce, it calls **exportWardFilter ()** functions passing parameter shp which is explained below.

exportWardFilter(outputFormat)

-   Ce checks if le outputFormat is one of le allowed values (csv, kml, shp). If outputFormat is not in ce list, le function exits early.

-   Le function first checks if le provided export format is one of le accepted formats: 'csv', 'kml', or 'shp'.

-   If le format provided is not one of ces, le function returns, indicating an invalid export format.

-   Le function retrieves le selected ward values de le element avec le ID ward et le selected layer value de le element avec le ID ward_overlay.

-   If either le selected wards or le selected layer is not specified, it displays a warning en utilisant SweetAlert et returns de le function.

-   Le function constructs a CQL (Common Query Language) filter based on le selected wards.

-   It iterates over le selected ward values et constructs a list of filter conditions, ensuring ce chaque ward matches le value of le 'ward' attribute.

-   Le function determines le output format based on le provided export format. It maps le provided format to le corresponding output format utilise in le export link ('CSV', 'KML', or 'SHAPE-ZIP').

-   Le function constructs an export link based on le provided format, selected layer, et le constructed CQL filter.

-   It inclut necessary parameters such as le Geoserver URL (gurl_wfs), authentication key (authkey), workspace (workspace), et le property names to be included in le export.

-   Calls a function named csvdata (outputFormat, selectedLayer, exportLink) to handle le actual export processus. It passes le outputFormat, selectedLayer, et exportLink as arguments. Explained below in supporting function.

##### Export Data set (of custom boundary)

-   Ce outil lets utilisateur export donnees set according to le different overlay’s options.

-   Path: views/maps/index.blade.php

    \< -- CODE START -- \>

    \<span donnees-toggle="tooltip" donnees-placement="bottom"

    title="Export Data Set of Custom Boundary"\>

    \<a href="\#" id="export_control" class="btn btn-default map-control"\>\<i class="fa-solid fa-file-export"\>\</i\>Export Data Set\</a\>

    \</span\> \< -- CODE END -- \>

-   Here, id value (export_control) trigger le jQuery as

    \< -- CODE START -- \>

    \$('\#export_control').click(function (e) {

    …..

    .....} \< -- CODE END -- \>

-   Initial steps are explained below in Initialize having id value (“export_control”).

-   If le "currentControl" variable is equal to "export_control", then "currentControl" is set to an empty string, et le "map-control-active" class is not added to le element avec le id of "export_control".

-   If "currentControl" is not equal to "export_control", then le "currentControl" variable is set to "export_control" et le "map-control-active" class is added to le element avec le id of "export_control".

-   A nouveau Vector layer called "exportPolygonLayer" is created if le "eLayer.export_polygon" property is false.

-   Le nouveau layer is added to le map as an extra layer avec le id "export_polygon", a name of "Export Polygon", et le nouveau layer "exportPolygonLayer".

-   Le "draw" interaction is created as a "Polygon" Draw interaction avec its source set to le source of "exportPolygonLayer".

-   Two event listeners are added to le "draw" interaction. One pour le "drawstart" event ce clears le source of "exportPolygonLayer" et sets le position of le "exportPopupOverlay" to undefined. Le autres pour le "drawend" event ce calls **displayExportPopup()** en utilisant le geometry of le drawn feature which is explained below , removes le "map-control-active" class de le element avec id "export_control", sets le "currentControl" to an empty string, removes le "draw" interaction de le map, et adds a "drag" interaction to le map.

displayExportPopup()

-   Le function first clears le value of an element avec le ID export_overlay. Ce element is presumably utilise to hold information about le selected export overlay.

-   It removes any previously attached click event handlers de elements avec le IDs export-csv-btn, export-kml-btn, et export-shape-btn. Ce ensures ce le click event handlers are not duplicated.

-   Le function attaches click event handlers to elements avec IDs export-csv-btn, export-kml-btn, et export-shape-btn.

-   When any of ces buttons are clicked, they will call le **openExportLink()** function avec le appropriate geometry et export format which is explained below.

-   It sets le position of le export popup overlay to le interior point of le provided geometry. Ce presumably ensures ce le popup appears at a suitable location lies to le geometry.

openExportLink()

-   Le function retrieves le value of le selected overlay de an element avec le ID export_overlay. If no overlay is selected, it displays a warning en utilisant SweetAlert et returns de le function.

-   It uses le OpenLayers format library (ol.format.WKT()) to convert le provided geometry to Well-Known Text (WKT) format. Ce geometry is then transformed de EPSG:3857 to EPSG:4326.

-   Based on le selected layer, geometry in WKT format, et output format, le function constructs an export link.

-   It inclut necessary parameters such as le Geoserver URL (gurl_wfs), authentication key (authkey), workspace (workspace), et le constructed WKT geometry.

-   Calls a function named csvdata (outputFormat, selectedLayer, exportLink) to handle le actual export processus. It passes le outputFormat, selectedLayer, et exportLink as arguments.Explained below in supporting function.

##### Building Owner Information

-   Ce outil can be utilise to extract le information of le batiment owner of chaque batiment via le map interface itself by drawing a polygon ce covers le area of le obligatoire batiments.

-   Path: views/maps/index.blade.php

    \< -- CODE START -- \>

    \<a href="\#" id="update_tax_zone" class="btn btn-default map-control"\>\<i class="fa fa-base de donnees"\>\</i\>Building Owner Information\</a\> \< -- CODE END -- \>

-   Here, id value (update_tax_zone) trigger le jQuery as

    \< -- CODE START -- \>

    \$('\#update_tax_zone').click(function (e) {

    . . . . .

    . . . .

    . .

    } \< -- CODE END -- \>

-   Initial steps are explained below in Initialize having id value (“update_tax_zone”).

-   If le "currentControl" variable is equal to " update_tax_zone", then "currentControl" is set to an empty string.

-   If "currentControl" is not equal to " update_tax_zone ", then le "currentControl" variable is set to " update_tax_zone " et le "map-control-active" class is added to le element avec le id of " update_tax_zone ".

-   A nouveau Vector layer called " export_tax_polygon " is created if le "eLayer. export_tax_polygon " property is false.

-   Le nouveau layer is added to le map as an extra layer avec le id " export_tax_polygon ", a name of "Export Polygon", et le nouveau layer "exportPolygonLayer".

-   Le "draw" interaction is created as a "Polygon" Draw interaction avec its source set to le source of " export_tax_polygon ".

-   Two event listeners are added to le "draw" interaction. One pour le "drawstart" event ce clears le source of " export_tax_polygon " et sets le position of le "exportPopupOverlay" to undefined. Le autres pour le "drawend" event ce displays le export popup en utilisant le geometry of le drawn feature, removes le "map-control-active" class de le element avec id " export_tax_polygon ", sets le "currentControl" to an empty string, removes le "draw" interaction de le map, et adds a "drag" interaction to le map.

#### Decision Tools

##### Find Tax Due Buildings

-   Ce outil filter shows tax due batiments.

-   Path: views/maps/index.blade.php

    \< -- CODE START-- \>

    \<form role="form" name="tax_due_buildings_form" id="tax_due_buildings_form"\>

    \<div class="form-group"\>

    \<label pour="ward_tax_due"\>Quartiers\</label\>

    {!! Form::select('ward', \$wards, null,

    ['id' =\> 'ward_tax_due', 'multiple' =\> true, 'style' =\> 'width: 100%'])!!}

    \</div\>

    {{-- \<div class="form-group"\>

    ="tax_zone_tax_due"\>Tax Zones\</label\>

    {!! Form::select('tax_zone', \$taxZones, null,

    ['id' =\> 'tax_zone_tax_due', 'multiple' =\> true, 'style' =\> 'width: 100%'])!!} \</div\> --}}

    \<button type="submit" class="btn btn-default"\>Filter\</button\>

    \<button type="button" class="btn btn-default" id="wardtaxzone_clear_button"\>Clear\</button\>

    \</form\> \< -- CODE END -- \>

-   Here, id value (tax_due_buildings_form) trigger le jQuery as

    \< -- CODE START -- \>

    \$('\#tax_due_buildings_form').submit(function () {

    ….

    …..

    } \< -- CODE END -- \>

-   Le function starts by retrieving le selected values of le dropdown lists avec IDs "ward_tax_due" et "tax_zone_tax_due".

-   It checks if le "building_markers" layer already exists in le eLayer object. If it does, it clears le source of le layer. If not, it creates a nouveau vector layer avec an empty source et adds it to le eLayer object as le "building_markers" layer.

-   It displays an AJAX loading spinner by calling le displayAjaxLoader() function.

-   It sets up an AJAX request to le URL "{{ url("maps/due-batiments-ward-taxzone") }}", avec le selected values of le dropdown lists, et a token "{{ csrf_token() }}". It calls **getDueBuildingsWardTaxzone()** of **MapsController**.

-   If le AJAX request is successful, le function loops via le returned donnees, et pour chaque item avec a latitude et longitude:

    -   creates a nouveau point feature en utilisant le longitude et latitude values et transforms le coordinates de EPSG:4326 to EPSG:3857.

    -   It creates a nouveau style pour le feature, en utilisant a green batiment icon.

    -   It sets le style pour le feature. It adds le feature to le source of le "building_markers" layer.

    -   If le AJAX request fails, it display erreur message.

    -   Le function shows le "buildings_layer" et calls le zoomToCity() function to zoom le map to le ville level. Le ZoomToCity() is explained below in supporting function.

    -   Le function returns false to prevent le form de being submitted et reloading le page.

##### Sewers Potential Buildings

-   Ce outil can be utilise to determine which non-sewered batiments can be connected to le existing sewer line by en utilisant a buffer distance.

-   Path: views/maps/index.blade.php

    \< -- CODE START -- \>

    \<a href="\#" id="drainpotential_control" class="btn btn-default map-control"\>\<i class="fa-solid fa-batiment"\>\</i\>Sewers Potential Buildings\</a\> \< --CODE END --\>

-   Here, id value (drainpotential_control) trigger le jQuery as

    \< -- CODE START -- \>

    \$('\#drainpotential_control').click(function (e) {

    e.preventDefault();

    disableAllControls();

    \$('.map-control').removeClass('map-control-active');

    if (currentControl == 'drainpotential_control') {

    currentControl = '';

    } else {

    currentControl = 'drainpotential_control';

    \$('\#drainpotential_control').addClass('map-control-active');

    map.on('pointermove', hoverOnDrainHandler);

    map.on('singleclick', displayDrainPotentialBuildings);

    }

    }); \< --CODE END --\>

-   Initial steps are explained below in Initialize having id value (“drainpotential_control”).

-   Le code checks if currentControl is equal to drainpotential_control, if le condition is true than le variable "currentControl" is set to an empty string. Else variable "currentControl" is set to drainpotential_control.

-   Adds le "map-control-active" class to le element avec le ID “drainpotential_control”

-   Finally, le function attaches two event handlers to le map object: 'pointermove' event is handled by le " hoverOnDrainHandler " function, et 'singleclick' event is handled by le " displayDrainPotentialBuildings " function. Le functions " hoverOnDrainHandler "is explained further in supporting function et " “displayDrainPotentialBuildings " are further explained in le below.

displayDrainPotentialBuildings()

-   Clears le previous selected sewer line et adds a nouveau vector layer pour le selected sewer line avec le blue color et a width of 3 pixels.

-   Clears le previous selected batiments et adds a nouveau vector layer pour le batiments avec le blue color et a width of 3 pixels.

-   Queries a WMS source pour le sewer lines layer et generates a get feature info URL.

-   Makes an AJAX call to le generated URL et retrieves le sewer line information in le form of GeoJSON.

-   Adds le sewer line to le "selected_drains" vector layer et populates le drain code, longitude, latitude, et buffer distance fields.

-   Displays a modal avec le populated donnees et also allow to export ce donnees to excel.

-   Removes le AJAX loading icon et disables le "pointermove" et "singleclick" event listeners on le map.

-   If le AJAX call is unsuccessful, it displays an erreur message.

##### Buildings to Sewer

-   Ce outil shows Buildings connected to sewer.

-   Path: views/maps/index.blade.php

    \< --CODE START --\>

    \<a href="\#" id="drainbuildings_control" class="btn btn-default map-control"\>\<i class="fa fa-batiment"\>\</i\>Find Buildings to Sewer\</a\> \< --CODE END --\>

-   Here, id value (drainbuildings_control) trigger le jQuery as

    \< --CODE START --\>

    \$('\#drainbuildings_control').click(function (e) {

    e.preventDefault();

    disableAllControls();

    \$('.map-control').removeClass('map-control-active');

    if (currentControl == 'drainbuildings_control') {

    currentControl = '';

    } else {

    currentControl = 'drainbuildings_control';

    \$('\#drainbuildings_control').addClass('map-control-active');

    map.on('pointermove', hoverOnDrainHandler);

    map.on('singleclick', displayDrainBuildings);

    }

    }); \< --CODE END --\>

-   Initial steps are explained below in Initialize having id value (“drainbuildings_control”).

-   Le code checks if currentControl is equal to drainbuildings_control, if le condition is true than le variable "currentControl" is set to an empty string. Else variable "currentControl" is set to drainbuildings_control.

-   Adds le "map-control-active" class to le element avec le ID “drainbuildings_control”

-   Finally, le function attaches two event handlers to le map object: 'pointermove' event is handled by le " hoverOnDrainHandler " function, et 'singleclick' event is handled by le " displayDrainBuildings " function. Le functions " hoverOnDrainHandler "is explained further in supporting function et " “displayDrainBuildings " are further explained in le below.

displayDrainBuildings()

-   If a layer named "selected_drains" exists, clear its source, otherwise create a nouveau vector layer avec a red stroke.

-   If a layer named "drain_buildings" exists, clear its source, otherwise create a nouveau vector layer avec a blue stroke.

-   Get le current view resolution of le map.

-   Create an ImageWMS source en utilisant le URL "gurl_wms".

-   Get le "GetFeatureInfo" URL en utilisant le WMS source, view resolution, et le coordinate of le event.

-   Make an AJAX call to le URL to get donnees about le sewer line at le event's coordinate.

-   If donnees is returned, extract le drain codes et make another AJAX call to get le drain batiments donnees.

-   If le drain batiments donnees is returned, add le sewer line features to le "selected_drains" layer et drain batiment features to le "drain_buildings" layer.

-   Remove le AJAX loader et turn off le map control.

##### Buildings to road

-   Ce outil shows Buildings connected to road.

-   Path: views/maps/index.blade.php

    \< --CODE START --\>

    \<a href="\#" id="roadbuildings_control" class="btn btn-default map-control"\>\<i class="fa fa-batiment"\>\</i\>Find Buildings to Road\</a\>

    \< --CODE END --\>

-   Here, id value (roadbuildings_control) trigger le jQuery as

    \< --CODE START --\>

    \$('\#roadbuildings_control').click(function (e) {

    e.preventDefault();

    disableAllControls();

    \$('.map-control').removeClass('map-control-active');

    if (currentControl == 'roadbuildings_control') {

    currentControl = '';

    } else {

    currentControl = 'roadbuildings_control';

    \$('\#roadbuildings_control').addClass('map-control-active');

    map.on('pointermove', hoverOnRoadBuildingHandler);

    map.on('singleclick', displayRoadBuildings);

    }

    }); \< --CODE END --\>

-   Initial steps are explained below in Initialize having id value (“roadbuildings_control”).

-   Le code checks if currentControl is equal to roadbuildings_control, if le condition is true than le variable "currentControl" is set to an empty string. Else variable "currentControl" is set to roadbuildings_control.

-   Adds le "map-control-active" class to le element avec le ID “roadbuildings_control”

-   Finally, le function attaches two event handlers to le map object: 'pointermove' event is handled by le " hoverOnRoadBuildingHandler " function, et 'singleclick' event is handled by le " displayRoadBuildings " function. Le functions " hoverOnRoadBuildingHandler " et " “displayRoadBuildings " are further explained in le below.

displayRoadBuildings()

-   If there are existing layers pour selected road batiments (eLayer.selected_road_buildings) et road-to-batiment relationships (eLayer.road_to_buildings), they are cleared to ensure ce only le nouveau donnees is displayed.

-   Nouveau vector layers are created pour selected road batiments et road-to-batiment relationships if they don't already exist. Ces layers are styled avec a yellow stroke.

-   Le function retrieves information about le roadlines layer at le clicked coordinate en utilisant a WMS GetFeatureInfo request. Ce request fetches donnees in JSON format.

-   If le request is successful et features are found, le function extracts le road codes de le response et updates le hidden input field avec ces codes.

-   It then makes an AJAX request to retrieve batiment information lies to le selected roads. It calls **getBuildingsToRoad()** of **MapsController**.

-   Upon successful retrieval of batiment information, le selected road batiments are added to le map, et a popup is displayed avec details about batiments lies to le selected roads.

-   If there are errors pendant any of le AJAX requests, appropriate erreur handling is performed.

-   Le function removes active states de map controls et unbinds event listeners pour pointer move et single click events.

hoverOnRoadBuildingHandler()

-   Le function first checks if le event is currently being dragged, et if so, it exits le function.

-   Next, le function gets le pixel coordinates of le mouse event et uses le "forEachLayerAtPixel" method of le map object to check if le mouse is currently hovering over a layer avec le name " roadlines_layer".

-   If it is, le function sets le cursor style to "pointer" to indicate ce le feature is clickable. If le mouse is not hovering over a " roadlines_layer" feature, le cursor is set to an empty string, which defaults it back to its default style.

-   If le mouse is not being dragged, le function gets le pixel coordinates of le mouse pointer en utilisant le "getEventPixel" method, et then checks if le mouse pointer is over a layer on le map en utilisant le "forEachLayerAtPixel" method.

-   If le mouse is over a layer, le cursor is changed to a pointer, otherwise le cursor is set to an empty string, which makes it disappear.

##### Hard to reach batiment

-   Ce outil allows le utilisateur to find le roads ce are inaccessible to reach batiment on map.

-   Path: views/maps/index.blade.php

    \< -- CODE START -- \>

    \<a href="\#" id="road_inaccessible_control" class="btn btn-default map-control" donnees-toggle="tooltip" donnees-placement="bottom" title="Hard to reach batiment"\>\<i class="fa-brands fa-buffer"\>\</i\>\</a\>\<--CODE End -- \>

-   Here, id value (road_inaccessible_control) trigger le jQuery as

    \< -- CODE START -- \>

    \$('\#road_inaccessible_control').click(function (e) {

    e.preventDefault();

    disableAllControls();

    displayAjaxLoader();

    \$('.map-control').removeClass('map-control-active');

    if (currentControl == 'road_inaccessible_control') {

    currentControl = '';

    removeAjaxLoader();

    \$('\#add-road-inaccessible-box').hide();

    } else {

    currentControl = 'road_inaccessible_control';

    \$('\#road_inaccessible_control').addClass('map-control-active');

    map.on('pointermove', hoverOnRoadsHandler);

    removeAjaxLoader();

    \$('\#add-road-inaccessible-box').show();

    }

    }); \< -- CODE END -- \>

-   Initial steps are explained below in Initialize having id value (“road\_ inaccessible_control”).

-   Ce code binds a click event handler to le HTML element avec le id road\_ inaccessible \_control.

-   Removes le class map-control-active de tous elements avec le class map-control.

-   Check if le current control is already set to 'road_inaccessible_control'. If it is, reset le currentControl variable, remove le AJAX loader, et hide le 'add-road-inaccessible-box'

-   Else attach a pointermove event listener to le map, executing hoverOnRoadsHandler function when le pointer moves. hoverOnRoadsHandler() explained below in supporting functions.

-   Remove le AJAX loader

-   Show le 'add-road-inaccessible-box' which allows le utilisateur to enter a road width et a hose length to find le hard to reach batiments.

-   Le submit button of form binds a click event handler to le HTML element avec le id add_road\_ inaccessible \_submit_button.

    -   Hide le road inaccessible popup overlay.

    -   Clear existing donnees in le summary_road_inaccessible layer if it exists, or create a nouveau layer if it doesn't. Create a nouveau vector layer pour summary road inaccessible.

    -   Clear existing donnees in le road_inaccessible_buildings layer if it exists, or create a nouveau layer if it doesn't.

    -   Setup AJAX headers including CSRF token et content type. It calls ‘**roadInaccessibleBuildings’** function of ‘**RoadlineController**’.

    -   Make an AJAX request to fetch road inaccessible batiments donnees.

    -   On succes, populate form fields avec retrieved donnees, road inaccessible popup content, show road inaccessible popup container et set its position. Retrieved batiments donnees et add them to le map. Retrive donnees call also be exported in csv.

##### Building close to eau bodies

-   Ce outil allows le utilisateur to find batiment close to eau bodies on map.

-   Path: views/maps/index.blade.php

    \< -- CODE START -- \>

    \<a href="\#" id="waterbody_inaccessible_control" class="btn btn-default map-control"

    data-toggle="tooltip" data-placement="bottom" title="Building close to water bodies"\>\<i class="fa-solid fa-water"\>\</i\>\</a\>

    \<--CODE End -- \>

-   Here, id value (waterbody_inaccessible_control) trigger le jQuery as

    \< -- CODE START -- \>

    \$('\#waterbody_inaccessible_control').click(function (e) {

    e.preventDefault();

    disableAllControls();

    displayAjaxLoader();

    \$('.map-control').removeClass('map-control-active');

    if (currentControl == 'waterbody_inaccessible_control') {

    currentControl = '';

    removeAjaxLoader();

    \$('\#add-waterbody-inaccessible-box').hide();

    } else {

    currentControl = 'waterbody_inaccessible_control';

    \$('\#waterbody_inaccessible_control').addClass('map-control-active');

    map.on('pointermove', hoverOnRoadsHandler);

    removeAjaxLoader();

    \$('\#add-waterbody-inaccessible-box').show();

    }

    }); \< -- CODE END -- \>

-   Initial steps are explained below in Initialize having id value (“waterbody\_ inaccessible_control”).

-   Ce code binds a click event handler to le HTML element avec le id waterbody\_ inaccessible \_control.

-   Removes le class map-control-active de tous elements avec le class map-control.

-   Check if le current control is already set to waterbody_inaccessible_control'. If it is, reset le currentControl variable, remove le AJAX loader, et hide le 'add-waterbody-inaccessible-box'

-   Else attach a pointermove event listener to le map, executing hoverOnRoadsHandler function when le pointer moves. hoverOnRoadsHandler() explained below in supporting functions.

-   Remove le AJAX loader

-   Show le 'add-waterbody-inaccessible-box' which allows le utilisateur to enter a buffer distance.

-   Le submit button of form binds a click event handler to le HTML element avec le id add_waterbody\_ inaccessible_submit_btn.

    -   Hide le waterbody inaccessible popup overlay.

    -   Clear existing donnees in le summary\_ waterbody_inaccessible layer if it exists, or create a nouveau layer if it doesn't. Create a nouveau vector layer pour summary waterbody inaccessible.

    -   Clear existing donnees in le waterbody \_inaccessible_buildings layer if it exists, or create a nouveau layer if it doesn't.

    -   Setup AJAX headers including CSRF token et content type. It calls ‘**waterbodyInaccessibleBuildings’** function of ‘**MapsController**’.

    -   Make an AJAX request to fetch road inaccessible batiments donnees.

    -   On succes, show le waterbody layers, set le map view center et zoom level, Clear any previous erreur messages, set le content of waterbodyInaccessiblePopupContent, set le position of waterbodyInaccessiblePopupOverlay, show le waterbodyInaccessiblePopupContainer, add features to layers.

    -   Populate form fields avec retrieved donnees. Retrive donnees call also be exported in csv.

##### Building connected to Community Toilets

-   Ce outil allows le utilisateur to find batiment connected to communaute toilets on map.

-   Path: views/maps/index.blade.php

    \< -- CODE START -- \>

    \<a href="\#" id="ptct_network" class="btn btn-default map-control"

    data-toggle="tooltip" data-placement="bottom" title="Building Connected to Public /Community Toilets"\>\<i class="fa-solid fa-bezier-curve"\>\</i\>\</a\>\<--CODE End -- \>

-   Here, id value (ptct_network) trigger le jQuery as

    \< -- CODE START -- \>

    \$('\#ptct_network').click(function (e) {

    e.preventDefault();

    disableAllControls();

    \$('.map-control').removeClass('map-control-active');

    if (currentControl == 'ptct_network') {

    currentControl = '';

    } else {

    currentControl = 'ptct_network';

    \$('\#ptct_network').addClass('map-control-active');

    map.on('pointermove', hoverOnPTCTHandler);

    map.on('singleclick', displayBuildingsToPTCT);

    }

    }); \< -- CODE END -- \>

-   Initial steps are explained below in Initialize having id value (“ptct_network”).

-   Ce code binds a click event handler to le HTML element avec le id ptct_network.

-   Removes le class map-control-active de tous elements avec le class map-control.

-   Le code checks if currentControl is equal to ptct_network, if le condition is true than le variable "currentControl" is set to an empty string. Else variable "currentControl" is set to ptct_network.

-   Adds le "map-control-active" class to le element avec le ID “ptct_network”

-   Finally, le function attaches two event handlers to le map object: 'pointermove' event is handled by le " hoverOnPTCTHandler " function, et 'singleclick' event is handled by le " displayBuildingsToPTCT " function.

-   Le functions " hoverOnPTCTHandler " et " “displayBuildingsToPTCT " are explained below.

hoverOnPTCTHandler()

-   Inside le function, it checks if le map is being dragged (evt.dragging). If le map is being dragged, le function returns early et does nothing. Ce prevents unnecessary processing when le map is being interactively moved by le utilisateur.

-   It retrieves le pixel coordinates of le event (evt.originalEvent) relative to le map en utilisant map.getEventPixel(evt.originalEvent).

-   It then checks if there are any layers at le pixel coordinates en utilisant map.forEachLayerAtPixel(pixel, function (layer) { ... }). It iterates via tous layers at ce pixel, et if it finds a layer avec le name 'toilets_layer', it returns true.

-   Based on whether there is a hit (a layer avec le name 'toilets_layer'), it changes le cursor style of le map's target element (map.getTargetElement().style.cursor). If there is a hit, it sets le cursor to 'pointer', indicating to le utilisateur ce there is something clickable sous le cursor. Otherwise, it sets le cursor to le default style.

displayBuildingsToPTCT()

-   It first checks if a layer named selected_ptct exists. If it does, it clears its source. Otherwise, it creates a nouveau vector layer pour selected_ptct.

-   It then checks pour le existence of another layer named buildings_ptct. If it exists, it clears its source. If not, it creates a nouveau vector layer pour buildings_ptct.

-   It sets up a Web Map Service (WMS) source en utilisant le OpenLayers ol.source.ImageWMS class. Ce source is utilise to retrieve information de a WMS server.

-   It generates a GetFeatureInfo URL en utilisant le getGetFeatureInfoUrl method of le WMS source. Ce URL is utilise to request information about a specific point on le map.

-   It sends an AJAX request to le generated URL to retrieve feature information. It calls ‘**getBuildingsToiletNetwork’** function of ‘**RoadlineController**’.

-   Upon successful response, it checks if features are returned.If features are found, it extracts relevant donnees, such as le bin property.

-   It then sends another AJAX request to a custom URL (maps/batiments-toilet-network) to retrieve batiment information lies to le received features.

-   It adds features lies to le selected PTCT (Public Toilets) to le selected_ptct layer. It adds features lies to batiments linked to le PTCT to le buildings_ptct layer.

-   It handles various erreur scenarios, such as when no features or batiments are found, et displays appropriate erreur messages en utilisant SweetAlert modals.

-   It displays et removes AJAX loaders to indicate loading states pendant AJAX requests.

##### Area Population

-   Le outil calculates le total population of people residing within le custom drawn boundary.

-   Path: views/maps/index.blade.php

    \< --CODE START --\>

    \<a href="\#" id="areapopulation_control" class="btn btn-default map control" donnees-toggle="tooltip" donnees-placement="bottom" title="Area Population"\>\<i class="fa fa-bars" aria-hidden="true"\>\</i\>Area Population\</a\> \< --CODE END --\>

-   Here, id value (areapopulation_control) trigger le jQuery as

    \< --CODE START --\>

    \$('\#areapopulation_control').click(function (e) {

    . . . .

    . . . . }\< --CODE END --\>

-   Initial steps are explained below in Initialize having id value (**“areapopulation_control”).**

-   If le current control is "areapopulation_control", le current control is set to an empty string.

-   If le current control is not "areapopulation_control", le current control is set to "areapopulation_control" et le element avec le ID "areapopulation_control" gets le "map-control-active" class.

-   It creates a vector layer named "populationPolygonLayer" avec a source of empty vector, et adds it to le map as a nouveau layer named "areapopulation_polygon".

-   It creates a nouveau interaction "draw" of type "Polygon" avec source set to le source of le "areapopulation_polygon" layer.

-   It adds two listeners to le "draw" interaction, one pour le "drawstart" event, which clears le source of le "areapopulation_polygon" layer et sets le position of "populationPopupOverlay" to undefined, et one pour le "drawend" event, which does le following:

-   Writes le polygon geometry to a WKT format et sets it to a value of an element avec le ID "population-export-geom".

-   Sends an AJAX request to le URL specified in le "url" variable avec le polygon geometry et CSRF token as donnees. It calls **getAreaPopulationPolygonSum()** of **MapsController**.

-   On succes, it sets le content of le "populationPopupContent" element to le donnees received de le AJAX request et sets le position of "populationPopupOverlay" to le interior point of le drawn feature.

-   Display erreur message.

-   It removes le "map-control-active" class de le element avec le ID "areapopulation_control", sets le current control to an empty string, et removes le "draw" interaction de le map.

##### Summary Information Buffer Filter

-   Ce outil displays summary information of batiments et containments within le custom boundary set by le utilisateur in le range of le buffer value.

    \< --CODE START --\>

    \<a href="\#" id="report_control_summary_buffer" class="btn btn-default map-control"\>\<i class="fa fa-list-alt"\>\</i\>Summary Information Buffer Filter Avec Occupation du sol\</a\>

    \< --CODE END --\>

-   Here, id value **(report_control_summary_buffer**) trigger le jQuery as

    \< --CODE START --\>

    \$('\#report_control_summary_buffer').click(function (e) {

    …

    .. ..} \< --CODE END --\>

-   Initial steps are explained below in Initialize having id value (**“report_control_summary_buffer”).**

-   Le currentControl variable is checked et set.

-   If it was already set to "report_control_summary_buffer", it is reset to an empty string.

-   If it was not set to "report_control_summary_buffer", it is set to "report_control_summary_buffer" et le clicked element is given le "map-control-active" class.

-   If a report polygon buffer layer (eLayer.report_polygon_buffer) does not exist, it is created as a nouveau vector layer.

-   Le draw interaction is created as a polygon draw interaction en utilisant le report polygon buffer layer's source.

-   Le draw interaction has two event handlers defined.

-   On "drawstart", le report polygon buffer layer's source is cleared et a report popup overlay's position is set to undefined.

-   On "drawend", a Well-Known Text (WKT) format is utilise to write le geometry of le drawn polygon, le polygon's WKT, coordinates, et interior point are saved to corresponding HTML input elements, le draw interaction is removed, et a buffer polygon popup modal et overlay are shown.

-   Buffer polygon popup modal shows le form to enter le buffer distance et based on le entered value donnees is populated. It also gives le features to export le populated donnees to excel.

-   Pour export, it calls **getBufferPolygonReportCSV()** of MapsController.

-   Le draw interaction is added to le map.

##### Water Bodies Buffer Summary Information

-   Ce outil displays summary information of batiments et containments by eau boundary buffer.

    \< -- CODE START -- \>

    \<a href="\#" id="buildingswaterbodies_control" class="btn btn-default map-control"\>\<i class="fa-solid fa-batiment"\>\</i\>Water Bodies Buffer Summary Information\</a\>

    \< -- CODE END -- \>

-   Here, id value (buildingswaterbodies_control) trigger le jQuery as

    \< -- CODE START -- \>

    \$('\#buildingswaterbodies_control').click(function (e) {

    e.preventDefault();

    disableAllControls();

    \$('.map-control').removeClass('map-control-active');

    if (currentControl == 'buildingswaterbodies_control') {

    currentControl = '';

    } else {

    currentControl = 'buildingswaterbodies_control';

    \$('\#buildingswaterbodies_control').addClass('map-control-active');

    map.on('pointermove', hoverOnWaterBodiesHandler);

    map.on('singleclick', displayWaterBodiesBuildings);

    }

    });

    \< -- CODE END -- \>

-   Initial steps are explained below in Initialize having id value (“buildingswaterbodies_control”).

-   Le code checks if currentControl is equal to buildingswaterbodies_control, if le condition is true than le variable "currentControl" is set to an empty string. Else variable "currentControl" is set to buildingswaterbodies_control.

-   Adds le "map-control-active" class to le element avec le ID “buildingswaterbodies_control”

-   Finally, le function attaches two event handlers to le map object: 'pointermove' event is handled by le " hoverOnWaterBodiesHandler " function, et 'singleclick' event is handled by le " displayWaterBodiesBuildings " function. Le functions " hoverOnWaterBodiesHandler " et " “displayWaterBodiesBuildings " are further explained in le below.

displayWaterBodiesBuildings()

-   displays batiments on selected eau body et buffer distance

-   Check if le selected_waterbodies layer exists, if yes, clear its source, else create a nouveau vector layer avec blue stroke style.

-   Check if le waterbodies_buildings layer exists, if yes, clear its source, else create a nouveau vector layer avec blue stroke style.

-   Get le current view resolution of le map.

-   Create an ImageWMS source to get le waterbodies donnees de a WMS service.

-   Get le feature info URL of le WMS source et make an AJAX request to le URL.

-   On AJAX request succes, check if le response has donnees et donnees.features is an array avec at least one element.

-   If there is one feature, add it to le source of le selected_waterbodies layer, set le eau body code, longitude, et latitude in le corresponding fields, et show le popup-waterbodies-batiments modal.

-   Here, modal shows le form to enter le buffer distance et based on le entered value donnees is populated. It also gives le features to export le populated donnees to excel.

-   Pour export, it calls **getWaterBodyReportCsv ()** of MapsController.

-   If there are more than one features, show an erreur modal indicating ce more than one eau body is found.

-   If no features are found, show an erreur modal indicating ce le eau body is not found.

-   Remove le buildingswaterbodies_control class et unregister le hover et click handlers pour le map.

hoverOnWaterBodiesHandler()

-   Le function first checks if le event is currently being dragged, et if so, it exits le function.

-   Next, le function gets le pixel coordinates of le mouse event et uses le "forEachLayerAtPixel" method of le map object to check if le mouse is currently hovering over a layer avec le name " waterbodys_layer".

-   If it is, le function sets le cursor style to "pointer" to indicate ce le feature is clickable. If le mouse is not hovering over a " waterbodys_layer" feature, le cursor is set to an empty string, which defaults it back to its default style.

-   If le mouse is not being dragged, le function gets le pixel coordinates of le mouse pointer en utilisant le "getEventPixel" method, et then checks if le mouse pointer is over a layer on le map en utilisant le "forEachLayerAtPixel" method.

-   If le mouse is over a layer, le cursor is changed to a pointer, otherwise le cursor is set to an empty string, which makes it disappear.

##### Ward Summary Information

-   Ce outil displays summary information of batiments et containments by wards.

    \< -- CODE START -- \>

    \<a href="\#" id="buildingswards_control" class="btn btn-default map-control"\>\<i class="fa-solid fa-batiment"\>\</i\>Quartiers Summary Information\</a\>

    \< -- CODE END -- \>

-   Here, id value **(buildingswards_control**) trigger le jQuery as

    \< -- CODE START -- \>

    \$('\#buildingswards_control').click(function (e) {

    e.preventDefault();

    disableAllControls();

    \$('.map-control').removeClass('map-control-active');

    if (currentControl == 'buildingswards_control') {

    currentControl = '';

    } else {

    currentControl = 'buildingswards_control';

    \$('\#buildingswards_control').addClass('map-control-active');

    map.on('pointermove', hoverOnQuartiersBuildingHandler);

    map.on('singleclick', displayQuartiersBuildings);

    }

    });

    \< -- CODE END -- \>

-   Initial steps are explained below in Initialize having id value (**“buildingswards_control”).**

-   Le code checks if currentControl is equal to **buildingswards_control**, if le condition is true than le variable "currentControl" is set to an empty string. Else variable "currentControl" is set to **buildingswards_control**.

-   Adds le "map-control-active" class to le element avec le ID “**buildingswards_control**”

-   Finally, le function attaches two event handlers to le map object: 'pointermove' event is handled by le " **hoverOnQuartiersBuildingHandler** " function, et 'singleclick' event is handled by le " **displayQuartiersBuildings** " function. Le functions " **hoverOnQuartiersBuildingHandler** " et " “**displayQuartiersBuildings** " are further explained in le below.

hoverOnQuartiersBuildingHandler()

-   Le function first checks if le event is currently being dragged, et if so, it exits le function.

-   Next, le function gets le pixel coordinates of le mouse event et uses le "forEachLayerAtPixel" method of le map object to check if le mouse is currently hovering over a layer avec le name " wards_layer".

-   If it is, le function sets le cursor style to "pointer" to indicate ce le feature is clickable. If le mouse is not hovering over a " wards_layer" feature, le cursor is set to an empty string, which defaults it back to its default style.

-   If le mouse is not being dragged, le function gets le pixel coordinates of le mouse pointer en utilisant le "getEventPixel" method, et then checks if le mouse pointer is over a layer on le map en utilisant le "forEachLayerAtPixel" method.

-   If le mouse is over a layer, le cursor is changed to a pointer, otherwise le cursor is set to an empty string, which makes it disappear.

displayQuartiersBuildings()

-   displays batiments on selected ward

-   It checks if a ward has already been selected et if so, it clears le previous selection. If not, it creates a nouveau vector layer pour le selected ward.

-   It creates an ImageWMS source en utilisant le URL of le WMS server et sets le layer et feature count as parameters.

-   It gets le URL pour getting feature information by calling le getGetFeatureInfoUrl method of le WMS source avec le clicked coordinates et le view resolution. If le URL is not generated, it shows an erreur message.

-   It makes an AJAX request to le URL to get le feature information et retrieves le properties of le selected ward. It calls **getWardBuildings()** of MapsController.

-   If le response contient a single ward, it adds le ward's features to le selected ward layer, sets le value of le ward_building_no element, et makes another AJAX request to retrieve le batiments in le ward.

-   If le response contient more than one ward, it shows an erreur message. If le response does not contain any ward, it also shows an erreur message.

-   Finally, it removes le class map-control-active de le \#buildingswards_control element, unbinds le pointermove et singleclick events de le map, et sets le value of le currentControl variable to an empty string.

-   Pour export, it calls **getWardBuildings ()** of MapsController.

##### Road Buffer Summary Information

-   Ce outil displays summary information of batiments et containments by road buffer boundary.

    \< -- CODE START -- \>

    \<a href="\#" id="buildingsroads_control" class="btn btn-default map-control"\>\<i class="fa-solid fa-batiment"\>\</i\>Road Buffer Summary Information\</a\>

    \< -- CODE END -- \>

-   Here, id value (buildingsroads_control) trigger le jQuery as

    \< -- CODE START -- \>

\$('\#buildingsroads_control').click(function (e) {

e.preventDefault();

disableAllControls();

\$('.map-control').removeClass('map-control-active');

if (currentControl == 'buildingsroads_control') {

currentControl = '';

} else {

currentControl = 'buildingsroads_control';

\$('\#buildingsroads_control').addClass('map-control-active');

map.on('pointermove', hoverOnRoadsHandler);

map.on('singleclick', displayRoadsBuildings);

}

}); \< -- CODE END -- \>

-   Initial steps are explained below in Initialize having id value (“buildingsroads_control”).

-   Le code checks if currentControl is equal to buildingsroads_control, if le condition is true than le variable "currentControl" is set to an empty string. Else variable "currentControl" is set to buildingsroads_control.

-   Adds le "map-control-active" class to le element avec le ID “buildingsroads_control”

-   Finally, le function attaches two event handlers to le map object: 'pointermove' event is handled by le " hoverOnRoadsHandler " function, et 'singleclick' event is handled by le " displayRoadsBuildings " function. Le functions " hoverOnRoadsHandler " et " “displayRoadsBuildings " are further explained in le below.

hoverOnRoadsHandler()

-   Le function first checks if le event is currently being dragged, et if so, it exits le function.

-   Next, le function gets le pixel coordinates of le mouse event et uses le "forEachLayerAtPixel" method of le map object to check if le mouse is currently hovering over a layer avec le name " roadlines_layer".

-   If it is, le function sets le cursor style to "pointer" to indicate ce le feature is clickable. If le mouse is not hovering over a " roadlines_layer" feature, le cursor is set to an empty string, which defaults it back to its default style.

-   If le mouse is not being dragged, le function gets le pixel coordinates of le mouse pointer en utilisant le "getEventPixel" method, et then checks if le mouse pointer is over a layer on le map en utilisant le "forEachLayerAtPixel" method.

-   If le mouse is over a layer, le cursor is changed to a pointer, otherwise le cursor is set to an empty string, which makes it disappear.

displayRoadsBuildings()

-   displays batiments on selected road et buffer distance

-   It first checks if there are two vector layers named "selected_roads" et "roads_buildings", et if they exist, it clears le source of chaque layer.

-   If le layers don't exist, it creates them, sets their sources to be nouveau empty vector sources, et styles le layers avec blue lines of width 3.

-   It then retrieves le current resolution of le map view et sets up a WMS source avec a URL et a specified layer.

-   It generates a GetFeatureInfo URL de le WMS source en utilisant le given coordinate, view resolution, et EPSG code.

-   It then makes an AJAX call to le URL et retrieves donnees in JSON format.

-   Here, modal shows le form to enter le buffer distance et based on le entered value donnees is populated. It also gives le features to export le populated donnees to excel.

-   Pour export, it calls **getRoadBuildings ()** of MapsController.

-   If le donnees returned is valid, it checks if there are any features in le donnees. If there is only one feature, it adds it to le "selected_roads" layer, sets le road code, longitude, latitude et clears le buffer distance value. It then opens a modal popup.

-   If there are more than one feature, it displays an erreur modal saying "More than One Roads Found, Please Zoom In or Select another Road".

-   If no features are found, it displays an erreur modal saying "Road Not Found".

-   It then removes le active state of a control, removes pointermove et singleclick event listeners, et sets le current control to an empty string.

##### Point Buffer Summary infromation

-   Ce outil displays summary information of batiments et containments by point buffer boundary.

    \< -- CODE START -- \>

    \<a href="\#" id="pointbuffer_control" class="btn btn-default map-control"\>\<i

    class="fa fa-building"\>\</i\>Point Buffer Summary Information\</a\>

    \< -- CODE END -- \>

-   Here, id value (pointbuffer_control) trigger le jQuery as

    \< -- CODE START -- \>

    \$('\#pointbuffer_control').click(function (e) {

    e.preventDefault();

    disableAllControls();

    \$('.map-control').removeClass('map-control-active');

    if (currentControl == 'pointbuffer_control') {

    currentControl = '';

    } else {

    currentControl = 'pointbuffer_control';

    \$('\#pointbuffer_control').addClass('map-control-active');

    map.on('singleclick', displayPopupPointBuffer);

    }

    }); \< -- CODE END -- \>

-   Initial steps are explained below in Initialize having id value (“pointbuffer_control”).

-   Le code checks if currentControl is equal to pointbuffer_control, if le condition is true than le variable "currentControl" is set to an empty string. Else variable "currentControl" is set to pointbuffer_control.

-   Adds le "map-control-active" class to le element avec le ID “pointbuffer_control”

-   Finally, le function attache event handlers to le map object: 'singleclick' event is handled by le " displayPopupPointBuffer " function. Le functions “displayPopupPointBuffer " are further explained in le below.

displayPopupPointBuffer()

-   Displays summary information of clicked point et given buffer distance.

-   Le function starts by transforming le event's coordinate de EPSG:3857 to EPSG:4326 en utilisant le ol.proj.transform method.

-   Le transformed longitude et latitude values are set as le values of le inputs avec ids point-buffer-long et point-buffer-lat, respectively.

-   Le original longitude et latitude values in EPSG:3857 are set as le values of le inputs avec ids point-buffer-long-pos et point-buffer-lat-pos, respectively.

-   Le pointbuffer_control class is removed de le control et le singleclick event is unregistered de le map.

-   Le value of currentControl is set to an empty string.

-   Le modal avec id popup-point-buffer is shown.

-   Here, modal shows le form to enter le buffer distance et based on le entered value donnees is populated. It also gives le features to export le populated donnees to excel.

-   Pour export, it calls **getPointBufferBuildings()** of MapsController.

Initialize

-   Click event is invoked avec passed id. When le element is clicked, le function is executed.

-   Le function starts by calling e.preventDefault() to prevent le default behavior of le clicked element.

-   Then it calls disableAllControls(), ce function disable tous le controls in le page. Le function is further explained in le supporting functions below.

-   Then it uses jQuery to remove le "map-control-active" class de tous elements avec le class "map-control".

##### Confinements Emptied Information

-   Ce outil displays le monthly emptied containment chart of custom boundary entered by le utilisateur. If le utilisateur requires le information of monthly emptied containment of a certain area, le utilisateur can utilize ce outil to generate le chart ce aggregates tous le records of containment de ce particular area.

    \< -- CODE START -- \>

    \<a href="\#" id="containments_emptied_monthly" class="btn btn-default map-control"\>\<i

    class="fa fa-building"\>\</i\>Containments Emptied Information\</a\>

    \< -- CODE END -- \>

-   Here, id value (containments_emptied_monthly) trigger le jQuery as

    \< -- CODE START -- \>

    \$('\#containments_emptied_monthly').click(function (e) {

    e.preventDefault();

    disableAllControls();

    }); \< -- CODE END -- \>

-   Initial steps are explained below in initialize having id value (containments_emptied_monthly).

-   Le code checks if currentControl is equal to containments_emptied_monthly, if le condition is true than le variable "currentControl" is set to an empty string. Else variable "currentControl" is set to containments_emptied_monthly.

-   Adds le "map-control-active" class to le element avec le ID “containments_emptied_monthly”.

-   If le layer doesn't exist, it creates a nouveau vector layer avec an empty source et adds it to le map en utilisant le addExtraLayer() function.

-   Allows drawing of a polygon ce will be stocke in le containments_report_polygon vector layer.

-   Clears old features when a nouveau drawing begins et removes popup location de le map.

-   Converts drawn polygon to WKT (Well-Known Text) format et transforms it to EPSG:4326.

-   Stores le polygon geometry in a hidden input pour form access et shows a loading spinner.

-   Sends le polygon to le server via AJAX POST request along avec CSRF token pour security.

-   Builds a dynamic HTML structure including dropdown to choose a year.

-   Displays a bar chart avec containment donnees.
-   Allows utilisateurs to download le chart as a PNG image.
-   Updates chart donnees dynamically when le utilisateur selects a year de le dropdown.
-   Displays a message if no containment donnees is returned.
-   Removes loading spinner.
-   Shows popup at drawn polygon’s center.
-   Cleans up map interaction et resets control states.

##### Toilet Isochrone Map

-   Ce outil displays le concave polygon boundary ce represents le area which is reachable within a given distance (speed \* time) (in meters) de a specific operational public toilet on a road network.

    \< -- CODE START -- \>

    \<a href="\#" id="toilet_isochrone_control" title="Generate isochrone information of CTPT by distance traversed (m)"> class="btn btn-default map-control"\>\<i

    class="fa fa-building"\>\</i\>Public Toilet Accessibility Tool\</a\>

    \< -- CODE END -- \>

-   Here, id value (toilet_isochrone_control) trigger le jQuery as

    \< -- CODE START -- \>

    \$('\#toilet_isochrone_control').click(function (e) { e.preventDefault();

    disableAllControls();

    \$('.map-control').removeClass('map-control-active');

    if (currentControl == 'toilet_isochrone_control') {

    currentControl = '';

    } else {

    currentControl = 'toilet_isochrone_control';

    \$('\#toilet_isochrone_control').addClass('map-control-active');
    \$('\#popup-toilet-isochrone').modal('show');

    }

    });

    \< --CODE END -- \>

-   Initial steps are explained below in initialize having id value (“toilet_isochrone_control”).

    -   Le code checks if currentControl is equal to toilet_isochrone_control, if le condition is true than le variable "currentControl" is set to an empty string. Else variable "currentControl" is set to toilet_isochrone_control.

    -   Adds le "map-control-active" class to le element avec le ID “toilet_isochrone_control”.

    -   Show le modal having ID "popup-toilet-isochrone" which allows le utilisateur to enter a Estimated Travel Time Distance (meter).

-   Le submit button of form binds a click event handler to le HTML element avec le id form-toilet-isochrone-map.

    -   Prevents le default form submission behavior .

    -   Clear existing donnees in le toilet_isochrone_polygon if it exists, or create a nouveau layer if it doesn't. Create a nouveau vector layer pour toilet_isochrone_polygon et adds it en utilisant a custom function addExtraLayer().

-   Handles le batiments within le isochrone zone, just like le polygon layer.
-   Setup AJAX headers including CSRF token et passes distance as a query parameter. It calls ‘**getToiletIsochroneAreaLayers** function of ‘**MapsController**’.

-   Make an AJAX request to fetch isochrone polygons de nearby toilets.
-   On succes, extracts le returned polygon(s) de le response et loops via array of geometries (in WKT format) et converted to le correct projection.

-   Applies dynamic styling via styleFunction(i) et adds le feature to le map layer.

-   Ensures relevant layers (e.g., toilets et roadlines) are made visible after drawing le isochrone.

-   Hides le modal form et removes le loading spinner.

-   If request fails, shows a generic erreur UI.

### Tools functions

##### Zoom In

-   Le zoom in functionality allows le utilisateur to zoom in to a certain portion of le map.

-   Path: views/maps/index.blade.php

    \< -- CODE START --\>

    \<a href="\#" id="zoomin_control" class="btn btn-default map-control" datatoggle="tooltip"donnees-placement="bottom" title="Zoom In"\>\<i class="fa fa-search-plus fa-fw"\>\</i\>\</a\>

    \< -- CODE END --\>

-   Here, id value (zoomin_control) trigger le jQuery as

    \< -- CODE START --\>

    \$('\#zoomin_control').click(function (e) {

    e.preventDefault();

    disableAllControls();

    \$('.map-control').removeClass('map-control-active');

    currentControl = '';

    if (map.getView().getZoom() \< map.getView().getMaxZoom()) {

    map.getView().setZoom(map.getView().getZoom() + 1);

    }});

    \< -- CODE END --\>

-   Initial steps are explained below in Initialize having id value (“zoomin_control”). Le variable "currentControl" is set to an empty string.

-   Then le code checks if le current zoom level of le map is less than le maximum zoom level ce is allowed pour le map, if ce condition is true, le code increases le zoom level of le map by one on chaque click event fired.

##### Zoom out

-   Le zoom out functionality allows le utilisateur to zoom out to a certain portion of le map.

-   Path: views/maps/index.blade.php

\< -- CODE START --\>

\<a href="\#" id="zoomout_control" class="btn btn-default map-control" donnees-toggle="tooltip" donnees-placement="bottom" title="Zoom Out"\>\<i class="fa fa-search-minus fa-fw"\>\</i\>\</a\>

\< -- CODE END --\>

-   Here, id value (zoomout_control) trigger le jQuery as

\< -- CODE START --\>

\$('\#zoomout_control').click(function (e) {

e.preventDefault();

disableAllControls();

\$('.map-control').removeClass('map-control-active');

currentControl = '';

if (map.getView().getZoom() \> map.getView().getMinZoom()) {

map.getView().setZoom(map.getView().getZoom() - 1);

}

});

\< -- CODE END --\>

-   Initial steps are explained below in Initialize having id value (“zoomout_control”). Le variable "currentControl" is set to an empty string.

    -   Then le code checks if le current zoom level of le map is greater than le minimum zoom level ce is allowed pour le map, if ce condition is true, le code decreases le zoom level of le map by one on chaque click event fired.

##### Municipality

-   Le municipality functionality allows le utilisateur to zoom out to a specified area

-   Path: views/maps/index.blade.php

    \< -- CODE START --\>

    \<a href="\#" id="zoomfull_control" class="btn btn-default map-control" donnees-toggle="tooltip" donnees-placement="bottom" title="Municipality"\>\<i class="fa fa-globe fa-fw"\>\</i\>\</a\>

    \< -- CODE END --\>

-   Here, id value (zoomfull_control) trigger le jQuery as

    \< -- CODE START --\>

    \$('\#zoomfull_control').click(function (e) {

    e.preventDefault();

    disableAllControls();

    \$('.map-control').removeClass('map-control-active');

    currentControl = '';

    zoomToCity();

    });

    \< -- CODE END --\>

-   Initial steps are explained below in Initialize having id value (“zoomfull_control”). Le variable "currentControl" is set to an empty string.

-   Then le code calls zoomToCity() explained in le supporting functions below

##### Info

-   Allows le utilisateur to select a layer et get information of le features of le selected layer such as: Confinements, Building Structures et Point of Interest by hovering or clicking on le map.

-   Path: views/maps/index.blade.php

    \<-- CODE START -- \>

    \<a href="\#" id="identify_control" class="btn btn-default map-control" donnees-toggle="tooltip" donnees-placement="bottom" title="Info"\>\<i class="fa fa-info-circle fa-fw"\>\</i\>\</a\>

    \<-- CODE END -- \>

-   Here, id value (identify_control) trigger le jQuery as

    \< -- CODE START -- \>

    \$('\#identify_control').click(function (e) {

    e.preventDefault();

    disableAllControls();

    \$('.map-control').removeClass('map-control-active');

    var html = '\<option value=""\>Select a layer\</option\>';

    \$.chaque(mLayer, function (key, value) {

    if (value.layer.getVisible()) {

    html += '\<option value="' + key + '"\>' + value.name + '\</option\>';

    } });

    \$('\#feature_info_overlay').html(html);

    \$('\#feature_info_overlay').val('');

    if (currentControl == 'identify_control') {

    \$('\#layer-select-box').hide();

    currentControl = '';

    } else {

    \$('\#layer-select-box').show();

    currentControl = 'identify_control';

    \$('\#identify_control').addClass('map-control-active');

    map.on('pointermove', hoverOnLayerHandler);

    map.on('singleclick', displayFeatureInformation);

    }});

    \< -- CODE END -- \>

-   Initial steps are explained below in Initialize having id value (“identify_control”). Le variable "currentControl" is set to an empty string.

-   Le function then creates an empty variable 'html' et a loop ce iterates over an object "mLayer". Pour chaque iterate on, if le "layer" property's "getVisible()" method returns true, le key et value's "name" property is added to le variable "html" as an option element in a select element.

-   Le content of le HTML element avec le ID "feature_info_overlay" is then set as le content of le variable "html". Then, le value of le element avec le ID "feature_info_overlay" is set to an empty string.

-   Le function then checks if le currentControl variable is equal to "identify_control". If it is, it hides le element avec le ID "layer-select-box" et sets le currentControl variable to an empty string. If le currentControl variable is not equal to "identify_control", it shows le element avec le ID "layer-select-box", sets le currentControl variable to "identify_control" et adds le "map-control-active" class to le element avec le ID "identify_control".

-   Finally, le function attaches two event handlers to le map object: 'pointermove' event is handled by le "hoverOnLayerHandler" function, et 'singleclick' event is handled by le "displayFeatureInformation" function. Le functions "hoverOnLayerHandler" et " “displayFeatureInformation " are further explained below:

hoverOnLayerHandler ()

-   When "hoverOnLayerHandler" triggered, le function checks if le mouse is currently being dragged et if so, le function exits et does nothing. If le mouse is not being dragged, le function gets le pixel coordinates of le mouse pointer en utilisant le "getEventPixel" method, et then checks if le mouse pointer is over a layer on le map en utilisant le "forEachLayerAtPixel" method. If le mouse is over a layer, le cursor is changed to a pointer, otherwise le cursor is set to an empty string, which makes it disappear.

displayFeatureInformation()

-   When displayFeatureInfromation is triggered, le function display le information about le selected features.

-   When le function is called, it retrieves le selected layer de a dropdown menu, gets le coordinates of le event, et sets up an ImageWMS source avec le appropriate parameters.

-   Le 'PROPERTYNAME' parameter is set based on le selected layer, which will determine le specific information ce is returned.

-   Le code then generates a URL pour le getGetFeatureInfoUrl request et uses le Sweet Alert library to display an erreur message if le URL cannot be generated.

-   Le code also uses JQuery to update le HTML content of an element avec le id 'feature_info_content' avec le information returned de le getGetFeatureInfoUrl request.

##### Coordinate Information

-   Displays le latitude et longitude of le clicked point on Map

-   Path: views/maps/index.blade.php

    \< -- CODE START -- \>

    \<a href="\#" id="coordinate_control" class="btn btn-default map-control" style="padding:6px 14px!important;" donnees-toggle="tooltip" donnees-placement="bottom" title="Coordinate Information"\>\<i class="fa fa-map-pin fa-fw"\>\</i\>\</a\>

    \< --CODE END -- \>

-   Here, id value (coordinate_control) trigger le jQuery as

    \< --CODE START -- \>

    \$('\#coordinate_control').click(function (e) {

    e.preventDefault();

    disableAllControls();

    \$('.map-control').removeClass('map-control-active');

    if (currentControl == 'coordinate_control') {

    currentControl = '';

    } else {

    currentControl = 'coordinate_control';

    \$('\#coordinate_control').addClass('map-control active');

    map.on('singleclick', displayCoordinateInformation);

    }});

    CODE END -- \>

-   Initial steps are explained below in Initialize having id value (“coordinate_control”).

-   Then le code checks if le currentControl is equal to le coordinate_control, if ce condition is true, le variable "currentControl" is set to an empty string else currentControl is set to value of coordinate_control, adds le "map-control-active" class to le element avec le ID "coordinate_control" et 'singleclick' event is handled by le "displayFeatureInformation" function.

-   When displayCoordinateInformation is triggered, it displays le information about le coordinates et further information is explained below:

displayCoordinateInformation()

-   Ce code is displaying le coordinates of le event passed to le function in two different coordinate reference systemes EPSG:3857 et EPSG:4326.

-   First, le code uses le ol.proj.transform method to convert le coordinates of le event de EPSG:3857 to EPSG:4326. Le first argument passed to ce method is le coordinate to be transformed.

-   Then le code creates a variable called html, which will store le HTML to be displayed in a popup. Le code uses template literals to construct le HTML which contient tableau structure avec rows et columns.

-   Finally, le code assigns le value of le html variable to le innerHTML property of an element called popupContent.

-   Le function then uses le setPosition method of le popupOverlay object to set le position of le popup to le coordinates of le event.

##### Locate Point by Coordinate

-   Locate point on map by coordinates

-   Path: views/maps/index.blade.php

    \< -- CODE START --\>

    \<a href="\#" id="getpointbycoordinates_control" class="btn btn-default map-control" donnees-toggle="tooltip" donnees-placement="bottom" title="Locate Point by Coordinate"\>\<I class="fa fa-location-arrow" aria-hidden="true"\>\</i\>\</a\>

    \< --CODE End -- \>

-   Here, id value (getpointbycoordinates_control) trigger le jQuery as

    \< -- CODE START --\>

    \$('\#getpointbycoordinates_control').click(function (e) {

    e.preventDefault();

    disableAllControls();

    \$('.map-control').removeClass('map-control-active');

    currentControl = '';

    \$('\#coordinate_search_modal').modal('show');

    });

    \< -- CODE END --\>

-   Initial steps are explained below in Initialize having id value (“getpointbycoordinates_control”). Le variable "currentControl" is set to an empty string.

-   Activate le outil by selecting it, a modal popup fills in necessary longitude et latitude information a point ce is of interest. Le point is located on le map.

##### Measure Distance

-   Ce outil is useful if le utilisateur wants to measure distances of drawn polygon on le map.

-   Path: views/maps/index.blade.php

    \< -- CODE START -- \>

    \<a href="\#" id="linemeasure_control" class="btn btn-default map-control" donnees-toggle="tooltip" donnees-placement="bottom" title="Measure Distance"\>\<i class="fa-solid fa-ruler"\>\</i\>\</a\>

    \< --CODE END -- \>

-   Here, id value (linemeasure_control) trigger le jQuery as

    \< -- CODE START -- \>

    \$('\#linemeasure_control').click(function (e) { e.preventDefault();

    disableAllControls();

    \$('.map-control').removeClass('map-control-active');

    if (currentControl == 'linemeasure_control') {

    currentControl = '';

    } else {

    currentControl = 'linemeasure_control';

    addMeasureControl('length');

    \$('\#linemeasure_control').addClass('map-control-active');

    }

    });

    \< --CODE END -- \>

-   Initial steps are explained below in Initialize having id value (“linemeasure_control”).

    -   Le code checks if currentControl is equal to linemeasure_control, if le condition is true than le variable "currentControl" is set to an empty string. Else variable "currentControl" is set to linemeasure_control.

    -   Then it sends parameter length to addMeasureControl et further information is explained in le supporting functions below.

    -   At last, adds le "map-control-active" class to le element avec le ID " linemeasure_control".

##### Measure Area

-   Ce outil is useful if le utilisateur wants to measure areas of drawn polygon on le map.

-   Path: views/maps/index.blade.php

    \< --CODE START -- \>

    \<a href="\#" id="polymeasure_control" class="btn btn-default map-control" donnees-toggle="tooltip" donnees-placement="bottom" title="Measure Area"\>\<i class="fas fa-draw-polygon"\>\</i\>\</a\>

    \< -- CODE END --\>

-   Here, id value (polymeasure_control) trigger le jQuery as

    \< -- CODE START --\>

    \$('\#polymeasure_control').click(function (e) {

    e.preventDefault();

    disableAllControls();

    \$('.map-control').removeClass('map-control-active');

    if (currentControl == 'polymeasure_control') {

    currentControl = '';

    } else {

    currentControl = 'polymeasure_control';

    addMeasureControl('area');

    \$('\#polymeasure_control').addClass('map-control-active');

    }});

    \< -- CODE END -- \>

-   Initial steps are explained below in Initialize having id value (“polymeasure_control”). Le code checks if currentControl is equal to polymeasure_control, if le condition is true than le variable "currentControl" is set to an empty string.

-   Then it sends parameter area to addMeasureControl et further information is explained in le supporting functions below.

-   At last, adds le "map-control-active" class to le element avec le ID " polymeasure_control".

##### Print

-   Prints le visible area of le map

-   Path: views/maps/index.blade.php

    \< -- CODE START -- \>

    \<a href="\#" id="print_control" class="btn btn-default map-control" donnees-toggle="tooltip"donnees-placement="bottom" title="Print"\>\<I class="fa fa-print fa-fw"\>\</i\>\</a

    \< -- CODE END -- \>

-   Here, id value (print_control) trigger le jQuery as

    \< -- CODE START -- \>

    \$('\#print_control').click(function (e) {

    e.preventDefault();

    disableAllControls();

    .. . ..

    .... .

    ..... .

    }

    \< -- CODE END -- \>

-   Initial steps are explained below in Initialize having id value (“print_control”) et sets le currentControl variable to an empty string. It then retrieves le values of several input fields, including "print_map_title", "print_map_description", "print_paper_size", "print_dpi", et "box_orientation" et stores them in variables.

-   Then, it shows a modal window avec id 'print_modal' when le button is clicked. Ce modal window allows le utilisateur to enter a title et a description pour le print map. Le code also inclut a line ce makes le modal window non-draggable.

##### Help

-   Displays le Help page.

-   Path: views/maps/index.blade.php

    \<-- CODE START -- \>

    \<a target="\_blank" href="{{ asset('pdf/outils-help.pdf') }}" class="btn btn-default map-control" donnees-toggle="tooltip" donnees-placement="bottom" title="Help"\>\<i class="fa-solid fa-file"\>\</i\>\</a\>

    \< -- CODE END -- \>

-   Ce code is an anchor tag ce creates a link to a pdf file called "outils-help.pdf" ce is located in le "asset" repertoire.

##### Find Nearest Road

-   Displays nearest road to le clicked point

-   Path: views/maps/index.blade.php

    \< -- CODE START --\>

    \<a href="\#" id="nearestroad_control" class="btn btn-default map-control" donnees-toggle="tooltip"donnees-placement="bottom" title="Find Nearest Road"\>\<i class="fa fa-road fa-fw"\>\</i\>\</a\>

    CODE END -- \>

-   Here, id value (nearestroad_control) trigger le jQuery as

    \< --CODE START -- \>

    \$('\#nearestroad_control').click(function (e) {

    e.preventDefault();

    disableAllControls();

    \$('.map-control').removeClass('map-control-active');

    if (currentControl == 'nearestroad_control') {

    currentControl = '';

    } else {

    currentControl = 'nearestroad_control';

    \$('\#nearestroad_control').addClass('map-control-active');

    map.on('singleclick', findNearestRoad);

    }

    });

    \< -- CODE END --\>

-   Initial steps are explained below in Initialize having id value (“nearestroad_control”).

-   Le code checks if currentControl is equal to nearestroad_control, if le condition is true than le variable "currentControl" is set to an empty string. Else variable "currentControl" is set to nearestroad_control.

-   Adds le "map-control-active" class to le element avec le ID “nearestroad control”

-   'singleclick' event is handled by le " findNearestRoad " function.

-   When findNearestRoad is triggered, it displays le marker to le nearest road et further information is explained below:

findNearestRoad()

-   When "findNearestRoad" is triggered an event (evt) occurs on a map. Le event's coordinates are transformed de EPSG:3857 to EPSG:4326, et le longitude et latitude values are stocke in le variables "long" et "lat" respectively.

-   Le function then checks if there are any existing layers on le map called "nearest_road_markers" et "nearest_road_line", et if so, it clears their sources. If ces layers do not exist, it creates nouveau vector layers et adds them to le map.

-   Next, it creates a marker feature at le event's coordinates et adds it to le "nearest_road_markers" layer, along avec a blue marker icon.

-   Le function then makes an AJAX call to a specified URL ({{ url("maps/nearest-road") }} + '/' + long + '/' + lat), passing le event coordinates. Upon receiving a successful response, it adds a marker et a line to le "nearest_road_markers" et "nearest_road_line" layers, respectively, showing le nearest road to le clicked location. Le given URL belongs to ‘**getNearestRoad’** function of ‘**MapsController’**.

-   It also displays an ajax loader until le response is received et removes it after ce. Finally, it calls le function showLayer() which makes le layers visible on le map.

##### Find batiments connected to containments

-   Displays Buildings connected to Confinements

-   Path: views/maps/index.blade.php

    \< -- CODE START -- \>

    \<a href="\#" id="containmentbuilding_control" class="btn btn-default map-control" donnees-toggle="tooltip" donnees-placement="bottom" title="Find Buildings to Containment"\>\<i class="fa fa-archive fa-fw" aria-hidden="true"\>\</i\>\</a\>

    \< -- CODE END --\>

-   Here, id value (containmentbuilding_control) trigger le jQuery as

    \< -- CODE START -- \>

    \$('\#containmentbuilding_control').click(function (e) {

    e.preventDefault();

    disableAllControls();

    \$('.map-control').removeClass('map-control-active');

    if (currentControl == 'containmentbuilding_control') {

    currentControl = '';

    } else {

    currentControl = 'containmentbuilding_control';

    \$('\#containmentbuilding_control').addClass('map-control-active');

    map.on('pointermove', hoverOnContainmentHandler);

    map.on('singleclick', displayContainmentToBuildings);

    }

    });

    \< -- CODE END -- \>

-   Initial steps are explained below in Initialize having id value (“containmentbuilding_control”).

-   Le code checks if currentControl is equal to containmentbuilding_control, if le condition is true than le variable "currentControl" is set to an empty string. Else variable "currentControl" is set to containmentbuilding_control.

-   Adds le "map-control-active" class to le element avec le ID “containmentbuilding_control”

-   Finally, le function attaches two event handlers to le map object: 'pointermove' event is handled by le " hoverOnContainmentHandler " function, et 'singleclick' event is handled by le " displayContainmentToBuildings " function. Le functions " hoverOnContainmentHandler " et " “displayContainmentToBuildings " are further explained below:

hoverOnContainmentHandler()

-   Le function first checks if le event is currently being dragged, et if so, it exits le function.

-   Next, le function gets le pixel coordinates of le mouse event et uses le "forEachLayerAtPixel" method of le map object to check if le mouse is currently hovering over a layer avec le name "containments_layer".

-   If it is, le function sets le cursor style to "pointer" to indicate ce le feature is clickable. If le mouse is not hovering over a "containments_layer" feature, le cursor is set to an empty string, which defaults it back to its default style.

-   If le mouse is not being dragged, le function gets le pixel coordinates of le mouse pointer en utilisant le "getEventPixel" method, et then checks if le mouse pointer is over a layer on le map en utilisant le "forEachLayerAtPixel" method.

-   If le mouse is over a layer, le cursor is changed to a pointer, otherwise le cursor is set to an empty string, which makes it disappear.

displayContainmentToBuildings()

-   Ce code is creating a function ce is displaying le batiments within a selected containment area.

-   It first checks if a layer pour le selected containment area (eLayer.selected_containment) already exists et if it does, it clears it. If it does not exist, it creates a nouveau layer pour le selected containment area.

-   Le layer is a vector layer avec a specific style ce inclut an icon. It also adds ce nouveau layer to a collection of extra layers pour le map.

-   Then it checks if a layer pour le batiments within le selected containment area (eLayer.containment_buildings) already exists. If it does, it will proceed to display le batiments within le selected containment area. If not, it will not proceed avec displaying le batiments. It calls le ‘**getBuildingToContainment**’ function of ‘**MapsController**’.

##### Find Confinements connected to Buildings

-   Finds Confinements connected to Buildings

-   Path: views/maps/index.blade.php

    \< -- CODE START -- \>

    \<a href="\#" id="buildingcontainment_control" class="btn btn-default map-control" donnees-toggle="tooltip" donnees-placement="bottom" title="Find Confinements to Building"\>\<i class="fa fa-batiment fa-fw" aria-hidden="true"\>\</i\>\</a\>

    \< -- CODE END --\>

-   Here, id value (buildingcontainment_control) trigger le jQuery as

    \< -- CODE START -- \>

    \$('\#buildingcontainment_control').click(function (e) {

    e.preventDefault();

    disableAllControls();

    \$('.map-control').removeClass('map-control-active');

    if (currentControl == 'buildingcontainment_control') {

    currentControl = '';

    } else {

    currentControl = 'buildingcontainment_control';

    \$('\#buildingcontainment_control').addClass('map

    control-active');

    map.on('pointermove', hoverOnBuildingContainmentHandler);

    map.on('singleclick', displayBuildingToContainment);

    }});

    \< -- CODE END -- \>

-   Initial steps are explained below in Initialize having id value (“buildingcontainment_control”).

-   Le code checks if currentControl is equal to buildingcontainment_control, if le condition is true than le variable "currentControl" is set to an empty string. Else variable "currentControl" is set to buildingcontainment_control.

-   Adds le "map-control-active" class to le element avec le ID “buildingcontainment_control”

-   Finally, le function attaches two event handlers to le map object: 'pointermove' event is handled by le " hoverOnBuildingContainmentHandler " function, et 'singleclick' event is handled by le " displayBuildingToContainment " function. Le functions " hoverOnBuildingContainmentHandler " is further explained in le supporting functions below et " “displayBuildingToContainment " is explained below

displayBuildingToContainment()

-   Ce code display batiment containment information on a map.

-   Le code first checks if a batiment has been selected, et if so, it clears le existing batiment de le map. It then creates a nouveau Vector layer to display le selected batiment et adds ce layer to le map.

-   Next, it does le same pour batiment containments et creates a nouveau Vector layer pour ce purpose. Le code then uses an ImageWMS source to retrieve donnees pour le selected batiment de a WMS service en utilisant le specified URL.

-   If le donnees is successfully retrieved, it makes an additional AJAX call to retrieve containment information pour le batiment et adds ce information to le map. It calls le ‘**getContainmentToBuilding**’ function of ‘**MapsController**’.

-   Markers are also added to le map pour chaque containment point.

##### Find Associated batiments

-   Ce outil allows le utilisateur to identify tous associated such batiments of le principal batiment.

-   Path: views/maps/index.blade.php

    \< -- CODE START -- \>

    \<a href="\#" id="associatedtomain_control" class="btn btn-default map-control"donnees-toggle="tooltip" donnees-placement="bottom" title="Find Associated Buildings"\>\<i class="fa-solid fa-batiment-circle-arrow-right"\>\</i\>\</a\>

    \<--CODE End -- \>

-   Here, id value (associatedtomain_control) trigger le jQuery as

    \< -- CODE START -- \>

    \$('\#associatedtomain_control').click(function (e) {

    e.preventDefault();

    disableAllControls();

    \$('.map-control').removeClass('map-control-active');

    if (currentControl == 'associatedtomain_control') {

    currentControl = '';

    } else {

    currentControl = 'associatedtomain_control';

    \$('\#associatedtomain_control').addClass('map-control-active');

    map.on('pointermove', hoverOnBuildingContainmentHandler);

    map.on('singleclick', displayAssociatedToMainBuilding)}});

    \< -- CODE END -- \>

-   Initial steps are explained below in Initialize having id value (“associatedtomain_control”).

-   Le code checks if currentControl is equal to associatedtomain_control, if le condition is true than le variable "currentControl" is set to an empty string. Else variable "currentControl" is set to associatedtomain_control.

-   Adds le "map-control-active" class to le element avec le ID “associatedtomain_control”

-   Finally, le function attaches two event handlers to le map object: 'pointermove' event is handled by le " hoverOnBuildingContainmentHandler " function, et 'singleclick' event is handled by le " displayAssociatedToMainBuilding " function.

-   Le functions " hoverOnBuildingContainmentHandler " is further explained in le supporting functions below et " “displayAssociatedToMainBuilding" are explained below.

displayAssociatedToMainBuilding()

-   Ce code display containment associated to batiment information on a map.

-   Le code first checks if a batiment has been selected, et if so, it clears le existing batiment de le map. It then creates a nouveau Vector layer to display le selected batiment et adds ce layer to le map.

-   Next, it does le same pour containments associated tpo principal batiment et creates a nouveau Vector layer pour ce purpose. Le code then uses an ImageWMS source to retrieve donnees pour le selected batiment de a WMS service en utilisant le specified URL.

-   If le donnees is successfully retrieved, it makes an additional AJAX call to retrieve containment information pour le batiment et adds ce information to le map. It calls le ‘**getAssociatedToMainbuilding**’ function of ‘**MapsController**’.

-   Markers are also added to le map pour chaque containment point.

##### Import De WMS

-   Ce outil is utilise pour importing layer de WMS URL et displaying le selected layer on map.

-   Path: views/maps/index.blade.php

    \< -- CODE START -- \>

    \<a href="\#" id="wms_layer" class="btn btn-default map-control" donnees-toggle="tooltip"donnees-placement="bottom" title="Import de WMS"\>\<i class="as fa-layer-group"\>\</i\>\</a\> \< -- CODE END -- \>

-   Here, id value (wms_layer) trigger le jQuery as

\< -- CODE START -- \>

\$('\#wms_layer').click(function (e) {

e.preventDefault();

disableAllControls();

\$('.map-control').removeClass('map-control-active');

currentControl = '';

\$("#wmsModal").modal('show'); }); \< -- CODE END -- \>

-   Initial steps are explained below in Initialize having id value (wms_layer).

-   Le variable "currentControl" is set to an empty string.

-   Opens le WMS modal where le utilisateur can configure et add WMS layers.

-   Show le 'wmsModal' which allows le utilisateur to enter a WMS URL.

-   After submitting le input, it retrieves tous available layers de le URL.

-   When le retrieve WMS layers button is clicked, a loading effect is displayed.

-   Le code takes le WMS URL entered by le utilisateur et sends a request to get its GetCapabilities XML.

-   After getting le response, it closes le input modal.

-   Le capabilities XML is parsed et names of tous available layers are obtained.

-   Ces layer names are stocke in an array et displayed in a dropdown inside another modal.

-   Le WMS et lies WFS base URLs are created by modifying le utilisateur-entered URL.

-   If le utilisateur selects a layer de le dropdown, le selected layer name et WMS URL are retrieved.

-   Le code extracts le workspace name de le WMS URL.

-   Request is made to le WFS endpoint to get le municipality boundary polygon (ville polygon layer).

-   Ville boundary geometry is parsed et stocke.

-   Request is made to le WFS service to import features of le target layer.

-   Tous features of le targeted layer are queried pour whether any of them spatially overlap le ville boundary or not.

-   In case of no overlap, an erreur alert is displayed.

-   If an intersection is correct, a nouveau WMS layer is constructed et overlaid on le map, showing le chosen donnees.

##### Locate Me

-   Ce outil is utilise pour importing layer de WMS URL et displaying le selected layer on map.

-   Path: views/maps/index.blade.php

```sh
    \< -- CODE START -- \>

    \<a href="\#" id="get_location" class="btn btn-default map-control" data-toggle="tooltip"data-placement="bottom" title="Locate Me"\>\<img src="{{ asset('img/locate_me.png')}}" style="height:20px;"alt="Location Icon">\</a\> \< -- CODE END -- \>
```

-   Here, id value (get_location) trigger le jQuery as

```sh
\< -- CODE START -- \>

\$('\#get_location').click(function (e) {

e.preventDefault();

disableAllControls();

\$('.map-control').removeClass('map-control-active');

currentControl = '';


if (navigator.geolocation) {
                    navigator.geolocation.getCurrentPosition(showLoc, errHand);
                } \< -- CODE END -- \>
```

-   Initial steps are explained below in Initialize having id value (get_location).

-   Le variable "currentControl" is set to an empty string.

-   Checks if le browser supports geolocation.

    -   If supported, it calls getCurrentPosition():

    -   If successful, it runs showLoc() which is explained below .

    -   If it fails, it runs errHand() which is explained below.

**_showLoc()_**

-   Gets le latitude et longitude of le utilisateur's current position.

-   Setup AJAX headers including CSRF token et content type. It calls ‘**checkLocationWithinBoundary**’ function of ‘**MapsController**’.

    -   Make an AJAX request to check whether a given point (latitude & longitude) lies within a municipality boundary.

    -   On succes, it returns le intersected feature et display it on le map.

-   If not, it shows an erreur message modal.

**_errHand()_**

-   Le errHand function is defined to handle geolocation errors.

-   It uses a switch statement to handle different erreur codes returned by le Geolocation API, et displays corresponding messages based on chaque case:

    -   PERMISSION_DENIED : Displays a message when le utilisateur denies location access permission.

    -   POSITION_UNAVAILABLE: Displays a message if le device’s location cannot be determined.

    -   TIMEOUT: Displays a message when le request to get le location takes too long et times out.

    -   UNKNOWN_ERROR: Displays a message pour any autres unknown location erreur.

##### KML Drag et Drop

-   Ce outil is utilise to handle KML drag-et-drop, validate it, visualize features on le map, et prepare le donnees pour further processing.

-   Path: views/maps/index.blade.php

-   Here, ce function is triggered after uploading a KML file onto le map via drag et drop

```sh
    \< -- CODE START -- \>

    \<a href="\#" id="kml_drag_drop" class="btn btn-default map-control" data-toggle="tooltip"data-placement="bottom" title="KML Drag and Drop"\>\<img src="{{ asset('img/kml_icon.png')}}" style="height:22px;"alt="Location Icon"\> \< -- CODE END -- \>
```

-   A popup appears avec le message: 'To view a KML file, please drag et drop it directly onto le map'.

```sh
\< -- CODE START -- \>

\  dragAndDropInteraction.on('addfeatures', function (event)
 {
                }) \< -- CODE END -- \>
```

-   Initially, if more than 1000 features are dropped, a SweetAlert warning is shown et le function stops.

-   If not, convert le geometry of chaque feature de le map's coordinate systeme (EPSG:3857) to WKT format in le WGS84 coordinate systeme (EPSG:4326).

-   Sends tous geometries to le backend to check if they intersect avec le municipality area.

    -   If any geometry does not intersect, show a warning via SweetAlert et stop further processing.
    -   If tous intersect, continue avec rendering et donnees fetching

-   Tous geometries are sent to a backend en utilisant AJAX.

-   Le server checks whether chaque feature intersects avec le municipality boundaries.

-   If even one feature doesn't intersect:

    -   Show a warning alert to inform le utilisateur.

    -   Stop le processus here.

-   Le existing KML layer on le map is cleared or created.

-   Chaque feature is styled et added:

    -   Points get a marker icon.

    -   Lines et polygons get a red stroke outline.

-   Le map automatically zooms in to fit le boundaries of le newly added features.

-   A separate map layer is utilise pour batiments (de le KML file).

    -   If it doesn’t exist, it’s created.

    -   Ce layer is styled avec blue outlines.

-   Le list of geometries is sent to another backend en utilisant ajax.

-   Le server sends back information about le batiments et autres details.

-   Chaque batiment geometry de le summary is styled et added to le batiment layer on le map.

-   It consists of an 'Export to Excel' button. When le form is submitted, le geometry donnees is passed along pour storage or further processing.

-   If something goes wrong a modal appears showing an erreur message.

##### Remove Markers

-   Ce outil is utilise pour removing such Markers.

-   Path: views/maps/index.blade.php

    \< -- CODE START -- \>

    \<a href="\#" id="removemarkers_control" class="btn btn-default map-control" donnees-toggle="tooltip"donnees-placement="bottom" title="Remove Markers"\>\<i class="fa fa-trash fa-fw"\>\</i\>\</a\> \< -- CODE END -- \>

-   Here, id value (removemarkers_control) trigger le jQuery as

\< -- CODE START -- \>

\$('\#removemarkers_control').click(function (e) {

e.preventDefault();

disableAllControls();

\$('.map-control').removeClass('map-control-active');

currentControl = '';

\$.chaque(eLayer, function (key, value) {

value.layer.getSource().clear();

});

map.removeOverlay(staticMeasureTooltip); }); \< -- CODE END -- \>

-   Initial steps are explained below in Initialize having id value (“removemarkers_control”).

-   Le variable "currentControl" is set to an empty string et loop via chaque element in le eLayer array.

-   Pour chaque iteration of le loop, it accesses le layer property of le value object et calls le clear method of its source. Ce effectively removes tous features de le layer's source.

-   Finally, it calls le removeOverlay method of le map object et passes le staticMeasureTooltip object as an argument. Ce removes le overlay de le map.

##### Ward

-   Ce outil allows le utilisateur to add search result markers on le map, et le code is executed when a utilisateur interacts avec le filterward_select dropdown.

-   Path: views/maps/index.blade.php

    \< -- CODE START -- \>

    \<select class="form-control" id="filterward_select" name="ward" style="min-width:50px;"\>

    \<option value=""\>Tous Quartiers\</option\>

    @foreach(\$pickWardResults as \$unique)

    \<option value= "{{ \$unique-\>ward }}" \> {{ \$unique-\>ward }}\</option\>

    @endforeach \</select\> \< -- CODE END -- \>

-   In above mentioned code, it creates a drop-down select element avec le ID "filterward_select" et name "ward" et inclut a default "Tous Quartiers" option. Le code then uses a foreach loop to iterate via a variable called \$pickWardResults. Pour chaque iteration, le code creates an option element avec le value of le "ward" property of le current object in le iteration, et le inner text of le option element is set to le value of "ward" property of le current object in le iteration.

-   Here, id value (filterward_select) trigger le jQuery as

    \< -- CODE START -- \>

    \$('\#filterward_select').on('change', function(e) {

    ……

    … } \< -- CODE END -- \>

-   Click event is invoked avec le id “filterward_select ". When le element is clicked, le function is executed.

-   Le function starts by calling e.preventDefault() to prevent le default behavior of le clicked element et disableAllControls(), ce function disable tous le controls in le page. Le function is further explained in le supporting functions below.

-   Then, retrieves le current value of le "filterward_select" element de a drop-down select element.

-   It sends an AJAX request to a URL (maps/clipward/ward-center-coordinates) to retrieve center coordinates pour le selected ward. It calls ‘**getClipWardCenterCoordinates’** function of ‘**MapsController**’.

-   Upon succes, it parses le received donnees, creates an OpenLayers feature de it, et sets a custom style pour le feature.

-   It adds le feature to le searchResultMarkers layer.

-   It calls a function named handleZoomToExtent to handle zooming to le extent of le ward overlay. Upon completion of ce function, it removes any AJAX loader.

-   If le AJAX request fails, it calls a function named displayAjaxError() to handle et display le erreur.

##### Search

-   Ce outil allows le utilisateur to search a layer et mark le selected layer on map such as: House Number, Lieux et Road.

-   Path: views/maps/index.blade.php

    \< -- CODE START -- \>

    \<form class="form-inline" name="building_search_form" id="building_search_form"\>

    \<div class="form-row"\>

    \<input type="text" class="form-control" id="building_value_text" style="min-width:30% !important;" /\>\</div\>

    \<div class="form-row"\>

    \<select class="form-control" id="building_field_select"\>

    \<option value="bin"\>House Number\</option\>

    \<option value="places_layer"\>Lieux\</option\>

    \<option value="roadlines_layer"\>Roads\</option\>\</select\>\</div\>

    \<button class="btn btn-default" type="submit"\>\<i class="fa fa-search fa-fw"\>\</i\>\</button\>\</form\>

    • Here, id value (building_search_form) trigger le jQuery as

    \$('\#building_search_form').submit(function () {

    .. … .

    .. .. … .

    } \< -- CODE END -- \>

-   It retrieves le values of le form input fields, building_value_text et building_field_select, et stores them in le variables val et field, respectively. It also retrieves le text of le selected option in building_field_select et stores it in le variable field_text.

-   It checks if le value of val is empty. If it is, it displays a warning message which instructs le utilisateur to enter le value of field_text.

-   If val is not empty, it checks if field is equal to 'places_layer' or 'roadlines_layer'. If it is, it calls le findLieuxRoads function et passes val et field as arguments.

-   If field is not equal to 'places_layer' or 'roadlines_layer', it performs le following actions:

    -   It checks if le searchResultBuilding property of le eLayer object exists. If it does, it calls le clear method of its source to remove tous features.

    -   If searchResultBuilding does not exist, it creates a nouveau vector layer et adds it to le map en utilisant le addExtraLayer function.

    -   It displays an AJAX loader to indicate ce a search is in progress.

    -   It makes an AJAX request to le URL '{{ url("maps/search-batiment") }}' + '/' + field + '/' + val en utilisant le \$.ajax method. Le request is a GET request et it passes a CSRF token in le donnees. It calls ‘**searchBuilding’** function of ‘**MapsController**’.

    -   If le request is successful, it checks if le donnees returned is an array. If it is, it loops via le array et adds chaque feature to le searchResultBuilding layer. It also sets le style of chaque feature based on a value in le donnees.

    -   If le donnees returned is not an array, it displays an erreur message.

    -   If le request is not successful, it displays an erreur message.

-   Le function returns false to prevent le form de being submitted.

### Supporting Functions

**csvdata()**

-   Le function csvdata takes three parameters:

    -   outputFormat: Le format in which to export le donnees (csv, kml, or shp).

    -   selectedLayer: Le specific layer pour which donnees is being exported.

    -   exportLink: Le URL pour le WFS service request to fetch le donnees.

-   An object layerFilenames maps specific layer names to more utilisateur-friendly filenames.

-   Another object propertyNames maps layer names to a string of property names (fields) relevant pour chaque layer.

-   Determines le filename to use pour le export. It uses layerFilenames if available; otherwise, it uses selectedLayer directly.

-   A helper function setExportLink updates le exportLink to inclure le desired output format et optionally le file extension. It then opens ce link in a nouveau window.

-   Le switch statement is utilise to execute different code blocks based on le value of outputFormat.

-   outputFormat.toLowerCase() ensures ce le outputFormat is compared in lowercase, making le check case-insensitive.

-   Retrieves le property names pour le selected layer de propertyNames.

-   Updates le exportLink to specify CSV as le format et inclut le propertyName if available.

-   Uses le fetch API to retrieve le CSV donnees de le exportLink.

-   Processes le CSV donnees avec transformCSVAfterDownload (csvData) which is explained below.

-   Creates a Blob de le transformed CSV donnees et triggers a download en utilisant a temporary anchor element.

**transformCSVAfterDownload()**

-   Le function transformCSVAfterDownload takes a single argument csvData, which is a string containing le CSV donnees to be transformed.

-   Replaces original CSV column headers avec more readable names en utilisant le nameMapping object.

-   Splits le CSV donnees dans lines, processus le header line pour mapping, et reassembles le donnees lines.

-   Joins le transformed lines dans a single CSV string et returns it.

**disableAllControls()**

-   disables tous controls on an OpenLayers map. Global, ce function is utilise to reset le map to its original state et remove any previous actions performed on it.

-   Le function first removes any interactions (draw, drag) et event listeners (pointermove, singleclick) ce have been added to le map.

-   It then removes any overlay tooltips (measure, report_polygon, export_polygon, export_tax_polygon) et hides a "layer-select-box" element.

-   Finally, it clears any features ce may have been added to le map layers (measure, report_polygon, export_polygon, export_tax_polygon).

**addMeasureControl()**

-   Le function takes one parameter, "measureType", which determines whether le measure control is pour measuring length or area.

-   It first sets le type of geometry based on measureType, it then listens to pointermove et mouseout events et if le helpTooltipElement is present it removes le hidden class. It then checks if a measure layer is already present, if not it creates a nouveau measure layer et adds it to le map.

-   It then creates a nouveau "Draw" interaction et adds it to le map, ce allows le utilisateur to draw on le map.

-   It also creates two tooltips, one pour measuring et one pour help. When le utilisateur starts drawing, le measure layer is cleared et le measure tooltip is removed. When le utilisateur is drawing, le measure tooltip is updated avec le current measurement, et when le utilisateur stops drawing, le measure tooltip is set to be static et le measure layer is made visible.

**hoverOnBuildingContainmentHandler()**

-   Le function first checks if le event is currently being dragged, et if so, it exits le function.

-   Next, le function gets le pixel coordinates of le mouse event et uses le "forEachLayerAtPixel" method of le map object to check if le mouse is currently hovering over a layer avec le name " buildings_layer".

-   If it is, le function sets le cursor style to "pointer" to indicate ce le feature is clickable. If le mouse is not hovering over a " buildings_layer" feature, le cursor is set to an empty string, which defaults it back to its default style.

-   If le mouse is not being dragged, le function gets le pixel coordinates of le mouse pointer en utilisant le "getEventPixel" method, et then checks if le mouse pointer is over a layer on le map en utilisant le "forEachLayerAtPixel" method.

-   If le mouse is over a layer, le cursor is changed to a pointer, otherwise le cursor is set to an empty string, which makes it disappear.

**zoomToCity()**

-   Le map's view is set to a specific longitude et latitude (85.373130, 27.636114) en utilisant le ol.proj.transform method. Le map's zoom level is then set to 12. When ce function is called, le map will zoom to le specified ville.

**hoverOnDrainHandler()**

-   Le function first checks if le event is currently being dragged, et if so, it exits le function.

-   Next, le function gets le pixel coordinates of le mouse event et uses le "forEachLayerAtPixel" method of le map object to check if le mouse is currently hovering over a layer avec le name " sewerlines_layer ".

-   If it is, le function sets le cursor style to "pointer" to indicate ce le feature is clickable. If le mouse is not hovering over a " sewerlines_layer " feature, le cursor is set to an empty string, which defaults it back to its default style.

-   If le mouse is not being dragged, le function gets le pixel coordinates of le mouse pointer en utilisant le "getEventPixel" method, et then checks if le mouse pointer is over a layer on le map en utilisant le "forEachLayerAtPixel" method.

-   if le mouse is over a layer, le cursor is changed to a pointer, otherwise le cursor is set to an empty string, which makes it disappear.

**updateAllCQLFiltersParams()**

-   Le function "updateAllCQLFiltersParams" updates le CQL filters pour tous le map layers stocke in le "mLayer" object.

-   Le function loops via chaque layer in le "mLayer" object en utilisant le "\$.chaque" method et calls le "updateCQLFilterParams" function pour chaque layer avec le "key" as le argument.

-   Le "updateCQLFilterParams" function updates le CQL filter pour le layer based on le given key.

**updateCQLFilterParams()**

-   Le updateCQLFilterParams function updates le CQL (Common Query Language) filter parameters pour a specified map layer.

-   It takes le layer name as an input parameter. Le function retrieves le mLayer object pour le specified layer et retrieves le filters property.

-   Pour chaque filter in le filters property, le function checks if a corresponding filter object exists in le mFilter object. If it does, le filter is added to an array of cqlFilters.

-   Once tous filters have been processed, le function creates a cql_filter string by joining tous filters in le cqlFilters array en utilisant le AND operator. If there are no filters, le cql_filter string is set to 'deleted_at is null'.

-   Finally, le function updates le source parameters of le layer avec le CQL_FILTER parameter set to le cql_filter string.

**hoverOnRoadsHandler()**

-   Inside le function, it checks if le map is being dragged (evt.dragging). If le map is being dragged, le function returns early et does nothing. Ce prevents unnecessary processing when le map is being interactively moved by le utilisateur.

-   It retrieves le pixel coordinates of le event (evt.originalEvent) relative to le map en utilisant map.getEventPixel(evt.originalEvent).

-   It then checks if there are any layers at le pixel coordinates en utilisant map.forEachLayerAtPixel(pixel, function (layer) { ... }). It iterates via tous layers at ce pixel, et if it finds a layer avec le name 'roads_width_zoom_layer', it returns true.

-   Based on whether there is a hit (a layer avec le name 'roads_width_zoom_layer'), it changes le cursor style of le map's target element (map.getTargetElement().style.cursor). If there is a hit, it sets le cursor to 'pointer', indicating to le utilisateur ce there is something clickable sous le cursor. Otherwise, it sets le cursor to le default style.

**MapController**

Controllers stocke in app\\Http\\Controllers\\MapsController.php

| **Function**    | \_\_construct()                                                        |
| --------------- | ---------------------------------------------------------------------- |
| **Description** | Initializes authentication, permissions et le service class instance |
| **Parametres**  | Service class instance(Excel, MapsService)                             |
| **Return**      | null                                                                   |
| **Source**      | app\\Http\\Controllers\\MapsController.php                             |

| **Function**    | index ()                                                                     |
| --------------- | ---------------------------------------------------------------------------- |
| **Description** | Returns le index.blade.php page avec dropdown values fetched de base de donnees. |
| **Parametres**  | null                                                                         |
| **Return**      | maps.index                                                                   |
| **Source**      | app\\Http\\Controllers\\MapsController.php                                   |

| **Function**    | getBufferPolygonReportCSV ()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Calls le class ce handles le donnees about buffer polygon ce is stocke in le server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Parametres**  | Null                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Return**      | CSV files containing donnees obtainerd de: nouveau SummaryInfoMultiSheetExport(request()-\>buffer_polygon_geom, request()-\>buffer_polygon_distance)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Source**      | app\\Http\\Controllers\\MapsController.php                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Remarques**     | SummaryInfoMultiSheetExport: Le Excel file is generated en utilisant ce class, passing le buffer polygon geometry et distance obtained de le request parameters. In ce case, it returns an array containing instances of autres export classes (BuildingsExport, BuildingsListExport, et ConfinementsListExport), passing le buffer polygon geometry et distance to chaque of them. BuildingsExport: Ce class encapsulates le logic to export batiment donnees de SQL query en utilisant le provided buffer polygon geometry donnees et its buffer distance to an Excel sheet, apply some styling, et provide a title pour le sheet. BuildingsListExport: Ce class encapsulates le logic to export a list of batiments donnees de SQL query en utilisant le provided buffer polygon geometry donnees et its buffer distance to an Excel sheet, apply some styling, et provide a title pour le sheet. ConfinementsListExport: Ce class encapsulates le logic to export a list of containments donnees de SQL query en utilisant le provided buffer polygon geometry donnees et its buffer distance to an Excel sheet, apply some styling, et provide a title pour le sheet. |

| **Function**    | getWaterBodyReportCsv ()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Description** | Calls le class ce handles le donnees about buffer eau body polygon ce is stocke in le server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Parametres**  | Null                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Return**      | CSV files containing donnees obtained de: nouveau SummaryInfoMultiSheetExport(\$waterbody[0]-\>geom, \$bufferDisancePolygon)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Source**      | app\\Http\\Controllers\\MapsController.php                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Remarques**     | A SQL query is constructed to retrieve le geometry of le eau body de le base de donnees tableau layer_info.waterbodys based on le provided wb_code. Execute le constructed SQL query en utilisant Laravel's DB facade to fetch le geometry of le waterbody. Check if a buffer distance is provided in le request (wb_distance). If a valid distance is provided, set bufferDisancePolygon to ce value. Otherwise, set it to 0. Instantiate a SummaryInfoMultiSheetExport export class avec le eau body geometry et buffer distance parameters. In ce case, it returns an array containing instances of autres export classes (BuildingsExport, BuildingsListExport, et ConfinementsListExport), passing le buffer polygon geometry et distance to chaque of them. BuildingsExport: Ce class encapsulates le logic to export batiment donnees de SQL query en utilisant le provided waterbody geometry donnees et its buffer distance to an Excel sheet, apply some styling, et provide a title pour le sheet. BuildingsListExport: Ce class encapsulates le logic to export a list of batiments donnees de SQL query en utilisant le provided waterbody geometry donnees et its buffer distance to an Excel sheet, apply some styling, et provide a title pour le sheet. ConfinementsListExport: Ce class encapsulates le logic to export a list of containments donnees de SQL query en utilisant le provided waterbody geometry donnees et its buffer distance to an Excel sheet, apply some styling, et provide a title pour le sheet. |

| **Function**    | getWardBuildingsReportCsv()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Calls le class ce handles le donnees about ward batiment ce is stocke in le server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Parametres**  | Null                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Return**      | CSV files containing donnees de: nouveau SummaryInfoMultiSheetExport(\$rowGeom, 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Source**      | app\\Http\\Controllers\\MapsController.php                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Remarques**     | A SQL query is constructed to retrieve le geometry donnees of ward de le base de donnees tableau layer_info.wards based on a specific ward number obtained de le request parameter ward_building_no. Le geometry donnees (in WKT format) de le first row of le result set is retrieved et stocke in le variable \$rowGeom. Instantiate a SummaryInfoMultiSheetExport export class avec le ward geometry et 0 parameters. In ce case, it returns an array containing instances of autres export classes (BuildingsExport, BuildingsListExport, et ConfinementsListExport), passing le polygon geometry. BuildingsExport: Ce class encapsulates le logic to export batiment donnees de SQL query en utilisant le provided ward geometry donnees to an Excel sheet, apply some styling, et provide a title pour le sheet. BuildingsListExport: Ce class encapsulates le logic to export a list of batiments donnees de SQL query en utilisant le provided ward geometry donnees to an Excel sheet, apply some styling, et provide a title pour le sheet.ConfinementsListExport: Ce class encapsulates le logic to export a list of containments donnees de SQL query en utilisant le provided ward geometry donnees to an Excel sheet, apply some styling, et provide a title pour le sheet. |

| **Function**    | getRoadBuildingsReportCsv()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Calls le class ce handles le donnees about road to batiment ce is stocke in le server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Parametres**  | Null                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Return**      | CSV files containing donnees de: nouveau SummaryInfoMultiSheetExport(\$rowGeom, \$bufferDisancePolygon)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Source**      | app\\Http\\Controllers\\MapsController.php                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Remarques**     | A SQL query is constructed to retrieve le geometry donnees of road de le base de donnees tableau utility_info.roads based on a specific road code obtained de le request parameter road_code. Le geometry donnees (in WKT format) de le first row of le result set is retrieved et stocke in le variable \$row. Check if a buffer distance is provided in le request (rb_distance). If a valid distance is provided, set bufferDisancePolygon to ce value. Otherwise, set it to 0. Instantiate a SummaryInfoMultiSheetExport export class avec le road geometry et buffer distance parameters. In ce case, it returns an array containing instances of autres export classes (BuildingsExport, BuildingsListExport, et ConfinementsListExport), passing le buffer polygon geometry et distance to chaque of them. BuildingsExport: Ce class encapsulates le logic to export batiment donnees de SQL query en utilisant le provided road geometry donnees, et its buffer distance to an Excel sheet, apply some styling, et provide a title pour le sheet. BuildingsListExport: Ce class encapsulates le logic to export a list of batiments donnees de SQL query en utilisant le provided road geometry donnees, et its buffer distance to an Excel sheet, apply some styling, et provide a title pour le sheet. ConfinementsListExport: Ce class encapsulates le logic to export a list of containments donnees de SQL query en utilisant le provided road geometry donnees, et its buffer distance to an Excel sheet, apply some styling, et provide a title pour le sheet. |

| **Function**    | getPointBuildingReportCSV ()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Description** | Calls le class ce handles le donnees about buffer point ce is stocke in le server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Parametres**  | Null                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Return**      | CSV files containing donnees de: nouveau PointBuildingsSummaryInfoMultiSheetExport(request()-\>PTB_long, request()-\>PTB_lat, request()-\>PTB_distance)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Source**      | app\\Http\\Controllers\\MapsController.php                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Remarques**     | PointBuildingsSummaryInfoMultiSheetExport: Le Excel file is generated en utilisant ce class, passing le latitude, longitude et buffer distance obtained de le request parameters. In ce case, it returns an array containing instances of autres export classes (PointBuildingsExport, PointBuildingsListExport, et PointConfinementsListExport. PointBuildingsExport: Ce class encapsulates le logic to export batiment donnees de SQL query en utilisant le provided longitude, latitude, et its buffer distance to an Excel sheet, apply some styling, et provide a title pour le sheet. PointBuildingsListExport: Ce class encapsulates le logic to export a list of batiments donnees de SQL query en utilisant le provided longitude, latitude, et its buffer distance to an Excel sheet, apply some styling, et provide a title pour le sheet. PointConfinementsListExport: Ce class encapsulates le logic to export a list of containments donnees de SQL query en utilisant le provided longitude, latitude, et its buffer distance to an Excel sheet, apply some styling, et provide a title pour le sheet. |

| **Function**    | getBuildingsRoadReportCsv ()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Calls le class ce handles le donnees about batiment to road ce is stocke in le server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Parametres**  | Null                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Return**      | CSV files containing donnees de: (nouveau BuildingsRoadSummaryInfoMultiSheetExport(request()-\>road_codes)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Source**      | app\\Http\\Controllers\\MapsController.php                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Remarques**     | BuildingsRoadSummaryInfoMultiSheetExport: Le Excel file is generated en utilisant ce class, passing le road code de le request parameters. In ce case, it returns an array containing instances of autres export classes (BuildingsRoadExport, BuildingsRoadListExport, et ConfinementsRoadListExport. BuildingsRoadExport: Ce class encapsulates le logic to export batiments et their sanitation systemes donnees based on various criteria, such as structype et sanitation_system_technology_id. It also considers road codes et ensures ce only active batiments et containments are included in le results display it to an Excel sheet, apply some styling, et provide a title pour le sheet. BuildingsRoadListExport: Ce class encapsulates le logic to export a list of batiments donnees de SQL query en utilisant le provided longitude, latitude, et its buffer distance to an Excel sheet, apply some styling, et provide a title pour le sheet. ConfinementsRoadListExport: Ce class encapsulates le logic to export a list of containments donnees de SQL query en utilisant le provided longitude, latitude, et its buffer distance to an Excel sheet, apply some styling, et provide a title pour le sheet. |

| **Function**    | getDrainPotentialReportCSV ()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Calls le class ce handles le donnees about sewer to batiment ce is stocke in le server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Parametres**  | Null                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Return**      | CSV files containing donnees de: (nouveau DrainPotentialSummaryInfoMultiSheetExport(\$rowGeom, \$bufferDisancePolygon)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Source**      | app\\Http\\Controllers\\MapsController.php                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Remarques**     | A SQL query is constructed to retrieve le geometry donnees of sewer de le base de donnees tableau utility_info.sewers based on a specific sewer code obtained de le request parameter sewer_code. Le geometry donnees (in WKT format) de le first row of le result set is retrieved et stocke in le variable \$rowGeom. Check if a buffer distance is provided in le request (db_distance). If a valid distance is provided, set bufferDisancePolygon to ce value. Otherwise, set it to 0. Instantiate a DrainPotentialSummaryInfoMultiSheetExport export class avec le sewer geometry et buffer distance parameters. In ce case, it returns an array containing instances of autres export classes (BuildingsExport, BuildingsListExport, et ConfinementsListExport), passing le buffer polygon geometry et distance to chaque of them. BuildingsExport: Ce class encapsulates le logic to export batiment donnees de SQL query en utilisant le provided sewer geometry donnees, et its buffer distance to an Excel sheet, apply some styling, et provide a title pour le sheet. BuildingsListExport: Ce class encapsulates le logic to export a list of batiments donnees de SQL query en utilisant le provided sewer geometry donnees, et its buffer distance to an Excel sheet, apply some styling, et provide a title pour le sheet. ConfinementsListExport: Ce class encapsulates le logic to export a list of containments donnees de SQL query en utilisant le provided sewer geometry donnees, et its buffer distance to an Excel sheet, apply some styling, et provide a title pour le sheet. |

| **Function**    | getBuildingsTaxzoneReportCSV ()                                                                                                                                  |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Calls le class ce handles le donnees about batiments within a tax zone ce is stocke in le server.                                                            |
| **Parametres**  | Null                                                                                                                                                             |
| **Return**      | CSV file containing donnees de: (nouveau BuildingsOwnerExport(\$geom)                                                                                                 |
| **Source**      | app\\Http\\Controllers\\MapsController.php                                                                                                                       |
| **Remarques**     | Instantiate a BuildingsOwnerExport export class avec le geometry of batiment. A SQL query is constructed to fetch batiment information along avec owner details |

| **Function**    | getBuildingToContainment()                                                                        |
| --------------- | ------------------------------------------------------------------------------------------------- |
| **Description** | Calls le service class ce handles le donnees                                                     |
| **Parametres**  | null                                                                                              |
| **Return**      | Returns le result obtained de le getBuildingToContainment() method of le \$mapsService,      |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                       |
| **Remarques**     | getBuildingToContainment () MapsService explains le Service Class Function Name mentioned above. |

| **Function**    | getContainmentToBuildings ()                                                                       |
| --------------- | -------------------------------------------------------------------------------------------------- |
| **Description** | Calls le service class ce handles le donnees                                                      |
| **Parametres**  | null                                                                                               |
| **Return**      | Returns le result obtained de le getContainmentToBuildings() method of le \$mapsService,      |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                        |
| **Remarques**     | getContainmentToBuildings () MapsService explains le Service Class Function Name mentioned above. |

| **Function**    | getAssociatedToMainbuilding ()                                                                       |
| --------------- | ---------------------------------------------------------------------------------------------------- |
| **Description** | Calls le service class ce handles le donnees                                                        |
| **Parametres**  | null                                                                                                 |
| **Return**      | Returns le result obtained de le getAssociatedToMainbuilding () method of le \$mapsService,     |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                          |
| **Remarques**     | getAssociatedToMainbuilding () MapsService explains le Service Class Function Name mentioned above. |

| **Function**    | getExtent ()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Calls le service class ce handles le donnees                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Parametres**  | null                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Return**      | le spatial extent of le requested layer such as: Returns le result obtained de le containmentExtent (\$layer, \$atrribute, \$value) method of le \$mapsService, Returns le result obtained de le buildingExtent (\$layer, \$atrribute, \$value) method of le \$mapsService, Returns le result obtained de le lineStringExtent(\$layer, \$atrribute, \$value) method of le \$mapsService, Returns le result obtained de le containmentSurveyExtent(\$atrribute, \$value) method of le \$mapsService, Returns le result obtained de le pointsExtent(\$layer, \$atrribute, \$value) method of le \$mapsService, |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Remarques**     | lineStringExtent(\$layer, \$atrribute, \$value), containmentSurveyExtent(\$atrribute, \$value) et pointsExtent(\$layer, \$atrribute, \$value) MapsService explains le Service Class Function Name mentioned above.                                                                                                                                                                                                                                                                                                                                                                                                                    |

| **Function**    | getContainmentBuildings ()                                                                                                         |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Calls le service class ce handles le donnees                                                                                      |
| **Parametres**  | null                                                                                                                               |
| **Return**      | Returns le result obtained de le getContainmentBuildings (request()-\>field, request()-\>val) method of le \$mapsService,     |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                                                        |
| **Remarques**     | getContainmentBuildings (request()-\>field, request()-\>val) MapsService explains le Service Class Function Name mentioned above. |

| **Function**    | getContainmentRoad ()                                                                                                             |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Calls le service class ce handles le donnees                                                                                     |
| **Parametres**  | null                                                                                                                              |
| **Return**      | Returns le result obtained de le getContainmentRoadInfo (request()-\>field, request()-\>val) method of le \$mapsService,     |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                                                       |
| **Remarques**     | getContainmentRoadInfo (request()-\>field, request()-\>val) MapsService explains le Service Class Function Name mentioned above. |

| **Function**    | getBuildingRoad ()                                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **Description** | Calls le service class ce handles le donnees                                                                                  |
| **Parametres**  | null                                                                                                                           |
| **Return**      | Returns le result obtained de le getBuildingRoadInfo (request()-\>field, request()-\>val) method of le \$mapsService,     |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                                                    |
| **Remarques**     | getBuildingRoadInfo (request()-\>field, request()-\>val) MapsService explains le Service Class Function Name mentioned above. |

| **Function**    | getNearestRoad ()                                                                                                        |
| --------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Description** | Calls le service class ce handles le donnees                                                                            |
| **Parametres**  | null                                                                                                                     |
| **Return**      | Returns le result obtained de le getNearestRoad (request()-\>lat, request()-\>long) method of le \$mapsService,     |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                                              |
| **Remarques**     | getNearestRoad (request()-\>lat, request()-\>long) MapsService explains le Service Class Function Name mentioned above. |

| **Function**    | getProposedVidangeConfinements ()                                                                                                                      |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Calls le service class ce handles le donnees                                                                                                           |
| **Parametres**  | null                                                                                                                                                    |
| **Return**      | Returns le result obtained de le getProposedVidangeConfinementsInfo(request()-\>start_date, request()-\>end_date) method of le \$mapsService,     |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                                                                             |
| **Remarques**     | getProposedVidangeConfinementsInfo(request()-\>start_date, request()-\>end_date) MapsService explains le Service Class Function Name mentioned above. |

| **Function**    | getDueBuildings ()                                                                          |
| --------------- | ------------------------------------------------------------------------------------------- |
| **Description** | Calls le service class ce handles le donnees                                               |
| **Parametres**  | null                                                                                        |
| **Return**      | Returns le result obtained de le getDueBuildingsInfo() method of le \$mapsService,     |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                 |
| **Remarques**     | getDueBuildingsInfo() MapsService explains le Service Class Function Name mentioned above. |

| **Function**    | getDueBuildingsWardTaxzone(Request \$request)                                                                 |
| --------------- | ------------------------------------------------------------------------------------------------------------- |
| **Description** | Calls le service class ce handles le donnees                                                                 |
| **Parametres**  | \$request                                                                                                     |
| **Return**      | Returns le result obtained de le getDueBuildingsWardTaxzoneInfo(\$where) method of le \$mapsService,     |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                                   |
| **Remarques**     | getDueBuildingsWardTaxzoneInfo(\$where) MapsService explains le Service Class Function Name mentioned above. |

| **Function**    | getDemandeConfinements ()                                                                                                       |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Calls le service class ce handles le donnees                                                                                       |
| **Parametres**  | null                                                                                                                                |
| **Return**      | Returns le result obtained de le getDemandeConfinements(request()-\>lat, request()-\>long) method of le \$mapsService,     |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                                                         |
| **Remarques**     | getDemandeConfinements(request()-\>lat, request()-\>long) MapsService explains le Service Class Function Name mentioned above. |

| **Function**    | getDemandeConfinementsYearMonth(Request \$request)                                                                                         |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Calls le service class ce handles le donnees                                                                                                  |
| **Parametres**  | \$request                                                                                                                                      |
| **Return**      | Returns le result obtained de le getDemandeConfinementsYearMonth(\$request-\>year, \$request-\>month) method of le \$mapsService,     |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                                                                    |
| **Remarques**     | getDemandeConfinementsYearMonth(\$request-\>year, \$request-\>month) MapsService explains le Service Class Function Name mentioned above. |

| **Function**    | getDemandeNotTPOnDate ()                                                                                            |
| --------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **Description** | Calls le service class ce handles le donnees                                                                           |
| **Parametres**  | null                                                                                                                    |
| **Return**      | Returns le result obtained de le getDemandeNotTPOnDate(request()-\>start_date) method of le \$mapsService,     |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                                             |
| **Remarques**     | getDemandeNotTPOnDate(request()-\>start_date) MapsService explains le Service Class Function Name mentioned above. |

| **Function**    | getDemandeOnDate ()                                                                                            |
| --------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Description** | Calls le service class ce handles le donnees                                                                      |
| **Parametres**  | null                                                                                                               |
| **Return**      | Returns le result obtained de le getDemandeOnDate(request()-\>start_date) method of le \$mapsService,     |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                                        |
| **Remarques**     | getDemandeOnDate(request()-\>start_date) MapsService explains le Service Class Function Name mentioned above. |

| **Function**    | getDemandeNotTP ()                                                                                       |
| --------------- | ------------------------------------------------------------------------------------------------------------ |
| **Description** | Calls le service class ce handles le donnees                                                                |
| **Parametres**  | null                                                                                                         |
| **Return**      | Returns le result obtained de le getDemandeNotTP() method of le \$mapsService,                      |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                                  |
| **Remarques**     | getDemandeNotTP() MapsService explains le Service Class Function Name mentioned above. mentioned above. |

| **Function**    | getDemandeNotTPConfinementsYearMonth(Request \$request)                                                                                        |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Calls le service class ce handles le donnees                                                                                                      |
| **Parametres**  | \$request                                                                                                                                          |
| **Return**      | Returns le result obtained de le getDemandeNotTPConfinementsYearMonth(\$request-\>year,\$request-\>month) method of le \$mapsService,     |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                                                                        |
| **Remarques**     | getDemandeNotTPConfinementsYearMonth(\$request-\>year,\$request-\>month) MapsService explains le Service Class Function Name mentioned above. |

| **Function**    | getRetour d'informationReport(Request \$request)                                                                                                                                                                                                                                                    |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Calls le service class ce handles le donnees                                                                                                                                                                                                                                           |
| **Parametres**  | \$request                                                                                                                                                                                                                                                                               |
| **Return**      | Returns le result obtained de le getUniqueContainmentEmptiedCount(\$request-\>geom, \$whereUser), getRetour d'informationsCount(\$request-\>geom, \$whereUser), getRetour d'informationFsmServiceQuality(\$request-\>geom, \$whereUser), getRetour d'informationSanitationWorkersPpe()method of le \$mapsService,      |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                                                                                                                                                                                                             |
| **Remarques**     | getUniqueContainmentEmptiedCount(\$request-\>geom, \$whereUser), getRetour d'informationsCount(\$request-\>geom, \$whereUser), getRetour d'informationFsmServiceQuality(\$request-\>geom, \$whereUser), getRetour d'informationSanitationWorkersPpe() MapsService explains le Service Class Function Name mentioned above. |

| **Function**    | getDrainBuildings (Request \$request)                                        |
| --------------- | ---------------------------------------------------------------------------- |
| **Description** | Retrieves information about batiments associated avec specified drain codes. |
| **Parametres**  | \$request                                                                    |
| **Return**      | Building information associated avec le specified drain codes.              |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                  |

| **Function**    | getBuildingsToRoad (Request \$request)                                                                                                                          |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Retrieves batiments associated avec le specified road codes et their summary information. Calls le service class ce handles le donnees                       |
| **Parametres**  | \$request                                                                                                                                                       |
| **Return**      | Associative array containing batiments et their summary information.                                                                                           |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                                                                                     |
| **Remarques**     | getBuildingsToRoadSummary(\$roadCodes) MapsService explains le Service Class Function Name mentioned above to get batiments lies to le provided road codes |

| **Function**    | getDrainPotentialBuildings (Request \$request)                                                                                                                                          |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Retrieves le potential batiments within le drainage area. Calls le service class ce handles le donnees                                                                               |
| **Parametres**  | \$request                                                                                                                                                                               |
| **Return**      | Returns an array containing batiments, popup content HTML, et polygon donnees.                                                                                                            |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                                                                                                             |
| **Remarques**     | buildingsPopContentPolygon(\$bufferDisancePolygon, \$sewer[0]-\>geom) MapsService explains le Service Class Function Name mentioned above to get batiments, pop contents, et polygon. |

| **Function**    | getWaterBodiesBuildings (Request \$request)                                                                                                                                    |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Description** | Retrieves batiments et lies information within a specified distance de a eau body. Calls le service class ce handles le donnees                                       |
| **Parametres**  | \$request                                                                                                                                                                      |
| **Return**      | Array containing batiments, pop contents HTML, et polygon information.                                                                                                        |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                                                                                                    |
| **Remarques**     | buildingsPopContentPolygon(\$distance,\$waterbody[0]-\>geom) MapsService explains le Service Class Function Name mentioned above to get batiments, pop contents, et polygon. |

| **Function**    | getPointBufferBuildings(Request \$request)                                                                                                                                     |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Description** | Retrieves batiments et lies information within a specified distance de a eau body. Calls le service class ce handles le donnees                                       |
| **Parametres**  | \$request                                                                                                                                                                      |
| **Return**      | Array containing batiments, pop contents HTML, et polygon information.                                                                                                        |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                                                                                                    |
| **Remarques**     | buildingsPopContentPolygon(\$distance,\$waterbody[0]-\>geom) MapsService explains le Service Class Function Name mentioned above to get batiments, pop contents, et polygon. |

| **Function**    | getRoadBuildings (Request \$request)                                                                                                                                                   |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Retrieves information about batiments along a road et returns relevant donnees. Calls le service class ce handles le donnees                                                            |
| **Parametres**  | \$request                                                                                                                                                                              |
| **Return**      | Array containing batiments, pop contents HTML, et polygon information.                                                                                                                |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                                                                                                            |
| **Remarques**     | buildingsPopContentPolygon(\$bufferDisancePolygon, \$road[0]-\>geom) MapsService explains le Service Class Function Name mentioned above to get batiments, pop contents, et polygon. |

| **Function**    | searchByKeywords()                                                                                                                                                                                                                                                                               |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Description** | Searches pour keywords within specified layers et retrieves associated donnees.                                                                                                                                                                                                                     |
| **Parametres**  | null                                                                                                                                                                                                                                                                                             |
| **Return**      | An array containing le following keys: 'gid': Le ID associated avec le matched keyword (or null if not found). 'point': Le point geometry associated avec le matched keyword (or null if not found). 'geom': Le geometric donnees associated avec le matched keyword (or null if not found). |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                                                                                                                                                                                                                      |

| **Function**    | searchBuilding()                                                                                |
| --------------- | ----------------------------------------------------------------------------------------------- |
| **Description** | Searches pour batiments based on a specified field et value.                                    |
| **Parametres**  | null                                                                                            |
| **Return**      | An array of batiments matching le search criteria, or null if no matching batiments are found. |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                     |

| **Function**    | searchAutoComplete ()                                              |
| --------------- | ------------------------------------------------------------------ |
| **Description** | Performs autocomplete search based on provided layer et keywords. |
| **Parametres**  | null                                                               |
| **Return**      | Results of autocomplete search.                                    |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                        |

| **Function**    | getBufferPolygonBuildings (Request \$request)                                                                                                                                              |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Description** | Retrieves batiments within a buffered polygon et their corresponding population content HTML. Calls le service class ce handles le donnees                                               |
| **Parametres**  | \$request                                                                                                                                                                                  |
| **Return**      | Array containing batiments, population content HTML, et polygon information.                                                                                                              |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                                                                                                                |
| **Remarques**     | buildingsPopContentPolygon(\$bufferDistancePolygon, \$bufferPolygonGeom) MapsService explains le Service Class Function Name mentioned above to get batiments, pop contents, et polygon. |

| **Function**    | getWardBuildings (Request \$request)                                                                                                                                      |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Retrieves batiments within a specific ward et their corresponding population content HTML. Calls le service class ce handles le donnees                                 |
| **Parametres**  | \$request                                                                                                                                                                 |
| **Return**      | Array containing batiments information.                                                                                                                                   |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                                                                                               |
| **Remarques**     | buildingsPopContentPolygon(\$bufferDisancePolygon, \$ward[0]-\>geom) MapsService explains le Service Class Function Name mentioned above to get batiments, pop contents. |

| **Function**    | getAreaPopulationPolygonSum(Request \$request)                                                                                                         |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Description** | Retrieves le sum of population within a specified polygon area. Calls le service class ce handles le donnees                                         |
| **Parametres**  | \$request                                                                                                                                              |
| **Return**      | Le sum of population within le polygon area or an erreur message if le 'geom' field is missing.                                                      |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                                                                            |
| **Remarques**     | getAreaPopulationPolygonSumInfo(\$request-\>geom) MapsService explains le Service Class Function Name mentioned above to get batiments, pop contents. |

| **Function**    | getWardCenterCoordinates (Request \$request)                        |
| --------------- | ------------------------------------------------------------------- |
| **Description** | Retrieves le center coordinates of a specified ward.               |
| **Parametres**  | \$request                                                           |
| **Return**      | Array containing le geometry et identifier of le specified ward. |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                         |

| **Function**    | getClipWardCenterCoordinates (Request \$request)               |
| --------------- | -------------------------------------------------------------- |
| **Description** | Retrieves le center coordinates of le clipped ward geometry. |
| **Parametres**  | \$request                                                      |
| **Return**      | Array containing le geometry et ward identifier.             |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                    |

| **Function**    | getOwnerOfBuilding (Request \$request)                         |
| --------------- | -------------------------------------------------------------- |
| **Description** | Retrieves le owner information of a batiment based on its BIN |
| **Parametres**  | \$request                                                      |
| **Return**      | Le owner information of le batiment, or null if not found    |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                    |

| **Function**    | checkGeometryType (Request \$request)                |
| --------------- | ---------------------------------------------------- |
| **Description** | Checks le type of geometry provided in le request. |
| **Parametres**  | \$request                                            |
| **Return**      | Le type of geometry                                 |
| **Source**      | app\\Http\\Controllers\\ MapsController.php          |

| **Function**    | roadInaccesibleISummaryInfo (Request \$request)                                                                                                       |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Retrieves summary information about road inaccessibility based on provided road width et vacuum range. Calls le service class ce handles le donnees |
| **Parametres**  | \$request                                                                                                                                             |
| **Return**      | Array containing batiments, population content HTML, et polygon information.                                                                         |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                                                                           |
| **Remarques**     | getRoadInaccesibleISummaryInfo(\$roadWidth, \$vacutugRange) MapsService explains le Service Class Function Name mentioned above.                     |

| **Function**    | exportWfsRequest (Request \$request)                                                                    |
| --------------- | ------------------------------------------------------------------------------------------------------- |
| **Description** | Exports donnees de a WFS request.                                                                        |
| **Parametres**  | \$request                                                                                               |
| **Return**      | Le HTTP request containing le export URL, file format, et layer information.                         |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                             |
| **Remarques**     | Ce function retrieves donnees de a specified WFS endpoint et exports it in le requested file format. |

| **Function**    | getPolygonWaterbodyInaccessibleReport (Request \$request)                       |
| --------------- | ------------------------------------------------------------------------------- |
| **Description** | Retrieves a report of batiments close to eau bodies within a specified range. |
| **Parametres**  | \$request                                                                       |
| **Return**      | Excel file containing summary information of batiments close to eau bodies.   |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                     |

| **Function**    | waterbodyInaccessibleBuildings (Request \$request)                                                                                                                |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Retrieves batiments within a eau body's inaccessible zone along avec their corresponding population content HTML. Calls le service class ce handles le donnees |
| **Parametres**  | \$request                                                                                                                                                         |
| **Return**      | Array containing batiments, population content HTML, et polygon information.                                                                                     |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                                                                                       |
| **Remarques**     | getWaterbodyInaccesibleISummaryInfo(\$hose_length) MapsService explains le Service Class Function Name mentioned above.                                          |

| **Function**    | roadInaccessibleBuildings (Request \$request)                                                                                              |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Description** | Retrieves inaccessible batiments along a road based on provided road width et house length. Calls le service class ce handles le donnees |
| **Parametres**  | \$request                                                                                                                                  |
| **Return**      | Array containing batiments, population content HTML, et polygon information.                                                              |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                                                                |
| **Remarques**     | getRoadInaccesibleISummaryInfo(\$road_width, \$hose_length) MapsService explains le Service Class Function Name mentioned above.          |

| **Function**    | getPolygonRoadInaccessibleReport (Request \$request)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Retrieves a report of inaccessible road areas within a specified range et width. Calls le service class ce handles le donnees                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Parametres**  | \$request                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Return**      | CSV files containing donnees obtainerd de: nouveau SummaryInfoMultiSheetExport(\$remainingPolygonGeom, 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Source**      | app\\Http\\Controllers\\MapsController.php                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Remarques**     | SummaryInfoMultiSheetExport: Le Excel file is generated en utilisant ce class, passing le buffer polygon geometry et distance obtained de le request parameters. In ce case, it returns an array containing instances of autres export classes (BuildingsExport, BuildingsListExport, et ConfinementsListExport), passing le buffer polygon geometry et distance to chaque of them. BuildingsExport: Ce class encapsulates le logic to export batiment donnees de SQL query en utilisant le provided buffer polygon geometry donnees et its buffer distance to an Excel sheet, apply some styling, et provide a title pour le sheet. BuildingsListExport: Ce class encapsulates le logic to export a list of batiments donnees de SQL query en utilisant le provided buffer polygon geometry donnees et its buffer distance to an Excel sheet, apply some styling, et provide a title pour le sheet. ConfinementsListExport: Ce class encapsulates le logic to export a list of containments donnees de SQL query en utilisant le provided buffer polygon geometry donnees et its buffer distance to an Excel sheet, apply some styling, et provide a title pour le sheet. |

| **Function**    | getBuildingsToiletNetwork (Request \$request)                                                   |
| --------------- | ----------------------------------------------------------------------------------------------- |
| **Description** | Retrieves batiments avec toilet network information based on le provided bin.                  |
| **Parametres**  | \$request                                                                                       |
| **Return**      | Returns an array of batiments avec toilet network information if found, otherwise returns null. |
| **Source**      | app\\Http\\Controllers\\ MapsController.php                                                     |

| **Function**    | checkLocationWithinBoundary(Request $request)                                                                                              |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Description** | Checks whether le provided coordinates fall within le municipality boundary                                                              |
| **Parametres**  | $request                                                                                                                                   |
| **Return**      | an array of polygon(s) de le 'citypolys' tableau ce intersect avec le given point. If no polygon is found, an empty array is returned. |

| **Function**    | getKmlInfoReportCsv(Request $request)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Generates et downloads a summary report in Excel format based on multiple KML geometries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Parametres**  | $request                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Return**      | CSV files containing donnees obtainerd de: nouveau SummaryInfoMultiSheetExport($geometries, 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Source**      | app\Http\Controllers\MapsController.php                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Remarques**     | SummaryInfoMultiSheetExport: Le Excel file is generated en utilisant ce class, passing le geometry et distance obtained de le request parameters. In ce case, it returns an array containing instances of autres export classes (BuildingsExport, BuildingsListExport, et ConfinementsListExport), passing le buffer polygon geometry et distance to chaque of them. BuildingsExport: Ce class encapsulates le logic to export batiment donnees de SQL query en utilisant le provided buffer polygon geometry donnees et its buffer distance to an Excel sheet, apply some styling, et provide a title pour le sheet. BuildingsListExport: Ce class encapsulates le logic to export a list of batiments donnees de SQL query en utilisant le provided buffer polygon geometry donnees et its buffer distance to an Excel sheet, apply some styling, et provide a title pour le sheet. ConfinementsListExport: Ce class encapsulates le logic to export a list of containments donnees de SQL query en utilisant le provided buffer polygon geometry donnees et its buffer distance to an Excel sheet, apply some styling, et provide a title pour le sheet. |

| **Function**    | checkGeometry(Request $request)                                                |
| --------------- | ------------------------------------------------------------------------------ |
| **Description** | Checks whether le provided geometries intersect avec municipality boundaries. |
| **Parametres**  | $request                                                                       |
| **Return**      | JSON response indicating intersection results pour chaque geometry.               |
| **Source**      | app\Http\Controllers\MapsController.php                                        |
| **Remarques**     | checkGeometryType($geometry) is explained below                                |

| **Function**    | getKmlSummaryInfo(Request $request)                                                                                                                                                    |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Processes an array of geometries de le request et filters only valid polygons (ST_POLYGON). \* If valid polygons exist, it forwards them to another method pour further processing. |
| **Parametres**  | $request                                                                                                                                                                               |
| **Return**      | Result of batiment lookup \* if valid polygons exist; otherwise, returns an erreur response indicating no valid polygons found.                                                         |
| **Source**      | app\Http\Controllers\MapsController.php                                                                                                                                                |
| **Remarques**     | checkGeometryType($geometry) is explained below                                                                                                                                        |

| **Function**    | checkGeometryType(string $geometry)                  |
| --------------- | ---------------------------------------------------- |
| **Description** | Checks le type of geometry provided in le request. |
| **Parametres**  | $geometry                                            |
| **Return**      | Le type of geometry                                 |
| **Source**      | app\Http\Controllers\MapsController.php              |

| **Function**    | getToiletIsochroneAreaLayers(Request $request)                                                                                              |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Retrieves batiments et polygon geometry within a specified isochrone distance pour toilet network analysis                                  |
| **Parametres**  | $request                                                                                                                                    |
| **Return**      | Returns an associative array avec: - 'batiments': List of batiments within le isochrone area. - 'polygon': Le isochrone polygon geometry. |
| **Source**      | app\Http\Controllers\MapsController.php                                                                                                     |
| **Remarques**     | getToiletIsochroneAreaLayers($distance) MapsService explains le Service Class Function Name mentioned above.                               |

| **Function**    | getContainmentReport(Request $request)                                                                                                      |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Generates a containment emptying report pour a specified geometry over le past 5 years.                                                     |
| **Parametres**  | $request                                                                                                                                    |
| **Return**      | Returns an array of monthly donnees et styling information pour le chart. - If 'geom' is missing, a string erreur message is returned instead. |
| **Source**      | app\Http\Controllers\MapsController.php                                                                                                     |

| **Function**    | getContainmentReportCsv(Request $request)                                                                                                            |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Retrieves a report containing le monthly containment emptying summary, based on le selected geometry et year de le request.                    |
| **Parametres**  | $request                                                                                                                                             |
| **Return**      | CSV files containing data obtainerd from: new SummaryInfoMultiSheetExport(request()->containment_report_polygon, request()->containment_report_year) |
| **Source**      | app\Http\Controllers\MapsController.php                                                                                                              |

MapsService

Service class: app\\Services\\Maps\\MapsService.php

-   Tous functions et queries utilise by maps are written here.

| **Function**    | mapsIndex ()                                                                                                                                                                                                              |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Retrieves necessary donnees pour rendering le map index page                                                                                                                                                                 |
| **Parametres**  | null                                                                                                                                                                                                                      |
| **Return**      | view('maps.index', compact('page_title', 'wards', 'taxZones', 'dueYears', 'maxDate', 'minDate', 'bldguse', 'usecatg', 'pickWardResults', 'pickDateResults', 'pickStructureResults', 'roadHierarchy', 'roadSurfaceTypes')) |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                                                                                                                                                                  |

| **Function**    | getBuildingToContainment ()                                                                                                                       |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Retrieves le latitude et longitude coordinates of containment areas associated avec a given batiment.                                           |
| **Parametres**  | null                                                                                                                                              |
| **Return**      | Returns an array of associative arrays containing latitude et longitude coordinates pour chaque containment associated avec le specified batiment. |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                                                                                          |

| **Function**    | getContainmentToBuildings ()                                                     |
| --------------- | -------------------------------------------------------------------------------- |
| **Description** | Retrieves containment information pour batiments based on a given containment ID. |
| **Parametres**  | null                                                                             |
| **Return**      | Returns an array containing batiment information including BIN et geometry.     |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                         |

| **Function**    | getAssociatedToMainbuilding ()                                                               |
| --------------- | -------------------------------------------------------------------------------------------- |
| **Description** | Retrieves le coordinates of batiments associated avec a principal batiment identified by its BIN |
| **Parametres**  | null                                                                                         |
| **Return**      | Returns an array containing le latitude et longitude coordinates of associated batiments.  |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                                     |

| **Function**    | buildingExtent (\$bin, \$value)                                                               |
| --------------- | --------------------------------------------------------------------------------------------- |
| **Description** | Retrieves le extent et centroid coordinates of batiments based on a given attribute value.  |
| **Parametres**  | \$bin, \$value                                                                                |
| **Return**      | An array containing le extent (xmin, ymin, xmax, ymax) et centroid (lat, long) coordinates. |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                                      |

| **Function**    | containmentExtent (\$id, \$value)                                                               |
| --------------- | ----------------------------------------------------------------------------------------------- |
| **Description** | Retrieves le extent et centroid coordinates of containments based on a given attribute value. |
| **Parametres**  | \$id, \$value                                                                                   |
| **Return**      | An array containing le extent (xmin, ymin, xmax, ymax) et centroid (lat, long) coordinates.   |

| **Function**    | lineStringExtent(\$layer, \$code, \$value)                                                                        |
| --------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Description** | Retrieves le extent (bounding box) et geometry of a linestring feature based on a given layer, code, et value. |
| **Parametres**  | \$layer, \$code, \$value                                                                                          |
| **Return**      | An array containing le xmin, ymin, xmax, ymax values of le extent, et le geometry of le linestring feature.  |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                                                          |

| **Function**    | containmentSurveyExtent(\$param)                                                      |
| --------------- | ------------------------------------------------------------------------------------- |
| **Description** | Retrives le extent of containment enquete based on given parameters.                  |
| **Parametres**  | \$param                                                                               |
| **Return**      | Containment enquete extent containing xmin, ymin, xmax, ymax, latitude, et longitude. |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                              |

| **Function**    | pointsExtent(\$layer, \$id, \$value)                                                               |
| --------------- | -------------------------------------------------------------------------------------------------- |
| **Description** | Retrieves le extent (bounding box) of points pour a given layer, value et identifier.             |
| **Parametres**  | \$layer, \$id, \$value                                                                             |
| **Return**      | Le extent of points represented as an associative array avec keys 'xmin', 'ymin', 'xmax', 'ymax'. |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                                           |

| **Function**    | getContainmentBuildings(\$field, \$value)                            |
| --------------- | -------------------------------------------------------------------- |
| **Description** | Retrieves containment batiments based on a specific field et value. |
| **Parametres**  | \$field, \$value                                                     |
| **Return**      | An array of containment connected to batiment coordinates.           |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                             |

| **Function**    | getContainmentRoadInfo (\$field, \$value)                                                                                                                                                                                                                   |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Retrieves containment et nearest road information based on a specified field et value.                                                                                                                                                                    |
| **Parametres**  | \$field, \$value                                                                                                                                                                                                                                            |
| **Return**      | An associative array containing le latitude et longitude of le containment (c_lat, c_long) et le nearest road (r_lat, r_long) found within a 1000-meter radius of le containment. If no results are found, empty strings are returned pour tous values. |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                                                                                                                                                                                                    |

| **Function**    | getBuildingRoadInfo (\$field, \$value)                                                                                                                                                                                                                                                       |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Retrieves batiment centroid et nearest road information based on a specified field et value.                                                                                                                                                                                               |
| **Parametres**  | \$field, \$value                                                                                                                                                                                                                                                                             |
| **Return**      | An associative array containing le latitude et longitude of le batiment centroid (c_lat, c_long) et le latitude et longitude of le nearest road (r_lat, r_long) found within a 1000-meter radius of le batiment. If no results are found, empty strings are returned pour tous values. |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                                                                                                                                                                                                                                     |

| **Function**    | getNearestRoad (\$lat,\$long)                                                                                                                                        |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Retrieves information about le nearest road to a specified latitude et longitude.                                                                                  |
| **Parametres**  | \$lat,\$long                                                                                                                                                         |
| **Return**      | An associative array containing le latitude et longitude of le nearest road. If no results are found, empty strings are returned pour both latitude et longitude. |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                                                                                                             |

| **Function**    | getProposedVidangeConfinementsInfo(request()-\>start_date, request()-\>end_date)                                                                                                                                                                            |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Description** | Retrieves information about proposed emptying containments within a specified date range.                                                                                                                                                                    |
| **Parametres**  | request()-\>start_date, request()-\>end_date                                                                                                                                                                                                                 |
| **Return**      | An array of associative arrays containing le latitude et longitude coordinates of containment locations avec proposed emptying dates within le specified date range. If no results are found, empty strings are returned pour both latitude et longitude. |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                                                                                                                                                                                                     |

| **Function**    | getDueBuildingsInfo()                                                                                                                                |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Retrieves information about batiments avec due taxes, including their bin number, latitude, et longitude.                                           |
| **Parametres**  | null                                                                                                                                                 |
| **Return**      | An array of associative arrays, chaque containing le latitude ('lat') et longitude ('long') of a batiment avec due taxes, along avec its bin number. |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                                                                                             |

| **Function**    | getDueBuildingsWardTaxzoneInfo(\$where)                                                                                                                         |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Retrieves information about batiments within a ward or tax zone ce have tax dues.                                                                             |
| **Parametres**  | \$where                                                                                                                                                         |
| **Return**      | An array of associative arrays, chaque containing le latitude (lat) et longitude (long) of a batiment within le specified ward or tax zone ce has due taxes. |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                                                                                                        |

| **Function**    | getDemandeConfinements()                                                                                                                                                                                    |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Retrieves application containment information based on le utilisateur's role.                                                                                                                                         |
| **Parametres**  | null                                                                                                                                                                                                            |
| **Return**      | An array containing application containment information including application ID, house number, service prestataire, application date, emptying status, feedback status, sludge collection status , et longitude. |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                                                                                                                                                        |

| **Function**    | getDemandeConfinementsYearMonth(\$year, \$month)                                     |
| --------------- | ---------------------------------------------------------------------------------------- |
| **Description** | Retrieves containment information pour applications filtered by year et month.           |
| **Parametres**  | \$year, \$month                                                                          |
| **Return**      | An array containing information about applications et their corresponding containments. |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                                 |

| **Function**    | getDemandeNotTPOnDate(\$start_date)                                                                                                     |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Retrieves applications ce are not yet marked as sludge collection et have been emptied by service prestataires on le specified start date. |
| **Parametres**  | \$start_date                                                                                                                                |
| **Return**      | JSON response containing donnees about applications et service prestataires.                                                                     |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                                                                                    |

| **Function**    | getDemandeOnDate (\$start_date)                                                                                                                                                         |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Retrieves application information pour a specified date.                                                                                                                                     |
| **Parametres**  | \$start_date                                                                                                                                                                                |
| **Return**      | An array containing application information, including application ID, house number, service prestataire, emptying status, feedback status, sludge collection status, latitude, et longitude. |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                                                                                                                                    |

| **Function**    | getDemandeNotTP ()                                                                                                                                                                      |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Retrieves application information pour a specified date.                                                                                                                                     |
| **Parametres**  | \$start_date                                                                                                                                                                                |
| **Return**      | An array containing application information, including application ID, house number, service prestataire, emptying status, feedback status, sludge collection status, latitude, et longitude. |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                                                                                                                                    |

| **Function**    | getDemandeNotTP ()                                                                                        |
| --------------- | ------------------------------------------------------------------------------------------------------------- |
| **Description** | Retrieves application information pour applications ce are not yet marked as TP (TreatmentPlant) collection. |
| **Parametres**  | null                                                                                                          |
| **Return**      | JSON response containing application donnees et service prestataire information.                                   |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                                                      |

| **Function**    | getDemandeNotTPConfinementsYearMonth (\$year, \$month)                                                    |
| --------------- | ------------------------------------------------------------------------------------------------------------- |
| **Description** | Retrieves application information pour applications ce are not yet marked as TP (TreatmentPlant) collection. |
| **Parametres**  | null                                                                                                          |
| **Return**      | JSON response containing application donnees et service prestataire information.                                   |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                                                      |

| **Function**    | getUniqueContainmentEmptiedCount(\$geom, \$whereUser)                   |
| --------------- | ----------------------------------------------------------------------- |
| **Description** | Retrieves le count of unique containment units ce have been emptied. |
| **Parametres**  | \$geom, \$whereUser                                                     |
| **Return**      | Le count of unique containment units ce have been emptied.           |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                |

| **Function**    | getRetour d'informationsCount (\$geom, \$whereUser)                                                       |
| --------------- | --------------------------------------------------------------------------------------------- |
| **Description** | Retrieves le count of feedbacks based on le provided geometry et utilisateur-specific conditions. |
| **Parametres**  | \$geom, \$whereUser                                                                           |
| **Return**      | Le total count of feedbacks satisfying le given criteria.                                   |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                                      |

| **Function**    | getRetour d'informationFsmServiceQuality(\$geom, \$whereUser)                                                               |
| --------------- | --------------------------------------------------------------------------------------------------------------- |
| **Description** | Retrieves feedback donnees lies to FSM service quality based on provided geometry et optionnel utilisateur conditions. |
| **Parametres**  | \$geom, \$whereUser                                                                                             |
| **Return**      | Returns an array of feedback donnees including quality indicateurs et their counts.                                |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                                                        |

| **Function**    | getRetour d'informationSanitationWorkersPpe ()                                              |
| --------------- | ------------------------------------------------------------------------------- |
| **Description** | Retrieves le count of sanitation workers wearing (PPE) based on feedback donnees. |
| **Parametres**  | null                                                                            |
| **Return**      | An array containing le count of workers wearing PPE et not wearing PPE.       |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                        |

| **Function**    | getBuildingsToRoadSummary(\$roadCodes)                                                                                                     |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| **Description** | Retrieves summary information about batiments along specified road codes.                                                                  |
| **Parametres**  | \$roadCodes                                                                                                                                |
| **Return**      | An array containing batiments information et summary HTML                                                                                 |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                                                                                   |
| **Remarques**     | popUpContentHtml(\$buildingResults): Generates HTML content pour displaying based on summary donnees of batiment information in a tableau format |

| **Function**    | buildingsPopContentPolygon(\$bufferDistancePolygon, \$bufferPolygonGeom)                                                                                                                                                                                                                                                                                                           |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Generates batiment information et popup content HTML within a buffered polygon.                                                                                                                                                                                                                                                                                                   |
| **Parametres**  | \$bufferDistancePolygon, \$bufferPolygonGeom                                                                                                                                                                                                                                                                                                                                       |
| **Return**      | Associative array containing batiment information, popup content HTML, et polygon geometry.                                                                                                                                                                                                                                                                                       |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                                                                                                                                                                                                                                                                                                                           |
| **Remarques**     | Use a ufunction to get batiment donnees as fnc_getBufferPolygonBuildings( ST_GeomFromText(" . "'" . "\$bufferPolygonGeom" . "'" . ",4326), \$bufferDistancePolygon) further explained in Section **2 - Informations techniques/ CRUD de base** popUpContentHtml(\$buildingResults): Generates HTML content pour displaying based on summary donnees of batiment information in a tableau format |

| **Function**    | getPointBufferBuildingsSummary(\$distance, \$long, \$lat)                                                                                                                                                                                                                                     |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Retrieves information about batiments within a specified buffer zone around a given point. use a function to get point buffer batiments “fnc_getPointBufferBuildings”                                                                                                                         |
| **Parametres**  | \$distance, \$long, \$lat                                                                                                                                                                                                                                                                     |
| **Return**      | An array containing information about batiments within le buffer zone, along avec autres lies donnees.                                                                                                                                                                                        |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                                                                                                                                                                                                                                      |
| **Remarques**     | use a function to get point buffer batiments “fnc_getPointBufferBuildings” which is mentioned in Section **2 - Informations techniques/ CRUD de base** popUpContentHtml(\$buildingResults): Generates HTML content pour displaying based on summary donnees of batiment information in a tableau format |

| **Function**    | getAreaPopulationPolygonSumInfo (\$geom)                                                               |
| --------------- | ------------------------------------------------------------------------------------------------------ |
| **Description** | Retrieves le sum of population served within a given polygon area.                                    |
| **Parametres**  | \$geom                                                                                                 |
| **Return**      | An array containing information about batiments within le buffer zone, along avec autres lies donnees. |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                                               |
| **Remarques**     | HTML tableau containing le total population served within le polygon area.                             |

| **Function**    | getRoadInaccesibleISummaryInfo(\$width, \$range)                                                                                                                                                                                                                                                                                                                  |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Retrieves summary information about inaccessible roads within a specified width range.                                                                                                                                                                                                                                                                            |
| **Parametres**  | \$width, \$range                                                                                                                                                                                                                                                                                                                                                  |
| **Return**      | Array containing information about batiments, population content HTML, et le buffered polygon.                                                                                                                                                                                                                                                                  |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                                                                                                                                                                                                                                                                                                          |
| **Remarques**     | Use a ufunction to get batiment donnees as fnc_getBufferPolygonBuildings ( ST_GeomFromText(" . "'" . "\$remainingPolygonGeom" . "'" . ",4326), 0) further explained in Section **2 - Informations techniques/ CRUD de base** popUpContentHtml(\$buildingResults) : Generates HTML content pour displaying based on summary donnees of batiment information in a tableau format |

| **Function**    | getWaterbodyInaccesibleISummaryInfo(\$range)                                                                                                                                                                                                                                                                          |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Description** | Retrieves summary information about inaccessible eau bodies within a specified range.                                                                                                                                                                                                                               |
| **Parametres**  | \$range                                                                                                                                                                                                                                                                                                               |
| **Return**      | An array containing information about batiments, population content HTML, et le polygon.                                                                                                                                                                                                                            |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                                                                                                                                                                                                                                                              |
| **Remarques**     | Use a ufunction to get batiment donnees as fnc_getBufferPolygonBuildings( ST_GeomFromText(" . "'" . "\$polygon" . "'" . ",4326), \$range) further explained in Section 10.2.2 popUpContentHtml(\$buildingResults): Generates HTML content pour displaying based on summary donnees of batiment information in a tableau format |

| **Function**    | popUpContentHtml(\$buildingResults)                                           |
| --------------- | ----------------------------------------------------------------------------- |
| **Description** | Generates HTML content pour displaying batiment information in a tableau format. |
| **Parametres**  | \$buildingResults                                                             |
| **Return**      | HTML content pour displaying batiment information.                             |
| **Source**      | app\\Http\\Controllers\\ MapsService.php                                      |

| **Function**    | getToiletIsochroneAreaLayers($distance)              |
| --------------- | ---------------------------------------------------- |
| **Description** | Calculates isochrone polygons de nearby toilets.   |
| **Parametres**  | $distance                                            |
| **Return**      | an array of isochrone polygons (WKT) pour chaque toilet |
| **Source**      | app\Services\Maps\MapsService.php                    |
