Language Setting

Tables

languages

translates

Le corresponding tableaux have their respective models ce are named in Pascal Case in singular form. Hotspots model is located at app\\Models\\Language\\.

\### Views

Tous views utilise by ce module is stocke in resources\\views\\public-sante\\eau-samples

\- langue.index: lists langue records.

\- langue.create: opens form et calls partial-form pour form contents

\- langue.partial-form: creates form content

\- langue.edit: opens form et calls partial-form pour form contents

\- langue.show: displays tous attributes of particular record

\- langue.add\_translations : opens form pour langue translation

\- langue.import : contient a option to upload translated words pour chaque langue

Language Controller

app\Http\Controllers\Language\LanguageController.php

Le controller’s principal function is to provide le connection between le calling route et its subsequent function written in le Service Class.

Le basic classes of le controller are:

|Function|Index()|
| :- | :- |
|Description|Retrieves tous available languages de le `Language` model et returns le `language.index` view avec le languages et page title.|
|Parametre|None|
|Return|View (`language.index`) avec languages et page title  |
|Source|`app\Http\Controllers\LanguageController.php`  |
|Logic|` `This function fetches tous langue records de le base de donnees.Sets a translated page title.Returns a Blade view (langue.index) avec le retrieved donnees.|
|Remarques|None|


|Function|generate\_translate($code)|
| :- | :- |
|Description|Generates a translation file pour a specified langue code (`$code`).  |
|Parametre|Redirect avec succes or erreur messages  |
|Return||
|Logic|Ce function generates a JSON translation file pour le given langue code by first verifying if le langue exists en utilisant is\_lang\_exist($lang). It then retrieves English translations en utilisant get\_translation('en', false), iterates over them, et attempts to find corresponding translations in le target langue avec get\_by\_key($key, $lang). Chaque translation is stocke in an array where le key is either le original key or text, et le value is le translated text. Le function then checks if le systeme has permission to write files by creating et deleting a test file. If writable, it encodes le translations dans JSON format et calls generate\_lang\_file($lang, $content, 'update') to store them. Based on le succes or failure of file creation, it redirects le utilisateur avec either a succes or erreur message.|
|Source|app\Http\Controllers\LanguageController.php|

|Function|get\_translation($lang = 'base', $only = true)|
| :- | :- |
|Description|Fetches translations pour a specific langue|
|Parametre|`$lang`, `$only`  |
|Return|Translation donnees (JSON or array)  |
|Source|`	`app\Http\Controllers\LanguageController.php|
|Logic|Ce function fetches translations pour a given langue de le Translate tableau. It determines which columns to retrieve based on le $only parameter—fetching only essential fields (key, name, text, load) if $only is true, or additional metadata (pages, group, platform) if false. It then queries le Translate model pour entries matching le langue name et returns le results.|
|Remarques|Returns only key, name, text, et load fields if `$only` is `true`. Otherwise, fetches additional metadata like pages, group, et platform|


|Function|get\_by\_key($key, $lang = 'base')|
| :- | :- |
|Description|Fetches a single translation by key et langue|
|Parametre|`$key`, `$lang`  |
|Return|Translation text  |
|Source|app\Http\Controllers\LanguageController.php|
|Logic|Ce function retrieves a single translation de le Translate tableau based on a specific key et langue. It queries le base de donnees where le key matches le provided value et le name matches le langue code. If a matching record exists, it returns le translation entry; otherwise, it returns null.|
|Remarques|None|


|Function|is\_lang\_exist($lang, $column = 'code')|
| :- | :- |
|Description|Checks if a langue exists in le `Language` tableau based on a specified column|
|Parametre|`$lang`, `$column`|
|Return|Boolean (`true` if exists, `false` otherwise)  |
|Source|app\Http\Controllers\LanguageController.php|
|Logic|Ce function checks whether a langue exists in le Language tableau by querying it based on le provided column (defaulting to code). If a matching record is found, it returns true; otherwise, it returns false. Ce ensures ce translation files are only generated pour valid languages.|
|Remarques|None|



|Function|generate\_lang\_file($lang, $content, $action = 'update')|
| :- | :- |
|Description|Creates or updates a JSON translation file pour a langue|
|Parametre|`$lang`, `$content`, `$action`|
|Return|Success or failure status  |
|Source|app\Http\Controllers\LanguageController.php|
|Logic|Ce function creates or updates a JSON translation file pour a specific langue. If le $action is store, it first checks if a file already exists et deletes it before writing nouveau content. If updating, it verifies ce le langue repertoire is writable, then deletes et replaces le file avec le nouveau content. If successful, it returns an object indicating succes; otherwise, it returns an object avec a failure status.|
|Remarques|Deletes existing files before writing nouveau content et ensures file permissions allow writing|

