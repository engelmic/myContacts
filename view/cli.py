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
            # service.edit_contact(__get_conid('edit'))
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


def __get_fname() -> str:
    return input("Contact's first name (required):").capitalize()


def __get_lname() -> Union[str, None]:
    try:
        return input("Contact's last name:").capitalize()
    except:
        return None

def __get_priphone() -> int:
    return int(input("Contact's primary phone number (required):"))


def __get_secphone() -> Union[int, None]:
    try:
        return int(input("Contact's secondary phone number:"))
    except:
        return None


def __get_conid(act):
    try:
        return int(input("Please enter the Contact ID number you wish to {}: ".format(act)))
    except ValueError:
        input("I will only accept 1 valid integer. Press enter to continue.")
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
