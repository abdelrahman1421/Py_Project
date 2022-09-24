import re
import time
from check import saveRegistration


def insertName(message):
    name = input(message)

    if name.isspace() or not name:
        print("Please Type a Valid Name")
        return insertName(message)

    return name


def insertPhone(message):
    phone = input(message)
    phonepattern = "^01[0125][0-9]{8}$"

    if re.match(phonepattern, phone):
        return str(phone)
    else:

        print("\n\t--<<< Invalid Number >>>--\n")
        return insertPhone(message)


def insertEmail(message):
    email = input(message)
    mailPattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"

    if re.match(mailPattern, email):
        return str(email)
    else:
        print("\n\t---<<< Invalid Email >>>--\n")
        return insertEmail(message)


def insertPassword(message):
    password = input(message)
    rewritepassword = input("Confirm Password: ")

    if rewritepassword == password:
        return str(password)
    else:
        print("\n\t--<<< *Password Dose not Match >>>--\n")
        insertPassword(message)


def insertUsrData():
    firstname = insertName("Please Enter Your Firstname: ")
    lastname = insertName("Please Enter Your Lastname: ")
    email = insertEmail("Please Enter Your E-mail: ")
    password = insertPassword("Please Enter Your Password: ")
    phone = insertPhone("Please Enter Your Phone Number : ")
    return firstname, lastname, email, password, phone


def idCreation():
    id = round(time.time())
    return id


def registration():
    userinfo = list(insertUsrData())
    id = idCreation()
    userinfo.insert(0, str(id))
    userinfo = ":".join(userinfo)
    new_user = saveRegistration(userinfo)
    if new_user:
        print("*** Registration Complete ***")
    else:
        print("*** Registration Failed ***")
        return registration()
