import pandas as pd
import streamlit as st
import plotly.graph_objects as go
    
def avis_prc_ville():    
    # Charger les données des scores des villes d'Île-de-France
    datafr = pd.read_csv('../Data/csv/taux_ville.csv', sep=';')

    # Créer une liste des options de sélection pour le dropdown
    villes = datafr['Ville'].unique()
    
    st.markdown("<h6>La répartition des avis par ville et l’observation des préférences et opinions des utilisateurs. La visualisation claire des proportions relatives des avis positifs, négatifs et neutres, facilitant ainsi la détection de tendances et de disparités entre les villes en termes de satisfaction des services.</h6>", unsafe_allow_html=True)

    # Sélection de la ville via le dropdown
    selected_ville = st.selectbox('Sélectionnez une ville', villes)

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
    # fig_performance.update_layout(height=400, width=400, margin=dict(l=20, r=20, t=30, b=20))

    # Afficher les graphiques
    st.plotly_chart(fig_avis, use_container_width=True)
    # st.plotly_chart(fig_performance, use_container_width=True)
