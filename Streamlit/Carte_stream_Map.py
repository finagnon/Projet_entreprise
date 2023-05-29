import streamlit as st
import folium
import pandas as pd
from geopy.geocoders import Nominatim

# Charger les données contenant les informations sur les Pôle Emploi en Île-de-France
data = pd.read_csv('C:/Users/sylva/OneDrive/Bureau/scrap_project_MD4/Projet_entreprise/Data/Île-de-France_POLE_EMPLOI_copie.csv', sep=';').head(15)

# Créer une carte centrée sur l'Île-de-France
map = folium.Map(location=[48.8566, 2.3522], zoom_start=10)

# Géocoder les adresses pour obtenir les coordonnées géographiques
geolocator = Nominatim(user_agent='my_app')

for index, row in data.iterrows():
    ville = row['Ville']
    localisation = row['Localisation']
    
    # Géocoder l'adresse pour obtenir les coordonnées géographiques
    location = geolocator.geocode(localisation + ', ' + ville + ', Île-de-France')
    
    if location is not None:
        latitude = location.latitude
        longitude = location.longitude
        
        # Créer un marqueur à la position du Pôle Emploi avec le nom de la ville en tant qu'étiquette
        folium.Marker(location=[latitude, longitude], popup='Pôle Emploi - {}'.format(ville)).add_to(map)

# Convertir la carte Folium en HTML
map_html = map._repr_html_()

# Afficher la carte dans Streamlit
st.markdown(map_html, unsafe_allow_html=True)
