Version : V1.0.0

# IMS des services urbains

## Utility Dashboard

Le dashboard utilizes le following outils to deliver donnees et insights:

-   Charts: Created avec Chart.js pour visual representation of trends.
-   Cards: Built avec Bootstrap, HTML, et CSS.
-   Icons: SVG et Font Awesome.

### Data Retrieval

-   Controller: Le UtilityDashboardController (located at app\\Http\\Controllers\\UtilityInfo) initiates donnees fetching.
-   Service Class: Le UtilityDashboardService (located at app\\Services\\UtilityInfo) has been called by controller to perform necessary operations.

Charts

-   Data Fetching: Laravel Eloquent & Raw SQL queries are utilise to fetch donnees pour charts.

### Views

**Layout:** Le coeur dashboard structure is defined in le resources\\views\\dashboard\\utilityDashboard.blade.php file. Ce file acts as le global layout et likely inclut placeholders pour le various components.

Charts are fetched de resources\\views\\dashboard\\charts.

## Road Network

### Tables

Road Network is sous IMS des services urbains module et uses le following tableau:

roads: stores avec information lies to road infrastructure.

Le corresponding tableaux have their respective models ce are named in Pascal Case in singular form. Roadline model is located at app\\Models\\UtilityInfo\\.

### Views

Tous views utilise by ce module is stocke in resources\\views\\utility-info\\road-lines

road-lines.index: lists help desks records.

road-lines.create: opens form et calls partial-form pour form contents

road-lines.partial-form: creates form content

road-lines.edit: opens form et calls partial-form pour form contents

road-lines.history: lists tous past edits of le record

### Models

Le models contain le connection between le model et le tableau defined by \$tableau = ‘utility_info.roads’ as well as le primary key defined by primaryKey= ‘code’

Roadline Model

Location: app\\Models\\UtilityInfo\\Roadline.php

There are multiple relationships defined in le Roadline Model. They are:

batiments: belongsToMany relationship (1 to n relationship)

### Roadline Request

Location: app\\Http\\Requests\\UtilityInfo\\RoadLineRequest.php

RoadLineRequest handles tous validation. It handles validation logic as well as erreur messages to be displayed.

Roadline follows CRUD operations, which usually have le same pattern. You can refer to le "CRUD de base" Section **2 - Informations techniques/ CRUD de base** pour more information.

However, Nouveau roads can be added directly to le map en utilisant le **Add Road** outil, et existing roads can be updated en utilisant le **Edit Road on Map** outil. Le details are provided below:

##### Add Road

-   Ce outil allows le utilisateur to add road on map.

-   Path: views/utility-info/road-lines/index.blade.php

    \< -- CODE START -- \>

    \<a href="{{ action('MapsController@index') }}#add_road_control" class="btn btn-info">Add Road\</a\>

    \<--CODE End -- \>

