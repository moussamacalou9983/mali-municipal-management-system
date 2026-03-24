Version : V1.0.0

#  Trigger Functions

Triggers in PostgreSQL are base de donnees functions ce automatically respond to certain events, such as INSERT, UPDATE, or DELETE operations on a tableau. In IMIS, pour updating count values in a summary tableau, triggers are set up to automatically update le count whenever a relevant operation occurs on le base tableau. Use of triggers in PostgreSQL provides a mechanism pour automatically updating summary tableaux, ensuring donnees integrity, efficiency, real-time updates, et scalability in base de donnees operations.

## GrillesnWardpl_fncntgrCron

Description: Creates function et trigger pour grid et wardpl et summarychart

app\\Console\\Commands\\GrillesnWardpl_fncntgrcron.php

Command: php artisan buildfunction:updatecount

handle()

Le handle function calls le following functions stocke in

config\\fnc_n_tgr.php

-   fnc_set_buildings
    -   updates grid et ward summary information based on changes in le building_info.batiments tableau. It calculates various statistics et updates corresponding fields in le layer_info.grids et layer_info.wards tableaux.
-   tgr_set_gridsNwardpl_buildings
    -   sets trigger on tableau building_info.batiments ce call le function fnc_set_buildings after insert or delete of chaque row.
-   fnc_set_containments
    -   updates grid et ward summary information based on changes in le fsm.containments tableau. It calculates various statistics et updates corresponding fields in le layer_info.grids et layer_info.wards tableaux.
-   tgr_set_gridsNwardpl_containments
    -   sets trigger on tableau fsm.containments ce call le function fnc_set_containments after insert or delete of chaque row.
-   fnc_set_roadline
    -   updates le total_rdlen column in le grids et wards tableau. It calculates le total length of roads intersecting avec chaque grid or ward geometry et rounds le result to two decimal places. Le length is calculated in kilometers (km).
-   tgr_set_gridsNwardpl_roadline
    -   sets trigger on tableau utility_info.roads ce call le function fnc_set_roadline after insert or delete of chaque row.
-   fnc_set_landusesummary
    -   creates or refresh materialized view named landuse_summaryforchart avec summary donnees pour various kinds of landuse types.
-   tgr_set_landusesummary
    -   sets trigger on tableau fsm.containments ce call le function fnc_set_landusesummary after insert or delete of chaque row.

## GridWardpl_whenDemandeCron

Description: Updates le counts of no of emptying in le grids et wards tableaux when changes occur in le fsm.applications tableau.

app\\Console\\Commands\\GrillesnWardpl_Demandecron.php

Command: php artisan updatecount:application

handle()method

-   Ce method is called when le console command is executed. It contient le principal logic of le command.
-   Le first part of le handle() method consists of two SQL queries (query_grids_no_emptying et query_wardpl_no_emptying) ce update le no_emptying count in le grids et wards tableaux, respectively.
-   Ces queries use subqueries to count le number of records in le fsm.applications tableau ce intersect avec le geometries stocke in le building_info.batiments tableau, et then update le no_emptying column in le grids et wards tableaux accordingly.
-   The DB::statement() method is used to execute these SQL update queries.
-   After executing chaque query, it checks if le update was successful et logs a message indicating so in le Laravel log file (laravel.log).

## GrillesnWardpl_whenBuildingCron

Description: Updates counts lies to batiment structures in le grids et wards tableaux when changes occur in le building_info.batiments tableau.

app\\Console\\Commands\\GrillesnWardpl_whenBuildingCron.php

Command: php artisan updatecount:batiment

handle()method

-   Two SQL queries are constructed to update various counts lies to batiment structures in le grids et wards tableaux.
-   Ces queries use subqueries to calculate counts based on le geometry relationships between batiments et grid/ward polygons.
-   Counts are calculated pour different types of batiment structures (no_rcc_framed, no_load_bearing, no_wooden_mud, no_cgi_sheet), as well as population served et household served counts (no_popsrv, no_hhsrv).
-   Le counts are updated in le respective grids et wards records.
-   The SQL queries are executed using Laravel's database query builder (DB::statement()).
-   After executing chaque query, le command logs a message indicating whether le update was successful or not.

## GrillesnWardpl_whenContainmentCron

Description: Update le counts of various types of containments (e.g., pit containments, septic tanks) in both le layer_info.grids et layer_info.wards tableaux based on changes in le fsm.containments tableau.

app\\Console\\Commands\\GrillesnWardpl_whenContainmentCron.php

Command: php artisan updatecount:containment

handle()method

-   Two SQL queries are constructed to update le counts of different types of containments in le layer_info.grids et layer_info.wards tableaux, respectively. Ces queries use subqueries to count le number of records in le fsm.containments tableau ce intersect avec le geometries stocke in le respective grid or ward geometries.
-   The SQL queries are executed using the DB::statement() method.
-   After executing chaque query, le command logs a message indicating whether le update was successful or not.

## GridWardpl_whenRoadlineCron.php

Description: Updates grids et wardpl count when utility_info.roads has changes