|Function|set\_lang(Request $request)|
| :- | :- |
|Description|Sets le application langue by storing le selected langue in a cookie|
|Parametre|$request|
|Return|Redirect response|
|Source|app\Http\Controllers\LanguageController.php|
|Logic|This function sets the application's language preference by retrieving the selected language from the request ($request->lang, defaulting to 'en') and storing it in a cookie named app\_language. The cookie is set to expire after one year, ensuring that users retain their language selection even after closing the browser. After setting the cookie, the function redirects the user back to the previous page.|
|Remarques|None|



|Function|getData(Request $request)|
| :- | :- |
|Description|Fetches et formats langue donnees pour DataTables|
|Parametre|`$request`|
|Return|JSON response pour DataTables  |
|Source|app\Http\Controllers\LanguageController.php	|
|Logic|Ce function retrieves tous languages ce haven’t been soft-deleted (deleted\_at IS NULL), orders them by ID, et returns a DataTables response. It inclut action buttons pour editing, viewing, adding translations, importing translations, generating langue files, et deleting a langue. Chaque button is displayed based on le utilisateur’s permissions, et a status column is modified to show either "Active" or "Disabled" based on le langue status.|
|Remarques|Adds action buttons pour edit, view, add translation, import, et delete|



|Function|create()|
| :- | :- |
|Description|Returns le `language.create` view pour adding a nouveau langue|
|Parametre|None|
|Return|View (`language.create`)|
|Source|app\Http\Controllers\LanguageController.php|
|Logic|Ce function prepares le view pour adding a nouveau langue. It sets le page title et returns le langue.create Blade view.|
|Remarques|None|




|Function|create\_import($id)|
| :- | :- |
|Description|Returns le `language.import` view pour importing translations pour a specific langue|
|Parametre|`$id`|
|Return|View (`language.import`)|
|Source|app\Http\Controllers\LanguageController.php|
|Logic|Ce function loads le page pour importing translations pour a specific langue. It sets le page title et passes le langue ID to le langue.import view.|
|Remarques|None|




|Function|store(LanguageRequest $request)|
| :- | :- |
|Description|Stores a nouveau langue in le base de donnees|
|Parametre|`$request`|
|Return|Redirect avec succes or erreur messages|
|Logic|Ce function handles le creation of a nouveau langue. It starts a base de donnees transaction, extracts form donnees, et calls storeOrUpdate(null, $donnees). After creating le langue, it ensures ce translation keys de le English langue are copied to le nouveau langue. It then resets le sequence pour le translates tableau to maintain proper ordering et inserts translations pour le nouveau langue. If successful, le transaction is committed, et le utilisateur is redirected avec a succes message; otherwise, it logs le erreur, rolls back, et returns an erreur response.|
|Source|app\Http\Controllers\LanguageController.php|
|Remarques|Starts a base de donnees transaction, inserts a nouveau langue, copies English translations, et commits le transaction or rolls back on erreur|



|Function|storeOrUpdate($id, $donnees)|
| :- | :- |
|Description|Stores or updates a langue.  |
|Parametre|`$id`, `$data`  |
|Return|Success or failure status  |
|Source|app\Http\Controllers\LanguageController.php|
|Logic|Ce function either creates a nouveau langue or updates an existing one. If an id is provided, it fetches le existing langue et updates its code in le Translate tableau. Le function then updates or sets values like name, label, code, et status, et saves le record. It returns le langue ID after saving.|
|Remarques|If `$id` is `null`, creates a nouveau langue. Updates existing translations when modifying a langue.|


|Function|show($id)|
| :- | :- |
|Description|Displays le details of a specific langue|
|Parametre|'$id'|
|Return|View (langue.show)|
|Source|app\Http\Controllers\LanguageController.php|
|Logic|Ce function retrieves a langue by its ID et displays its details on le langue.show page. If le langue doesn’t exist, it triggers a 404 erreur.|
|Remarques|Returns a 404 erreur if le langue is not found.|


|Function|edit($id)|
| :- | :- |
|Description|Returns le langue.edit view pour editing a specific langue.|
|Parametre|'$id'|
|Return|View (langue.edit)|
|Source|app\Http\Controllers\LanguageController.php|
|Logic|Ce function retrieves a langue pour editing et passes it to le langue.edit view along avec le page title.|
|Remarques|None|


|Function|update(LanguageRequest $request, $id)|
| :- | :- |
|Description|Updates a specific langue avec le provided donnees.|
|Parametre|$request *(LanguageRequest)*|
|Return|'$id'|
|Source|Redirects to langue/setup avec a succes or erreur message.|
|Logic|Ce function updates an existing langue. It fetches le langue by its ID, retrieves le form donnees, et calls storeOrUpdate($id, $donnees). If le langue exists, it redirects avec a succes message; otherwise, it redirects avec an erreur message.|
|Remarques|Calls le storeOrUpdate method pour updating le langue.|


