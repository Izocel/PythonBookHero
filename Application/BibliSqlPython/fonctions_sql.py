from mysql import connector as _mysqlConnector # Alias
from getpass import getpass
import hashlib

def __init__(self):
    pass

# Mysql Connection class
__MySqlConnType = _mysqlConnector.connection.MySQLConnection


# Variables globales
BD_CONNECTION = {}
BD_CONFIG = {}
CURSEUR = {}
BASETABLE = ''

def get_config(key:str = ''):
    global BD_CONFIG
    if(key == ''):
        return BD_CONFIG
    else:
        return BD_CONFIG[key]


def disconnect_from_mysql():
    global BD_CONNECTION
    global BD_CONFIG
    global CURSEUR

    CURSEUR.reset()
    CURSEUR.close()
    CURSEUR = {}
    
    BD_CONNECTION.disconnect()
    BD_CONNECTION = {}

    BD_CONFIG = {}
    print("\n La session SQL est terminée")
    return True


####-####-####-#### MySQL App Connection ####-####-####-#### 
def connect_to_mysql(config_input:dict = {}, autocommit:bool = False, max_retry:int = 5):

    global BD_CONNECTION
    global BD_CONFIG
    global CURSEUR

    max_retry = 1 if(max_retry == 0) else max_retry
    max_retry = abs(max_retry)
    max_retry = min(max_retry, 15)

    for x in range(max_retry):
        while( type(BD_CONNECTION) is not __MySqlConnType ):
            
            BD_CONFIG = {
                'host' : config_input['host'],
                'user' : config_input['user'],
                'password' : config_input['password'],
                'database' : '',
                'autocommit': autocommit
            }

            #TODO:.dontDieOnBadInfosPlz()
            BD_CONNECTION = _mysqlConnector.connect(**BD_CONFIG)
            config_warning(BD_CONNECTION)
    BD_CONFIG['database'] =  'python_book_hero'
    CURSEUR = BD_CONNECTION.cursor()
    print("\n La session SQL est établie")
    return CURSEUR


def config_warning( connection ):

    autocommit = connection.autocommit

    if( autocommit == False):
        print("\n\n'Autocommit' est: " + str(autocommit) )
        print("Les transactions ne seront pas automatiquement soumissent au LGBD...")
        print("Des confirmations vous seront demandées lors d'insertions/suppressions/modifications.\n")
    else:
        print("\n\n!!!!! Attention 'Autocommit' est: " + str(autocommit) + " !!!!!")
        print("Les transactions seront automatiquement soumissent au LGBD...\n")


def show_databases_querry():
    querry = "SHOW DATABASES;"
    return querry

def show_tables_querry(database):
    querry = "SHOW TABLES FROM " + database
    return querry

def select_data_querry(table:str, fields:str = '*', where:str = '', order:str = '', group:str = '',  limit:str = ''):
    querry = "SELECT "+ fields + " FROM " + table

    if(where != ''):
        querry += " " + where

    if(order != ''):
        querry += " " + order

    if(group != ''):
        querry += " " + group

    if(limit != ''):
        querry += " " + limit

    return querry

def select_colum_name_type_querry(table, database):

    querry = "SELECT COLUMN_NAME,COLUMN_TYPE FROM INFORMATION_SCHEMA.COLUMNS "
    querry +="WHERE TABLE_SCHEMA='" + database +"' AND TABLE_NAME='" + table + "';"
    return querry

def CURSEUR_name_and_type(CURSEUR, table, database):
    
    tpye_and_colum_querry = select_colum_name_type_querry(table, database)
    CURSEUR.execute(tpye_and_colum_querry)

    table_resultat = []
    table_type = []
    table_col = []
    for(col, col_type) in CURSEUR:

        col_type_format = str(col_type).replace("'", '').replace("b", '')
        table_resultat.append( (col, col_type_format) )
        table_type.append(col_type_format)
        table_col.append(col)

    return {'querry': tpye_and_colum_querry, 'results': table_resultat, 'types': table_type, 'names': table_col}

def insertion_querry(table:str, inserts = [[]], champs = []):

    querry = "INSERT INTO " + table

    champsConcat = ' ('
    for champ in champs:
        champsConcat += champ
        if(champ == champs[len(champs)-1]):
            champsConcat += ')'
            continue
        champsConcat += ", "

    typeValeurString = '('

    x = 0
    valeursSql = []
    for valeurs in inserts:

        tempValeur = []
        for valeur in valeurs:

            tempValeur.append(valeur)

            if( x == 0):
                typeValeurString += "%s"

                if(valeur == valeurs[len(valeurs)-1]):
                    typeValeurString += ')'
                    continue
                typeValeurString += ", "

        valeursSql.append(tuple(tempValeur))
        x += 1
    
    if(champ):
        querry += champsConcat

    if(valeur):
        querry += " VALUES " + typeValeurString

    return {
        'sql': querry,
        'val' : valeursSql
    }


