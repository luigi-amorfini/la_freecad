from la_freecad import *

torus1 = Torus("torus1")
print("init torus1")


Radius1, Radius2, Angle1, Angle2, Angle3 = 10, 8, 0, 0, 180

torus1.create(Radius1, Radius2, Angle1, Angle2, Angle3)
print("create torus1")
torus1.placement(FreeCAD.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0)))
print("place torus1")
DocumentOperations.refresh()
print("refresh1")