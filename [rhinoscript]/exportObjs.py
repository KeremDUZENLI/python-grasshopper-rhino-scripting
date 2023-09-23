import rhinoscriptsyntax as rs
import createBox



def Run(objs, dir, ext):
    rs.EnableRedraw(False)

    for i in range(len(objs)):
        obj = objs[i]

        filepath = dir + "/exported" + str(i) + "." + ext
        rs.SelectObject(obj)
        rs.Command("!_-Export \"" + filepath + "\" -Enter -Enter")
        rs.UnselectAllObjects()

    rs.EnableRedraw(True)



#boxes = createBox.Run(3, 5)
#dir = rs.BrowseForFolder(None, "Select folder to save files")

#Run(boxes, dir, "3dm")
