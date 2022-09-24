from  insert import insertNum,insertDetails
from create import savePrList,serPrUsingId,viewPrFromFile
from list import lsProjects

def delProjectFromFile(project_id, usermail):
    project_found = serPrUsingId(project_id, usermail)

    if project_found:
        project_index = project_found[1]

        allprojects = viewPrFromFile()
        del allprojects[project_index]

        deleted = savePrList(allprojects)
        return deleted


def delProject(usermail):
    lsProjects()
    project_id = insertNum("Please choose id of the book to delete: ")
    deleted = delProjectFromFile(project_id, usermail)

    if deleted:
        print("Project Deleted Successfully")


def edProjectFromFile(project_index, new_info):
    allprojects = viewPrFromFile()
    allprojects[project_index] = f"{new_info}\n"
    updated = savePrList(allprojects)

    if updated:
        print("Project Updated Successfully")


def edProject(usermail):
    lsProjects()
    project_id = insertNum("Enter Project ID To Edit It : ")
    check_founding_project = serPrUsingId(project_id, usermail)

    if check_founding_project:
        new_project_info = list(insertDetails(usermail))
        new_project_info.insert(0, str(project_id))
        new_project_info.insert(6, str(usermail))
        new_info = ":".join(new_project_info)

        edProjectFromFile(check_founding_project[1], new_info)
