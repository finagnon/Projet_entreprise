import datetime
from matplotlib import pyplot as plt
import pandas as pd
import streamlit as st


def etoile_periode():
    dfm = pd.read_csv('../Data/csv/Île-de-France_POLE_EMPLOI_copie.csv', sep=';')
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