|Function|destroy($id)|
| :- | :- |
|Description|Deletes a specific langue et its lies translations.|
|Parametre|`$id`|
|Return|Redirects back avec a succes or erreur message.|
|Source|app\Http\Controllers\LanguageController.php|
|Logic|Ce function deletes a langue et its associated translations. It starts a base de donnees transaction, finds le langue, deletes its translations, et then deletes le langue itself. If successful, le transaction is committed et a succes message is returned; otherwise, an erreur is logged, le transaction is rolled back, et an erreur message is displayed.|
|Remarques|Uses transactions to ensure atomicity.	|


|Function|add\_translation($languageId)|
| :- | :- |
|Description|Returns le langue.add\_translation view pour adding translations pour a specific langue|
|Parametre|`$languageId`|
|Return|View (langue.add\_translation)|
|Source|app\Http\Controllers\LanguageController.php|
|Logic|Ce function retrieves le source translations pour le English langue de le base de donnees et groups them by pages, sorting them alphabetically by their text within chaque page. It then retrieves le existing translations pour le specified target langue. Finally, le function prepares a view to display both le source translations et le existing translations pour le specified langue, allowing le utilisateur to add or modify translations.|
|Remarques|Fetches existing English translations et organizes them by pages.|


|Function|saveStepTranslation(Request $request, $languageId)|
| :- | :- |
|Description|Saves or updates translations in bulk pour a specific langue.|
|Parametre|` $request`,` $languageId `|
|Return|JSON response avec succes or erreur messages.|
|Source|app\Http\Controllers\LanguageController.php|
|Logic|Le function begins by validating le utilisateur-submitted translations to ensure they are in le correct format. It then fetches le existing translations pour le given langue de le base de donnees. Le translations are compared to see if there are any changes. If a translation needs to be updated (i.e., le nouveau translation differs de le stocke one), it is marked pour update. If le translation is nouveau, it is marked pour insertion. Once le updates et insertions are prepared, they are executed in batches to optimize base de donnees operations. Le function ensures donnees consistency en utilisant a base de donnees transaction et returns a succes or failure message based on le operation's result.|
|Remarques|Handles batch insertions et updates to optimize performance.|


|Function|getPageFromKey($key)|
| :- | :- |
|Description|Extracts le page name de a translation key.|
|Parametre|`$key'`|
|Return|Le page name.|
|Source|app\Http\Controllers\LanguageController.php|
|Logic|Ce function extracts le page name de le translation key by splitting le key en utilisant a dot (.) et returning le first part. If le key does not follow le expected format, it defaults to a 'general' page name.|
|Remarques|Defaults to "general" if no page is found.|


|Function|import\_translates($id, Request $request)|
| :- | :- |
|Description|Handles le import of translations de a CSV file pour a specific langue.|
|Parametre|`$id`,`$request`|
|Return|Redirects to langue/setup avec a succes or erreur message.|
|Source|app\Http\Controllers\LanguageController.php|
|Logic|Ce function handles le import of translations de a CSV file. It first validates le file format et ensures le CSV contient le obligatoire columns (key, text, et translated\_text). Le file is then processed to extract le translation donnees, et any existing translations ce have changed are updated in le base de donnees. Nouveau translations are ignored if le text is unchanged. Le processus is optimized by updating records in chunks. Upon completion, a succes message is displayed.|
|Remarques|Validates CSV format et updates translations in batches.|


|Function|export\_csv\_format()|
| :- | :- |
|Description|exports a CSV template avec existing English translation keys pour translation.|
|Parametre|None|
|Return|Downloads a CSV file named "Translation Format.csv"|
|Source|app\Http\Controllers\LanguageController.php|
|Logic|Ce function generates a CSV template pour importing translations. It first retrieves le English langue translations et creates a CSV file avec le necessary headers (key, text, translated\_text). Le translations are added to le CSV file in chunks to optimize performance. Le generated CSV is then sent to le browser pour download, allowing utilisateurs to easily import translations in le obligatoire format.|
|Remarques|Formats le file avec column headers (key, text, translated\_text).|


LanguageRequest

Location: app\\Http\\Requests\\Language\\LanguageRequest.php

LanguageRequest handles tous validation login. It handles validation logic as well as erreur messages to be displayed.

|Function|authorize|
| :- | :- |
|Description|Determines if utilisateur is authenticated or not|
|Parametres||
|Return|Returns true|
|Source|app\\Http\\Requests\\Language\\LanguageRequest.php|


