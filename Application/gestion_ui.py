# Workspace related
from BibliSqlPython.fonctions_sql import *

BASETABLE = ''
CURSEUR = {}

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

