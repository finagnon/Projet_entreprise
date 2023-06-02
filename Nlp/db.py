#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 08:32:27 2023

@author: finagnon
"""

import csv
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def gestDb(file):
    # Création de la base de données
    engine = create_engine('sqlite:///AVI.db', echo=True)
    Base = declarative_base()

    class Avi(Base):
        __tablename__ = 'avi'
        id = Column(Integer, Autoincrement=True, primary_key=True)
        date_publication = Column(Date)
        AVI = Column(String)
        SCORE = Column(Float)
        VILLE = Column(String)
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
            avis_table = Avi(date_publication=row['Date de publication'], AVI=row['Avis'], SCORE=row['Score'], VILLE=row['Ville'],
                             TYPE=row['Type'])
            existing_avi = session.query(Avi).filter_by(AVI=row['Avis']).first()
            if not existing_avi:
                session.add(avis_table)
                session.commit()
                print(f"L'avi avec l'ID {row['id']} a été ajouté à la base de données.")
            else:
                print(f"L'avi {row['Avis']} est déjà présent dans la base de données et ne sera pas ajouté.")

    # Fermeture de la session
    session.close()
