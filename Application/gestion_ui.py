# Workspace related
from logging import currentframe
from BibliSqlPython.fonctions_sql import *

BASETABLE = ''
CURSEUR = {}

def mysql_app_create_tables():
    global CURSEUR

    # BASE DE DONNÉE
    sql = "CREATE DATABASE IF NOT EXISTS python_book_hero"
    CURSEUR.execute(sql)
    CURSEUR.reset()

    sql = "USE python_book_hero"
    CURSEUR.execute(sql)
    CURSEUR.reset()
    
    # TABLE USAGERS
    sql = '''CREATE TABLE IF NOT EXISTS Usagers(
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    age TINYINT(3),
    courriel VARCHAR(255) NOT NULL,
    mot_de_passe VARCHAR(312) NOT NULL
    )'''
    CURSEUR.execute(sql)
    CURSEUR.reset()

    # TABLE LIVRES
    sql = '''CREATE TABLE IF NOT EXISTS Livres(
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    titre VARCHAR(150) NOT NULL,
    isbn VARCHAR(255) NOT NULL,
    auteur VARCHAR(255) NOT NULL
    )'''
    CURSEUR.execute(sql)
    CURSEUR.reset()

    # TABLE CHAPITRES_LIVRES
    sql = '''CREATE TABLE IF NOT EXISTS Chapitres_livres(
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    id_livre INT NOT NULL,
    numero tinyint(4) NOT NULL,
    contenue TEXT NOT NULL,
    FOREIGN KEY (id_livre) REFERENCES Livres(id)
    )'''
    CURSEUR.execute(sql)
    CURSEUR.reset()

    # TABLE PERMISSIONS_LIVRES_USAGERS
    sql = '''CREATE TABLE IF NOT EXISTS Permission_livres_usagers(
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    id_usager INT NOT NULL,
    id_livre INT,
    FOREIGN KEY (id_usager) REFERENCES Usagers(id),
    FOREIGN KEY (id_livre) REFERENCES Livres(id)
    )'''
    CURSEUR.execute(sql)
    CURSEUR.reset()

    # TABLE SAUVEGARDES_PARTIES
    sql = '''CREATE TABLE IF NOT EXISTS Sauvegardes_paties(
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    id_usager INT NOT NULL,
    id_livre INT NOT NULL,
    id_chapitre INT NOT NULL,
    page TINYINT(8),
    FOREIGN KEY (id_usager) REFERENCES Usagers(id),
    FOREIGN KEY (id_livre) REFERENCES Livres(id),
    FOREIGN KEY (id_chapitre) REFERENCES Chapitres_livres(id)
    )'''
    CURSEUR.execute(sql)
    CURSEUR.reset()



def mysql_app_connection(config_input:dict = {}, autocommit:bool = False):

    global CURSEUR
    CURSEUR = connect_to_mysql(config_input, autocommit)
    return CURSEUR

def mysql_app_disconnection():
    global CURSEUR
    CURSEUR.reset()
    CURSEUR = {}
    disconnect_from_mysql()
    return True

def list_data(table):
    querry = select_data_querry(table)
    CURSEUR.execute(querry)
    list = fetch_CURSEUR(CURSEUR, True)
    return list

