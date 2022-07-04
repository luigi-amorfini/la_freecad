# -*- coding: utf-8 -*-
import FreeCAD as App
import FreeCADGui as Gui


class Cylinder:

    def __init__(self, name):
        self.name = name
        self.obj = None

    def create(self, Radius , Height , Angle):
        cylinder = App.ActiveDocument.addObject("Part::Cylinder", self.name)
        cylinder.Label = self.name
        cylinder.Radius = Radius
        cylinder.Height = Height
        cylinder.Angle  = Angle
        self.obj = cylinder

    def placement(self, placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))):
        self.obj.Placement = placement
