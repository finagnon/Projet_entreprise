import streamlit as st
import matplotlib.pyplot as plt

def prc_etoile():
    st.markdown("<h2 style='color: #000000;'>Somme des Etoiles en %</h2>", unsafe_allow_html=True)
    st.markdown("La répartition en pourcentage des différentes catégories d'étoiles. Les résultats montrent que 1 étoile représente 56,5% dépassant la moyenne. Ce graphique met en évidence la prédominance de la catégorie 1 étoile. ", unsafe_allow_html=True)
    Labels = ["\u2605", '\u2605\u2605', '\u2605\u2605\u2605', '\u2605\u2605\u2605\u2605', '\u2605\u2605\u2605\u2605\u2605']
    sizes = [1305, 104, 131, 154, 616]
    color = ['#ff0000', '#ffa700', '#fff400', '#a3ff00', '#2cba00']

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, colors=color, labels=Labels, autopct='%1.1f%%', startangle=90)
    
    # Cercle de dessin
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    
    # Le rapport hauteur / largeur égal garantit que la tarte est dessinée sous forme de cercle
    ax1.axis('equal')
    plt.tight_layout()
    st.pyplot(fig)  