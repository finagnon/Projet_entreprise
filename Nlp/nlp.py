import pandas as pd
from transformers import pipeline
from db import gestDb



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
    ville = []

    for idx, row in data.iterrows():
        avi = row["Commentaires"]
        dt_publi = row["Date"]
        vil = row["Ville"]

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
                ville.append(vil)
            elif ab > ab1 and ab < ab2:
                print("{} ===================> {}".format(avi, ab2))
                av.append(avi)
                score.append(ab2)
                tp.append('Positif')
                publication.append(dt_publi)
                ville.append(vil)
            elif ab1 > ab and ab1 > ab2:
                print("{} ===================> {}".format(avi, ab1))
                av.append(avi)
                score.append(ab1)
                tp.append('Neutre')
                publication.append(dt_publi)
                ville.append(vil)
            elif ab2 > ab and ab2 > ab1:
                print("{} ===================> {}".format(avi, ab2))
                av.append(avi)
                score.append(ab2)
                tp.append('Positif')
                publication.append(dt_publi)
                ville.append(vil)

    Data = {'Date de publication': publication, 'Ville': ville, 'Avis': av, 'Score': score, 'Type': tp}
    df = pd.DataFrame(Data)
    df1= df.groupby('Ville')
    df2 = df1["Score"].sum()
    df22=df1["Score"].count()
    df22.to_csv("Count_Ville.csv")
    df1 = pd.DataFrame(df1)
    df1.to_csv("SUM_Ville.csv")
    df22 =pd.DataFrame(df22)
    df2 = pd.DataFrame(df2)
    #regroupement par avi
    df4 = df[df.Type=="Positif"]
    df5 = df[df.Type=="Negatif"]

    df6 = df[df.Type=="Neutre"]

    df44=df4.groupby('Ville')
    df444 = df44['Type'].count()

    df55=df5.groupby('Ville')
    df555 = df55['Type'].count()


    df66=df6.groupby('Ville')
    df666 = df66['Type'].count()
    #Fin regroupement par avi

    #Transformation en CSV
    df444.to_csv("Positif_ville.csv")
    df555.to_csv("Negatif_ville.csv")
    df666.to_csv("Neutre_ville.csv")
    df2.to_csv("Sum_Score.csv")
    vari_db =df.to_csv("avi.csv")
    #gestDb(vari_db)
    print("SUCCESS")

    return df
