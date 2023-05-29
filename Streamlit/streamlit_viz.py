import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopy.geocoders as geocoders
from geopy.extra.rate_limiter import RateLimiter
import geopandas as gpd
<<<<<<< HEAD
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

    selected_option = st.sidebar.selectbox("Choisir une option", ["Accueil", "Pourcentages des Etoiles" ,"Tableau de données", "Nombre d'étoiles par période", "Qualité des services par période","Les Score par ville", "Total avis en % par ville","Carte des agences"])


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
        
    elif selected_option == "Qualité des services par période":



# Charger les données depuis le fichier CSV
        df = pd.read_csv('C:/Users/sylva/OneDrive/Bureau/scrap_project_MD4/Projet_entreprise/Data/Île-de-France_Ville.csv', sep=',')

        # Calculer les pourcentages des types d'avis
        total_avis = len(df)
        positifs = len(df[df['Type_Avis'] == 'positif'])
        negatifs = len(df[df['Type_Avis'] == 'negatif'])
        neutres = len(df[df['Type_Avis'] == 'neutre'])

        pourcentages = [positifs/total_avis, negatifs/total_avis, neutres/total_avis]
        labels = ['Positifs', 'Négatifs', 'Neutres']

        # Créer une figure et un axe
        fig, ax = plt.subplots()

        # Tracer le graphique circulaire
        ax.pie(pourcentages, labels=labels, autopct='%1.1f%%')

        # Ajouter une aiguille au centre du graphique
        ax.annotate('', xy=(0.5, 0.5), xytext=(0.5, 0.6), arrowprops=dict(facecolor='black', arrowstyle='-|>'))

        # Ajuster l'aspect du graphique
        ax.set_aspect('equal')

        # Afficher le graphe
        plt.show()


        
    elif selected_option == "Les Score par ville":
        # Charger les données des scores des villes d'Île-de-France
        data = pd.read_csv('C:/Users/sylva/OneDrive/Bureau/scrap_project_MD4/Projet_entreprise/Data/Count_Ville.csv', sep=',')

        # Créer une liste des options de sélection pour le dropdown
        villes = data['Ville'].unique()

        # Sélection de la ville via le dropdown
        selected_ville = st.selectbox('Sélectionner une ville', villes)

        # Filtrer les données pour la ville sélectionnée
        ville_data = data[data['Ville'] == selected_ville]

        # Créer une figure en utilisant le graphique semi-circulaire de Plotly
        fig = go.Figure()

        # Ajouter une trace semi-circulaire pour les performances de la ville sélectionnée
        fig.add_trace(go.Indicator(
            mode="gauge+number",
            value=ville_data['Score'].iloc[0],
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': 'Etude Comparative'},
            gauge={'axis': {'range': [None, 100]},
                'bar': {'color': 'blue'},
                'steps': [{'range': [0, 50], 'color': 'red'},
                            {'range': [50, 70], 'color': 'yellow'},
                            {'range': [70, 100], 'color': 'green'}],
                'threshold': {'line': {'color': 'black', 'width': 4}, 'thickness': 0.75, 'value': ville_data['Score'].iloc[0]}}))

        # Mise en forme du layout du graphique
        fig.update_layout(height=400, width=600, margin=dict(l=20, r=20, t=30, b=20))
        # Afficher le graphique
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


        
=======

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
>>>>>>> 4b92cccc2160f4e3d156647b4cb7ac1944d0559a

def load_data(nrows):
<<<<<<< HEAD
    data = pd.read_csv('C:/Users/sylva/OneDrive/Bureau/scrap_project_MD4/Projet_entreprise/Data/Île-de-France_POLE_EMPLOI_copie.csv', nrows=nrows, sep=';')
    data['Date'] = pd.to_datetime(data['Date'])
    return data

if __name__ == '__main__':
    main()
=======
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
>>>>>>> 4b92cccc2160f4e3d156647b4cb7ac1944d0559a
