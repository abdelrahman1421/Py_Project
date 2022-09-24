from create import viewPrFromFile
def lsProjects():
    projects = viewPrFromFile()

    if projects == False:
        print("No Projects Yet")
    else:
        print(projects)