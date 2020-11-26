from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def insert_book(title, isbn):

    query = "INSERT INTO boks(title,isbn) " \
            "VALUES(%s,%S)"
    args = (title, isbn)

    try:
        db_config = read_db_config()
        conn = MysqlConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query,args)

        if cursor.lastrowid:
            print('last insert id':cursor.lastrowid)
        else:
            print('las insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def main():
    insert_book('A Sudden Lighth','978456123')

if __name__ == '__main__':
    main()
