import rhinoscriptsyntax as rs
import os



def Run(dir, ext):
    files = []
    importedObjs = []

    for file in os.listdir(dir):
        if file.endswith("." + ext):
            files.append(dir + "/" + file)

    rs.EnableRedraw(False)

    for i in range(len(files)):
        filepath = files[i]

        rs.Command("!_-Import \"" + filepath + "\" -Enter -Enter")
        selectedObjs = rs.SelectedObjects()
        importedObjs.extend(selectedObjs)

    rs.UnselectAllObjects()
    rs.EnableRedraw(True)

    return importedObjs


#dir = rs.BrowseForFolder(None, "Select folder to import files")
#print(len(Run(dir, "3dm")))
