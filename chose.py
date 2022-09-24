from del_ed import delProject,edProject
from create import  createNewProject
from list import lsProjects
def menu(usermail):
    choice = input("Please Select From These Options:\n  <<n>> to Create a New Project\n  <<l>> to List All Projects\n  <<e>> to Edit an Existing Project \n  <<d>> to Delete an Existing Project\n")
    
    if choice == "n":
        createNewProject(usermail)
        
    elif choice == "l":
        lsProjects()
        
    elif choice == "e":
        edProject(usermail)
        
    elif choice == "d":
        delProject(usermail)
            
    else:
        print("Not Correct Choice")
        menu()
        


