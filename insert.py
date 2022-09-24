import datetime
import time

def insertNum(message):
    num = input(message)

    try:
        num = int(num)
    except:
        return insertNum(message)
    else:
        return str(num)


def insertString(message):
    string = input(message)

    if string.isspace() or not string:
        print("Please Insert String")
        return insertString(message)

    return string


def insertDetails(usermail):
    title = insertString("Please Enter Title: ")
    details = insertString("Please Enter Details: ")
    totaltarget = insertNum("PLease Enter Total Target: ")
    startdate = insertDate("Please Enter Start Date In This Format (YYYY-MM-DD): ")
    enddate = insertDate("Please Enter End Date In This Format (YYYY-MM-DD): ")
    return title, details, totaltarget, startdate, enddate, usermail


def insertDate(message):
    projdate = input(message)

    try:
        datetime.datetime.strptime(projdate, '%Y-%m-%d')

    except:
        print("Incorrect Format, It's a Must To Be YYYY-MM-DD")
        insertDate(message)

    else:
        return str(projdate)


def generate_id():
    id = round(time.time())
    return str(id)

