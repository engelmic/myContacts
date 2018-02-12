import os
import sqlite3
from model.contact import Contact


def create_contact(fname, lname, priphone, secphone) -> Contact:
    con = Contact()
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


def store_contact(o, conn) -> None:
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Contacts (FirstName, LastName, PriPhone, SecPhone) VALUES (?,?,?,?)",
                   (o.fname, o.lname, o.priphone, o.secphone))
    conn.commit()


def find_contact(conn, searchterm, intype):
    cursor = conn.cursor()
    if intype == 1:
        cursor.execute("SELECT "
               "ContactID, "
               "FirstName, "
               "LastName, "
               "PriPhone, "
               "SecPhone "
               "FROM Contacts WHERE FirstName=? OR LastName=?", (searchterm, searchterm))
    elif intype == 2:
        cursor.execute("SELECT "
                       "ContactID, "
                       "FirstName, "
                       "LastName, "
                       "PriPhone, "
                       "SecPhone "
                       "FROM Contacts WHERE PriPhone=? OR SecPhone=?", (searchterm, searchterm))
    data = cursor.fetchall()
    con_list = []
    for con in data:
        con_list.append(create_contact(con['FirstName'], con['LastName'], con['PriPhone'], con['SecPhone']))
    return con_list

def delete_contact():
    pass




# import sqlite3
# import json
# from model import service as service
#
#
# def store_contact(o) -> None:
#     '''
#     This function performs 3 actions:
#     1. Takes a list of Contact objects, translates them to dictionaries.
#     2. Stores dictionaries in list f.
#     3. List f is written to the json file.
#
#     :param o: array of Contact objects
#     :return: -> None
#     '''
#
#     f = []
#     file = open("contactsdb.json", "w")
#     for contact in o:
#         f.append(contact.__dict__)
#     file.write(json.dumps(f))
#     file.close()
#
# def load_contacts() -> list:
#     '''
#     This function performs 2 actions:
#     1. Attempt to open data file. If it doesn't exist, create a blank file.
#     2. Read the file and append a dictionary version of the object to the rtn list.
#
#     :return: rtn -> list
#     '''
#     rtn = []
#     try:
#         file = open("contactsdb.json", "r")
#     except FileNotFoundError:
#         file = open("contactsdb.json", "w")
#         file.write("")
#         file.close()
#         file = open("contactsdb.json", "r")
#     try:
#         data = json.loads(file.readline())
#         for contact in data:
#             rtn.append(service.create_contact(contact['_Contact__fname'], contact['_Contact__lname'],
#                                               contact['_Contact__priphone'], contact['_Contact__secphone'], ))
#     except json.decoder.JSONDecodeError:
#         pass
#     return rtn
