import re
from chose import menu


def insertMail(message):
    email = input(message)
    emailPattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"

    if re.match(emailPattern, email):
        return str(email)
    else:
        print("\n\t--<<< Invalid Email >>>--\n")
        return insertMail(message)


def saveRegistration(infodetails):
    try:
        regchdata = open("login_data.txt", "a")
    except:
        print("Error In registration ")
        return False
    else:
        regchdata.write(f"{infodetails}\n")
        return True


def login():
    print("\n\t\t --<<< Loging Page >>>-- \n")
    email = insertMail("Enter Your E-mail: ")
    password = input("Enter Your Password: ")

    try:
        logindata = open("login_data.txt", "r")
    except Exception as e:
        print(" Error reading the file  ")
    else:

        credintials = logindata.readlines()
        logindata.close()

        for info in credintials:
            mydata = info.strip("\n")
            mydata = mydata.split(":")

            if mydata[3] == str(email) and mydata[4] == str(password):
                print("\n\t\t--<<< Welcome >>>--\n")

                return menu(email)


        else:
            print("E-mail or Password Dose not Match Please Check Them ")
            login()
