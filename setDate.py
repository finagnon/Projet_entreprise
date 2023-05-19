import re
from datetime import date, timedelta
import pandas as pd
#J'ai installé aussi la bibliothèque openpyxl, pour lire les fichiers XLSX
#pip install openpyxl


date_actuelle = date.today()

list_date = pd.read_excel("transformeDate.xlsx")

def calculDate(list_date):
    date_calcul = ''
    for this_date in list_date['Date']:
        print(this_date)
        #ON VERIFIE LE FORMAT DU TEMPS (jour, mois, année)
        #Création des regex :
        #___Vérification pour les années
        verif_year = re.findall(r"\b(\d+|un) (an|ans)\b", this_date)
        #___Vérification pour les mois
        verif_month = re.findall(r"\b(\d+|un) (mois)\b", this_date)
        #___Vérification pour les semaines
        verif_week = re.findall(r"\b(\d+|une) (semaine|semaines)\b", this_date)
        #___Vérification pour les jours
        verif_days = re.findall(r"\b(\d+|un) (jour|jours)\b", this_date)

        if len(verif_year) != 0:
            try:
                if(int(verif_year[0][0])):#Soustraction de plusieurs années
                    print(date_actuelle-timedelta(days=365*int(verif_year[0][0])))
                    date_calcul = date_actuelle-timedelta(days=365*int(verif_year[0][0]))
            except ValueError:#Soustraction d'un seul
                date_calcul = date_actuelle-timedelta(days=365)
                print(date_actuelle-timedelta(days=365))
                
        elif len(verif_month) != 0:
            try:
                if(int(verif_month[0][0])):#Soustraction de plusieurs mois
                    print(date_actuelle-timedelta(days=30*int(verif_month[0][0])))
                    date_calcul = date_actuelle-timedelta(days=30*int(verif_month[0][0]))
            except ValueError:#Soustraction d'un seul
                date_calcul = date_actuelle-timedelta(days=30)
                print(date_actuelle-timedelta(days=30))
        elif len(verif_week) != 0:
            try:
                if(int(verif_week[0][0])):#Soustraction de plusieurs semaines
                    print(date_actuelle-timedelta(days=7*int(verif_week[0][0])))
                    date_calcul = date_actuelle-timedelta(days=7*int(verif_week[0][0]))
            except ValueError:#Soustraction d'un seul
                date_actuelle-timedelta(days=7)
                print(date_actuelle-timedelta(days=7))
        elif len(verif_days) != 0:
            try:
                if(int(verif_days[0][0])):#Soustraction de plusieurs jours
                    date_calcul = date_actuelle-timedelta(days=int(verif_days[0][0]))
                    print(date_actuelle-timedelta(days=int(verif_days[0][0])))
            except ValueError:#Soustraction d'un seul
                date_calcul = date_actuelle-timedelta(days=1)
                print(date_actuelle-timedelta(days=1))
        else:
            print("aucune correspondance")
    return date_calcul
            
calculDate(list_date)