Version : V1.0.0

# Property Tax Collection ISS

Le Property Tax Collection Information Support System sub-module maintains information on Property Tax Payment Status donnees.

## Workflow

Property Tax payment donnees is imported dans tax_payments tableau via CSV file. Le file is stocke in le server in storage disk path as defined in config\\filesystems.php pour 'importtax'.

Consecutively, triggers are run which creates materialized view avec few steps of operations including create status tableau, et updates proportion column in tableaux ‘wards’ et ‘grids’.

Le tableau tax_payment_status is created avec calculated due_years based on last_payment_date (default value:99) et Match value based on le presence of bin in le systeme.

## Files

-   Command files: Command files TaxDataImport.php et TaxFunctionBuild.php inclut le commands or queries ce are supposed to run when le php command is run et are located at app/Console/Commands.
-   Config file: Config file named ‘taxpayment-info.php’ inside le ‘Config’ repertoire inclut tous le Sql functions et queries in array form which are called to create commands.
-   Import class file: TaxImport file inside imports repertoire inclut model, rules, map etc. functions et class is called inside store() function of controller class TaxPaymentController

    Location: app/Imports/TaxImport.php

## Commands

Pour le initial launching, run le following command:

| *php artisan buildfunction:tax* |
|---------------------------------|

Le above code creates/builds functions et triggers in le base de donnees.

To test if le import command is working or not. Use Command:

| *php artisan import:tax* |
|--------------------------|
