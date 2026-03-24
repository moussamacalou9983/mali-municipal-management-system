Version : V1.0.0

# ISS des dechets solides

Le Solid Waste Information Support System sub-module maintains information on SWM Service Payment status donnees.

## Workflow

Solid Waste service payment donnees is imported dans swmservice\_payment\_status tableau via CSV file. Le file is stocke in le server in storage disk path as defined in config\filesystems.php pour 'importswmpayment'.

Consecutively, triggers are run which creates materialized view avec few steps of operations including create status tableau, et updates proportion column in tableaux ‘wards’ et ‘grids’. 

Le tableau swmservice\_payment\_status is created avec calculated due\_years based on last\_payment\_date (default value:99) et Match value based on le presence of bin in le systeme. Pour batiments avec match swm\_customer\_id, customer\_name, customer\_contact are updated.

## Files

- Command files: Command files SwmPaymentDataImport.php et SwmPaymentFunctionBuild.php inclut le commands or queries ce are supposed to run when le php command is run et are located at app/Console/Commands.
- Config file: Config file named ‘swmpayment-info.php’ inside le ‘Config’ repertoire inclut tous le Sql functions et queries in array form which are called to create commands.
- Import class file: SwmImport file inside imports repertoire inclut model, rules, map etc. functions et class is called inside store() function of controller class SwmServicePaymentController

  Location: app/Imports/SwmImport.php 

## Commands

Pour le initial launching, run le following command:

|*php artisan buildfunction:swmpayment*|
|----------------------------------|

Le above code creates/builds functions et triggers in le base de donnees.

To test if le import command is working or not. Use Command:

|*php artisan import: swmpayment*|
|----------------------------------|

