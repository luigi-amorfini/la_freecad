from la_freecad import *

wedge1 = Wedge("wedge1")
print("init wedge1")

Xmin,Ymin,Zmin,X2min,Z2min,Xmax,Ymax,Zmax,X2max,Z2max = 1 , 2 , 3 , 4 , 6 , 15 , 20 ,  55 , 10 , 12 

wedge1.create(Xmin,Ymin,Zmin,X2min,Z2min,Xmax,Ymax,Zmax,X2max,Z2max)
print("create wedge1")
wedge1.placement(FreeCAD.Placement(App.Vector(100,-50,40), App.Rotation(App.Vector(0,0,0),0), App.Vector(0,0,0)))
print("place wedge1")
DocumentOperations.refresh()
print("refresh1")