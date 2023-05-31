import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import geopy.geocoders as geocoders
# from geopy.extra.rate_limiter import RateLimiter
import geopandas as gpd
# import folium
from geopy.geocoders import Nominatim
# from geopy.geocoders import Nominatim

import plotly.graph_objects as go
import matplotlib.dates as mdates
from PIL import Image
import plotly.graph_objects as goa
import webbrowser
import base64
from io import BytesIO
import datetime
from plotly.subplots import make_subplots
import plotly.express as px



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

        background-color: #ffffff /* Couleur de la barre de menu */

        background-color: #FFFFFF /* Couleur de la barre de menu */
    }
    
    .sidebar .sidebar-content {
        background-color: #C0C0C0; /* Couleur de fond du menu à gauche de l'écran */
    }

    </style>
    """

    # Afficher le style CSS personnalisé
    st.markdown(background_css, unsafe_allow_html=True)
  
    data = load_data(2336)  
    data = pd.read_csv('../Data/csv/Île-de-France_POLE EMPLOI.csv', sep=';')


    # data = load_data(2336)  
    data = pd.read_csv('../Data/csv/Île-de-France_POLE EMPLOI.csv', nrows=2336, sep=';')
    data['Date'] = pd.to_datetime(data['Date'])
    st.sidebar.header("Menu")
    
    # data = pd.read_csv('Data/Île-de-France_POLE EMPLOI.csv', sep=';')

    selected_option = st.sidebar.selectbox("Choisir une option", ["Accueil", "Pourcentages des Etoiles" ,"Tableau de données", "Nombre d'avis positifs par ville /année", "Qualité de services par Ville","Taux des avis par ville en %", "Les Scores par ville", "Carte des agences"])

    if selected_option == "Accueil":

        # Charger et afficher l'image 
        image_icon = Image.open("C:/Users/sylva/OneDrive/Bureau/scrap_project_MD4/Projet_entreprise/Data/Image/RF.png")      
        width, height = 100, 100
        image_icon_resized = image_icon.resize((width, height))
        st.image(image_icon_resized)
        
        image1 = Image.open("C:/Users/sylva/OneDrive/Bureau/scrap_project_MD4/Projet_entreprise/Data/Image/Logo-Pôle-Emploi.png")
        st.image(image1, use_column_width=True)
        

        
    
        st.markdown("<h1 style='color: #191970;'>Bienvenue dans Projet Entreprise</h1>", unsafe_allow_html=True)
        # pass

        accueil()
    
    elif selected_option == "Pourcentages des Etoiles":
        prc_etoile()
    
    elif selected_option == "Tableau de données":
        tab_data()
        
    elif selected_option == "Nombre d'avis positifs par ville /année":
        
        # Charger les données depuis le fichier CSV
        df = pd.read_csv('../Data/csv/avi.csv', sep=';')

        # Extraire l'année à partir de la colonne "Date de publication"
        df['Year'] = pd.to_datetime(df['Date de publication'], format='%d/%m/%Y').dt.strftime('%Y')

        # Récupérer toutes les années du CSV
        annees = df['Year'].unique()

        # Sélection de la ville via le dropdown
        selected_ville = st.selectbox('Sélectionner une ville', df['Ville'].unique())

        # Filtrer les données pour la ville sélectionnée
        positifs_par_ville = df[df['Ville'] == selected_ville]
        positifs_par_ville = positifs_par_ville[positifs_par_ville['Type'] == 'Positif'].groupby(['Year']).size().reset_index(name='Count')

        # Créer le graphique en courbe
        fig = px.line(positifs_par_ville, x='Year', y='Count')
        

        # Mise en forme du layout du graphique
        fig.update_layout(title=f'Nombre d\'avis positifs par année pour la ville : {selected_ville}',
                     
                        
                        yaxis_title='Nombre d\'avis positifs')
        fig.update_xaxes(title_text='Année',dtick=1)
        
        fig.update_yaxes(title_text='Nombre d\'avis positifs',dtick=1)

        # Afficher le graphique en courbe
        st.plotly_chart(fig)

        
    elif selected_option == "Qualité de services par Ville":

        # Charger les données depuis le fichier CSV
        df = pd.read_csv('../Data/csv/taux_ville.csv', sep=';')

        # Sélection de la colonne "Ville" via le dropdown
        selected_ville_1 = st.selectbox('Sélectionner la première ville', df['Ville'].unique())

        # Filtrer les données pour la première ville sélectionnée
        ville_data_1 = df[df['Ville'] == selected_ville_1]

        # Récupérer les nombres d'avis positifs, négatifs et neutres de la première ville
        avis_positifs_1 = ville_data_1["Nombre d’avis Positif"].iloc[0]
        avis_negatifs_1 = ville_data_1["Nombre d’avis négatif"].iloc[0]
        avis_neutres_1 = ville_data_1["Nombre d’avis Neutre"].iloc[0]

        # Créer les données pour le premier graphique en barres
        categories = ['Avis positifs', 'Avis négatifs', 'Avis neutres']
        values_1 = [avis_positifs_1, avis_negatifs_1, avis_neutres_1]
        colors = ['green', 'red', 'yellow']

        # Créer le premier graphique en barres
        fig1 = go.Figure(data=[go.Bar(x=categories, y=values_1, marker=dict(color=colors))])

        # Mise en forme du layout du premier graphique en barres
        fig1.update_layout(title='Etude Comparative de la qualité de service par ville : ' + selected_ville_1,
                        xaxis_title='Ville 1',
                        yaxis_title='Nombre d\'avis')

        # Sélection de la colonne "Ville" via le dropdown
        selected_ville_2 = st.selectbox('Sélectionner la deuxième ville', df['Ville'].unique())

        # Filtrer les données pour la deuxième ville sélectionnée
        ville_data_2 = df[df['Ville'] == selected_ville_2]

        # Récupérer les nombres d'avis positifs, négatifs et neutres de la deuxième ville
        avis_positifs_2 = ville_data_2["Nombre d’avis Positif"].iloc[0]
        avis_negatifs_2 = ville_data_2["Nombre d’avis négatif"].iloc[0]
        avis_neutres_2 = ville_data_2["Nombre d’avis Neutre"].iloc[0]

        # Créer les données pour le deuxième graphique en barres
        values_2 = [avis_positifs_2, avis_negatifs_2, avis_neutres_2]

        # Créer le deuxième graphique en barres
        fig2 = go.Figure(data=[go.Bar(x=categories, y=values_2, marker=dict(color=colors))])

        # Mise en forme du layout du deuxième graphique en barres
        fig2.update_layout(title='Etude Comparative de la qualité de service par ville  : ' + selected_ville_2,
                        xaxis_title='Ville 2',
                        yaxis_title='Nombre d\'avis')

        # Afficher les graphiques en barres côte à côte avec les titres
        fig = make_subplots(rows=1, cols=2, subplot_titles=(selected_ville_1, selected_ville_2))
        fig.add_trace(fig1.data[0], row=1, col=1)
        fig.add_trace(fig2.data[0], row=1, col=2)

        fig.update_layout(title='Etude Comparative de la qualité de service par ville')
        fig.update_xaxes(title_text='Vile 1', row=1, col=1)
        fig.update_xaxes(title_text='Ville 2', row=1, col=2)

        st.plotly_chart(fig)





    elif selected_option == "Taux des avis par ville en %":
        # Charger les données des scores des villes d'Île-de-France
        datafr = pd.read_csv('../Data/csv/taux_ville.csv', sep=';')

        # Créer une liste des options de sélection pour le dropdown
        villes = datafr['Ville'].unique()

        # Sélection de la ville via le dropdown
        selected_ville = st.selectbox('Sélectionner une ville', villes)

        # Filtrer les données pour la ville sélectionnée
        ville_data = datafr[datafr['Ville'] == selected_ville]

        # Récupérer le nombre d'avis négatifs, positifs et neutres
        avis_negatifs = ville_data["Nombre d’avis négatif"].iloc[0]
        avis_positifs = ville_data["Nombre d’avis Positif"].iloc[0]
        avis_neutres = ville_data["Nombre d’avis Neutre"].iloc[0]

        # Calculer le pourcentage des avis négatifs, positifs et neutres
        total_avis = avis_negatifs + avis_positifs + avis_neutres
        pourcentage_negatifs = (avis_negatifs / total_avis) * 100
        pourcentage_positifs = (avis_positifs / total_avis) * 100
        pourcentage_neutres = (avis_neutres / total_avis) * 100

        # Créer une figure en utilisant le graphique semi-circulaire de Plotly pour les avis
        fig_avis = go.Figure()

        # Ajouter une trace semi-circulaire pour les avis négatifs
        fig_avis.add_trace(go.Indicator(
            mode="gauge+number",
            value=pourcentage_negatifs,
            domain={'x': [0, 0.3], 'y': [0, 1]},
            title={'text': '% Avis négatifs'},
            gauge={'axis': {'range': [0, 100]},
                'bar': {'color': 'red'},
                'steps': [{'range': [0, 50], 'color': 'red'}],
                'threshold': {'line': {'color': 'black', 'width': 4}, 'thickness': 0.75, 'value': pourcentage_negatifs}}))

        # Ajouter une trace semi-circulaire pour les avis positifs
        fig_avis.add_trace(go.Indicator(
            mode="gauge+number",
            value=pourcentage_positifs,
            domain={'x': [0.35, 0.65], 'y': [0, 1]},
            title={'text': '% Avis positifs'},
            gauge={'axis': {'range': [0, 100]},
                'bar': {'color': 'green'},
                'steps': [{'range': [0, 50], 'color': 'green'}],
                'threshold': {'line': {'color': 'black', 'width': 4}, 'thickness': 0.75, 'value': pourcentage_positifs}}))

        # Ajouter une trace semi-circulaire pour les avis neutres
        fig_avis.add_trace(go.Indicator(
            mode="gauge+number",
            value=pourcentage_neutres,
            domain={'x': [0.7, 1], 'y': [0, 1]},
            title={'text': ' % Avis neutres'},
            gauge={'axis': {'range': [0, 100]},
                'bar': {'color': 'blue'},
                'steps': [{'range': [0, 50], 'color': 'blue'}],
                'threshold': {'line': {'color': 'black', 'width': 4}, 'thickness': 0.75, 'value': pourcentage_neutres}}))

        # Créer une figure en utilisant le graphique semi-circulaire de Plotly pour la performance totale
        fig_performance = go.Figure()


        # Mise en forme du layout des graphiques
        fig_avis.update_layout(height=400, width=600, margin=dict(l=20, r=20, t=30, b=20))
        # fig_performance.update_layout(height=400, width=400, margin=dict(l=20, r=20, t=30, b=20))

        # Afficher les graphiques
        st.plotly_chart(fig_avis, use_container_width=True)
        # st.plotly_chart(fig_performance, use_container_width=True)
        
    elif selected_option == "Les Scores par ville":

        datafr = pd.read_csv('../Data/csv/taux_ville.csv', sep=';')
        # Créer une liste des options de sélection pour le dropdown
        villes = datafr['Ville'].unique()

        # Sélection de la ville via le dropdown
        selected_ville = st.selectbox('Sélectionner une ville', villes)

        # Filtrer les données pour la ville sélectionnée
        ville_data = datafr[datafr['Ville'] == selected_ville]

        # Récupérer le nombre d'avis négatifs, positifs et neutres
        avis_positifs = ville_data["Nombre d’avis Positif"].iloc[0]
        avis_negatifs = ville_data["Nombre d’avis négatif"].iloc[0]        
        avis_neutres = ville_data["Nombre d’avis Neutre"].iloc[0]

       
        score_positifs = avis_positifs
        score_negatifs = avis_negatifs       
        score_neutres = avis_neutres

        # Créer une figure en utilisant le graphique semi-circulaire de Plotly pour les avis
        fig_avis = go.Figure()


        # Ajouter une trace semi-circulaire pour les avis positifs
        fig_avis.add_trace(go.Indicator(
            mode="gauge+number",
            value=score_positifs,
            domain={'x': [0.35, 0.65], 'y': [0, 1]},
            title={'text': 'Avis positifs'},
            gauge={'axis': {'range': [0, 100]},
                'bar': {'color': 'green'},
                'steps': [{'range': [0, 50], 'color': 'green'}],
                'threshold': {'line': {'color': 'black', 'width': 4}, 'thickness': 0.75, 'value': score_positifs}}))
        
        
        # Ajouter une trace semi-circulaire pour les avis négatifs
        fig_avis.add_trace(go.Indicator(
            mode="gauge+number",
            value=score_negatifs,
            domain={'x': [0, 0.3], 'y': [0, 1]},
            title={'text': 'Avis négatifs'},
            gauge={'axis': {'range': [0, 100]},
                'bar': {'color': 'red'},
                'steps': [{'range': [0, 50], 'color': 'red'}],
                'threshold': {'line': {'color': 'black', 'width': 4}, 'thickness': 0.75, 'value': score_negatifs}}))



        # Ajouter une trace semi-circulaire pour les avis neutres
        fig_avis.add_trace(go.Indicator(
            mode="gauge+number",
            value=score_neutres,
            domain={'x': [0.7, 1], 'y': [0, 1]},
            title={'text': ' Avis neutres'},
            gauge={'axis': {'range': [0, 100]},
                'bar': {'color': 'blue'},
                'steps': [{'range': [0, 50], 'color': 'yellow'}],
                'threshold': {'line': {'color': 'black', 'width': 4}, 'thickness': 0.75, 'value': score_neutres}}))

         
        # Mise en forme du layout des graphiques
        fig_avis.update_layout(height=400, width=600, margin=dict(l=20, r=20, t=30, b=20))
        

        # Afficher les graphiques
        st.plotly_chart(fig_avis, use_container_width=True)
     
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
        webbrowser.open('file:///C:/Users/sylva/OneDrive/Bureau/scrap_project_MD4/Projet_entreprise/Streamlit/carte_pole_emploi.html')


def load_data(nrows):
    data = pd.read_csv('../Data/csv/Île-de-France_POLE_EMPLOI_copie.csv', nrows=nrows, sep=';')
    data['Date'] = pd.to_datetime(data['Date'])
    return data

# def load_data(nrows):
#     data = pd.read_csv('Data/Île-de-France_POLE_EMPLOI_copie.csv', nrows=nrows, sep=';')
#     data['Date'] = pd.to_datetime(data['Date'])
#     return data

if __name__ == '__main__':
    main()