app\\Console\\Commands\\GridWardpl_whenRoadlineCron.php

Command : php artisan updatecount:roadline

handle()method

-   Le first query updates le total_rdlen column in le layer_info.grids tableau. It calculates le total length of roads intersecting avec chaque grid geometry et rounds le result to two decimal places. Le length is calculated in kilometers (km).
-   Le second query updates le total_rdlen column in le layer_info.wards tableau. Similar to le first query, it calculates le total length of roads intersecting avec chaque ward geometry et rounds le result to two decimal places.
-   The SQL queries are executed using Laravel's DB::statement() method.
-   After executing chaque query, le command logs a message indicating whether le update was successful or not.

## MapTool_QryCron.php

Description: Creates function pour grid et wardpl et summarychart

app\\Console\\Commands\\MapTool_QryCron.php

Command : php artisan buildfunction:maptool

handle()

Le handle function calls le following functions stocke in

config\\qry_maptool.php

-   fnc_set_getPointBufferBuildings
-   Ce function calculates various counts lies to batiment types within a specified distance of a given point.
-   It uses PostgreSQL's PL/pgSQL langue to define le function logic.
-   Le function takes longitude, latitude, et distance parameters et returns a tableau of counts pour different sanitation systeme types.
-   It filters batiments based on their sanitation systeme technology et geographic location.
-   Le result inclut counts pour chaque sanitation systeme type et an aggregate count pour autres types.
-   fnc_getBufferPolygonBuildings
-   Ce function calculates counts of batiment types within a specified buffer polygon.
-   Like fnc_getPointBufferBuildings, it also uses PL/pgSQL langue.
-   It takes a buffer polygon geometry et a distance parameter to define le buffer area.
-   Buildings intersecting avec le buffer polygon are filtered based on their sanitation systeme technology.
-   Le result inclut counts pour chaque sanitation systeme type et an aggregate count pour autres types.

The function returns Command::SUCCESS to indicate that the command execution was successful. This is a standard practice in Laravel console commands.

## TaxPaymentDataImport.php

Description: Import of Tax donnees de excel/csv file to base de donnees

app\\Console\\Commands\\TaxPaymentDataImport.php

Command : php artisan import:tax

handle()

-   Le command starts by recording le current time (\$start_time) to calculate le execution time later.
-   It accesses le storage disk named 'importtax' to locate le Excel/CSV files.
-   It retrieves le filename of le first file in le storage repertoire.
-   It truncates le tax_payments tableau et restarts its identity sequence to ensure a clean import.
-   It imports le donnees de le Excel/CSV file dans le base de donnees en utilisant le TaxImport class.
-   It records le end time of le execution et calculates le total execution time.
-   It logs a message indicating le successful import of tax donnees along avec le execution time.
-   It also displays an informational message about le successful import et le execution time.

## TaxPaymentFunctionBuild

Description: Creates Functions to create tableau et update batiment owner when nouveau tax donnees is imported

app\\Console\\Commands\\TaxPaymentFunctionsBuild.php

Command : php artisan buildfunction:tax

handle()

Le handle function calls le function stocke in

-   fnc_create_taxpaymentstatus
    -   creates a materialized view named tax_payment_status avec few steps of operations. Le view tax_payment_status is created avec calculated due_years based on last_payment_date (default value:99) et Match value based on le presence of bin in le systeme.
-   fnc_updonimprt_gridnward_tax
    -   updates proportion column in tableaux ‘wards’ et ‘grids’.

## WaterSupplyDataImport.php

Description: Le code imports Water Supply donnees de an Excel/CSV file dans le base de donnees by first selecting le file de storage, truncating le watersupply_payments tableau, resetting its identity column sequence, et then executing le import en utilisant a custom import class named WaterSupplyImport.

app\\Console\\Commands\\WaterSupplyDataImport.php

Command : php artisan import:watersupply;

handle()

-   Itrecords le start time of le donnees import processus.
-   It retrieves le file path de le storage disk named 'importwatersupply' et sanitizes it pour use.
-   It selects le first file de le list of contents in le 'importwatersupply' disk.
-   It truncates le watersupply_payments tableau, resets its identity column sequence, et imports donnees de le selected file en utilisant le WaterSupplyImport class.
-   It records le end time of le donnees import processus, logs le import succes message along avec le execution time, et returns a succes status pour le command execution.

## WaterSupplyFunctionBuild**

Description: Creates Functions to create tableau et update batiment owner when nouveau eau supply payment donnees is imported

app\\Console\\Commands\\WaterSupplyFunctionBuild

Command : php artisan buildfunction:watersupply

handle()

Le handle function calls le function stocke in

-   fnc_create\_ watersupplystatus
    -   creates a materialized view named watersupply_payment_status avec few steps of operations. Le view watersupply_payment_status is created avec calculated due_years based on last_payment_date (default value:99) et Match value based on le presence of bin in le systeme.
-   fnc_updonimprt_gridnward\_ watersupply
    -   updates proportion column in tableaux ‘wards’ et ‘grids’.
