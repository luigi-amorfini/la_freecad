# -*- coding: utf-8 -*-
import FreeCAD as App
import FreeCADGui as Gui


class Torus:

    def __init__(self, name):
        self.name = name
        self.obj = None

    def create(self, Radius1, Radius2, Angle1, Angle2, Angle3):
        Torus = App.ActiveDocument.addObject("Part::Torus",self.name)
        Torus.Label = self.name
        Torus.Radius1 = Radius1
        Torus.Radius2 = Radius2
        Torus.Angle1 = Angle1
        Torus.Angle2 = Angle2
        Torus.Angle3 = Angle3

        self.obj = Torus

    def placement(self, placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))):
        self.obj.Placement = placement
