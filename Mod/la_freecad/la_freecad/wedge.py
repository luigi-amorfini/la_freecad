# -*- coding: utf-8 -*-
import FreeCAD as App
import FreeCADGui as Gui


class Wedge:

    def __init__(self, name):
        self.name = name
        self.obj = None

    def create(self,Xmin,Ymin,Zmin,X2min,Z2min,Xmax,Ymax,Zmax,X2max,Z2max):
        Wedge = App.ActiveDocument.addObject("Part::Wedge",self.name)
        Wedge.Label = self.name
        Wedge.Xmin=Xmin
        Wedge.Ymin=Ymin
        Wedge.Zmin=Zmin
        Wedge.X2min=X2min
        Wedge.Z2min=Z2min
        Wedge.Xmax=Xmax
        Wedge.Ymax=Ymax
        Wedge.Zmax=Zmax
        Wedge.X2max=X2max
        Wedge.Z2max=Z2max
        self.obj = Wedge

    def placement(self, placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))):
        self.obj.Placement = placement
