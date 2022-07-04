from la_freecad import *

bool1 =  BooleanOperations("bool1")
print("init bool")
objs = ("cubo1","cylinder1")
bool1.multi_common(objs)
print("fuse objs")