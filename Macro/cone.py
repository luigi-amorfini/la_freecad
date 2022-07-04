from la_freecad import *


Radius1, Radius2, Height, Angle = 80, 60, 100, 360

cone1 = Cone("cone1")
print("init cone")
cone1.create(Radius1, Radius2, Height, Angle)
print("create cone")
cone1.placement(FreeCAD.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0)))
print("place cone")
DocumentOperations.refresh()
print("refresh1")