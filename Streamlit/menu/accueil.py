from PIL import Image
import streamlit as st

def accueil():
    # Charger et afficher l'image 
<<<<<<< HEAD
    image_pole_emploi = Image.open("../Data/Image/Logo.png")    
    st.image(image_pole_emploi, use_column_width=True)    
    st.markdown("<h1 style='color: #FFFFFF;'>Bienvenue dans Projet Entreprise</h1>", unsafe_allow_html=True)
    
    # Charger et afficher l'image 
    image_icon = Image.open("../Data/Image/images.jpeg")      
    width, height = 250, 250
    image_icon_resized = image_icon.resize((width, height))
    st.image(image_icon_resized)
    
    # image1 = Image.open("C:/Users/sylva/OneDrive/Bureau/scrap_project_MD4/Projet_entreprise/Data/Image/Logo-Pôle-Emploi.png")
    # st.image(image1, use_column_width=True)
=======
    image_RF = Image.open("Streamlit/Image/RF.png")      
    width, height = 100, 100
    image_RF_resized = image_RF.resize((width, height))
    st.image(image_RF_resized)

    image_pole_emploi = Image.open("Streamlit/Image/Logo-Pôle-Emploi.png")
    st.image(image_pole_emploi, use_column_width=True)
    st.markdown("<h1 style='color: #191970;'>Bienvenue dans Projet Entreprise</h1>", unsafe_allow_html=True)
    # pass
>>>>>>> main
