"""
Program: person_student_database_gui.py
Author: Kelly Klein
Last date modified: 7/23/2020
This program will use a gui to get user interface to make a person and
    student class, and then display it back
"""

import sqlite3
from sqlite3 import Error
import tkinter as tk
from tkinter import END


first_name_text = ''
last_name_text = ''
id_text = ''
major_text = ''
date_started_text = ''


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


def create_table(conn, sql_create_table):
    """ Creates table with give sql statement
    :param conn: Connection object
    :param sql_create_table: a SQL CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)


def create_tables(database):
    sql_create_person_table = """ CREATE TABLE IF NOT EXISTS person (
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

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_person_table)
        # create tasks table
        create_table(conn, sql_create_student_table)
    else:
        print("Unable to connect to " + str(database))


def create_person(conn, person):
    """Create a new person for table
    :param conn:
    :param person:
    :return: person id
    """
    sql = ''' INSERT INTO person(firstname,lastname)
              VALUES(?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, person)
    return cur.lastrowid  # returns the row id of the cursor object, the person id


def create_student(conn, student):
    """Create a new person for table
    :param conn:
    :param student:
    :return: student id
    """
    sql = ''' INSERT INTO student(major, begin_date)
              VALUES(?, ?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, student)
    return cur.lastrowid  # returns the row id of the cursor object, the student id


def person(firstname, lastname):
    """Create a person to pass in to db
    :param firstname
    :param lastname
    :return firstname, lastname"""
    firstname = firstname.get()
    lastname = lastname.get()
    return person


def student(first_name, last_name, major, begin_date):
    """Create a student to pass in to db
    :param first_name
    :param last_name
    :param major
    :param begin_date"""
    first_name = first_name.get()
    last_name = last_name.get()
    major = major.get()
    begin_date = begin_date.get()

    return student


def view_person():
    conn = sqlite3.connect('person_student.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM person")
    records = cur.fetchall()

    print_records = ''
    for record in records:
        print_records += str(record) + "\n"

    query_label = tk.Label(window, text=print_records).grid(row=9, column=0)

    conn.commit()
    conn.close()
    return


def test_add_person():
    query_label = tk.Label(window, text="person added").grid(row=9, column=1)
    insert_person_tuple = (first_name_text.get(), last_name_text.get())
    conn = create_connection('person_student.db')
    with conn:
        create_person(conn, insert_person_tuple)


def add_person():
    query_label = tk.Label(window, text="person added").grid(row=9, column=1)
    conn = sqlite3.connect('person_student.db')
    insert_person_tuple = (first_name_text.get(), last_name_text.get())
    with conn:
        create_person(conn, insert_person_tuple)


def test_add_student():
    query_label = tk.Label(window, text="student added").grid(row=9, column=1)
    insert_student_tuple = (major_text.get(), date_started_text.get())
    conn = create_connection('person_student.db')
    with conn:
        create_student(conn, insert_student_tuple)


def add_student():
    query_label = tk.Label(window, text="student added").grid(row=9, column=1)
    conn = sqlite3.connect('person_student.db')
    insert_student_tuple = (major_text.get(), date_started_text.get())
    with conn:
        create_student(conn, insert_student_tuple)


def view_student():
    conn = sqlite3.connect('person_student.db')
    cur = conn.cursor()

    cur.execute("SELECT *, oid FROM student")
    records = cur.fetchall()

    print_records = ''
    for record in records:
        print_records += str(record) + "\n"

    query_label = tk.Label(window, text=print_records).grid(row=9, column=1)

    conn.commit()
    conn.close()
    return


def clear_databases():
    sql = 'DELETE FROM person'
    sql1 = 'DELETE FROM student'
    conn = sqlite3.connect('person_student.db')
    cur = conn.cursor()

    cur.execute(sql)
    cur.execute(sql1)
    records = cur.fetchall()
    print_records = ''
    for record in records:
        print_records += str(record) + "\n"

    query_label = tk.Label(window, text='').grid(row=9, column=0)
    query_label = tk.Label(window, text='').grid(row=9, column=0)

    conn.commit()
    conn.close()


window = tk.Tk()
window.title("Person and Student database")

tk.Label(window, text="First Name:").grid(row=0)
tk.Label(window, text="Last Name:").grid(row=1)

first_name_text = tk.StringVar()
last_name_text = tk.StringVar()
firstname = tk.Entry(window, textvariable=first_name_text).grid(row=0, column=1)
lastname = tk.Entry(window, textvariable=last_name_text).grid(row=1, column=1)

create_db_table_button = tk.Button(window, text="Create Database and Table", command=lambda: [create_connection('person_student.db'), create_tables('person_student.db')]).grid(row=5, column=2)
create_person_button = tk.Button(window, text="Add Person", command=add_person).grid(row=2, column=1)
add_student_button = tk.Button(window, text="Add Student", command=add_student).grid(row=2, column=3)
view_person_button = tk.Button(window, text="View Person Table", command=view_person).grid(row=4, column=1, columnspan=2)
view_student_button = tk.Button(window, text="View Student Table", command=view_student).grid(row=4, column=2, columnspan=2)
clear_database_button = tk.Button(window, text="Clear Databases", command=clear_databases).grid(row=8, column=1, columnspan=3)
program_exit_button = tk.Button(window, text="Exit", command=window.quit).grid(row=9, column=2)


tk.Label(window, text="Major:").grid(row=0, column=2)
tk.Label(window, text="Date Started:").grid(row=1, column=2)

major_text = tk.StringVar()
date_started_text = tk.StringVar()
major = tk.Entry(window, textvariable=major_text).grid(row=0, column=3)
date_started = tk.Entry(window, textvariable=date_started_text).grid(row=1, column=3)

window.mainloop()
