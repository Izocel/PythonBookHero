# Workspace related
from mysql.connector import cursor
from BibliSqlPython.fonctions_sql import *


def verif_connection_usager(**user_credentials) -> bool:

    if 'courriel' in user_credentials:
        courriel = user_credentials['courriel']

    if 'hashmotpasse' in user_credentials:
        mdp_hash = user_credentials['hashmotpasse']

    if(courriel and mdp_hash):
        global CURSEUR
        global BASETABLE

        BASETABLE = 'usagers'
        quer = select_data_querry(BASETABLE, 'id', "where courriel = %s and mot_de_passe = %s",'','','limit 1')

        CURSEUR.execute(quer, (courriel,mdp_hash) )
        usager = CURSEUR.fetchone()
        return usager

    return False

def mysql_app_insert_user() -> None:
    global BASETABLE
    global CURSEUR
    BASETABLE = 'usagers'

    usagers = list_data(BASETABLE)

    if(len(usagers) == 0):

        data_usager = [
            ['Dumoulin', 'Bob', 13, 'triangle1232009@Hotmail.com', 'qwerty123'],
            ['Dumoulin', 'John', 18, 'whateverid@Hotmail.com', 'qwerty456'],
            ['Dumoulin', 'Lulu', 21, 'imashutthisoff@ny.com', 'qwerty789'],
            ['Dumoulin', 'Allan', 32, 'momoiscool@Hotmail.com', 'qwerty159'],
        ]

        for passwordAt in data_usager:
            passwordAt[4] = hash_sha2_data([passwordAt[4]])[0]

        champs = ['nom', 'prenom', 'age', 'courriel', 'mot_de_passe'] 

        builder = insertion_querry(BASETABLE, data_usager, champs)
        CURSEUR.executemany(builder['sql'], builder['val'])
        CURSEUR.reset()


def mysql_app_create_tables() -> None:
    global CURSEUR
    BD = get_config('database')

    # BASE DE DONNÉE
    sql = "CREATE DATABASE IF NOT EXISTS " + BD
    CURSEUR.execute(sql)
    CURSEUR.reset()

    sql = "USE " + BD
    CURSEUR.execute(sql)
    CURSEUR.reset()
    
    # TABLE USAGERS
    sql = '''CREATE TABLE IF NOT EXISTS usagers(
    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    prenom VARCHAR(50) NOT NULL,
    nom VARCHAR(50) NOT NULL,
    age TINYINT(3),
    courriel VARCHAR(255) NOT NULL,
    mot_de_passe VARCHAR(512) NOT NULL
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
    date_partie DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usager) REFERENCES usagers(id),
    FOREIGN KEY (id_livre) REFERENCES livres(id),
    FOREIGN KEY (id_chapitre) REFERENCES chapitres_livres(id)
    )'''
    CURSEUR.execute(sql)
    CURSEUR.reset()


def mysql_app_connection(config_input:dict = {}, autocommit:bool = False) -> cursor:

    global CURSEUR
    CURSEUR = connect_to_mysql(config_input, autocommit)
    return CURSEUR

def mysql_app_disconnection() -> bool:
    global CURSEUR
    CURSEUR.reset()
    CURSEUR = {}
    return disconnect_from_mysql()

def list_data(table) -> List[List[Any]]:
    querry = select_data_querry(table)
    CURSEUR.execute(querry)
    list = fetch_CURSEUR(CURSEUR, False)
    return list

