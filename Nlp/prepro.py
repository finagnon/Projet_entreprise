#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 11:34:50 2023

@author: finagnon
"""

from transformers import pipeline
#import re
from tqdm import tqdm
import pandas as pd
import nltk
import spacy
from spacy.lang.fr.stop_words import STOP_WORDS
nltk.download('punkt')
import neattext.functions as nfx
import re




#Fonction de lecture du fichier
def  liref(fichier):

        df = pd.read_csv(fichier, sep=';')
        return df



"""
def nlp_pipeline(text):

    text = text.lower()
    text = text.replace('\n', ' ').replace('\r', '')
    text = ' '.join(text.split())
    text = re.sub(r"[A-Za-z\.]*[0-9]+[A-Za-z%°\.]*", "", text)
    text = re.sub(r"(\s\-\s|-$)", "", text)
    text = re.sub(r"[,\!\?\%\(\)\/\"]", "", text)
    text = re.sub(r"\&\S*\s", "", text)
    text = re.sub(r"\&", "", text)
    text = re.sub(r"\+", "", text)
    text = re.sub(r"\#", "", text)
    text = re.sub(r"\$", "", text)
    text = re.sub(r"\£", "", text)
    text = re.sub(r"\%", "", text)
    text = re.sub(r"\:", "", text)
    text = re.sub(r"\@", "", text)
    text = re.sub(r"\-", "", text)

    return text
"""



def process_data(df):
        
        
        avs,dt_publi=[],[]
    # Fonction de traitement de données
                
        df["Commentaires"]=df["Commentaires"].apply(nfx.remove_userhandles)
        df["Commentaires"]=df["Commentaires"].apply(nfx.remove_phone_numbers)
        df["Commentaires"]=df["Commentaires"].apply(nfx.remove_emails)
        #df["Commentaires"]=df["Commentaires"].apply(nfx.remove_stopwords)
        df["Commentaires"]= df["Commentaires"].apply(lambda x: x.lower())

        df["Commentaires"] = df["Commentaires"].map(lambda x : re.sub(r'[^a-zA-Z ]', '', x))

        df["Commentaires"]= df["Commentaires"].apply(lambda x : nfx.remove_stopwords (x))

        df["Commentaires"]=df["Commentaires"].apply(nfx.remove_special_characters)
        df["Commentaires"]=df["Commentaires"].apply(nfx.remove_emojis)
        df["Commentaires"]=df["Commentaires"].apply(nfx.remove_hashtags)
        df["Commentaires"]=df["Commentaires"].apply(nfx.remove_html_tags)
        df["Commentaires"]=df["Commentaires"].apply(nfx.remove_multiple_spaces)
        #df["Description"]=df["Commentaires"].apply(nfx.remove_multiple_spaces)

        pattern = r"\b(\w+(?:-\w+)*)$"
        df["Ville"] = df["Localisation"].str.extract(pattern, expand=False)
        
        return df

#Fonction filtre
def filter_data(data):
    filtered_data = data[~data['Commentaires'].str.contains(r"(gouvernement|grnt|Gouvernement|Macron|président|President|Président|ministre|Ministre|Etat|état)", case=False)]
    return filtered_data




