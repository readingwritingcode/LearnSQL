import mysql.connector
from mysql.connector import Error

def connect():
    '''connect to MySQL database'''
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='python_mysql',
                                       user='root',
                                       password='asñl')
        if conn.is_connected():
            print('connected to mysql database')

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()

if __name__ == '__main__':
    connect()
