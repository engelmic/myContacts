from model.contact import Contact
import model.dao as dao


def create_contact(fname, lname, priphone, secphone) -> Contact:
    con = Contact()
    con.fname = fname
    con.lname = lname
    con.priphone = priphone
    con.secphone = secphone
    return con


def load_all_contacts() -> list:
    return dao.load_contacts()


def save_contact(info) -> None:
    dao.store_contacts(info)