def inserer_chapitres_livres() -> None:
    global CURSEUR
    global BASETABLE

    deja_present = list_data('chapitres_livres')

    if( len(deja_present) == 0 ):

        path =  os.path.dirname(os.path.abspath(__file__))

        fichier_chapitre = open(f"{path}/Livres/Livre1/Introduction.html", "rt", encoding='utf8')
        txt = fichier_chapitre.read()
        func = f"SELECT insertion_chapitre(1, 0,{txt})"
        CURSEUR.execute(func)
        fetch_CURSEUR(CURSEUR)

        fichier_chapitre = open(f"{path}/Livres/Livre2/Introduction.html", "rt", encoding='utf8')
        txt = fichier_chapitre.read()
        func = f"SELECT insertion_chapitre(2, 0,{txt})"
        CURSEUR.execute(func)
        fetch_CURSEUR(CURSEUR)

        i = 1
        for j in range(5):
            fichier_chapitre = open(f"{path}/Livres/Livre1/Chapitre0{i}.html", "rt", encoding='utf8')
            txt = fichier_chapitre.read()
            func = f"SELECT insertion_chapitre(1, {i},{txt})"
            CURSEUR.execute(func)
            fetch_CURSEUR(CURSEUR)

            fichier_chapitre = open(f"{path}/Livres/Livre2/Chapitre0{i}.html", "rt", encoding='utf8')
            txt = fichier_chapitre.read()
            func = f"SELECT insertion_chapitre(2, {i},{txt})"
            CURSEUR.execute(func)
            fetch_CURSEUR(CURSEUR)
            i+= 1


def inserer_livres() -> None:
    global CURSEUR
    global BASETABLE
    BASETABLE = 'livres'

    data = list_data(BASETABLE)

    if(len(data) == 0):
        data = [
            ['Les Maître Des Ténèbres', 'esbf123456789', 'Joe Dever et Gary Chalk'],
            ['Les Maître Des Ténèbres II', 'e234dfg877789', 'Joe Dever et Gary Chalk'],
            ['Les Maître Des Ténèbres III', '11d4dkvl67789', 'Joe Dever et Gary Chalk'],
            ['Les Maître Des Ténèbres IV', 'edkfws09ki54789', 'Joe Dever et Gary Chalk']
        ]
        champs = ['titre', 'isbn', 'auteur']

        builder = insertion_querry(BASETABLE, data, champs) 
        CURSEUR.executemany(builder['sql'], builder['val'])
        CURSEUR.reset()

def lister_chapitre(livre:int = 1):
    global CURSEUR
    global BASETABLE
    BASETABLE = 'chapitres_livres'
    select_chapitres = select_data_querry(BASETABLE, "*", "", "ORDER BY numero")
    CURSEUR.execute(select_chapitres)
    chapitres = fetch_CURSEUR(CURSEUR)

    return chapitres


def liste_livre_usager(usager_id:int) -> List[List]:
    global CURSEUR
    
    q = "SELECT livres.id,titre,auteur FROM permission_livres_usagers "
    q += "INNER JOIN livres ON id_livre = livres.id "
    q += f"WHERE id_usager = {usager_id} ORDER BY id;"

    CURSEUR.execute(q)
    return fetch_CURSEUR(CURSEUR)


def lister_sauvegardes_usager(usager_id:int) -> List[List]:
    global CURSEUR

    q = "SELECT id_chapitre, numero, page, date_partie, titre, livres.id FROM sauvegardes_parties "
    q += "INNER JOIN chapitres_livres ON id_chapitre = chapitres_livres.id "
    q += "INNER JOIN livres ON chapitres_livres.id_livre = livres.id "
    q += f"WHERE id_usager = {usager_id} "
    q += "ORDER BY date_partie DESC;"

    CURSEUR.execute(q)
    return fetch_CURSEUR(CURSEUR)


# acheter_livre_usager(usager_id int, livre_id int) RETURNS TINYINT(1)
def attribuer_livre_par_default() -> int:

    users = list_data('usagers')
    lepremierlivredanslistedelatable = list_data('livres')[0][0]

    resultat = 0
    for user in users:

        func = f"SELECT acheter_livre_usager ({user[0]}, {lepremierlivredanslistedelatable});" 
        CURSEUR.execute(func)
        r = fetch_CURSEUR(CURSEUR)
        if(r != 0 and resultat == 0):
            resultat = 0

    return resultat

def field_fenetre_chapitre(index:int) -> List[List[Any]]:
    global CURSEUR
    global BASETABLE
    BASETABLE = 'chapitres_livres'
    querry = select_data_querry(BASETABLE, "*", f"WHERE numero = {index}", "ORDER BY numero")
    CURSEUR.execute(querry)
    return fetch_CURSEUR(CURSEUR)