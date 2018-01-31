import json
from model import service as service

def store_contact(o):
    file = open("contactsdb.json", "a")
    file.write(json.dumps(o.__dict__))
    file.write("\n")


def load_contacts():
    rtn = []
    wrk = []
    file = open("contactsdb.json", "r")
    for line in file:
        wrk.append(json.loads(line))
    for contact in wrk:
        rtn.append(service.create_contact(contact['_Contact__fname'], contact['_Contact__lname'], contact['_Contact__priphone'], contact['_Contact__secphone'], ))
    return rtn
