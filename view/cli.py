from typing import Union
from model.contact import Contact
import model.service as service


def main_menu():
    while True:
        print("\n\n-----------------------------")
        print("         MY Contacts         ")
        print("-----------------------------\n")
        print("1. Create a New Contact\n")
        print("2. Edit a Contact\n")
        print("3. List Contacts\n")
        print("4. Search Contacts\n")
        print("5. Delete a Contact\n")
        print("6. Delete all Contacts\n")
        print("0. Exit\n")

        in_ok = True
        while in_ok:
            choice = input("Make your selection and press enter:  ")
            try:
                choice = int(choice)
                in_ok = False
            except ValueError:
                print("\nI need a valid integer 0-6!")
                input("Press Enter to continue")

        if choice > 6:
            input("Selection invalid! Press enter to continue")
        if choice == 0:
            exit(0)
        if choice == 1:
            service.save_contact(__create_contact())
        if choice == 2:
            __return_contacts(service.search_contacts(__search()))
            __edit_contact(input("Enter the Contact ID# of the contact you wish to edit: "))
        if choice == 3:
            __return_contacts(service.return_all_contacts())
        if choice == 4:
            __return_contacts(service.search_contacts(__search()))
        if choice == 5:
            __return_contacts(service.search_contacts(__search()))
            service.delete_contact(__get_conid('delete'))


def __create_contact() -> Contact:
    fname = __get_fname()
    lname = __get_lname()
    priphone = __get_priphone()
    secphone = __get_secphone()
    return service.create_contact(None, fname, lname, priphone, secphone)


def __edit_contact(in_ID) -> None:
    if in_ID:
        con_obj = (service.return_contact_by_ID(in_ID))
        fname = __get_fname(con_obj.fname)
        lname = __get_lname(con_obj.lname)
        priphone = __get_priphone(con_obj.priphone)
        secphone = __get_secphone(con_obj.secphone)
        return service.edit_contact(con_obj.conID, fname, lname, priphone, secphone)
    else:
        pass


def __get_fname(current=None) -> str:
    return input("Contact's first name (required)[{}]:".format(current)).capitalize() or current


def __get_lname(current=None) -> Union[str, None]:
    try:
        return input("Contact's last name [{}]:".format(current)).capitalize() or current
    except:
        return None

def __get_priphone(current=None) -> int:
    pnum = input("Contact's primary phone number (required)[{}]:".format(current)) or current
    return int(pnum)


def __get_secphone(current=None) -> Union[int, None]:
    try:
        return int(input("Contact's secondary phone number [{}]:".format(current))) or int(current)
    except:
        return None


def __return_contacts(list) -> None:
    print("\n")
    for contact in list:
        print("------")
        print("Contact ID #", contact.conID)
        print("First Name:", contact.fname)
        print("Last Name:", contact.lname)
        print("Primary Phone:", contact.priphone)
        print("Secondary Phone:", contact.secphone)
        print("------\n\n")
    input("Press enter to continue.")


def __search():
    # uin = int(input("Do you want to search by (1)Name or (2)Number?"))
    st = input("Please enter your search term: ")
    # return (st, uin)
    return st


def __get_conid(act):
    try:
        return int(input("Please enter the Contact ID number you wish to {}: ".format(act)))
    except ValueError:
        input("I will only accept 1 valid integer. Press enter to continue.")
        return None