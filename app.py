import pandas as pd
import pymysql

def lire_csv(nom_fichier: str) -> pd.DataFrame:
    """_summary_ : permet de lire à fichier CSV et de le retourner en dataframe

    Args:
        nom_fichier (str): nom du fichier CSV à lire : "nom_fichier.csv"

    Returns:
        pd.DataFrame: dataframe contenant les données du fichier CSV
    """
    table = pd.read_csv(nom_fichier)
    return table[1:4]

def se_connecter_db(host : str, user : str, password : str, database : str) -> pymysql.connections.Connection:
    """_summary_ : permet de se connecter à la base de données

    Args:
        host (str): machine sur laquelle se trouve la base de données
            - localhost : si c'est sur la même machine
            - ip : si c'est une autre machine 12.154.123.45
        user (str): login de la base de données
        password (str): password de la base de données
        database (str): nom de la base de données

    Returns:
        pymysql.connections.Connection: appel vers la base de données
    """
    conn = pymysql.connect(host=host, user=user, password=password, database=database)
    return conn

def inserer_donnees(conn, table):
    """_summary_ : insère des données utilisateurs dans la base de données

    Args:
        conn (_type_): _description_
        utilisateurs (_type_): _description_
    """
    cursor = conn.cursor()
    for index, row in table.iterrows():
        sql = "INSERT INTO clients (id, prenom, nom, email, profession, pays, ville) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (row['id'], row['firstname'], row['lastname'], row['email'], row['profession'], row['country'], row['city']))
    conn.commit()

table = lire_csv('clients.csv')

db_host = "localhost"
db_user = "root"
db_password = "example"
db_database = "exercice"

conn = se_connecter_db(db_host, db_user, db_password, db_database)

inserer_donnees(conn, table)