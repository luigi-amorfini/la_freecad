# -*- coding: utf-8 -*-
import FreeCAD as App
import FreeCADGui as Gui


class Sphere:

    def __init__(self, name):
        self.name = name
        self.obj = None

    def create(self, Radius, Angle1, Angle2, Angle3):
        Sphere = App.ActiveDocument.addObject("Part::Sphere",self.name)
        Sphere.Label = self.name
        Sphere.Radius = Radius
        Sphere.Angle1 = Angle1
        Sphere.Angle2 = Angle2
        Sphere.Angle3 = Angle3

        self.obj = Sphere

    def placement(self, placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))):
        self.obj.Placement = placement
