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

        choice = input("What would you like to do?  ")

        # this try statement doesn't actually check for a valid integer, just an integer **fix**
        try:
            choice = int(choice)
        except ValueError:
            print("\nI need a valid integer 0-6!")
            input("Press Enter to continue")
            pass

        if choice == 0:
            exit(0)
        if choice == 1:
            service.save_contact(__create_contact())
        if choice == 2:
            print("Not implemented yet!")
        if choice == 3:
            print("Not implemented yet")
        if choice == 4:
            __return_contacts(service.search_contacts(__search()))


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


def __search():
    uin = int(input("Do you want to search by (1)Name or (2)Number?"))
    st = input("Please enter your search term: ")
    return (st, uin)
