import streamlit as st


# Fonction pour afficher l'en-tête avec le logo
def show_header():
    st.image("Image/Logo.png", use_column_width=True)
    st.title("CLASSIFICATION D'AVIS")

# Fonction pour afficher le pied de page
def show_footer():
    st.write("---")
    st.write("© 2023 Projet NLP===========>AVIS-----Droit d'auteur ©")



#Page d'affichage des données
def show_data(df):
    st.title("Données")
    st.write(df)
    

# Page d'affichage du résultat du traitement des données
def show_processed_data(processed_data):
    st.title("Résultat du traitement des données")
    st.write(processed_data)
    



# Page d'affichage du résultat du traitement des données negatif
def show_processed(processed_data):
    st.title("Avis négatifs et problèmes évoqués")
    st.write(processed_data)
    

# Page d'affichage du résultat du traitement des données positif
def show_processed_p(processed_data):
    st.title("Avis positifs")
    st.write(processed_data)
    show_footer()
    




# Page d'affichage du résultat du classement des avis
def show_classified_data(classified_data):
    st.title("Résultat du classement des avis")
    st.write(classified_data.head(10))
   
