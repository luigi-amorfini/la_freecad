from la_freecad import *

length,  width, height = 250, 80, 40

box1 = Cube("cubo1")
print("init box")
box1.create(length,  width, height)
print("create box")
box1.placement(FreeCAD.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,0,0),45), App.Vector(0,0,0)))
print("place box")
