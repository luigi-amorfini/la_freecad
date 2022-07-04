from la_freecad import *

sphere1 = Sphere("Sphere1")
print("init sphere1")

Radius, Angle1 , Angle2 , Angle3  = 20 , -90, 90, 180
sphere1.create(Radius, Angle1, Angle2, Angle3)

print("create sphere1")

sphere1.placement(FreeCAD.Placement(App.Placement(App.Vector(0,20,20), App.Rotation(App.Vector(0,0,1),-180), App.Vector(0,300,0))))


print("place sphere1")

DocumentOperations.refresh()

print("refresh1")