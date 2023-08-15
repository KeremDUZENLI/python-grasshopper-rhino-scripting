import rhinoscriptsyntax as rs
import createBox
import exportObjs



xNum = rs.GetInteger("X number", 5, 1)
yNum = rs.GetInteger("Y number", 5, 1)
boxes = createBox.Run(xNum, yNum)


dir = rs.BrowseForFolder(None, "Select folder to save file")
ext = rs.GetString("Type file extension to save", "obj")


exportObjs.Run(boxes, dir, ext)
