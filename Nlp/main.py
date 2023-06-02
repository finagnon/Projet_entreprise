
#from  api2 import api2
from api2 import *
import streamlit as st

# Fonction principale pour exécuter l'application
def main():

    st.set_page_config(page_title= "CLASSIFICATION D'AVIS")
    
    # Page de sélection du fichier
    select_file()


if __name__ == "__main__":
    main()
