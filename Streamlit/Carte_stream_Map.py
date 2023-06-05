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
        
        if moyenne_etoiles < 2.5:
            couleur = 'red'
        elif 2.5 <= moyenne_etoiles < 3.5:
            couleur = 'blue'
        elif 3.5 <= moyenne_etoiles <= 5:
            couleur = 'green'
        else:
            pass
            
        marker = folium.Marker(
            location=[latitude, longitude],
            color=couleur,
            icon=folium.Icon(color=couleur),
            fill=True,
            # fill_color=couleur,
            popup='Pôle Emploi - {} \nmoyenne étoiles {:.2f}'.format(localisation, moyenne_etoiles)
        )
        moy = '{:.2f}'.format(moyenne_etoiles)
        folium.Tooltip(localisation+'\n Moyenne des étoiles : '+str(moy)).add_to(marker)
        
        marker.add_to(map)
        # .add_to(map)
    
        
# Ajouter le contrôle de légende en bas de la carte
folium.LayerControl().add_to(map)

# Ajouter la légende en bas de la carte
legende_html = """
<div style="
    position: fixed;
    bottom: 50px;
    left: 50px;
    z-index: 1000;
    font-size: 16px;
    # background-color: white;
    padding: 10px;
    border-radius: 5px;
    border: 1px solid grey;
    background: rgba(255, 255, 255, 0.7);
    ">
    <p><strong>Moyenne des étoiles Pôle emploi:</strong></p>
    <p style="color: red">Moins de 2.5 : Mauvais service</p>
    <p style="color: blue">Entre 2.5 et 3.5 : Moyen service</p>
    <p style="color: #70ad25">Entre 3.5 et 5 : Très bon service</p>
</div>
"""

map.get_root().html.add_child(folium.Element(legende_html))

# Convertir la carte Folium en HTML pour l'aaficher
map_html = map._repr_html_()

# # Afficher la carte dans Streamlit
# st.markdown(map_html, unsafe_allow_html=True)

# Afficher la carte
map.save('carte_pole_emploi.html')