def update_querry(table :str, updates :list[list], champs :list, conds_list :list[list]):

    querry = "UPDATE " + table + " SET "

    champsConcat = ''
    for champ in champs:
        champsConcat += champ
        
        if(champ == champs[len(champs)-1]):    
            champsConcat += " = %s "
            continue
        champsConcat += " = %s, "

    valeursSql = []
    for valeurs in updates:
        tempValeur = []
        for valeur in valeurs:
            tempValeur.append(valeur)

    condString = ''
    if(len(conds_list) == 2):

        for valeurs in conds_list['cond_valeurs']:
            for valeur in valeurs:
                tempValeur.append(valeur)

        for champ in conds_list['cond_champs']:
            condString += champ + " = %s AND "

    valeursSql.append(tuple(tempValeur))
    
    if(champ):
        querry += champsConcat

    if(condString != ''):
        querry += "WHERE " + condString[0:len(condString)-5]

    return {
        'sql': querry,
        'val' : valeursSql
    }

def convert_string_to_sql_type(input_str: str, sql_type_str: str):

    if( sql_type_str.startswith("char") ):
        return input_str
    if( sql_type_str.startswith("varchar") ):
        return input_str

    if( sql_type_str.startswith("int") ):
        return int(input_str)
    if( sql_type_str.startswith("float") ):
        return float(input_str)
    if( sql_type_str.startswith("double") ):
        return round(float(input_str),2)


    if( sql_type_str.startswith("year") ):
        return int(input_str)
    if( sql_type_str.startswith("date") ):
        return input_str
    if( sql_type_str.startswith("time") ):
        return input_str
    if( sql_type_str.startswith("time", 4) ):
        return input_str
    if( sql_type_str.startswith("stamp", 4) ):
        return input_str
    pass

def dataTypeStringNotation(value: any):

    percent_char = chr(37)

    if(type(value) is str):
        return percent_char + 's'

    if(type(value) == int):
        return percent_char + 'i'

    if(type(value) is float):
        return percent_char + 'f'

    return ''

def fetch_CURSEUR(CURSEUR, print_me = False):
    if(print_me == True):
        print("\n")

    table = []
    for results_row in CURSEUR:
        table_row = []
        for results in results_row:
            table_row.append(results)
        if(print_me == True):
            print(table_row)
        table.append(table_row)
    
    CURSEUR.reset()
    return table

def insert_commit_check(data, querry, basetable):

    if(BD_CONNECTION.autocommit == True):

        # Try
        CURSEUR.execute(querry['sql'], querry['val'][0])
        
        # Catch
        fetch_CURSEUR(CURSEUR) 

        querry = "SELECT * FROM " + basetable + " WHERE id="+ str(CURSEUR.lastrowid)
        CURSEUR.execute(querry)
        print("Donnée inserée:")
        fetch_CURSEUR(CURSEUR)

    else:
        print("\n" + str( data['champs'] ) )
        print( str( data['valeurs'][0] ) )
        u_input = input("\n Êtes-vous certains de vouloir insérer cette donnée? (y/n)\n ==> ")

        if( u_input == 'y'):

            # Try
            CURSEUR.execute(querry['sql'], querry['val'][0])
            
            # Catch
            fetch_CURSEUR(CURSEUR)

            BD_CONNECTION.commit()
            querry = "SELECT * FROM " + basetable + " WHERE id="+ str(CURSEUR.lastrowid)
            CURSEUR.execute(querry)
            print("Donnée inserée:")
            fetch_CURSEUR(CURSEUR)
        else:
            pass

def update_commit_check(data, querry, cond, basetable):

    if(BD_CONNECTION.autocommit == True):

        # Try
        CURSEUR.execute(querry['sql'], querry['val'][0])
        
        # Catch
        print("Données modifiés !")

    else:

        print("\nCONDITIONS")
        if(len(cond) > 1):
            print("AND")
            print( str( cond['cond_champs'] ) )
            print( str( cond['cond_valeurs'][0] ) +"\n" )
        else:
            print("Toutes les données !!!\n")

        print("\nMODIFICATIONS")
        print( str( data['champs'] ) )
        print( str( data['valeurs'][0] ) )
        u_input = input("\n Êtes-vous certains de vouloir modifier ces données? (y/n)\n ==> ")

        if( u_input == 'y'):

            # Try
            CURSEUR.execute(querry['sql'], querry['val'][0])
            
            # Catch

            BD_CONNECTION.commit()
            print("Données modifiés !")
        else:
            pass

def delete_commit_check(querry):

    if(BD_CONNECTION.autocommit == True):

        # Try 
        CURSEUR.execute(querry)
        # Catch

    else:

            # Try 
            CURSEUR.execute(querry)
            # Catch
            BD_CONNECTION.commit()
            print("\n Donnée supprimé !!!")



def hash_sha2_data(datalist:list[str] = [], hash_length:int = 256):

    hashes = []

    if hash_length == 224:
        for clear_str in datalist:
            string = clear_str
            encoded = string.encode()
            result = hashlib.sha224(encoded)
            hashes.append(result.hexdigest())

    elif hash_length == 384:
        for clear_str in datalist:
            string = clear_str
            encoded = string.encode()
            result = hashlib.sha384(encoded)
            hashes.append(result.hexdigest())

    elif hash_length == 512:
        for clear_str in datalist:
            string = clear_str
            encoded = string.encode()
            result = hashlib.sha512(encoded)
            hashes.append(result.hexdigest())

    else: # sha256 if hash_length not supported
        for clear_str in datalist:
            string = clear_str
            encoded = string.encode()
            result = hashlib.sha256(encoded)
            hashes.append(result.hexdigest())

    return hashes