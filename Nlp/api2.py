from transformers import pipeline
import streamlit as st
import pandas as pd
from prepro import process_data, nlp_function
from tqdm import tqdm
from db import gestDb


# Fonction pour afficher l'en-tête avec le logo
def show_header():
    st.image("../Data/Image/Logo.png", use_column_width=True)
    st.title("CLASSIFICATION D'AVIS")

# Fonction pour afficher le pied de page
def show_footer():
    st.write("---")
    st.write("© 2023 Projet NLP===========>AVIS-----Droit d'Auteur ©")

# Page de sélection du fichier
def select_file():
    show_header()
    # st.title("Sélectionnez un fichier")
    uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv")
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file, sep=';')
        
        # Affichage des données sur une nouvelle page
        show_data(df.head(10))
        
        # Bouton pour traiter le fichier
        if st.button("Traiter le fichier"):
            data_pre= process_data(df)
            data_pre2 = data_pre[ : 10]
            data_pre1 =  classify_data(data_pre2)
            data_pre1 =  classify_data(data_pre2)
            
            # Affichage du résultat sur une nouvelle page
            show_processed_data(data_pre)
            show_classified_data(data_pre1)

            
            #data_pre2 = data_pre[ : 10]
            # Bouton pour classer les avis
            #if st.button("Classer les avis"):
            #data_pre1 =  classify_data(data_pre2)

                #classified_data = classify_data(data_pre)
                # Affichage du résultat sur une nouvelle page
            #show_classified_data(data_pre1)



#Page d'affichage des données
def show_data(df):
    show_header()
    st.title("Données")
    st.write(df)
    #show_footer()

# Page d'affichage du résultat du traitement des données
def show_processed_data(processed_data):
    st.title("Résultat du traitement des données")
    st.write(processed_data)
    


# Page d'affichage du résultat du classement des avis
def show_classified_data(classified_data):
    st.title("Résultat du classement des avis")
    st.write(classified_data.head(10))
    show_footer()

# Fonction pour traiter les données
#def process_data(df):
    # Logique de traitement des données
    #processed_data = df  # Exemple : les données traitées sont identiques à celles d'origine
    
    #return processed_data

# Fonction pour classer les avis
#def classify_data(processed_data):
    #classified_data = nlp_function(processed_data)  # Exemple : les données classifiées sont identiques aux données traitées
    #processed_data["TYPE"] = processed_data["Description"].apply(lambda x: classify_data(x) if len(x) < 700 else None)
    #return processed_data


def classify_data(data):
    distilled_student_sentiment_classifier = pipeline(
        model="lxyuan/distilbert-base-multilingual-cased-sentiments-student",
        return_all_scores=True
    )

    analyzer = pipeline(
        task='text-classification',
        model="cmarkea/distilcamembert-base-sentiment",
        tokenizer="cmarkea/distilcamembert-base-sentiment"
    )

    av = []
    score = []
    tp = []
    publication = []

    for idx, row in tqdm(data.iterrows()):
        avi = row["Description"]
        dt_publi = row["Date de publication"]

        if len(avi) < 700:
            result = analyzer(avi, return_all_scores=True)
            ab = result[0][0]['score'] + result[0][1]['score']
            ab1 = result[0][2]['score']
            ab2 = result[0][3]['score'] + result[0][4]['score']

            if ab > ab1 and ab > ab2:
                print("{} ===================> {}".format(avi, ab))
                av.append(avi)
                score.append(ab)
                tp.append('Negatif')
                publication.append(dt_publi)
            elif ab > ab1 and ab < ab2:
                print("{} ===================> {}".format(avi, ab2))
                av.append(avi)
                score.append(ab2)
                tp.append('Positif')
                publication.append(dt_publi)
            elif ab1 > ab and ab1 > ab2:
                print("{} ===================> {}".format(avi, ab1))
                av.append(avi)
                score.append(ab1)
                tp.append('Neutre')
                publication.append(dt_publi)
            elif ab2 > ab and ab2 > ab1:
                print("{} ===================> {}".format(avi, ab2))
                av.append(avi)
                score.append(ab2)
                tp.append('Positif')
                publication.append(dt_publi)

    Data = {'Date de publication': publication, 'AVI': av, 'SCORE': score, 'TYPE': tp}
    df = pd.DataFrame(Data)
    df.to_csv("avi.csv")
    return df



# Fonction principale pour exécuter l'application
def main():
    st.set_page_config(page_title="CLASSIFICATION D'AVIS")
    
    # Page de sélection du fichier
    select_file()


if __name__ == "__main__":
    main()
