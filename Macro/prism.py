from la_freecad import *

prism1 = Prism("prism1")
print("init prism1")

Polygon, Circumradius, Height, FirstAngle, SecondAngle = 8, 16, 60 , 0, 0

prism1.create(Polygon, Circumradius, Height, FirstAngle, SecondAngle)
print("create prism1")
prism1.placement(FreeCAD.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0)))
print("place prism1")
DocumentOperations.refresh()
print("refresh1")