import streamlit as st
import matplotlib.pyplot as plt

def prc_etoile():
    st.markdown("<h2 style='color: #FFFFFF;'>Pourcentage de la Somme des Etoiles</h2>", unsafe_allow_html=True)
    Labels = ["\u2605", '\u2605\u2605', '\u2605\u2605\u2605', '\u2605\u2605\u2605\u2605', '\u2605\u2605\u2605\u2605\u2605']
    sizes = [1305, 104, 131, 154, 616]
    color = ['#ff0000', '#ffa700', '#fff400', '#a3ff00', '#2cba00']

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