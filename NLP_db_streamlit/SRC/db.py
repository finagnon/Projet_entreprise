#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 08:32:27 2023

@author: finagnon
"""

import csv
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def gestDb(file):
        
        
        # Création de la base de données
        engine = create_engine('sqlite:///AVI.db', echo=True)
        Base = declarative_base()

        class Avi(Base):
                
                __tablename__ = 'avi'
                id = Column(Integer,Autoincrement =True, primary_key=True)
                date_publication = Column(Date)
                AVI = Column(String)
                SCORE = Column(float)
                TYPE = Column(String, unique=True)
     

        # Création des tables dans la base de données
        Base.metadata.create_all(engine)

        # Ouverture d'une session pour interagir avec la base de données
        Session = sessionmaker(bind=engine)
        session = Session()

        # Lecture du fichier CSV et insertion des données dans la base de données
        with open(file, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                        avis_table = Avi(date_publication=row['date_publication'], AVI=row['AVI'], SCORE=row['SCORE'],
                          TYPE=row['TYPE'])
                        if not session.query(Avi).filter_by(AVI=row['AVI']).first():
                                session.add(avis_table)
                                session.commit()
                                print(f"L'avi avec l'ID {row['id']} a été ajouté à la base de données.")
                        else:
                                        
                                print(f"L'avi {row['AVI']} est déjà présent dans la base de données et ne sera pas ajouté.")

        # Fermeture de la session
        session.close()
