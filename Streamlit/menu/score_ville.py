import pandas as pd
import streamlit as st
import plotly.graph_objects as go   
    
def score_ville():
    datafr = pd.read_csv('../Data/csv/taux_ville.csv', sep=';')
    # Créer une liste des options de sélection pour le dropdown
    villes = datafr['Ville'].unique()
    
    
    st.markdown("<h6>Représentation visuelle des quantités d'avis positifs, négatifs et neutres dans chaque ville à travers des données brutes. Etablir une étude approfondie pour identifier les tendances et les disparités entres les villes en termes de satisfaction de services.</h6>", unsafe_allow_html=True)

    # Sélection de la ville via le dropdown
    selected_ville = st.selectbox('Sélectionnez une ville', villes)

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