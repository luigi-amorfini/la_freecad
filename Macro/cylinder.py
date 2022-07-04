from la_freecad import *

Radius , Height , Angle = 20, 100, 360

cylinder1 = Cylinder("cylinder1")
print("init cylinder1")
cylinder1.create(Radius , Height , Angle)
print("create cylinder1")
cylinder1.placement(FreeCAD.Placement(App.Vector(40,50,0), App.Rotation(App.Vector(0,0,0),0), App.Vector(0,0,0)))
print("place cylinder1")
DocumentOperations.refresh()
print("refresh1")