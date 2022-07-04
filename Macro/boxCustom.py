from la_freecad import *

nome, length,  width, height = "box001", 100, 90, 20

print("init box")
box1 = BoxCustom(nome)
box1.create(length,width,height)
print("create box")
