# Projet_entreprise

L'objectif est de scrapper (récupérer les données) tous les avis (commentaires) des services publics dans chaque régions de France.
Pour la réalisation de ce projet nous avons utilisés `Selenium` et on a eu à récuperer les données des avis sur `Google reviews maps`

Dans notre scrapping,

# Le code va parcourir chaque région et stocke les informations concernant ce service ainsi de suite.

# Apres chaque recherche, il récupère le lien et le stocke.  Nous pouvons retrouver cela dans le fichier : "scrapperNomLien.ipynb"



# Notre recherche s'effectue automatiquement et scrolle pour chaque service public.

# Nous arrivons à recuperer les avis des auteurs pour chaque services et par regions en affichant son INSEE, son nom, son commentaire, sa date de commentaire.

# nous obtenons apres chaque itération, un csv contenant "nom_region" qui varie suivi de "tous_services.csv

# Nous avons effectuer le calcul des dates de commentaires avec la date d'aujourd'hui, pour obtenir une date approcimative qui remonte à la date de publication avec comme référence aujourd'hui dans un format (19/05/22)


# Pour effectuer certaines taches, nous avons recuperé et stocké les csv region.csv (contenant la liste des regions de france ),
# regions_liens.csv (contenant les liens des regions), services.csv (contenant tous les servivces)


# **************ETAPES : *************************************************
 ------>Les fichiers à exectuer par étapes:
            fichier: "services.ipynb" = pour afficher tous les services qui feront l'objet du travai
            fichier : "scrapperNomLien.ipynb = pour récuperer les liens et les stockés "Nb: ça se fait automatiquement"
            - "servics.ipynb" : ce fichier permet d'extraire le nom de tous les services qui sont dans le fichier `./Data/export-experiences.csv`
            - `scrapperNomLien.ipynb` : permet de recherche tous les 13 regions de France qui sont les 
            fichier : "scrapping.ipynb = pour recuperer le csv d'un service selon la region défini.

Avant de commencer à lancer tous ses fichiers, assurez-vous d'avoir installer les dependances nécessaires en faisant :
- Installer python `pip install python` (vous pouvez aussi utiliser `anaconda`
- Créer un environnement virtuel `python -m venv .venv` (.venv : c'est le nom donner à un environnement donc vous pouvez toute fois le changer)
- Exécuter la commandes : `pip install -r requirements.txt` pour installer les resources
- Lancer le fichier `scrapping.ipynb` qui permet de scrapper tous les services.




