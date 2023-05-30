import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopy.geocoders as geocoders
from geopy.extra.rate_limiter import RateLimiter
import geopandas as gpd
import folium
from geopy.geocoders import Nominatim
import plotly.graph_objects as go
import matplotlib.dates as mdates
from PIL import Image
import plotly.graph_objects as go
import webbrowser
import base64
from io import BytesIO
import datetime




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
        background-color: #E0E0E0 /* Couleur de la barre de menu */
    }
    
    .sidebar .sidebar-content {
        background-color: #C0C0C0; /* Couleur de fond du menu à gauche de l'écran */
    }

    </style>
    """

    # Afficher le style CSS personnalisé
    st.markdown(background_css, unsafe_allow_html=True)

    
    

    def ouvrir_page(url):
        webbrowser.open(url)
  
    data = load_data(2336)  
    data = pd.read_csv('C:/Users/sylva/OneDrive/Bureau/scrap_project_MD4/Projet_entreprise/Data/Île-de-France_POLE EMPLOI.csv', sep=';')


    st.sidebar.header("Menu")

    selected_option = st.sidebar.selectbox("Choisir une option", ["Accueil", "Pourcentages des Etoiles" ,"Tableau de données", "Nombre d'étoiles par période", "Qualité de services par Ville","Total avis en % par ville", "Les Scores par ville", "Carte des agences"])


    if selected_option == "Accueil":
        # Charger et afficher l'image 
        image_icon = Image.open("C:/Users/sylva/OneDrive/Bureau/scrap_project_MD4/Projet_entreprise/Streamlit/Image/RF.png")      
        width, height = 100, 100
        image_icon_resized = image_icon.resize((width, height))
        st.image(image_icon_resized)
        
        image1 = Image.open("C:/Users/sylva/OneDrive/Bureau/scrap_project_MD4/Projet_entreprise/Streamlit/Image/Logo-Pôle-Emploi.png")
        st.image(image1, use_column_width=True)
        

        
    
        st.markdown("<h1 style='color: #191970;'>Bienvenue dans Projet Entreprise</h1>", unsafe_allow_html=True)
        # pass
    
    elif selected_option == "Pourcentages des Etoiles":
        st.markdown("<h2 style='color: #191970;'>Somme des Etoiles en Pourcentage</h2>", unsafe_allow_html=True)

        Labels = ['1 étoile', '2 étoiles', '3 étoiles', '4 étoiles', '5 étoiles']
        sizes = [1305, 104, 131, 154, 616]
        color = ['#ff0000', '#ffa700', '#fff400', '#a3ff00', '#2cba00']
        explode = (0.05, 0.05, 0.05, 0.05)

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, colors=color, labels=Labels, autopct='%1.1f%%', startangle=90)
        # draw circle
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        # Equal aspect ratio ensures that pie is drawn as a circle
        ax1.axis('equal')
        plt.tight_layout()
        st.pyplot(fig)  
    
    
    elif selected_option == "Tableau de données":
        data_load_state = st.text('Chargement des données...')
        data = load_data(2337)
        data_load_state.text("Chargement terminé")

        st.subheader('Les Données')
        st.write(data)
        
    elif selected_option == "Nombre d'étoiles par période":
        dfm = pd.read_csv('C:/Users/sylva/OneDrive/Bureau/scrap_project_MD4/Projet_entreprise/Data/Île-de-France_POLE_EMPLOI_copie.csv', sep=';')
        st.subheader('Nombre Etoiles par période')

        # Convertir les valeurs float en str dans la colonne "Date"
        dfm['Date'] = dfm['Date'].apply(lambda x: str(x) if isinstance(x, float) else x)

        # Exclure les valeurs 'nan' de la colonne "Date"
        dfm = dfm.dropna(subset=['Date'])

        # Appliquer la fonction strptime() en gérant les exceptions pour les valeurs non valides
        dfm['ParsedDate'] = dfm['Date'].apply(lambda x: pd.NaT if x == 'nan' else datetime.datetime.strptime(x, "%d/%m/%Y") if isinstance(x, str) else pd.NaT)

        # Supprimer les lignes avec des valeurs non valides
        dfm = dfm.dropna(subset=['ParsedDate'])

        # Regrouper par année et calculer la somme des étoiles
        etoiles_sum = dfm.groupby(dfm['ParsedDate'].dt.year)['Etoile'].sum()

        periodes = etoiles_sum.index
        etoiles = etoiles_sum.values

        fig = plt.figure()
        plt.plot(periodes, etoiles, label='Nombre Etoiles')
        plt.xlabel('Années')
        plt.ylabel('Somme des étoiles')
        plt.legend()
        plt.xticks(periodes, labels=[str(year) for year in periodes])  # Afficher les années au format "2023"
        st.pyplot(fig)
        
    elif selected_option == "Qualité de services par Ville":



        # Charger les données depuis le fichier CSV
        df = pd.read_csv('C:/Users/sylva/OneDrive/Bureau/scrap_project_MD4/Projet_entreprise/Data/taux_ville.csv', sep=';')

        # Sélection de la colonne "Ville" via le dropdown
        selected_ville = st.selectbox('Sélectionner une ville', df['Ville'].unique())

        # Filtrer les données pour la ville sélectionnée
        ville_data = df[df['Ville'] == selected_ville]

        # Récupérer les nombres d'avis positifs, négatifs et neutres
        avis_positifs = ville_data["Nombre d’avis Positif"].iloc[0]
        avis_negatifs = ville_data["Nombre d’avis négatif"].iloc[0]
        avis_neutres = ville_data["Nombre d’avis Neutre"].iloc[0]

        # Créer les données pour le graphique en barres
        categories = ['Avis positifs', 'Avis négatifs', 'Avis neutres']
        values = [avis_positifs, avis_negatifs, avis_neutres]
        colors = ['green', 'red', 'yellow']

        # Créer le graphique en barres
        fig = go.Figure(data=[go.Bar(x=categories, y=values, marker=dict(color=colors))])

        # Mise en forme du layout du graphique en barres
        fig.update_layout(title='Qualité de service pour la ville : ' + selected_ville,
                        xaxis_title='Types d\'avis',
                        yaxis_title='Nombre d\'avis')

        # Afficher le graphique en barres
        st.plotly_chart(fig)


    elif selected_option == "Total avis en % par ville":
        # Charger les données des scores des villes d'Île-de-France
        datafr = pd.read_csv('C:/Users/sylva/OneDrive/Bureau/scrap_project_MD4/Projet_entreprise/Data/taux_ville.csv', sep=';')

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

        # Calculer la performance totale en pourcentage
        performance_totale = (avis_positifs / total_avis) * 100

        # Ajouter une trace semi-circulaire pour la performance totale
        fig_performance.add_trace(go.Indicator(
            mode="gauge+number",
            value=performance_totale,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': 'Etude Comparative - Performance totale'},
            gauge={'axis': {'range': [0, 100]},
                'bar': {'color': 'purple'},
                'steps': [{'range': [0, 100], 'color': 'purple'}],
                'threshold': {'line': {'color': 'black', 'width': 4}, 'thickness': 0.75, 'value': performance_totale}}))

        # Mise en forme du layout des graphiques
        fig_avis.update_layout(height=400, width=600, margin=dict(l=20, r=20, t=30, b=20))
        fig_performance.update_layout(height=400, width=400, margin=dict(l=20, r=20, t=30, b=20))

        # Afficher les graphiques
        st.plotly_chart(fig_avis, use_container_width=True)
        st.plotly_chart(fig_performance, use_container_width=True)
        
    elif selected_option == "Les Scores par ville":

        datafr = pd.read_csv('C:/Users/sylva/OneDrive/Bureau/scrap_project_MD4/Projet_entreprise/Data/taux_ville.csv', sep=';')
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
     

    elif selected_option == "Carte des agences":
        # URL de la page de la carte des agences
        carte_url = 'file:///C:/Users/sylva/OneDrive/Bureau/scrap_project_MD4/Projet_entreprise/Streamlit/carte_pole_emploi.html'
        # Ouvrir automatiquement la page
        ouvrir_page(carte_url)

        

def load_data(nrows):
    data = pd.read_csv('C:/Users/sylva/OneDrive/Bureau/scrap_project_MD4/Projet_entreprise/Data/Île-de-France_POLE_EMPLOI_copie.csv', nrows=nrows, sep=';')
    data['Date'] = pd.to_datetime(data['Date'])
    return data

if __name__ == '__main__':
    main()












