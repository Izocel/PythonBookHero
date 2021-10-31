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
    sql = '''CREATE TABLE IF NOT EXISTS usagers(
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    nom VARCHAR(50) NOT NULL,
    age TINYINT(3),
    courriel VARCHAR(255) NOT NULL,
    mot_de_passe VARCHAR(312) NOT NULL
    )'''
    CURSEUR.execute(sql)
    CURSEUR.reset()

    # TABLE LIVRES
    sql = '''CREATE TABLE IF NOT EXISTS livres(
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    titre VARCHAR(150) NOT NULL,
    isbn VARCHAR(255) NOT NULL,
    auteur VARCHAR(255) NOT NULL
    )'''
    CURSEUR.execute(sql)
    CURSEUR.reset()

    # TABLE CHAPITRES_LIVRES
    sql = '''CREATE TABLE IF NOT EXISTS chapitres_livres(
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    id_livre INT NOT NULL,
    numero tinyint(4) NOT NULL,
    contenue TEXT NOT NULL,
    FOREIGN KEY (id_livre) REFERENCES livres(id)
    )'''
    CURSEUR.execute(sql)
    CURSEUR.reset()

    # TABLE PERMISSIONS_LIVRES_USAGERS
    sql = '''CREATE TABLE IF NOT EXISTS permission_livres_usagers(
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    id_usager INT NOT NULL,
    id_livre INT,
    FOREIGN KEY (id_usager) REFERENCES usagers(id),
    FOREIGN KEY (id_livre) REFERENCES livres(id)
    )'''
    CURSEUR.execute(sql)
    CURSEUR.reset()

    # TABLE SAUVEGARDES_PARTIES
    sql = '''CREATE TABLE IF NOT EXISTS sauvegardes_parties(
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    id_usager INT NOT NULL,
    id_livre INT NOT NULL,
    id_chapitre INT NOT NULL,
    page TINYINT(8),
    FOREIGN KEY (id_usager) REFERENCES usagers(id),
    FOREIGN KEY (id_livre) REFERENCES livres(id),
    FOREIGN KEY (id_chapitre) REFERENCES chapitres_livres(id)
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

def inserer_chapitres_livres():
    global CURSEUR
    global BASETABLE
    BASETABLE = 'chapitres_livres'

    querry = select_data_querry(BASETABLE)
    CURSEUR.execute(querry)
    data = fetch_CURSEUR(CURSEUR)

    if(len(data) == 0):

        data = [
            [1, 1, "aaaaaaaaaaa"],
            [1, 2, 'bbbbbbbbbbbbbbb'],
            [1, 3, 'cccccccccccccc'],
            [1, 4, 'ddddddddddddddd'],
            [1, 5, 'eeeeeeeeeeeeeee'],
            [1, 6, 'ffffffffffffffff'],
            [1, 7, 'ggggggggggggggggggg'],
            [1, 8, 'hhhhhhhhhhhhhhhhhh'],
            [1, 9, 'iiiiiiiiiiiiiiiiiii'],
            [1, 10, 'jjjjjjjjjjjjjjjjjj'] 
        ]
        champs = ['id_livre', 'numero', 'contenue']

        builder = insertion_querry(BASETABLE, data, champs) 
        CURSEUR.executemany(builder['sql'], builder['val'])
        CURSEUR.reset()

def inserer_livres():
    global CURSEUR
    global BASETABLE
    BASETABLE = 'livres'

    querry = select_data_querry(BASETABLE)
    CURSEUR.execute(querry)
    data = fetch_CURSEUR(CURSEUR)

    if(len(data) == 0):
        data = [
            ['Les Maître des Ténèbres', 'esbf123456789', 'Joe Dever'],
            ['Les Maître des Ténèbres II', 'e234dkvl67789', 'Joe Dever']
        ]
        champs = ['titre', 'isbn', 'auteur']

        builder = insertion_querry(BASETABLE, data, champs) 
        CURSEUR.executemany(builder['sql'], builder['val'])
        CURSEUR.reset()

def lister_chapitre(livre:int = 1):
    global CURSEUR
    global BASETABLE
    BASETABLE = 'chapitres_livres'
    select_chapitres = select_data_querry(BASETABLE)
    CURSEUR.execute(select_chapitres)
    chapitres = fetch_CURSEUR(CURSEUR)

    return chapitres