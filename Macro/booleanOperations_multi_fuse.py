from la_freecad import *

bool1 =  BooleanOperations("bool1")
print("init bool")
objs = ("cubo1","prism1")
bool1.multi_fuse(objs)
print("fuse objs")