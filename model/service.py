from model.contact import Contact
import model.dao as dao
from typing import List

def create_contact(conID, fname, lname, priphone, secphone) -> Contact():
    return dao.create_contact(conID, fname, lname, priphone, secphone)


def return_all_contacts() -> list:
    conn = dao.connect_db()
    return dao.return_all_contacts(conn)


def save_contact(info) -> None:
    conn = dao.connect_db()
    dao.store_contact(info, conn)


def search_contacts(searchterm) -> list:
    conn = dao.connect_db()
    return dao.find_contact(conn, searchterm)


def delete_contact(del_conn) -> None:
    conn = dao.connect_db()
    return dao.delete_contact(conn, del_conn)
