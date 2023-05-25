# Projet_entreprise -->

Dans notre scrapping, nous avons utilisé SELENIUM et BEAUTIFULSOUP ***

# L'objectif est de  scrapper les avis des services publics dans chaque régions de france.

Le code va parcourir chaque région et stocke les informations concernant ce service ainsi de suite.

Apres chaque recherche, il récupère le lien et le stocke.  Nous pouvons retrouver cela dans le fichier : "scrapperNomLien.ipynb"


# Notre recherche s'effectue automatiquement et scrolle pour chaque service public.

Nous arrivons à recuperer les avis des auteurs pour chaque services et par regions en affichant son INSEE, son nom, son commentaire, sa date de commentaire.

nous obtenons apres chaque itération, un csv contenant "nom_region" qui varie suivi de "tous_services.csv
Nous avons effectuer le calcul des dates de commentaires avec la date d'aujourd'hui, pour obtenir une date exacte qui remonte jusqu'à la date de publication avec comme référence aujourd'hui dans un format (19/05/22)


Pour effectuer certaines taches, nous avons recuperé et stocké les csv region.csv (contenant la liste des regions de france ),
# regions_liens.csv (contenant les liens des regions), services.csv (contenant tous les servivces)


# **************ETAPES : *************************************************
 ------>Les fichiers à exectuer par étapes:
            fichier: "services.ipynb" = pour afficher tous les services qui feront l'objet du travail
            fichier : "scrapperNomLien.ipynb = pour récuperer les liens et les stockés "Nb: ça se fait automatiquement"
            fichier : "scrapping.ipynb = pour recuperer le csv d'un service selon la region défini.








