import sqlite3
from sqlite3 import Error


def create_connection(db):
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None


def create_table(conn, sql_create_table):
    try:
        c = conn.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)


def create_tables(database):

    sql_create_person_table = """CREATE TABLE IF NOT EXISTS person (
                                        id integer PRIMARY KEY,
                                        firstname text NOT NULL,
                                        lastname text NOT NULL
                                    ); """

    sql_create_student_table = """CREATE TABLE IF NOT EXISTS student (
                                    id integer PRIMARY KEY,
                                    major text NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text,
                                    FOREIGN KEY (id) REFERENCES person (id)
                                );"""

    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_person_table)
        create_table(conn, sql_create_student_table)


if __name__ == '__main__':
    create_tables("pythonsqlite.db")
