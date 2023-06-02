import pandas as pd
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go 

# Charger les données depuis le fichier CSV
def avis_positif_annee():

    # Charger les données depuis le fichier CSV
    df = pd.read_csv('../Data/csv/avi.csv', sep=';')

    # Extraire l'année à partir de la colonne "Date de publication"
    df['Year'] = pd.to_datetime(df['Date de publication'], format='%d/%m/%Y').dt.strftime('%Y')

    # Récupérer toutes les années du CSV
    annees = df['Year'].unique()

    st.markdown("<h6 >Visualisation de l'évolution des avis positifs au fil des années et comparaison des différentes villes. L’analyse sur la satisfaction des utilisateurs dans chaque ville.Les variations temporelles et géographiques des avis positifs.</h6>", unsafe_allow_html=True)
    # Sélection de la ville via le dropdown
    selected_ville = st.selectbox('Sélectionnez une ville', df['Ville'].unique())

    # Filtrer les données pour la ville sélectionnée
    positifs_par_ville = df[df['Ville'] == selected_ville]
    positifs_par_ville = positifs_par_ville[positifs_par_ville['Type'] == 'Positif'].groupby(['Year']).size().reset_index(name='Count')

    # Créer le graphique en courbe
    fig = px.line(positifs_par_ville, x='Year', y='Count')
    

    # Mise en forme du layout du graphique
    fig.update_layout(title=f'Représentation du nombre d\'avis positifs par année pour la ville : {selected_ville}',
                    
                    
                    yaxis_title='Nombre d\'avis positifs')
    fig.update_xaxes(title_text='Année',dtick=1)
    
    fig.update_yaxes(title_text='Nombre d\'avis positifs',dtick=1)

    # Afficher le graphique en courbe
    st.plotly_chart(fig)