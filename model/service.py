from model.contact import Contact
import model.dao as dao
from typing import List


def create_contact(conID, fname, lname, priphone, secphone) -> Contact():
    return dao.create_contact(conID, fname, lname, priphone, secphone)


def return_all_contacts() -> List:
    conn = dao.connect_db()
    return dao.return_all_contacts(conn)


def save_contact(info) -> None:
    conn = dao.connect_db()
    dao.store_contact(info, conn)


def search_contacts(searchterm) -> List:
    conn = dao.connect_db()
    return dao.find_contact(conn, searchterm)


def delete_contact(del_con) -> None:
    conn = dao.connect_db()
    return dao.delete_contact(conn, del_con)


def return_contact_by_ID(con_ID) -> Contact:
    conn = dao.connect_db()
    return dao.get_contact_by_ID(conn, con_ID)[0]


def edit_contact(conID, fname, lname, priphone, secphone) -> Contact:
    conn = dao.connect_db()
    return dao.update_contact(create_contact(conID, fname, lname, priphone, secphone), conn)
