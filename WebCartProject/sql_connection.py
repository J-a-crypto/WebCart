import mysql.connector

_cnx = None

#This will be the authentication of the SQL connection between our server and db
def get_sql_connection():
    global __cnx 
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root',password='...',
                                        host = '127.0.0.1',
                                        database = '...')
    return __cnx