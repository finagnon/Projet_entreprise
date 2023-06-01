import streamlit as st
import folium
import pandas as pd
from geopy.geocoders import Nominatim

# Charger les données contenant les informations sur les Pôle Emploi en Île-de-France
data = pd.read_csv('../Data/csv/Île-de-France_POLE_EMPLOI_copie.csv', sep=';')

# Créer une carte centrée sur l'Île-de-France
map = folium.Map(location=[48.8566, 2.3522], zoom_start=11)

# Géocoder les adresses pour obtenir les coordonnées géographiques
geolocator = Nominatim(user_agent='my_app')

# Obtenir les villes uniques et les localisations uniques
# villes_uniques = data['Ville'].unique()
localisations_uniques = data['Localisation'].unique()

# print(localisations_uniques)

# moyenne par ville des étoiles
moyennes_par_ville = data.groupby('Localisation')['Etoile'].mean()


# Itérer sur les villes uniques et obtenir les coordonnées géographiques correspondantes
for localisation in localisations_uniques:
    # Géocoder l'adresse pour obtenir les coordonnées géographiques
    location = geolocator.geocode(localisation + ', Île-de-France')
    
    if location is not None:
        latitude = location.latitude
        longitude = location.longitude
        
        moyenne_etoiles = moyennes_par_ville[localisation]
        
        if moyenne_etoiles < 2:
            couleur = 'red'
        elif 2 <= moyenne_etoiles < 3:
            couleur = 'bleu'
        elif 3 <= moyenne_etoiles <= 5:
            couleur = 'green'
        else:
            couleur = 'black'
            
        # Créer un marqueur à la position du Pôle Emploi avec le nom de la ville en tant qu'étiquette
        html = f'<span style="color:{couleur}">Pôle Emploi - {localisation}</span>'
        folium.Marker(location=[latitude, longitude], popup='Pôle Emploi - {} \nmoyenne étoiles {}'.format(localisation, moyenne_etoiles)).add_to(map)

# Convertir la carte Folium en HTML
map_html = map._repr_html_()

# # Afficher la carte dans Streamlit
# st.markdown(map_html, unsafe_allow_html=True)

# Afficher la carte
map.save('carte_pole_emploi.html')