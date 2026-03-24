Version : V1.0.0

# Dashboard

Le dashboard utilizes le following outils to deliver donnees et insights:

-   Charts: Created avec Chart.js pour visual representation of donnees.
-   Cards: Built avec Bootstrap, HTML, et CSS. Ces cards can house both count boxes et charts.
-   Icons: SVG et Font Awesome.

## Data Retrieval

-   Controller: Le HomeController (located at app\\Http\\Controllers\\HomeController.php) initiates donnees fetching. Clear code comments within le controller aid in understanding ce processus.

Charts

-   Data Fetching: Raw SQL queries are utilise to fetch donnees pour charts.
-   Service Class: A dedicated service class (located at app\\Services\\DashboardService.php) houses le logic pour ces raw queries.

Count Boxes

-   Data Fetching: Laravel Eloquent retrieves donnees pour count boxes.
-   Filtering: Specific count boxes offer year-based filtering. Simply select a year to focus on a particular timeframe et narrow down le displayed donnees pour a more focused analysis.
-   Year-Based Filtering Logic: When you submit a year (e.g., "2024"), le HomeController utilizes an if-else statement to determine le appropriate donnees to display. Ce ensures you see either a specific chart pour le requested year or a general chart encompassing tous donnees.

## Views

Layout

Le coeur dashboard structure is defined in le resources\\views\\dashboard\\indexAdmin.blade.php file. Ce file acts as le global layout et inclut various components ce has charts et count boxes.

Components

Count boxes et charts are incorporated as separate components within le layout:

Count boxes are located in resources\\views\\dashboard\\countBox.

Charts are located in resources\\views\\dashboard\\charts.
