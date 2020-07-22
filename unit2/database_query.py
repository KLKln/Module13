
"""
Program: database_query.py
Author: Kelly Klein
Last date modified: 7/19/2020
This program will query tables and return rows
"""

import sqlite3
from sqlite3 import Error


def create_connection(db):
    """ Connect to a SQLite database
    :param db: filename of database
    :return connection if no error, otherwise None"""
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None


def select_all_persons(conn):
    """Query all rows of person table
    :param conn: the connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM person")

    rows = cur.fetchall()

    return rows  # return the rows


def select_all_students(conn):
    """Query all rows of student table
    :param conn: the connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")

    rows = cur.fetchall()

    return rows


if __name__ == '__main__':
    """conn = create_connection("pythonsqlite.db")
    with conn:
        rows = select_all_persons(conn)
        for row in rows:
            print(row)
    """
    conn = create_connection("pythonsqlite.db")
    with conn:
        rows = select_all_students(conn)
        for row in rows:
            print(row)
