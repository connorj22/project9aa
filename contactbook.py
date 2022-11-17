from peewee import *

db = PostgresqlDatabase('contactbook', user='connorharris', password='12345',
                        host='localhost', port=5432)


def Connect():
    db.connect()
    print("Connecting databse")
    return 0


Connect()


class BaseModel(Model):
    class Meta:
        database = db


class Contacts(BaseModel):
    name = CharField()
    phoneNumber = CharField()
    note = CharField()


db.create_tables([Contacts])


def inputContacts(InputtedName, InputtedphoneNumber, Inputtednote):
    newContact = Contacts(
        name=InputtedName, phoneNumber=InputtedphoneNumber, note=Inputtednote)
    newContact.save()
    print("Added to Contacts")
    return 0


status = "running"
while status == "running":
    toEnter = input(
        "Add a contact? (y/n) : ")
    if toEnter == "n":
        status = "notRunning"
        changeStatus = input("To run application, type (run): ")
        if changeStatus == "run":
            status = "running"
    elif toEnter == "y":
        name = input("Add Name: ")
        phoneNumber = input("Add phone phoneNumber: ")
        note = input("Add additional note: ")
        inputContacts(name, phoneNumber, note)
