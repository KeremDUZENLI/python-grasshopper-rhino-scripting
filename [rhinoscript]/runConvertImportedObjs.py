import rhinoscriptsyntax as rs
import importObjs
import exportObjs



dir = rs.BrowseForFolder(None, "Select folder to import stl files")
ext = rs.GetString("Extension to convert to", "3ds")

objs = importObjs.Run(dir, "stl")
exportObjs.Run(objs, dir, ext)

rs.DeleteObjects(objs)
