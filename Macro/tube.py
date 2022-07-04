from la_freecad import *

tube1 = Tube("tube1")
print("init tube1")

Diameter, Length, WallThickness = 10, 30, 2


tube1.create(Diameter, Length, WallThickness)
print("create tube1")

tube1.placement(FreeCAD.Placement(App.Vector(100,-50,40), App.Rotation(App.Vector(0,0,0),0), App.Vector(0,0,0)))

print("place tube1")
DocumentOperations.refresh()
print("refresh1")