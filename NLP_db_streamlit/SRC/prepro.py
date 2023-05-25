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
nltk.download('punkt')
import neattext.functions as nfx




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
                
        df["Description"]=df["Description"].apply(nfx.remove_userhandles)
        df["Description"]=df["Description"].apply(nfx.remove_phone_numbers)
        df["Description"]=df["Description"].apply(nfx.remove_emails)
        df["Description"]=df["Description"].apply(nfx.remove_stopwords)
        df["Description"]=df["Description"].apply(nfx.remove_special_characters)

        
        
        return df
"""
def nlp_function(data):
         
        #df_zip =dict(zip(avs, dt_publi))
      #  processed = [avs,dt_publi,df_zip]
        Data =data[0]
        df_z = data[2]
        av =[]
        score = []
        tp = []
        publication =[]
        analyzer = pipeline(
    task='text-classification',
    model="cmarkea/distilcamembert-base-sentiment",
    tokenizer="cmarkea/distilcamembert-base-sentiment"
)
        for avi in tqdm(Data):  
                if len(avi) < 700:
                        data["TYPE"] = data["Description"].apply(lambda x, )
                        result = analyzer(avi, return_all_scores=True)
                        ab = result[0][0]['score'] + result[0][1]['score']
                        ab1 = result[0][2]['score']
                        ab2 = result[0][3]['score'] + result[0][4]['score']
                        if ab > ab1 and ab > ab2:
                                print("{}===================> {}".format(avi, ab))
                                av.append(avi)
                                score.append(ab)
                                tp.append('Negatif')
                                publication.append(df_z[avi])
                                
                  
                        elif ab > ab1 and ab < ab2:
                                print("{}===================> {}".format(avi, ab2))
                                av.append(avi)
                                score.append(ab2)
                                tp.append('Positif')
                                publication.append(df_z[avi])

                        elif ab1 > ab and ab1 > ab2: 
                                        print("{}===================> {}".format(avi, ab1))
                                        av.append(avi)
                                        score.append(ab1)
                                        tp.append('Neutre')
                                        publication.append(df_z[avi])

                        elif ab2 > ab and ab2 > ab1:
                                        print("{}===================> {}".format(avi, ab2))
                                        av.append(avi)
                                        score.append(ab2)
                                        tp.append('Positif')
                                        publication.append(df_z[avi])
        
        
        data1 = {"Date de publication":publication, 'AVI':av,'SCORE':score, 'TYPE':tp}
        df = pd.DataFrame(data1)
        df1=df.to_csv("avi.csv")
        data2 = [df, df1]
        return data2
"""

def nlp_function(avi):

         #Negatif ='Negatif'
         #Positif ='Positif'
         #Neutre =' Neutre'
        #df_zip =dict(zip(avs, dt_publi))
      #  processed = [avs,dt_publi,df_zip]
        #av= []
        #score = []
        #tp = []
        #publication =[]
        analyzer = pipeline(
    task='text-classification',
    model="cmarkea/distilcamembert-base-sentiment",
    tokenizer="cmarkea/distilcamembert-base-sentiment"
)
        result = analyzer(avi, return_all_scores=True)
        ab = result[0][0]['score'] + result[0][1]['score']
        ab1 = result[0][2]['score']
        ab2 = result[0][3]['score'] + result[0][4]['score']

        if ab > ab1 and ab > ab2:
                                #print("{}===================> {}".format(avi, ab))
                                #av.append(avi)
                                #score.append(ab)
                                return 'Negatif'

                        
        elif ab > ab1 and ab < ab2:
                                #print("{}===================> {}".format(avi, ab2))
                                #av.append(avi)
                                #score.append(ab2)
                                return 'Positif'               
                                
                  
        elif ab1 > ab and ab1 > ab2: 
                                        #print("{}===================> {}".format(avi, ab1))
                                        #av.append(avi)
                                        #score.append(ab1)
                                return 'Neutre'

        elif ab2 > ab and ab2 > ab1:
                                        #print("{}===================> {}".format(avi, ab2))
                                        #av.append(avi)
                                        #score.append(ab2)
                                return 'Positif'
              
                                

                        
        
                
                                        
        
        """
        data1 = {"Date de publication":publication, 'AVI':av,'SCORE':score, 'TYPE':tp}
        df = pd.DataFrame(data1)
        df1=df.to_csv("avi.csv")
        data2 = [df, df1]
        return data2
"""







