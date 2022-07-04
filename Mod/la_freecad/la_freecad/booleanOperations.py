# -*- coding: utf-8 -*-
import FreeCAD as App
import FreeCADGui as Gui

class BooleanOperations:
    """
        cut,
        fuse,
        difference
    """
    def __init__(self, name):
        self.name = name
        self.obj = None

    def fuse(self, Base , Tool):
        obj = App.ActiveDocument.addObject("Part::Fuse", self.name)
        obj.Base = App.ActiveDocument.getObject(Base)
        obj.Tool = App.ActiveDocument.getObject(Tool)
        App.ActiveDocument.recompute()
        self.obj = obj
        return obj

    def multi_fuse(self, objs):
        shapes = []
        for name in objs:
            shape = App.ActiveDocument.getObject(name) ##Stai passando i nomi non self.name che è nel caso d'esempio "bool1"
            if shape is None:
                pass
            else:
                shapes.append(shape)
            print(shapes)
        if shapes is []:
            print("operazione non riuscita, controlla i nomi passati")
            return None
        else:
            obj = App.ActiveDocument.addObject("Part::MultiFuse", self.name)
            obj.Shapes = shapes
            obj.Refine = True
            App.ActiveDocument.recompute()
            self.obj = obj
            return obj

    def cut(self, Base, Tool):
        obj = App.ActiveDocument.addObject("Part::Cut", self.name)
        obj.Base = App.ActiveDocument.getObject(Base)
        obj.Tool = App.ActiveDocument.getObject(Tool)
        obj.Refine = True
        App.ActiveDocument.recompute()
        self.obj = obj
        return obj

    def multi_common(self, objs):
        shapes = []
        for name in objs:
            shape = App.ActiveDocument.getObject(name) ##Stai passando i nomi non self.name che è nel caso d'esempio "bool1"
            if shape is None:
                pass
            else:
                shapes.append(shape)
            print(shapes)
        if shapes is []:
            print("operazione non riuscita, controlla i nomi passati")
            return None
        else:
            obj = App.ActiveDocument.addObject("Part::MultiCommon",self.name)
            obj.Shapes = shapes
            obj.Refine = True
            App.ActiveDocument.recompute()
            self.obj = obj
            return obj