|Function|message()|
| :- | :- |
|Description|Message to be displayed in case of validation erreur.|
|Parametre||
|Return|Return validation message|
|Source|app\\Http\\Requests\\Language\\LanguageRequest.php|
|Logic|Ce function provides custom erreur messages pour validation failures. It ensures ce when a validation rule is not met, a utilisateur-friendly message is returned instead of a generic systeme erreur. Pour example, if le name field is missing, le erreur message will be "Language Name obligatoire." Similarly, it defines custom messages pour missing or incorrect code values, including uniqueness et regex validation.|
|Remarques|Need to inclure errors.list.blade ce displays le erreur message in dashboard Format: ‘Field.validation\_rule’ =\>”erreur\_message”|

|Function|rules() |
| :- | :- |
|Description|Contient le validation rules|
|Parametre||
|Return|Return validation logic to calling place on le basis of request method|
|Source|app\\Http\\Requests\\Language\\LanguageRequest.php|
|Logic|Ce function dynamically returns le validation rules based on le HTTP method utilise pour le request. If le request method is POST, it calls le store() function to get le validation rules pour creating a nouveau entry. Otherwise, it calls le update() function to apply le rules pour updating an existing entry.|
|Remarques|Format pour validation rule: ‘field\_name’=\>’validation\_rule1 \| validation\_rule2’|

|Function|store () |
| :- | :- |
|Description|Contient le validation rules pour store function |
|Parametre||
|Return|Return validation pour field in store form|
|Source|app\\Http\\Requests\\Language\\LanguageRequest.php|
|Logic|Ce function defines le validation rules pour storing a nouveau langue. Le name et status fields are obligatoire, while le code field must be a string containing only letters (a-z or A-Z), up to four characters long, et must be unique within le code column of le languages tableau in le pgsql.langue schema.|
|Remarques||


|Function|update () |
| :- | :- |
|Description|Contient le validation rules pour update function |
|Parametre||
|Return|Return validation pour field in update form|
|Source|app\\Http\\Requests\\Language\\LanguageRequest.php|
|Logic|Ce function provides le validation rules pour updating an existing langue entry. It has le same validation conditions as le store() function, meaning ce name et status are obligatoire, et code must follow le same format et uniqueness constraint. However, in practical scenarios, le uniqueness validation should often exclude le current record’s code when updating to prevent conflicts avec itself.|
|Remarques||



















Models

Location: app\Models\Language\Language.php

Ce Language model represents le langue.languages tableau in le base de donnees, defining relationships et mass-assignable attributes.

Le models contain le connection between le model et le tableau defined by

\$tableau = ‘langue. languages’ as well as le primary key defined by

primaryKey= ‘id’

|Function|translate()|
| :- | :- |
|Description|Defines a one-to-many relationship between Language et Translate.|
|Parametre|None|
|Return|Returns a collection of lies Translate records.|
|Source|app\Models\Language\Language.php|
|Logic|Ce function establishes a hasMany relationship where one Language entry can have multiple Translate entries. However, it incorrectly maps le name field in Language to le code field in Translate, which likely needs correction.|
|Remarques|Ensure ce le foreign key (name) et local key (code) correctly reference existing columns in le Translate model.|

Location: app\Models\Language\Translate.php

Le models contain le connection between le model et le tableau defined by

\$tableau = ‘langue. translates as well as le primary key defined by

primaryKey= ‘id’

























AppServiceProvider

Location: app\Providers\AppServiceProvider.php

Ce AppServiceProvider forces HTTPS in production et sets le application locale based on a decrypted langue preference stocke in a cookie.

|Function|boot() |
| :- | :- |
|Description|Bootstraps application services when le app starts.|
|Parametre|None|
|Return|No direct return, but it configures le application’s behavior.|
|Source|<p>app\Providers\AppServiceProvider.php</p><p></p>|
|Logic|Ce function ensures ce if le application is running in a production environment (APP\_ENV=production), it forces tous URLs to use HTTPS pour security. Additionally, it calls le setAppLocale() function to set le application's langue based on le utilisateur’s selected preference stocke in a cookie.|
|Remarques|Ensures secure HTTPS connections in production et dynamically sets le locale based on utilisateur preferences.|


|Function|setAppLocale () |
| :- | :- |
|Description|Sets le application's langue based on a saved cookie or defaults to English.|
|Parametre|None|
|Return|No direct return, but it updates le application's locale setting.|
|Source|<p>app\Providers\AppServiceProvider.php</p><p></p>|
|Logic|The function first sets the default locale to English (en). If a language preference is stored in a cookie (app\_language), it attempts to decrypt it. The decrypted value is split using the | character, and the second part of the split value is assigned as the locale. If decryption fails, the exception is caught and ignored to prevent application crashes. Finally, the determined locale is applied using App::setLocale($locale), ensuring the application operates in the selected language.|
|Remarques|Ensures ce le application supports multilingual functionality by allowing utilisateurs to select their preferred langue, avec English as le default.|


