from model.contact import Contact
import model.dao as dao


def create_contact(fname, lname, priphone, secphone):
    con = Contact()
    con.fname = fname
    con.lname = lname
    con.priphone = priphone
    con.secphone = secphone
    return con


def load_all_contacts():
    return dao.load_contacts()


def save_contact(info):
    dao.store_contact(info)
