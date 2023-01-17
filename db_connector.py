# This module interacts with the predefined DB , connect to DB and run SQL queries

import pymysql

#DB_Server_parameters
SCHEMA_NAME = 'devops_export'
HOST_IP_ADDR = '127.0.0.1'
PORT = 3306
USER_NAME = 'root'
PASSWD = 'Password1!'
DB_NAME = 'devops_export'


def connect_to_db(to_connect, conn=None):
    # Function establishes and disconnects from the predefined DB
    if to_connect:
        db_connector = pymysql.connect(host=HOST_IP_ADDR, port=PORT, user=USER_NAME, passwd=PASSWD,
                                       db=DB_NAME)
        db_connector.autocommit(True)
        return (db_connector)
    else:
        conn.close()


def add_user(user_id, username):
    # Establishing a connection to DB
    db_connector = connect_to_db(True)

    # Getting a cursor from Database
    cursor = db_connector.cursor()

    # Inserting data into table
    cursor.execute(f"INSERT into {SCHEMA_NAME}.users (name, id) VALUES ('{username}', {user_id})")
    cursor.close()
    connect_to_db(False, db_connector)


def update_user(user_id, username):
    # Establishing a connection to DB
    db_connector = connect_to_db(True)

    # Getting a cursor from Database
    cursor = db_connector.cursor()

    # Updating data in a table
    cursor.execute(f"UPDATE {SCHEMA_NAME}.users set name='{username}' where id={user_id}")
    cursor.close()
    connect_to_db(False, db_connector)


def delete_user(user_id):
    # Establishing a connection to DB
    db_connector = connect_to_db(True)

    # Getting a cursor from Database
    cursor = db_connector.cursor()

    # Deleting a data from table
    cursor.execute(f"DELETE FROM {SCHEMA_NAME}.users where id={user_id}")
    cursor.close()
    connect_to_db(False, db_connector)


def get_user(user_id):
    # Establishing a connection to DB
    db_connector = connect_to_db(True)

    # Getting a cursor from Database
    cursor = db_connector.cursor()

    # Bringing the data from table
    cursor.execute(f"SELECT name FROM {SCHEMA_NAME}.users where id={user_id}")
    result = cursor.fetchone()
    return (result[0])








