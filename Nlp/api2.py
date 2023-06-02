#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 14:27:55 2023

@author: finagnon
"""
from transformers import pipeline
from show_me import * 
import pandas as pd
from nlp import*
from prepro import *
from tqdm import tqdm
from diff import *




# Page de sélection du fichier
def select_file():
    show_header()
    st.title("Sélectionnez un fichier")
    uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv")
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file, sep=',')
        df =filter_data(df)
        # Affichage des données sur une nouvelle page
        show_data(df.head(10))
        
        # Bouton pour traiter le fichier
        if st.button("Traiter le fichier"):
            data_pre= process_data(df)
            #data_pre2 = data_pre[ : 10]
            #data_pre1 =  classify_data(data_pre2)
            data_pre1 =  classify_data(data_pre)

            df1 = negatif_avis(data_pre1)
            df2 = positif_avis(data_pre1)
            
            df1["Label"] = df1['Avis'].apply(assign_label)
            df3 = df1.groupby(["Ville","Label"]) 
            df4 = df3['Label'].count()
            df4.to_csv('label_ville.csv')
            # Affichage du résultat sur une nouvelle page
            #show_processed_data(data_pre)
            show_classified_data(data_pre1)
            show_processed(df1)
            show_processed_p(df2)
