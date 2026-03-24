#!/usr/bin/env python3
"""
Build French translation assets from the project's English translation CSV.

Outputs:
- web_app/resources/lang/fr.json
- mobile_app/src/i18n/fr.json
- deployment_documentation/sample_import_data/Language Translations - fr.csv
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE_CSV = (
    ROOT
    / "deployment_documentation"
    / "sample_import_data"
    / "Multilingual Translation Keys - en.csv"
)
WEB_JSON = ROOT / "web_app" / "resources" / "lang" / "fr.json"
MOBILE_JSON = ROOT / "mobile_app" / "src" / "i18n" / "fr.json"
FRENCH_CSV = (
    ROOT
    / "deployment_documentation"
    / "sample_import_data"
    / "Language Translations - fr.csv"
)


EXACT_TRANSLATIONS = {
    "Home": "Accueil",
    "Log out": "Se déconnecter",
    "Logging out": "Déconnexion en cours",
    "Loading": "Chargement",
    "Loading data..": "Chargement des données..",
    "Uploading": "Téléversement en cours",
    "Uploaded": "Téléversé",
    "Select Language": "Sélectionner la langue",
    "Remember me": "Se souvenir de moi",
    "Log In": "Se connecter",
    "Login failed": "Échec de connexion",
    "Email address is required": "L'adresse e-mail est obligatoire",
    "Password is required*": "Le mot de passe est obligatoire*",
    "Email Address": "Adresse e-mail",
    "Password": "Mot de passe",
    "e.g. email@address.com": "ex. : email@adresse.com",
    "Building Map": "Carte des bâtiments",
    "Building Map Information": "Informations cartographiques des bâtiments",
    "Buildings Data": "Données des bâtiments",
    "Containments Data": "Données des ouvrages de confinement",
    "Containment Map": "Carte des ouvrages de confinement",
    "Building location": "Localisation du bâtiment",
    "Containment location": "Localisation de l'ouvrage de confinement",
    "Applicant location": "Localisation du demandeur",
    "Containment Assessment": "Évaluation de l'ouvrage de confinement",
    "Application List": "Liste des demandes",
    "Land": "Parcelles",
    "Detail": "Détail",
    "Building survey form": "Formulaire d'enquête bâtimentaire",
    "Building Survey Form": "Formulaire d'enquête bâtimentaire",
    "Sewer Map": "Carte du réseau d'égout",
    "Sewer Data": "Données du réseau d'égout",
    "Confirm delete": "Confirmer la suppression",
    "Cancel": "Annuler",
    "Delete": "Supprimer",
    "Upload": "Téléverser",
    "View on map": "Voir sur la carte",
    "You have not added any containment data into this device": "Aucune donnée d'ouvrage de confinement n'a été ajoutée sur cet appareil",
    "Are you sure you want to delete this containment information?": "Voulez-vous vraiment supprimer ces informations sur l'ouvrage de confinement ?",
    "The containment code is already registered, deleting this list": "Le code de l'ouvrage de confinement est déjà enregistré, cette entrée va être supprimée",
    "Containment code": "Code de l'ouvrage de confinement",
    "Latitude": "Latitude",
    "Longitude": "Longitude",
    "Collected date": "Date de collecte",
    "Success": "Succès",
    "Error": "Erreur",
    "No house image": "Aucune image du bâtiment",
    "House image is required": "L'image du bâtiment est obligatoire",
    "Assessment has been submitted": "L'évaluation a été soumise",
    "File size error": "Erreur de taille de fichier",
    "The image size exceeds 5 MB, please select lower size image.": "La taille de l'image dépasse 5 Mo, veuillez choisir une image plus légère.",
    "The image size exceeds 5 MB, please try again": "La taille de l'image dépasse 5 Mo, veuillez réessayer.",
    "Please fill.": "Veuillez renseigner ce champ.",
    "Please fill": "Veuillez renseigner ce champ",
    "Road distance is required": "La distance à la route est obligatoire",
    "Road width is required": "La largeur de la route est obligatoire",
    "Assessed sludge is required": "Le volume de boues évalué est obligatoire",
    "Exceeds the maximum distance range": "La distance dépasse la valeur maximale autorisée",
    "Exceeds the maximum width range": "La largeur dépasse la valeur maximale autorisée",
    "Exceeds the maximum sludge value": "Le volume de boues dépasse la valeur maximale autorisée",
    "The field only accepts numerical values.": "Ce champ n'accepte que des valeurs numériques.",
    "Estimated cost is required": "Le coût estimé est obligatoire",
    "Required trips is required": "Le nombre de trajets requis est obligatoire",
    "Select a date": "Sélectionnez une date",
    "Select width": "Sélectionnez la largeur",
    "Select width and size": "Sélectionnez la largeur et la capacité",
    "Pit diameter is required": "Le diamètre de la fosse est obligatoire",
    "Pit depth is required": "La profondeur de la fosse est obligatoire",
    "Pit number is required": "Le nombre de fosses est obligatoire",
    "Customer name is required": "Le nom du client est obligatoire",
    "Customer gender is required": "Le sexe du client est obligatoire",
    "Distance From Road (m) *": "Distance à la route (m) *",
    "Road Width (m) *": "Largeur de la route (m) *",
    "Assessed Sludge (m3) *": "Boues évaluées (m3) *",
    "Estimated Cost *": "Coût estimé *",
    "No. of Trips *": "Nombre de trajets *",
    "Proposed Emptying Date *": "Date de vidange proposée *",
    "Vacutug accessible": "Accessible au vacutug",
    "Vacutug type": "Type de vacutug",
    "Tank Length (m)": "Longueur de la cuve (m)",
    "Tank Width (m)": "Largeur de la cuve (m)",
    "Tank Depth (m)": "Profondeur de la cuve (m)",
    "Pit Diameter (m)": "Diamètre de la fosse (m)",
    "Pit Depth (m)": "Profondeur de la fosse (m)",
    "Pit Number": "Nombre de fosses",
    "Customer Name *": "Nom du client *",
    "Customer Gender *": "Sexe du client *",
    "Comments": "Commentaires",
    "House Image": "Image du bâtiment",
    "Open Camera": "Ouvrir l'appareil photo",
    "Choose from gallery": "Choisir depuis la galerie",
    "Save": "Enregistrer",
    "Submit": "Soumettre",
    "Yes": "Oui",
    "No": "Non",
    "Unknown": "Inconnu",
    "Male": "Homme",
    "Female": "Femme",
    "Others": "Autres",
    "Date": "Date",
    "Start Time": "Heure de début",
    "End Time": "Heure de fin",
    "Receipt Number": "Numéro de reçu",
    "Total Cost": "Coût total",
    "Capacity": "Capacité",
    "License plate": "Plaque d'immatriculation",
    "Comments (If any)": "Commentaires (le cas échéant)",
    "File Size should not exceed 5MB": "La taille du fichier ne doit pas dépasser 5 Mo",
    "(Max 5MB)": "(Max. 5 Mo)",
    "Select A Driver": "Sélectionner un chauffeur",
    "Select Emptier 1": "Sélectionner l'opérateur de vidange 1",
    "Select Emptier 2": "Sélectionner l'opérateur de vidange 2",
    "Select A Disposal Place": "Sélectionner un lieu d'élimination",
    "The Service Receiver Name is required.": "Le nom du bénéficiaire du service est obligatoire.",
    "The Service Receiver Gender is required.": "Le sexe du bénéficiaire du service est obligatoire.",
    "The Service Receiver Contact Number is required.": "Le numéro de contact du bénéficiaire du service est obligatoire.",
    "The reason for emptying is required.": "Le motif de la vidange est obligatoire.",
    "Sludge Volume is required.": "Le volume de boues est obligatoire.",
    "The Desludging Vehicle Number Plate is required.": "La plaque d'immatriculation du véhicule de vidange est obligatoire.",
    "The Disposal Place is required.": "Le lieu d'élimination est obligatoire.",
    "The Driver Name is required.": "Le nom du chauffeur est obligatoire.",
    "The emptier1 name is required.": "Le nom de l'opérateur de vidange 1 est obligatoire.",
    "The Start Time is required.": "L'heure de début est obligatoire.",
    "The End Time is required.": "L'heure de fin est obligatoire.",
    "The number of trips is required.": "Le nombre de trajets est obligatoire.",
    "The Receipt Number is required.": "Le numéro de reçu est obligatoire.",
    "The Total Cost is required.": "Le coût total est obligatoire.",
    "The House Image must be an image file.": "L'image du bâtiment doit être un fichier image.",
    "The Receipt Image is required.": "L'image du reçu est obligatoire.",
    "Something is wrong, please try again or at a later time.": "Une erreur est survenue. Veuillez réessayer maintenant ou plus tard.",
    "Please log in again.": "Veuillez vous reconnecter.",
    "A language with this code already exists. Please choose a different code.": "Une langue avec ce code existe déjà. Veuillez choisir un autre code.",
    "Another language with this code exists (even if deleted). Please choose a different code.": "Une autre langue avec ce code existe déjà, même supprimée. Veuillez choisir un autre code.",
    "Language file generated successfully": "Le fichier de langue a été généré avec succès",
    "Failed to generate the language file.": "Échec de la génération du fichier de langue.",
    "Unable to generate language file. Please request system administrator to check file permission of your /lang folder.": "Impossible de générer le fichier de langue. Veuillez demander à l'administrateur système de vérifier les permissions du dossier /lang.",
    "Sorry! Unable find the language": "Impossible de trouver la langue demandée",
    "Import Translations": "Importer des traductions",
    "Generate Language": "Générer la langue",
    "Add/Edit Translations": "Ajouter / modifier des traductions",
    "Language": "Langue",
    "Languages": "Langues",
    "Detail": "Détail",
    "History": "Historique",
    "Map": "Carte",
    "Filter": "Filtrer",
    "Reset": "Réinitialiser",
    "Back to List": "Retour à la liste",
    "Show Filter": "Afficher le filtre",
    "Download CSV Template": "Télécharger le modèle CSV",
    "Import from CSV": "Importer depuis un CSV",
    "Export to CSV": "Exporter en CSV",
    "Export Unmatched Records": "Exporter les enregistrements non appariés",
    "Integrated Municipal Information System": "Système intégré d'information municipale",
    "Base IMIS © 2022-2025 by Innovative Solution Pvt. Ltd. (ISPL) & Global Water & Sanitation Center - Asian Institute of Technology (GWSC-AIT) is licensed under CC BY-NC-SA 4.0": "Base IMIS © 2022-2025 par Innovative Solution Pvt. Ltd. (ISPL) et le Global Water & Sanitation Center - Asian Institute of Technology (GWSC-AIT) est distribué sous licence CC BY-NC-SA 4.0",
}

PHRASE_REPLACEMENTS = [
    ("Public / Community Toilets", "toilettes publiques / communautaires"),
    ("Public / Community Toilet", "toilette publique / communautaire"),
    ("Integrated Municipal Information System", "Système intégré d'information municipale"),
    ("Water Supply Information Support System", "Système d'appui à l'information sur l'alimentation en eau"),
    ("Utility Information Management System", "Système de gestion des infrastructures"),
    ("Urban Management Decision Support System", "Système d'aide à la décision pour la gestion urbaine"),
    ("Public Health Information Support System", "Système d'appui à l'information en santé publique"),
    ("Property Tax Collection ISS", "ISS de collecte de la taxe foncière"),
    ("Property Tax Collection Support System", "Système d'appui à la collecte de la taxe foncière"),
    ("Sewer Connection Information Support System", "Système d'appui à l'information sur les branchements d'égout"),
    ("Fecal Sludge Information Management System", "Système de gestion de l'information sur les boues de vidange"),
    ("Community/Public Toilet Information Management System", "Système de gestion de l'information sur les toilettes communautaires / publiques"),
    ("Community Toilet", "toilette communautaire"),
    ("Public Toilet", "toilette publique"),
    ("Treatment Plant", "station de traitement"),
    ("Treatment Plants", "stations de traitement"),
    ("Service Provider", "prestataire de services"),
    ("Service Providers", "prestataires de services"),
    ("Sanitation Department", "service d'assainissement"),
    ("Public Health", "santé publique"),
    ("Water Supply", "alimentation en eau"),
    ("Solid Waste", "déchets solides"),
    ("Low Income Communities", "communautés à faible revenu"),
    ("Low Income", "faible revenu"),
    ("Emptying Service", "service de vidange"),
    ("Emptying Services", "services de vidange"),
    ("Emptying Information", "informations de vidange"),
    ("Sludge Collection", "collecte des boues"),
    ("Sludge Disposal", "élimination des boues"),
    ("Customer Satisfaction", "satisfaction des usagers"),
    ("Application Response Efficiency", "efficacité de réponse aux demandes"),
    ("Waterborne", "hydrique"),
    ("Containment Information", "informations sur l'ouvrage de confinement"),
    ("Containment Type", "type d'ouvrage de confinement"),
    ("Containment Types", "types d'ouvrages de confinement"),
    ("Containment", "ouvrage de confinement"),
    ("Containments", "ouvrages de confinement"),
    ("Building Survey", "enquête bâtimentaire"),
    ("Building Information", "informations sur le bâtiment"),
    ("Building", "bâtiment"),
    ("Buildings", "bâtiments"),
    ("Sewer Connection", "branchement d'égout"),
    ("Sewer Network", "réseau d'égout"),
    ("Sewer line", "conduite d'égout"),
    ("Sewer lines", "conduites d'égout"),
    ("Sewer", "égout"),
    ("Road Width", "largeur de la route"),
    ("Road Length", "longueur de la route"),
    ("Road Code", "code de la route"),
    ("Road Name", "nom de la route"),
    ("Road", "route"),
    ("Roads", "routes"),
    ("Drain", "drain"),
    ("Drains", "drains"),
    ("Driver", "chauffeur"),
    ("Drivers", "chauffeurs"),
    ("Desludging Vehicle", "véhicule de vidange"),
    ("Desludging Vehicles", "véhicules de vidange"),
    ("Receipt Image", "image du reçu"),
    ("House Image", "image du bâtiment"),
    ("House Number", "numéro du bâtiment"),
    ("Wardwise", "par quartier"),
    ("Ward", "quartier"),
    ("Wards", "quartiers"),
    ("Owner Information", "informations sur le propriétaire"),
    ("Owner Contact Number", "numéro de contact du propriétaire"),
    ("Owner NID", "NID du propriétaire"),
    ("Customer Name", "nom du client"),
    ("Customer ID", "ID client"),
    ("Customer", "client"),
    ("Contact Number", "numéro de contact"),
    ("Collected date", "date de collecte"),
    ("Surveyed Date", "date d'enquête"),
    ("Construction Date", "date de construction"),
    ("Date From", "date de début"),
    ("Date To", "date de fin"),
    ("Created", "créé"),
    ("Updated", "mis à jour"),
    ("Deleted", "supprimé"),
    ("Delete", "supprimer"),
    ("Upload", "téléverser"),
    ("Download", "télécharger"),
    ("Export", "exporter"),
    ("Import", "importer"),
    ("Select", "sélectionner"),
    ("Add", "ajouter"),
    ("Edit", "modifier"),
    ("View", "voir"),
    ("Details", "détails"),
    ("Detail", "détail"),
    ("History", "historique"),
    ("Settings", "paramètres"),
    ("Dashboard", "tableau de bord"),
    ("Help Desk", "assistance"),
    ("Permission", "permission"),
    ("Permissions", "permissions"),
    ("Role", "rôle"),
    ("Roles", "rôles"),
    ("Language", "langue"),
    ("Translations", "traductions"),
    ("Translation", "traduction"),
    ("Required", "obligatoire"),
    ("Invalid", "invalide"),
    ("Success", "succès"),
    ("Error", "erreur"),
    ("Failed", "échec"),
]

WORD_REPLACEMENTS = {
    "access": "accès",
    "active": "actif",
    "add": "ajouter",
    "address": "adresse",
    "admin": "administrateur",
    "after": "après",
    "all": "tous",
    "already": "déjà",
    "amount": "montant",
    "analysis": "analyse",
    "and": "et",
    "application": "demande",
    "applications": "demandes",
    "approve": "approuver",
    "approved": "approuvé",
    "area": "zone",
    "associated": "associé",
    "assessment": "évaluation",
    "average": "moyenne",
    "before": "avant",
    "between": "entre",
    "biosolids": "biosolides",
    "buffer": "tampon",
    "building": "bâtiment",
    "buildings": "bâtiments",
    "capacity": "capacité",
    "case": "cas",
    "cases": "cas",
    "change": "modifier",
    "check": "vérifier",
    "city": "ville",
    "close": "proche",
    "closest": "le plus proche",
    "code": "code",
    "coliform": "coliforme",
    "collected": "collecté",
    "collection": "collecte",
    "comment": "commentaire",
    "comments": "commentaires",
    "community": "communautaire",
    "compliance": "conformité",
    "connection": "branchement",
    "connections": "branchements",
    "contact": "contact",
    "containment": "ouvrage de confinement",
    "containments": "ouvrages de confinement",
    "content": "contenu",
    "cost": "coût",
    "count": "nombre",
    "create": "créer",
    "created": "créé",
    "creation": "création",
    "customer": "client",
    "data": "données",
    "date": "date",
    "delete": "supprimer",
    "deleted": "supprimé",
    "department": "service",
    "depth": "profondeur",
    "details": "détails",
    "different": "différent",
    "disabled": "désactivé",
    "disease": "maladie",
    "distance": "distance",
    "distribution": "répartition",
    "driver": "chauffeur",
    "drivers": "chauffeurs",
    "edit": "modifier",
    "education": "éducation",
    "educational": "éducatif",
    "efficiency": "efficacité",
    "effluent": "effluent",
    "email": "e-mail",
    "emptying": "vidange",
    "employee": "employé",
    "end": "fin",
    "error": "erreur",
    "existing": "existant",
    "export": "exporter",
    "facility": "installation",
    "facilities": "installations",
    "failed": "échec",
    "feedback": "retour d'information",
    "female": "femme",
    "file": "fichier",
    "filter": "filtrer",
    "floor": "étage",
    "floors": "étages",
    "for": "pour",
    "found": "trouvé",
    "from": "de",
    "function": "fonction",
    "gender": "sexe",
    "generate": "générer",
    "generated": "généré",
    "greywater": "eaux grises",
    "group": "groupe",
    "has": "a",
    "health": "santé",
    "help": "aide",
    "history": "historique",
    "hotspot": "point chaud",
    "hotspots": "points chauds",
    "house": "bâtiment",
    "household": "ménage",
    "households": "ménages",
    "image": "image",
    "import": "importer",
    "inactive": "inactif",
    "income": "revenu",
    "information": "information",
    "integer": "entier",
    "invalid": "invalide",
    "is": "est",
    "issue": "émission",
    "job": "tâche",
    "key": "clé",
    "label": "libellé",
    "land": "parcelle",
    "language": "langue",
    "languages": "langues",
    "last": "dernier",
    "length": "longueur",
    "license": "licence",
    "line": "ligne",
    "lines": "lignes",
    "list": "liste",
    "load": "charger",
    "location": "localisation",
    "log": "journal",
    "low": "faible",
    "male": "homme",
    "management": "gestion",
    "map": "carte",
    "material": "matériau",
    "max": "max",
    "maximum": "maximum",
    "mechanically": "mécaniquement",
    "minimum": "minimum",
    "mobile": "mobile",
    "monitoring": "suivi",
    "more": "plus",
    "must": "doit",
    "name": "nom",
    "network": "réseau",
    "new": "nouveau",
    "next": "suivant",
    "not": "ne ... pas",
    "notes": "notes",
    "number": "nombre",
    "numeric": "numérique",
    "of": "de",
    "on": "sur",
    "operator": "opérateur",
    "other": "autre",
    "others": "autres",
    "owner": "propriétaire",
    "password": "mot de passe",
    "payment": "paiement",
    "percentage": "pourcentage",
    "permission": "permission",
    "phone": "téléphone",
    "pit": "fosse",
    "place": "lieu",
    "plant": "station",
    "population": "population",
    "positive": "positif",
    "presence": "présence",
    "preview": "aperçu",
    "private": "privé",
    "provider": "prestataire",
    "public": "public",
    "quality": "qualité",
    "questionnaire": "questionnaire",
    "receiver": "bénéficiaire",
    "record": "enregistrement",
    "records": "enregistrements",
    "required": "obligatoire",
    "response": "réponse",
    "result": "résultat",
    "revenue": "recette",
    "road": "route",
    "roads": "routes",
    "role": "rôle",
    "safely": "en toute sécurité",
    "sample": "échantillon",
    "samples": "échantillons",
    "sanitation": "assainissement",
    "save": "enregistrer",
    "search": "rechercher",
    "selected": "sélectionné",
    "service": "service",
    "services": "services",
    "settings": "paramètres",
    "shared": "partagé",
    "show": "afficher",
    "size": "taille",
    "sludge": "boues",
    "source": "source",
    "start": "début",
    "status": "statut",
    "string": "chaîne",
    "successfully": "avec succès",
    "summary": "résumé",
    "support": "appui",
    "survey": "enquête",
    "system": "système",
    "systems": "systèmes",
    "tank": "cuve",
    "tax": "taxe",
    "time": "heure",
    "toilet": "toilette",
    "toilets": "toilettes",
    "total": "total",
    "transported": "transporté",
    "treatment": "traitement",
    "type": "type",
    "unmatched": "non apparié",
    "update": "mettre à jour",
    "updated": "mis à jour",
    "upload": "téléverser",
    "user": "utilisateur",
    "users": "utilisateurs",
    "utility": "infrastructure",
    "validation": "validation",
    "value": "valeur",
    "vehicle": "véhicule",
    "view": "voir",
    "volume": "volume",
    "ward": "quartier",
    "wardwise": "par quartier",
    "water": "eau",
    "waterborne": "hydrique",
    "wastewater": "eaux usées",
    "width": "largeur",
    "with": "avec",
    "without": "sans",
    "year": "année",
    "years": "années",
}

PATTERNS = [
    (re.compile(r"^(.*) created successfully\.?$", re.I), "Création réussie : {0}."),
    (re.compile(r"^(.*) updated successfully\.?$", re.I), "Mise à jour réussie : {0}."),
    (re.compile(r"^(.*) deleted successfully\.?$", re.I), "Suppression réussie : {0}."),
    (re.compile(r"^Failed to delete (.*)\.?$", re.I), "Échec de la suppression : {0}."),
    (re.compile(r"^Failed to update (.*)\.?$", re.I), "Échec de la mise à jour : {0}."),
    (re.compile(r"^Failed to create (.*)\.?$", re.I), "Échec de la création : {0}."),
    (
        re.compile(r"^Cannot delete (.*) that has associated (.*)\.?$", re.I),
        "Impossible de supprimer {0} car des données associées existent : {1}.",
    ),
    (
        re.compile(r"^Cannot delete (.*) that is associated with (.*)\.?$", re.I),
        "Impossible de supprimer {0} car des données associées existent : {1}.",
    ),
    (
        re.compile(r"^Cannot delete (.*), it is associated with (.*)\.?$", re.I),
        "Impossible de supprimer {0} car des données associées existent : {1}.",
    ),
    (
        re.compile(r"^The (.*) field is required\.?$", re.I),
        "Le champ {0} est obligatoire.",
    ),
    (re.compile(r"^The (.*) is required\.?$", re.I), "{0} est obligatoire."),
    (
        re.compile(r"^The selected (.*) is invalid\.?$", re.I),
        "{0} sélectionné est invalide.",
    ),
]


def preserve_case(source: str, target: str) -> str:
    if source.isupper():
        return target.upper()
    if source.istitle():
        return target[:1].upper() + target[1:]
    return target


def apply_word_replacements(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        word = match.group(0)
        replacement = WORD_REPLACEMENTS.get(word.lower())
        if not replacement:
            return word
        return preserve_case(word, replacement)

    return re.sub(r"[A-Za-z][A-Za-z'/()-]*", repl, text)


def cleanup(text: str) -> str:
    text = re.sub(r"\s+([,.;:!?])", r"\1", text)
    text = re.sub(r"\(\s+", "(", text)
    text = re.sub(r"\s+\)", ")", text)
    text = re.sub(r"\s{2,}", " ", text).strip()
    text = text.replace(" ,", ",")
    text = text.replace(" .", ".")
    text = text.replace(" :", " :")
    text = text.replace("  ", " ")
    return text


def translate_fragment(text: str) -> str:
    if text in EXACT_TRANSLATIONS:
        return EXACT_TRANSLATIONS[text]

    translated = text
    for source, target in PHRASE_REPLACEMENTS:
        translated = re.sub(
            re.escape(source),
            lambda m: preserve_case(m.group(0), target),
            translated,
            flags=re.I,
        )
    translated = apply_word_replacements(translated)
    return cleanup(translated)


def translate_text(text: str) -> str:
    if text in EXACT_TRANSLATIONS:
        return EXACT_TRANSLATIONS[text]

    for pattern, template in PATTERNS:
        match = pattern.match(text)
        if match:
            translated_parts = [translate_fragment(group) for group in match.groups()]
            return cleanup(template.format(*translated_parts))

    return translate_fragment(text)


def load_rows() -> list[dict[str, str]]:
    with SOURCE_CSV.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def write_json(rows: list[dict[str, str]]) -> None:
    payload = {row["text"]: translate_text(row["text"]) for row in rows}
    WEB_JSON.parent.mkdir(parents=True, exist_ok=True)
    MOBILE_JSON.parent.mkdir(parents=True, exist_ok=True)
    WEB_JSON.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    MOBILE_JSON.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def write_csv(rows: list[dict[str, str]]) -> None:
    FRENCH_CSV.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "id",
        "key",
        "name",
        "text",
        "pages",
        "Group",
        "platform",
        "load",
        "translated_text",
    ]
    with FRENCH_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "id": row["id"],
                    "key": row["key"],
                    "name": "fr",
                    "text": row["text"],
                    "pages": row["pages"],
                    "Group": row["Group"],
                    "platform": row["platform"],
                    "load": row["load"],
                    "translated_text": translate_text(row["text"]),
                }
            )


def main() -> None:
    rows = load_rows()
    write_json(rows)
    write_csv(rows)


if __name__ == "__main__":
    main()
