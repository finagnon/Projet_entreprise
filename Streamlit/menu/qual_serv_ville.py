import pandas as pd
import streamlit as st    
import plotly.graph_objects as go 

def qual_serv_ville():
    # Charger les données depuis le fichier CSV
    df = pd.read_csv('../Data/csv/taux_ville.csv', sep=';')
    
    st.markdown("<h6 >Représentation de la qualité des services par villes en fonction des avis. Perception des utilisateurs et l’identification des villes ayant les meilleurs et les moins bons résultats en termes de satisfaction des services. Analyse comparative et mise en évidence des variations entre les différentes localités.</h6>", unsafe_allow_html=True)

    # Sélection de la colonne "Ville" via le dropdown
    selected_ville = st.selectbox('Sélectionnez une ville', df['Ville'].unique())

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