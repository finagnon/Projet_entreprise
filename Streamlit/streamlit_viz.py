import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import geopy.geocoders as geocoders
# from geopy.extra.rate_limiter import RateLimiter
import geopandas as gpd
# import folium
# from geopy.geocoders import Nominatim
import plotly.graph_objects as go
import matplotlib.dates as mdates
from PIL import Image
import plotly.graph_objects as goa
import webbrowser
from menu.score_ville import score_ville
from menu.avis_prc_ville import avis_prc_ville
from menu.qual_serv_ville import qual_serv_ville
# import base64
# from io import BytesIO
# import datetime
from menu.etoile_periode import etoile_periode
from menu.tab_data import tab_data
from menu.pourcentage_etoiles import prc_etoile
from menu.accueil import accueil



def main():
    # Déplacer st.set_page_config() comme première commande Streamlit
    st.set_page_config(page_title="Projet-Entreprise", page_icon="🧊")
    
    # Définir le style CSS pour l'arrière-plan
    background_css = """
    <style>
    body {
        background-color: green; /* Couleur d'arrière-plan */
    }

    .stApp {
        background-color: #FFFFFF /* Couleur de la barre de menu */
    }
    
    .sidebar .sidebar-content {
        background-color: #C0C0C0; /* Couleur de fond du menu à gauche de l'écran */
    }

    </style>
    """

    # Afficher le style CSS personnalisé
    st.markdown(background_css, unsafe_allow_html=True)
  
    # data = load_data(2336)  
    data = pd.read_csv('Data/Île-de-France_POLE EMPLOI.csv', nrows=2336, sep=';')
    data['Date'] = pd.to_datetime(data['Date'])
    st.sidebar.header("Menu")
    
    # data = pd.read_csv('Data/Île-de-France_POLE EMPLOI.csv', sep=';')

    selected_option = st.sidebar.selectbox("Choisir une option", ["Accueil", "Pourcentages des Etoiles" ,"Tableau de données", "Nombre d'étoiles par période", "Qualité de services par Ville","Total avis en % par ville", "Les Scores par ville", "Carte des agences"])

    if selected_option == "Accueil":
        accueil()
    
    elif selected_option == "Pourcentages des Etoiles":
        prc_etoile()
    
    elif selected_option == "Tableau de données":
        tab_data()
        
    elif selected_option == "Nombre d'étoiles par période":
        etoile_periode()
        
    elif selected_option == "Qualité de services par Ville":
        qual_serv_ville()

    elif selected_option == "Total avis en % par ville":
       avis_prc_ville()
        
    elif selected_option == "Les Scores par ville":
        score_ville()

    elif selected_option == "Carte des agences":
        # URL de la page de la carte des agences
        webbrowser.open('file:///carte_pole_emploi.html')


# def load_data(nrows):
#     data = pd.read_csv('Data/Île-de-France_POLE_EMPLOI_copie.csv', nrows=nrows, sep=';')
#     data['Date'] = pd.to_datetime(data['Date'])
#     return data

if __name__ == '__main__':
    main()