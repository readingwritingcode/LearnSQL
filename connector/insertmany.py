'''
the following INSER statement allows you to insert multiple rows into the books table:

INSER INTO(title, isbn)
VALUES('title one', isbnone),
      ('titleTwo', isbnTwo),
      ('titleThree', isbNThree),
      ...;

to insert multiple rows into a table in python, you use the executemany() method of the
MySQLCursor object. See the following code:
'''

from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def insert_books(books):
    query = "INSERT INTO books(title,isbn) " \
            "VALUES(%s,%s)"

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execuremany(query,books)

        conn.commit()
    except Error as e:
        print('Error:', e)

    finally:
        cursor.close()
        conn.close()

def main():
    books = [(a,s),
             (q,w),
             (e,r),
             (t,y)]
    insert_books(books)
if __name__ == "__main__":
    main()
    
