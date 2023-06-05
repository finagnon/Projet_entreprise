from PIL import Image
import streamlit as st

def accueil():
    # Charger et afficher l'image 
    # image_pole_emploi = Image.open("../Data/Image/Logo.png")    
    # st.image(image_pole_emploi, use_column_width=True)    
    
    st.markdown("<h1 style='color: blue;'>Tableau de Bord</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='color: #000000;'>Bienvenue dans Projet Entreprise</h2>", unsafe_allow_html=True)
    
    # Charger et afficher l'image 
    # image_icon = Image.open("../Data/Image/images.jpeg")      
    # width, height = 250, 250
    # image_icon_resized = image_icon.resize((width, height))
    
    # st.image(image_icon_resized)
    
    # image1 = Image.open("C:/Users/sylva/OneDrive/Bureau/scrap_project_MD4/Projet_entreprise/Data/Image/Logo-Pôle-Emploi.png")
    # st.image(image1, use_column_width=True)
