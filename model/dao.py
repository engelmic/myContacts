import os
import sqlite3
from model.contact import Contact


def create_contact(conID, fname, lname, priphone, secphone) -> Contact:
    con = Contact()
    con.conID = conID
    con.fname = fname
    con.lname = lname
    con.priphone = priphone
    con.secphone = secphone
    return con


def connect_db():
    if os.path.exists('contacts.db'):
        conn = sqlite3.connect('contacts.db')
    else:
        conn = sqlite3.connect('contacts.db')
        create_db(conn)

    conn.row_factory = sqlite3.Row
    return conn


def create_db(conn) -> None:
    # conn = dbconn
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Contacts(ContactID INTEGER PRIMARY KEY AUTOINCREMENT, FirstName TEXT, '
                   'LastName TEXT, PriPhone INTEGER,SecPhone INTEGER)')


def format_contact_list(data) -> list:
    con_list = []
    for con in data:
        con_list.append(
            create_contact(con['ContactID'], con['FirstName'], con['LastName'], con['PriPhone'], con['SecPhone']))
    return con_list


def store_contact(o, conn) -> None:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Contacts (FirstName, LastName, PriPhone, SecPhone) VALUES (?,?,?,?)",
                   (o.fname, o.lname, o.priphone, o.secphone))
    conn.commit()


def return_all_contacts(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT ContactID, FirstName, LastName, PriPhone, SecPhone FROM Contacts")
    data = cursor.fetchall()
    return format_contact_list(data)

def find_contact(conn, searchterm):
    cursor = conn.cursor()
    cursor.execute("SELECT "
               "ContactID, "
               "FirstName, "
               "LastName, "
               "PriPhone, "
               "SecPhone "
               "FROM Contacts WHERE FirstName=? OR LastName=? OR PriPhone=? OR SecPhone=?",
                   (searchterm, searchterm, searchterm, searchterm))

    data = cursor.fetchall()
    return format_contact_list(data)


def delete_contact(conn, del_con):
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Contacts WHERE ContactID=?',(del_con,))
    conn.commit()
