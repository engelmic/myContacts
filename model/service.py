# from model.contact import Contact
import model.dao as dao


# def create_contact(fname, lname, priphone, secphone) -> Contact:
#     con = Contact()
#     con.fname = fname
#     con.lname = lname
#     con.priphone = priphone
#     con.secphone = secphone
#     return con


def load_all_contacts() -> list:
    return dao.load_contacts()


def save_contact(info) -> None:
    conn = dao.connect_db()
    dao.store_contact(info, conn)


def search_contacts(tup_in):
    conn = dao.connect_db()
    searchterm, intype = tup_in
    return dao.find_contact(conn, searchterm, intype)

def create_contact(fname, lname, priphone, secphone):
    return dao.create_contact(fname, lname, priphone, secphone)