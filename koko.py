import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn



def main():
    database = r"database\chinook\chinook.sqlite"

    # create a database connection
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Album")

    rows = cur.fetchall()

    for row in rows:
        print(row)



if __name__ == '__main__':
    main()