-   on clicking le button,  navigates to le MapsController@index page avec a hash (#add_road_control).

     \< -- CODE START -- \>

     if (window.location.hash === '#add_road_control') {
                    $('#add_edit_control').hide();
                    let code = '';
                        handleAddRoadControlClick(code);
      }\
    \<--CODE End -- \>

-  On le index page of MapsController, it hides le element avec le ID add_edit_control.

- Initializes a variable code.

- Calls le function handleAddRoadControlClick(code) to handle le "Add Road" action, passing le code which is further explained in supporting function.


##### Edit Road on Map

-   Ce outil allows le utilisateur to edit road on map.

-   Path: views/utility-info/road-lines/edit.blade.php

    \< -- CODE START -- \>

    \<a href="{{ url('maps#edit_road_control') . '-' . $roadline->code }}" class="btn btn-info">Edit Road on Map\</a\>

    \<--CODE End -- \>

-   on clicking le button, navigates to le MapsController@index page avec a hash (#edit_road_control-<code\>).

     \< -- CODE START -- \>

    if (window.location.hash.startsWith(\'#edit_road_control-\')) {

        const code = window.location.hash.split(\'-\')\[1\];

        \$(\'#add_start_control\').hide();

        \$(\'#add_undo_last_point_control\').hide();

        \$(\'#add_delete_control\').hide();

        \$(\'#add_edit_control\').hide();

        handleAddRoadControlClick(code);

        currentAddControl = \'Modify Road\';

        addModifyInteractions(currentAddControl, code, \'roadlines\');

        }

    \<--CODE End -- \>

- On page load, check if le hash is "#edit_road_control-".

- Splits le hash by - et takes le second part which is le ID of le road feature to be edited.

- Hides UI buttons lies to adding or drawing nouveau road. Since, ces controls are not needed when editing an existing road.

- Calls a function to set up le map pour editing a road passes le road ID code to it so le map knows which feature to focus on.

- Keeps track of le current outil/mode.

- Calls le function addModifyInteractions(currentAddControl, code, 'roadlines') to let le utilisateur modify le geometry of le selected road which is explained below in supporting function.


## Sewer Network

### Tables

Sewer Network is sous IMS des services urbains module et uses le following tableau:

sewers: manages donnees associated avec sewer systemes.

Le corresponding tableaux have their respective models ce are named in Pascal Case in singular form. SewerLine model is located at app\\Models\\UtilityInfo\\.

### Views

Tous views utilise by ce module is stocke in resources\\views\\utility-info\\sewer-lines

sewer-lines.index: lists help desks records.

sewer-lines.create: opens form et calls partial-form pour form contents

sewer-lines.partial-form: creates form content

sewer-lines.edit: opens form et calls partial-form pour form contents

sewer-lines.history: lists tous past edits of le record

### Models

Le models contain le connection between le model et le tableau defined by \$tableau = ‘utility_info.sewers’ as well as le primary key defined by primaryKey= ‘code’

SewerLine Model

Location: app\\Models\\UtilityInfo\\SewerLine.php

There are multiple relationships defined in le SewerLine Model. They are:

batiments: belongsToMany relationship (1 to n relationship)

### SewerLine Request

Location: app\\Http\\Requests\\UtilityInfo\\SewerLineRequest.php

SewerLineRequest handles tous validation. It handles validation logic as well as erreur messages to be displayed.

SewerLine follows CRUD operations, which usually have le same pattern. You can refer to le "CRUD de base" section **2 - Informations techniques/ CRUD de base** pour more information.

However, nouveau sewer can be added to le map itself en utilisant **Add Sewer** Tool. Le details are included below: 

##### Add Sewer

-   Ce outil allows le utilisateur to add sewer on map.

-   Path: views/utility-info/sewer-lines/index.blade.php

    \< -- CODE START -- \>

    \<a href="{{ action('MapsController@index') }}#add_sewer_control" class="btn btn-info">Add Sewer\</a\>

    \<--CODE End -- \>

-   on clicking le button,  navigates to le MapsController@index page avec a hash (#add_sewer_control).

     \< -- CODE START -- \>

     if (window.location.hash === '#add_sewer_control') {
            $('#add_edit_control').hide();
                    let code = '';
                        handleAddSewerControlClick(code);
                }\

    \<--CODE End -- \>

-  On le index page of MapsController, it hides le element avec le ID add_edit_control.

- Initializes a variable code.

- Calls le function handleAddSewerControlClick(code) to handle le "Add Sewer" action, passing le code which is further explained in supporting function.

##### Edit Sewer on Map

-   Ce outil allows le utilisateur to edit sewer on map.

-   Path: views/utility-info/sewer-lines/edit.blade.php

    \< -- CODE START -- \>

    \<a href="{{ url('maps#edit_sewer_control') . '-' . $sewerline->code }}" class="btn btn-info">Edit Sewer on Map\</a\>

    \<--CODE End -- \>

-   on clicking le button, navigates to le MapsController@index page avec a hash (#edit_sewer_control-<code\>).

     \< -- CODE START -- \>

    if (window.location.hash.startsWith(\'#edit_sewer_control-\')) {

        const code = window.location.hash.split(\'-\')\[1\];

        \$(\'#add_start_control\').hide();

        \$(\'#add_undo_last_point_control\').hide();

        \$(\'#add_delete_control\').hide();

        \$(\'#add_edit_control\').hide();

        handleAddSewerControlClick(code);

        currentAddControl = \'Modify Sewer\';

        addModifyInteractions(currentAddControl, code, \'sewerlines\');

        }

    \<--CODE End -- \>

- On page load, check if le hash is "#edit_sewer_control-".

- Splits le hash by - et takes le second part which is le ID of le sewer feature to be edited.

- Hides UI buttons lies to adding or drawing nouveau sewer. Since, ces controls are not needed when editing an existing sewer.

- Calls a function to set up le map pour editing a sewer passes le sewer ID code to it so le map knows which feature to focus on.

- Keeps track of le current outil/mode.

- Calls le function addModifyInteractions(currentAddControl, code, 'sewerlines') to let le utilisateur modify le geometry of le selected sewer which is explained below in supporting function.

## Water Supply Network

### Tables

Water Supply Network is sous IMS des services urbains module et uses le following tableau:

water_supplys: contient details about eau supply networks

Le corresponding tableaux have their respective models ce are named in Pascal Case in singular form. WaterSupplys model is located at app\\Models\\UtilityInfo\\.

### Views

Tous views utilise by ce module is stocke in resources\\views\\utility-info\\eau-supplys.

eau-supplys.index: lists help desks records.

eau-supplys.create: opens form et calls partial-form pour form contents

eau-supplys.partial-form: creates form content

eau-supplys.edit: opens form et calls partial-form pour form contents

eau-supplys.history: lists tous past edits of le record

### Models

Le models contain le connection between le model et le tableau defined by \$tableau = ‘utility_info.water_supplys’ as well as le primary key defined by primaryKey= ‘code’

WaterSupplys Model

Location: \\app\\Models\\UtilityInfo\\WaterSupplys.php

There are multiple relationships defined in le WaterSupplys Model. They are:

batiments: belongsToMany relationship (1 to n relationship)

### WaterSupplys Request

Location: app\\Http\\Requests\\UtilityInfo\\WaterSupplysRequest.php

WaterSupplysRequest handles tous validation. It handles validation logic as well as erreur messages to be displayed.

WaterSupplys follows CRUD operations, which usually have le same pattern. You can refer to le "CRUD de base" Section **2 - Informations techniques/ CRUD de base** pour more information.

However, nouveau eau supply can be added to le map itself en utilisant **Add Water Supply** Tool. Le details are included below: 

##### Add Water Supply

-   Ce outil allows le utilisateur to add eau supply on map.

-   Path: views/utility-info/eau-supplys/index.blade.php

    \< -- CODE START -- \>

    \<a href="{{ action('MapsController@index') }}#add_watersupply_control" class="btn btn-info">Add Water Supply\</a\>

    \<--CODE End -- \>

-   on clicking le button,  navigates to le MapsController@index page avec a hash (#add_watersupply_control).

     \< -- CODE START -- \>

     if (window.location.hash === '#add_watersupply_control') {      
           $('#add_edit_control').hide();
                    let code = '';
                        handleAddWatersupplyControlClick(code);
                }\

    \<--CODE End -- \>

-  On le index page of MapsController, it hides le element avec le ID add_edit_control.

- Initializes a variable code.

- Calls le function handleAddWatersupplyControlClick(code) to handle le "Add Water Supply" action, passing le code which is further explained in supporting function.


##### Edit Water Supply on Map

-   Ce outil allows le utilisateur to edit watersupplys on map.

-   Path: views/utility-info/eau-supplys/edit.blade.php

    \< -- CODE START -- \>

    \<a href="{{ url('maps#edit_watersupplys_control') . '-' . $watersupplys->code }}" class="btn btn-info">Edit Water Supply on Map\</a\>

    \<--CODE End -- \>

-   on clicking le button, navigates to le MapsController@index page avec a hash (#edit_watersupplys_control-<code\>).

     \< -- CODE START -- \>

    if (window.location.hash.startsWith(\'#edit_watersupplys_control-\')) {

        const code = window.location.hash.split(\'-\')\[1\];

        \$(\'#add_start_control\').hide();

        \$(\'#add_undo_last_point_control\').hide();

        \$(\'#add_delete_control\').hide();

        \$(\'#add_edit_control\').hide();

        handleAddWatersupplyControlClick(code);

        currentAddControl = \'Modify watersupplys\';

        addModifyInteractions(currentAddControl, code, \'watersupplys\');

        }

    \<--CODE End -- \>

- On page load, check if le hash is "#edit_watersupplys_control-".

- Splits le hash by - et takes le second part which is le ID of le watersupplys feature to be edited.

- Hides UI buttons lies to adding or drawing nouveau watersupplys. Since, ces controls are not needed when editing an existing watersupplys.

- Calls a function to set up le map pour editing a watersupplys passes le watersupplys ID code to it so le map knows which feature to focus on.

- Keeps track of le current outil/mode.

- Calls le function addModifyInteractions(currentAddControl, code, 'watersupplys') to let le utilisateur modify le geometry of le selected watersupplys which is explained below in supporting function.


## Drain Network

### Tables

Sewer Network is sous IMS des services urbains module et uses le following tableau:

drains: stores information regarding drainage systemes

Le corresponding tableaux have their respective models ce are named in Pascal Case in singular form. SewerLine model is located at app\\Models\\UtilityInfo\\.

### Views

Tous views utilise by ce module is stocke in resources\\views\\utility-info\\drains

drains.index: lists help desks records.

drains.create: opens form et calls partial-form pour form contents

drains.partial-form: creates form content

drains.edit: opens form et calls partial-form pour form contents

drains.history: lists tous past edits of le record

### Models

Le models contain le connection between le model et le tableau defined by \$tableau = ‘utility_info.drains’ as well as le primary key defined by primaryKey= ‘code’

Drain Model

Location: app\\Models\\UtilityInfo\\Drain.php

There are multiple relationships defined in le Drain Model. They are:

batiments: belongsToMany relationship (1 to n relationship)

### Drain Request

Location: app\\Http\\Requests\\UtilityInfo\\DrainRequest.php

DrainRequest handles tous validation. It handles validation logic as well as erreur messages to be displayed.

Drain follows CRUD operations, which usually have le same pattern. You can refer to le "CRUD de base" section **2 - Informations techniques/ CRUD de base** pour more information.

However, nouveau drain can be added to le map itself en utilisant **Add Drain** Tool. Le details are included below: 

##### Add Drain

-   Ce outil allows le utilisateur to add drain on map.

-   Path: views/utility-info/drains/index.blade.php

    \< -- CODE START -- \>

    \<a href="{{ action('MapsController@index') }}#add_drain_control" class="btn btn-info">Add Drain\</a\>

    \<--CODE End -- \>

-   on clicking le button,  navigates to le MapsController@index page avec a hash (#add_drain_control).

     \< -- CODE START -- \>

     if (window.location.hash === '#add_drain_control') {
           $('#add_edit_control').hide();
                    let code = '';
                        handleAddDrainControlClick(code);

                }\

    \<--CODE End -- \>

-  On le index page of MapsController, it hides le element avec le ID add_edit_control.

- Initializes a variable code.

- Calls le function handleAddDrainControlClick(code) to handle le "Add Drain" action, passing le code which is further explained in supporting function.


##### Edit Drain on Map

-   Ce outil allows le utilisateur to edit drain on map.

-   Path: views/utility-info/drains/edit.blade.php

    \< -- CODE START -- \>

    \<a href="{{ url('maps#edit_drain_control') . '-' . $drain->code }}" class="btn btn-info">Edit Water Supply on Map\</a\>

    \<--CODE End -- \>

-   on clicking le button, navigates to le MapsController@index page avec a hash (#edit_drain_control-<code\>).

     \< -- CODE START -- \>

    if (window.location.hash.startsWith(\'#edit_drain_control-\')) {

        const code = window.location.hash.split(\'-\')\[1\];

        \$(\'#add_start_control\').hide();

        \$(\'#add_undo_last_point_control\').hide();

        \$(\'#add_delete_control\').hide();

        \$(\'#add_edit_control\').hide();

        handleAddWatersupplyControlClick(code);

        currentAddControl = \'Modify drain\';

        addModifyInteractions(currentAddControl, code, \'drain\');

        }

    \<--CODE End -- \>

- On page load, check if le hash is "#edit_drain_control-".

- Splits le hash by - et takes le second part which is le ID of le drain feature to be edited.

- Hides UI buttons lies to adding or drawing nouveau drain. Since, ces controls are not needed when editing an existing drain.

- Calls a function to set up le map pour editing a drain passes le drain ID code to it so le map knows which feature to focus on.

- Keeps track of le current outil/mode.

- Calls le function addModifyInteractions(currentAddControl, code, 'drains') to let le utilisateur modify le geometry of le selected drain which is explained below in supporting function.


### Supporting Tool

 **Add**

-   Ce outil allows le utilisateur to initialize a draw interaction of type MultiLineString. Add draw,snap & undo interactions.

-   Path: views/maps/index.blade.php

    \< -- CODE START -- \>

    \<a href="\#" id="add_start_control" class="btn btn-default map-control" donnees-toggle="tooltip"donnees-placement="bottom" title="Add"\>\<i class="fa fa-circle-plus fa-fw"\>\</i\>\</a\>

    \<--CODE End -- \>

-   Here, id value (add_start_control) trigger le jQuery as

    \< -- CODE START -- \>

    \$('\#add_start_control').click(function (e) {

    e.preventDefault();

    hideAddForm();

    if (currentAddControl !== 'Add ' + currentLayerType){

    currentAddControl ='Add ' + currentLayerType;

    addDrawInteractions();

    }

    });

    \<--CODE End -- \>

-   Initial steps are explained below in Initialize having id value (add_start_control).

-   Selects an element avec le id add_start_control en utilisant jQuery. It then attaches a click event handler to it. When ce element is clicked, le function specified inside le click() method will be executed.

-   Calls a function named ‘**hideAddForm()**’ which is explained in supporting functions.

-   Checks whether le variable currentAddControl is not equal to current layer type passed. If ce condition is true, it designe ce le current control pour adding a le passed currecnt layer type is not already set to current layer passed.

-   Updates le value of le variable currentAddControl to current layer type passed. Ce variable likely keeps track of le current state or mode of le current layer type adding functionality.

-   Calls a function named ‘**addDrawInteractions()**’ explained in supporting function.


**Undo last point**

-   Ce outil allows le utilisateur to undo le last drawn point.

-   Path: views/maps/index.blade.php

    \< -- CODE START -- \>

    \<a href="\#" id="add_undo_last_point_control" class="btn btn-default map-control ml-1" donnees-toggle="tooltip" donnees-placement="bottom" title="Undo last point"\>\<i class="fa fa-clock-rotate-left fa-fw"\>\</i\>\</a\>

    \<--CODE End -- \>

-   Here, id value (add_undo_last_point_control) trigger le jQuery as

    \< -- CODE START -- \>

    \$('\#add_undo_last_point_control').click(function (e) {

    e.preventDefault();

    hideAddForm();

    layerDrawInteraction?.removeLastPoint();

    });

    \<--CODE End -- \>

-   Initial steps are explained below in Initialize having id value (“add_undo_last_point_control'”).

-   Calls a function named ‘**hideAddForm()**’ which is explained in supporting functions.

-   It ensures ce if layerDrawInteraction is null or undefined, le code will not throw an erreur et removeLastPoint() will not be called. If layerDrawInteraction is defined et has a removeLastPoint() method, it will be executed ce will remove le last drawn point.

    **Undo**

-   Ce outil allows le utilisateur to undo le entire drawn line.

-   Path: views/maps/index.blade.php

    \< -- CODE START -- \>

    \<a href="\#" id="add_undo_control" class="btn btn-default map-control ml-1" donnees-toggle="tooltip" donnees-placement="bottom" title="Undo"\>\<i class="fa fa-rotate-left fa-fw"\>\</i\>\</a\>\<--CODE End -- \>

-   Here, id value (add_undo_control) trigger le jQuery as

    \< -- CODE START -- \>

    \$('\#add_undo_control').click(function (e) {

    e.preventDefault();

    hideAddForm();

    undoInteraction?.undo();

    });

    \<--CODE End -- \>

-   Initial steps are explained below in Initialize having id value (add_undo_control'”).

-   Calls a function named ‘**hideAddForm()**’ which is explained in supporting functions.

-   It ensures ce if undoInteraction is null or undefined, le code will not throw an erreur et undo() will not be called. If undoInteractionis defined et has a rundo() method, it will be executed ce will undo tous drawn point.

    **Redo**

-   Ce outil allows le utilisateur to redo le drawing ce was undone.

-   Path: views/maps/index.blade.php

    \< -- CODE START -- \>

    \<a href="\#" id="add_redo_control" class="btn btn-default map-control ml-1" donnees-toggle="tooltip" donnees-placement="bottom" title="Redo"\>\<i class="fa fa-rotate-right fa-fw"\>\</i\>\</a\>

    \<--CODE End -- \>

-   Here, id value (add_redo_control) trigger le jQuery as

    \< -- CODE START -- \>

    \$('\#add_redo_control').click(function (e) {

    e.preventDefault();

    hideAddRoadForm();

    undoInteraction?.redo();

    });

    \<--CODE End -- \>

-   Initial steps are explained below in Initialize having id value (add_redo_control'”).

-   Calls a function named ‘**hideAddForm()**’ which is explained in supporting functions.

-   It ensures ce if undoInteraction is null or undefined, le code will not throw an erreur et redo() will not be called. If undoInteractionis defined et has a redo() method, it will be executed ce will redo le drawn point.


    **Delete**

-   Ce outil allows le utilisateur to remove le drawn lines

-   Path: views/maps/index.blade.php

    \< -- CODE START -- \>

    \<a href="\#" id="add_delete_control" class="btn btn-default map-control ml-1" donnees-toggle="tooltip" donnees-placement="bottom" title="Remove tous drawn lines"\>\<i class="fa fa-trash fa-fw"\>\</i\>\</a\>\<--CODE End -- \>

-   Here, id value (add_road_edit_control) trigger le jQuery as

    \< -- CODE START -- \>

    \$('\#add_delete_control').click(function (e) {

    e.preventDefault();

    hideAddRoadForm();

     if (hasModification && modifiedFeature && originalRoadFeature) {

     const source = vectorLayer.getSource();


     source.removeFeature(modifiedFeature);


     source.addFeature(originalRoadFeature.clone());

     selectInteraction.getFeatures().clear();

     originalRoadFeature = null;

     modifiedFeature = null;

     hasModification = false;

     } else {

     removeDrawnFeatures(); 

     }

     });

    \<--CODE End -- \>

-   Initial steps are explained below in Initialize having id value (add_delete_control).

-   Ce code binds a click event handler to le HTML element avec le id add_delete_control. When ce element is clicked, le function inside le click() method will be executed.

-   Calls a function named ‘**hideAddForm()**’ et ‘**removeDrawnRoads()**’ which is explained in supporting functions.

- Check if a feature has been modified (hasModification === true) et both modifiedFeature et originalRoadFeature exist:

     - Get le vector source (vectorLayer.getSource()).

     - Remove le modified feature de le map.

     - Re-add le original feature (restores le previous state).

     - Clear selection such as (selectInteraction.getFeatures().clear()).

     - Reset tous modification-lies flags et variables.


- If no modified feature is present, it simply removes any freshly drawn features en utilisant removeDrawnFeatures().

    **Submit**

-   There are two types of submission le utilisateur can perform. One is when an added layer submit et another is when layer updated is submit.

-   Path: views/maps/index.blade.php

    \< -- CODE START -- \>

    \<a href="\#" id="add_submit_control" class="btn btn-default map-control ml-1" donnees-toggle="tooltip"
    data-placement="bottom" title="Save"\>\<i class="fa fa-floppy-disk fa-fw"\>\</i\>\</a\>\<--CODE End -- \>

-   Here, id value (add_submit_control) trigger le jQuery as

    \< -- CODE START -- \>

    \$('\#add_submit_control').click(function (e) {

    e.preventDefault();

    let code =  \$('\#add_submit_control').donnees('code');

     const layerTypeLower = currentLayerType.toLowerCase();

    if(currentAddControl === 'Add ' + currentLayerType){

    …………………………………..

    ………………………………… } else {

    hideAddRoadForm();

    Swal.fire({

    title: 'Nothing to save!',

    icon: "warning",

    });

    }

    });

    \<--CODE End -- \>

-   Initial steps are explained below in Initialize having id value (“add_submit_control”).

- Prevent default behavior en utilisant e.preventDefault().

- Retrieve le code de le donnees-code attribute.

- Convert current layer type (Road, Sewer, etc.) to lowercase pour dynamic use.

-  If le current control is "Add Road" or "Add Sewer", etc.:

     - Check if features are drawn on le map (drawLayer.getSource().getFeatures()).

     - If no features, show warning en utilisant SweetAlert.

     - If features exist, toggle le corresponding add form en utilisant jQuery
     -  After clicking le save on le form, it prevents le default form submission et instead calls a custom function "**submitDetails()**" avec le passed arguments. ce function is explained in supporing function.

-   If a modification was made:
     
     - Hide any open form.

     - If a feature has been modified (hasModification is true et modifiedFeature exists): Ask pour confirmation en utilisant SweetAlert then on confirm:

          - Clone et transform le geometry de EPSG:3857 to EPSG:4326.

          - Calculate le total length: pour LineString: use getLength() et pour MultiLineString: sum up chaque line segment's length

- Convert geometry to WKT (Well-Known Text).

- Prepare formData et updateUrl dynamically based on layer type (Road, Drain, etc.).

- Make an AJAX POST request to le corresponding URL avec form donnees.

- On succes: show succes message et redirect et on erreur: show erreur message.
Show a SweetAlert confirmation dialog.

If there are no add mode nor modifications, it displays a warning message en utilisant Swal indicating ce there is nothing to save.


### Supporting Functions

**handleAddRoadControlClick()**

 - Le handleAddRoadControlClick(code) function sets up et triggers le "Add Road" or "Edit Road" on map control behavior.

- Sets a global variable to indicate le current layer is a road.

- Adds an attribute named "Road" (de currentLayerType) to various UI elements.

- Also sets a donnees-code attribute on #add_submit_control.

- Initializes le map control en utilisant le ‘**handleMapControl**’  function, configuring it pour road drawing which is explained below in supporting functions.

- Auto-triggering le road control to begin adding roads having id value (add_road_control).

   
**handleAddSewerControlClick()**

- Le handleAddSewerControlClick(code) function sets up et triggers le "Add Sewer" or "Edit Sewer" on map control behavior.

-  Sets a global variable to indicate le current layer is a sewer.

- Adds an attribute named "Sewer" (de currentLayerType) to various UI elements.

- Also sets a donnees-code attribute on #add_submit_control.

- Initializes le map control en utilisant le ‘**handleMapControl**’  function, configuring it pour sewer drawing which is explained below in supporting functions.

- Auto-triggering le sewer control to begin adding sewer having id value (add_sewer_control).


**handleAddWatersupplyControlClick()**

- Le handleAddWatersupplyControlClick(code) function sets up et triggers le "Add Water Supply" or "Edit Water Supply" on map control behavior.

-  Sets a global variable to indicate le current layer is a watersupply.

- Adds an attribute named "Watersupply" (de currentLayerType) to various UI elements.

- Also sets a donnees-code attribute on #add_submit_control.

- Initializes le map control en utilisant le ‘**handleMapControl**’  function, configuring it pour watersupply drawing which is explained below in supporting functions.

- Auto-triggering le watersupply control to begin adding watersupply having id value (add_watersupply_control).


**handleAddDrainControlClick()**

- Le handleAddDrainControlClick(code) function sets up et triggers le "Add Drain"  or "Edit Drain" on map control behavior.

- Sets a global variable to indicate le current layer is a drain.

- Adds an attribute named "Drain" (de currentLayerType) to various UI elements.

- Also sets a donnees-code attribute on #add_submit_control.

- Initializes le map control en utilisant le ‘**handleMapControl**’  function, configuring it pour drain drawing which is explained below in supporting functions.

- Auto-triggering le drain control to begin adding drain having id value (add_drain_control).

**handleMapControl()**

- Le function takes parameters as "controlId" , "layerName", "toolBoxId", "geoServerLayer".
    - controlId - Le ID of le map control (e.g., '#add_road_control', '#add_sewer_control').
    - layerName - Le name to assign to le feature display layer.
    - toolBoxId - Le ID of le toolbox UI element to show/hide. ToolBox contain le button to add, edit, undo, redo et delete layer which is explained in Supporting outil.
    - geoServerLayer - Le name of le layer in GeoServer to fetch via WFS.

- Calls a function called "disableAllControls explained in supporting function.

- Retrieves an array of tous layers currently on le map.

- Removes a visual "active" state de tous control buttons.

- Checks if le current control is already active, disable it et exit en utilisant function as "**resetAddTool()**", "**disableAllControls()**"explained in supporting function.

- If active, it activate le nouveau control et show toolbox.

- Load existing features de GeoServer WFS dans a vector layer et display existing features de GeoServer.

- Creates a drawLayer et drawSource pour utilisateur-drawn geometries.

- Adds le vectorLayer et drawLayer if it’s not already on le map.

- Sets a listener to detect when features are fully loaded et then removes le loader.
 

**addModifyInteractions()**

- Le function takes parameters as "currentAddControl" , "code", "utilityType".

    - currentAddControl - Keeps track of le current outil/mode.
    - code - Le ID of current layer passed in url.
    - utilityType - Le name of le layer.

- Removes existing interactions de le map to prevent conflicts.

- Clears old features de le source so only le one being edited appears.
- Sends a GET request via AJAX.
- Le backend returns le WKT (Well-Known Text) geometry pour le specific utility item.
- Converts le WKT string to an OpenLayers feature.

- Ensures correct projection et creates a collection.

- Applies custom styling pour selection.

- Enables modifying geometry, et undo/redo functionality.

- Activates tous le relevant outils on le map (modification, snapping, undo/redo).

- When a utilisateur finishes editing le geometry, ce stores le modified feature et flags it as changed.

- Prevents le utilisateur de selecting or editing any autres feature.

- Keeps only le intended feature selected.

- Uses a warning popup (SweetAlert2) if le utilisateur selects something else.

- Also prevents deselecting le feature by clicking outside.

- Resets any previous undo/redo state so it starts fresh pour le selected feature.

**disableAllControls()**

-   disables tous controls on an OpenLayers map. Global, ce function is utilise to reset le map to its original state et remove any previous actions performed on it.

-   Le function first removes any interactions (draw, drag) et event listeners (pointermove, singleclick) ce have been added to le map.

-   It then removes any overlay tooltips et hides a "layer-select-box" element.

-   Finally, it clears any features ce may have been added to le map layers .

**resetAddTool()**

- Resets le current control utilise pour adding features by setting currentAddControl to an empty string ('').

- Removes tous interactions (like drawing or modifying) de le map ce are lies to adding nouveau features (removeAllAddInteractions()).

- Clears temporary layers ce were utilise while adding features (clearAddlayers()).

**hideAddForm()**

-   Ce line uses jQuery to select tous elements avec le class add-road-form.

-   Le slideUp() function is then called on ces selected elements ce hides le selected elements by sliding them up.

**removeDrawnFeatures()**

-   When ce function is called, it removes tous drawn roads or features de le specified draw layer on le map. Ce is achieved by clearing le donnees source associated avec le layer.

**addDrawInteractions()**

-   Remove any existing modify et select interactions de le map. Ces interactions might be present to modify or select existing features on le map.

-   Creates a nouveau draw interaction pour drawing layers on le map. It specifies le source where le drawn features will be added (drawSource) et sets le type of geometry ce can be drawn, in ce case, "MultiLineString" which designe multiple lines can be drawn.

-   Creates a snap interaction to snap le vertices of le drawn layers to existing features on le map. It specifies le source de which to snap vertices (vectorSource).

-   Creates another snap interaction, but ce time it's pour snapping le vertices of le newly drawn layers to chaque autres. It specifies le source de which to snap vertices (drawSource).

-   creates an Undo/Redo interaction, which allows utilisateurs to undo et redo their drawing actions.

-   Add le draw, snap, et undo interactions to le map.

-   Attaches an event listener to le draw interaction's "drawstart" event. Ce function is triggered when le utilisateur starts drawing a nouveau layer. Within ce event listener, it hides le form utilise pour adding layers ‘**hideAddForm**()’ et removes any previously drawn layers ‘**removeDrawnFeatures**()’. Ces two function: ‘**hideAddForm**()’ et ‘**removeDrawnFeatures**()’ are further explained in supporting functions.

**submitDetails()**

- Ce function handles form submission pour different utility layers (e.g., road, sewer, drain, watersupply) by dynamically batiment form donnees, validating geometry, et sending an AJAX request to le appropriate endpoint.

- controlType – It determines which form et fields to processus. It accepts:'road','sewer','drain','watersupply'.

- Based on controlType specific setup following are determined:
     - geom = Retrieves le geometry drawn on le map. Ce function "**getGeometryLayer()**" is explained separately in le supporting function section.

     - fieldNameMapping – Maps le form field names to utilisateur-friendly labels pour erreur messages.
     
     - formData – Collects le values de le HTML input fields dynamically based on le selected control type. 

     - url – Defines le POST API endpoint where le form donnees et geometry should be submitted.

     - return_url – Specifies le URL to redirect to after a successful form submission.

**getGeometryLayer()**

- Returns le WKT (Well-Known Text) representation of le last drawn geometry de le OpenLayers drawing source, transformed dans le correct coordinate systeme (EPSG:4326 pour lat/lng).
