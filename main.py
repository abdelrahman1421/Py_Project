from register import registration
from check import login

def mainmenu():
    userInput = input("\nPlease Select From Comming:\n <<r>> for REGISTRATION in App \n <<l>> for LOGING if you already have an account")
    
    if userInput == "r":
        registration()
    elif userInput == "l":
        login()
    else:
        print("Not Correct Choice")
        mainmenu()
   
mainmenu()

