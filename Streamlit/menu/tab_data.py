import streamlit as st
import pandas as pd

def tab_data():
    st.markdown("<h2 style='color: #FFFFFF;'>Chargement des données...</h2>", unsafe_allow_html=True)
    data = pd.read_csv('../Data/csv/Île-de-France_POLE_EMPLOI_copie.csv', nrows=2337, sep=';')
    data['Date'] = pd.to_datetime(data['Date'])
    st.write(data)
    
