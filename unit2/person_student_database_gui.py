import sqlite3
from sqlite3 import Error
import tkinter as tk
from tkinter import END


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


def create_person1():
    """conn = sqlite3.connect('person.db')
    c = conn.cursor()

    c.execute("INSERT INTO person VALUES (:firstname, :lastname);",
              {
                  'firstname': firstname.get(),
                  'lastname': lastname.get()
              })

    conn.commit()

    conn.close()"""

    firstname.delete(0, END)
    lastname.delete(0, END)


def create_person(conn, person):
    """Create a new person for table
    :param conn:
    :param person:
    :return: person id
    """
    sql = ''' INSERT INTO person  
              VALUES(firstname, lastname)'''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, person)

    #firstname.delete(0, END)
    #lastname.delete(0, END)
    return cur.lastrowid  # returns the row id of the cursor object, the person id


def create_student(conn, student):
    """Create a new person for table
    :param conn:
    :param student:
    :return: student id
    """
    sql = ''' INSERT INTO student
              VALUES(id, major, begin_date '''
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


def student(id, major, begin_date):
    id = id.get()
    major = major.get()
    begin_date = begin_date.get()

    return student


def view_person():
    conn = sqlite3.connect('person_student.db')
    cur = conn.cursor()

    cur.execute("SELECT *, oid FROM person")
    records = cur.fetchall()

    print_records = ''
    for record in records:
        print_records += str(record) + "\n"

    query_label = tk.Label(window, text=print_records).grid(row=8, column=0)

    conn.commit()
    conn.close()
    return


window = tk.Tk()
window.title("Person and Student database")

tk.Label(window, text="First Name:").grid(row=0)
tk.Label(window, text="Last Name:").grid(row=1)

firstname = tk.Entry(window).grid(row=0, column=1)
lastname = tk.Entry(window).grid(row=1, column=1)

create_db_table_button = tk.Button(window, text="Create Database and Table", command=lambda: [create_connection('person_student.db'), create_tables('person_student.db')]).grid(row=5, column=2)
create_person_button = tk.Button(window, text="Add Person", command=lambda: [create_person(create_connection('person_student.db'), create_person(create_connection('person_student.db'), person))]).grid(row=3, column=1)
add_student_button = tk.Button(window, text="Add Student", command=lambda: [create_student(create_connection('person_student.db'), create_student(create_connection('person_student.db'), student))]).grid(row=4, column=3)
view_person_button = tk.Button(window, text="View Person Table").grid(row=6, column=2)
view_student_button = tk.Button(window, text="View Student Table", command=query).grid(row=7, column=2)
program_exit_button = tk.Button(window, text="Exit", command=window.quit).grid(row=8, column=2)

tk.Label(window, text="id:").grid(row=0, column=2)
tk.Label(window, text="Major:").grid(row=1, column=2)
tk.Label(window, text="Date Started:").grid(row=2, column=2)

id = tk.Entry(window).grid(row=0, column=3)
major = tk.Entry(window).grid(row=1, column=3)
date_started = tk.Entry(window).grid(row=2, column=3)

window.mainloop()
