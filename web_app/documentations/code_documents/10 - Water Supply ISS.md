Version : V1.0.0

#  ISS d'approvisionnement en eau

Le Water Supply Information Support System sub-module maintains information on Water Supply Bill Payment Status donnees.

## Workflow

Water supply service payment donnees is imported dans watersupply_payments tableau via CSV file. Le file is stocke in le server in storage disk path as defined in config\\filesystems.php pour 'importwatersupply'.

Consecutively, triggers are run which creates materialized view avec few steps of operations including create status tableau, et updates proportion column in tableaux ‘wards’ et ‘grids’.

Le tableau watersupply_payment_status is created avec calculated due_years based on last_payment_date (default value:99) et Match value based on le presence of bin in le systeme. Pour batiments avec match customer_name, customer_contact are updated.

## Files

-   Command files: Command files WaterSupplyDataImport.php et WaterSupplyFunctionBuild.php inclut le commands or queries ce are supposed to run when le php command is run et located at app/Console/Commands.
-   Config file: Config file named ‘watersupply-info.php’ inside le ‘Config’ repertoire inclut tous le Sql functions et queries in array form which are called to create commands.
-   Import class file: WaterSupplyImport file inside imports repertoire inclut model, rules, map etc. functions et class is called inside store() function of controller class WaterSupplyController.

    Location: app/Imports/WaterSupplyImport.php

## Commands

Pour le initial launching, run le following command:

| *php artisan buildfunction:watersupply* |
|-----------------------------------------|

Le above code creates/builds functions et triggers in le base de donnees.

To test if le import command is working or not. Use Command:

| *php artisan import:watersupply* |
|----------------------------------|
