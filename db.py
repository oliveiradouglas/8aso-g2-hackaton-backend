import os
import pymysql
from flask import jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_local_host = os.environ.get('DB_LOCAL_HOST')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')

def open_connection():
    try:
        if db_connection_name:
            print ('abrindo conexão com cloud run')
            unix_socket = '/cloudsql/{}'.format(db_connection_name)
            conn = pymysql.connect(user=db_user, password=db_password,
                                unix_socket=unix_socket, db=db_name,
                                cursorclass=pymysql.cursors.DictCursor
                                )
            print ('tchau')
        else:
            print ('abrindo conexão com db local')
            conn = pymysql.connect(user=db_user, password=db_password,
                                host=db_local_host, db=db_name,cursorclass=pymysql.cursors.DictCursor)

        return conn
    except pymysql.MySQLError as e:
        print(e)

def get_songs():
    conn = open_connection()

    if not conn:
        print("erro na conexão com o banco")
        return []

    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM songs;')
        songs = cursor.fetchall()
        if result > 0:
           got_songs = jsonify(songs)

        else:
            got_songs = 'Nenhuma Musica Cadastrada na Playlist'

    conn.close()

    return got_songs
