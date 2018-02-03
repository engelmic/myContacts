from typing import Union
from model.contact import Contact
import model.service as service



def main_menu():
    contacts = service.load_all_contacts()
    while True:
        # contacts = service.load_all_contacts()
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

        choice = input("What would you like to do?  ")
        try:
            choice = int(choice)
        except:
            print("\nI need a valid integer 0-6!")
            input("Press Enter to continue")
            pass

        if choice == 0:
            exit(0)
        if choice == 1:
            contacts.append(__create_contact())
            service.save_contacts(contacts)
        if choice == 2:
            pass
        if choice == 3:
            __return_contacts(contacts)
        if choice == 4:
            pass


def __create_contact() -> Contact:
    fname = __get_fname()
    lname = __get_lname()
    priphone = __get_priphone()
    secphone = __get_secphone()
    return service.create_contact(fname, lname, priphone, secphone)


def __get_fname() -> str:
    return input("Contact's first name:").capitalize()


def __get_lname() -> str:
    return input("Contact's last name:").capitalize()


def __get_priphone() -> int:
    return int(input("Contact's primary phone number:"))


def __get_secphone() -> Union[int, None]:
    try:
        return int(input("Contact's primary phone number:"))
    except:
        return None


def __return_contacts(list) -> None:
    print("\n")
    for contact in list:
        print("------")
        print("First Name:", contact.fname)
        print("Last Name:", contact.lname)
        print("Primary Phone:", contact.priphone)
        print("Secondary Phone:", contact.secphone)
        print("------\n\n")
    input("Press enter to continue.")
