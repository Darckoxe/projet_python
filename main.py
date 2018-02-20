#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
import csv


conn = mysql.connector.connect(host="localhost",user="root",password="root", database="python_td2")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS activite (
    id int AUTO_INCREMENT PRIMARY KEY NOT NULL,
    comInsee varchar(255) NOT NULL,
    comLib varchar(255) NOT NULL,
    equId varchar(255) NOT NULL,
    equNbEquiIdentique varchar(255)NOT NULL,
    actCode varchar(255) NOT NULL,
    actLib varchar(255) NOT NULL,
    equActPraticable varchar(255) NOT NULL,
    equActPratique varchar(255) NOT NULL,
    equActSalleSpe varchar(255) NOT NULL,
    actNiveauLib varchar(255) NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS equipement (
    id int AUTO_INCREMENT PRIMARY KEY NOT NULL,
    comInsee varchar(255) NOT NULL,
    comLib varchar(255) NOT NULL,
    insNumeroInstall varchar(255) NOT NULL,
    insNom varchar(255)NOT NULL,
    equId varchar(255) NOT NULL,
    equNom varchar(255) NOT NULL,
    equNbEquiIdentique varchar(255) NOT NULL,
    equTypeCode varchar(255) NOT NULL,
    equTypeLib varchar(255) NOT NULL,
    longitude varchar(255) NOT NULL,
    latitude varchar(255) NOT NULL,
    dateCreation varchar(255) NOT NULL,
    dateMaj varchar(255) NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS installation (
    id int AUTO_INCREMENT PRIMARY KEY NOT NULL,
    nomInstallation varchar(255) NOT NULL,
    numInstallation varchar(255) NOT NULL,
    comLib varchar(255) NOT NULL,
    comInsee varchar(255)NOT NULL,
    codePostal varchar(255) NOT NULL,
    nomLieuDit varchar(255) NOT NULL,
    numVoie varchar(255) NOT NULL,
    nomVoie varchar(255) NOT NULL,
    longitude varchar(255) NOT NULL,
    latitude varchar(255) NOT NULL,
    dateCreation varchar(255) NOT NULL,
    dateMaj varchar(255) NOT NULL
);
""")


with open('csv/extrait_activite.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    numero_ligne = 0

    for row in spamreader:
        if(numero_ligne != 0) :
            data = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
            cursor.execute("""INSERT INTO activite (comInsee, comLib, equId, equNbEquiIdentique, actCode, actLib, equActPraticable, equActPratique, equActSalleSpe, actNiveauLib) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",row)
            conn.commit()
        numero_ligne = numero_ligne +1

with open('csv/extrait_equipement.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
    numero_ligne = 0

    for row in spamreader:
        if(numero_ligne != 0) :
            data = (row[0], row[1], row[2], row[3], row[4], row[5], row[7], row[8], row[9], row[179], row[180], row[181], row[182])
            print data
            cursor.execute("""INSERT INTO equipement (comInsee, comLib, insNumeroInstall, insNom, equId, equNom, equNbEquiIdentique, equTypeCode, equTypeLib, longitude, latitude, dateCreation, dateMaj) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",data)
            conn.commit()
        numero_ligne = numero_ligne +1

with open('csv/extrait_installation.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    numero_ligne = 0

    for row in spamreader:
        if(numero_ligne != 0) :
            data = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[9], row[10], row[31], row[32])
            print data
            cursor.execute("""INSERT INTO installation (nomInstallation, numInstallation, comLib, comInsee, codePostal, nomLieuDit, numVoie, nomVoie, longitude, latitude, dateCreation, dateMaj) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",data)
            conn.commit()
        numero_ligne = numero_ligne +1

conn.close()


# cursor.execute("""SELECT id, comInsee, comLib FROM activite WHERE id = %s""", ("1", ))
# rows = cursor.fetchall()
# for row in rows:
#    print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))
