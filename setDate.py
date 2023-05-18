import re
from datetime import date, timedelta
import pandas as pd
#J'ai installé aussi la bibliothèque openpyxl, pour lire les fichiers XLSX
#pip install openpyxl


date_actuelle = date.today()
# print(date_actuelle-timedelta(days=30*3))

# list_date = pd.read_excel("transformeDate.xlsx")

# print(list_date['Date'])


chaine = "un an"
#ON VERIFIE LE FORMAT DU TEMPS (jour, mois, année)
#Création des regex :
#___Vérification pour les années
verif_year = re.findall(r"\b(\d+|un) (an|ans)\b", chaine)
#___Vérification pour les mois
verif_month = re.findall(r"\b(\d+|un) (mois)\b", chaine)
#___Vérification pour les semaines
verif_week = re.findall(r"\b(\d+|une) (semaine|semaines)\b", chaine)
#___Vérification pour les jours
verif_days = re.findall(r"\b(\d+|un) (jour|jours)\b", chaine)
    

if len(verif_year) != 0:
    try:
        if(int(verif_year[0][0])):#Soustraction de plusieurs
            print(date_actuelle-timedelta(days=365*int(verif_year[0][0])))
    except ValueError:#Soustraction d'un seul
        print(date_actuelle-timedelta(days=365))
        
elif len(verif_month) != 0:
    try:
        if(int(verif_month[0][0])):#Soustraction de plusieurs
            print(date_actuelle-timedelta(days=30*int(verif_month[0][0])))
    except ValueError:#Soustraction d'un seul
        print(date_actuelle-timedelta(days=30))
elif len(verif_week) != 0:
    try:
        if(int(verif_week[0][0])):#Soustraction de plusieurs
            print(date_actuelle-timedelta(days=7*int(verif_week[0][0])))
    except ValueError:#Soustraction d'un seul
        print(date_actuelle-timedelta(days=7))
elif len(verif_days) != 0:
    try:
        if(int(verif_days[0][0])):#Soustraction de plusieurs
            print(date_actuelle-timedelta(days=int(verif_days[0][0])))
    except ValueError:#Soustraction d'un seul
        print(date_actuelle-timedelta(days=1))
else:
    print("aucune correspondance")