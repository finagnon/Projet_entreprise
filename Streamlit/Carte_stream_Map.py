import streamlit as st
import folium
import pandas as pd
from geopy.geocoders import Nominatim

# Charger les données contenant les informations sur les Pôle Emploi en Île-de-France
data = pd.read_csv('../Data/csv/Île-de-France_POLE_EMPLOI_copie.csv', sep=';')

# Créer une carte centrée sur l'Île-de-France
map = folium.Map(location=[48.8566, 2.3522], zoom_start=12)

# Géocoder les adresses pour obtenir les coordonnées géographiques
geolocator = Nominatim(user_agent='my_app')

# Obtenir les villes uniques et les localisations uniques
localisations_uniques = data['Localisation'].unique()

couleurs_legende = {
    'Moins de 2': 'red',
    'De 2 à 3': 'blue',
    'De 3 à 5': 'green',
    'Plus de 5': 'yellow'
}

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
            couleur = 'blue'
        elif 3 <= moyenne_etoiles <= 5:
            couleur = 'green'
        else:
            couleur = 'yellow'
            
        folium.Marker(
            location=[latitude, longitude],
            # radius=5,
            color=couleur,
            icon=folium.Icon(color=couleur),
            fill=True,
            # fill_color=couleur,
            popup='Pôle Emploi - {} \nmoyenne étoiles {:.2f}'.format(localisation, moyenne_etoiles)
        ).add_to(map)
    
# Créer un marqueur circulaire à la position du Pôle Emploi avec le nom de la localisation en tant qu'étiquette
# for legende, couleur in couleurs_legende.items():
#     folium.Marker(
#         location=[48.8566, 2.3522],  # Coordonnées arbitraires
#         icon=folium.Icon(color=couleur),
#         popup=legende
#     ).add_to(map)

        
# Convertir la carte Folium en HTML
map_html = map._repr_html_()

# # Afficher la carte dans Streamlit
# st.markdown(map_html, unsafe_allow_html=True)

# Afficher la carte
map.save('carte_pole_emploi.html')