# -*- coding: utf-8 -*-
import FreeCAD as App
import FreeCADGui as Gui

class Cone:

    def __init__(self, name):
        self.name = name
        self.obj = None

    def create(self, Radius1, Radius2, Height, Angle):
        Cone = App.ActiveDocument.addObject("Part::Cone", self.name)
        Cone.Label = self.name
        Cone.Radius1 = Radius1
        Cone.Radius2 = Radius2
        Cone.Height = Height
        Cone.Angle = Angle
        self.obj = Cone

    def placement(self, placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))):
        self.obj.Placement = placement
