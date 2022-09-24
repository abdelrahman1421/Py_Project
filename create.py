from insert import insertDetails,generate_id

def createNewProject(usermail):
    print("\n\t --<<< Create a New Project >>>--\n")
    projectinfo = list(insertDetails(usermail))
    id = generate_id()
    projectinfo.insert(0, str(id))
    projectinfo = ":".join(projectinfo)
    print(projectinfo)
    new_project = ProjectMeta(projectinfo)

    if new_project:
        print("Project Created Successfully")
    else:
        print("Failed To Create New Project")
        return createNewProject()


def ProjectMeta(prInfo):
    try:
        proinfo = open("projects_meta.txt", "a")
    except:
        print("Error Creating New Project")
        return False
    else:
        proinfo.write(f"{prInfo}\n")
        return True


def viewPrFromFile():
    try:
        projobj = open("projects_meta.txt", "r")
    except Exception as e:
        print("Error In Opening ")
        return False
    else:
        projects = projobj.readlines()
        projobj.close()
        return projects

def serPrUsingId(project_id, usermail):
    allproject = viewPrFromFile()

    for project in allproject:
        myproject = project.strip("\n")
        myproject = myproject.split(":")

        if myproject[0] == project_id and myproject[6] == usermail:
            project_index = allproject.index(project)

            print(f"Project is found with index {project_index}")
            return True, project_index

    else:
        print("Project Not found")
        return False


def savePrList(projectlist):
    try:
        proj = open("projects_meta.txt", "w")
    except Exception as e:
        print("Error While Oppening")
        return False
    else:
        proj.writelines(projectlist)
        proj.close()
        return True
