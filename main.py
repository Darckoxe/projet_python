#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
import csv


conn = mysql.connector.connect(host="localhost",user="root",password="root", database="python_td2")
cursor = conn.cursor()

print("Bonjour")

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

with open('csv/testsql.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        data = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
        cursor.execute("""INSERT INTO activite (comInsee, comLib, equId, equNbEquiIdentique, actCode, actLib, equActPraticable, equActPratique, equActSalleSpe, actNiveauLib) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",row)
        conn.commit()

conn.close()
