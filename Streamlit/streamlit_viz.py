import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopy.geocoders as geocoders
from geopy.extra.rate_limiter import RateLimiter
import geopandas as gpd

st.title('Tableau de bord - Projet Entreprise')
st.markdown("<h2 style='color: blue;'>Les Etoiles</h2>", unsafe_allow_html=True)

Labels = ['1 étoile', '2 étoiles', '3 étoiles','4 étoiles','5 étoiles']
sizes = [1305, 104,131, 154, 616]
color = ['#ff0000', '#ffa700', '#fff400', '#a3ff00', '#2cba00']
explode = (0.05,0.05,0.05,0.05)


fig1, ax1 = plt.subplots()
ax1.pie(sizes, colors = color, labels=Labels, autopct='%1.1f%%', startangle=90)
#draw circle
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')  
plt.tight_layout()
st.pyplot(fig)

# df = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(df)


DATE_COLUMN = 'Date'

@st.cache_data
def load_data(nrows):
    data = pd.read_csv('../Data/Île-de-France_POLE_EMPLOI_copie.csv', nrows=nrows, sep=';')
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Chargement données...')
data = load_data(2337)
data_load_state.text("chargement terminé")

if st.checkbox('Afficher Tableau données'):
    st.subheader('Les Données')
    st.write(data)

st.subheader('Nombre Etoiles par période')
etoiles_sum = data.groupby('Date')['Etoile'].sum()

periodes = etoiles_sum.index
etoiles = etoiles_sum.values

fig = plt.figure()
plt.plot(periodes, etoiles, label='NOmbre Etoiles')
plt.xlabel('Périodes')
plt.ylabel('Somme des étoiles')
plt.legend()
st.pyplot(fig)




# Charger le second dataframe avec les colonnes "Ville", "Nombre_service" et "Periode"
df = pd.read_csv("../Data/ile-de-France_Nbre_service.csv", sep=';')


# # Géocoder les noms de villes en utilisant geopandas
# gdf = gpd.tools.geocode(df["Ville"], provider="nominatim", user_agent="my_app")

# # Ajouter les colonnes de latitude et de longitude au DataFrame d'origine
# df["Latitude"] = gdf["geometry"].y
# df["Longitude"] = gdf["geometry"].x




st.subheader('Évolution des services par ville et par périodes')





# Créer le graphique
fig, ax = plt.subplots()

# Parcourir chaque ville
for ville in df["Ville"].unique():
    data = df[df["Ville"] == ville]
    ax.plot(data["Période"], data["Nombre de services"], label=ville)

# Configurer les étiquettes des axes et la légende
ax.set_xlabel("Période")
ax.set_ylabel("Nombre de services")
ax.legend()

# Afficher le graphique
plt.show()




# data = pd.read_csv('C:/Users/sylva/OneDrive/Bureau/scrap_project_MD4/Projet_entreprise/Data/Île-de-France_POLE_EMPLOI_copie.csv', sep=';')
# # Calculer le nombre de services par secteur, ville et nombre d'étoiles
# result = data.groupby(["Ville", "Etoile"]).agg({"Services": "count", "Date": lambda x: f"{x.min()} - {x.max()}"}).reset_index()
# result = result.rename(columns={"Services": "Nombre de services", "Date": "Période"})

# Créer le graphique
# fig, ax = plt.subplots()

# # Parcourir chaque ville
# for ville in result["Ville"].unique():
#     data = result[result["Ville"] == ville]
#     ax.plot(data["Période"], data["Nombre de services"], label=ville)

# # Configurer les étiquettes des axes et la légende
# ax.set_xlabel("Période")
# ax.set_ylabel("Nombre de services")
# ax.legend()

# # Afficher le graphique
# plt.show()


DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)