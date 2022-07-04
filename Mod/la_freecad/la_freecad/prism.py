# -*- coding: utf-8 -*-
import FreeCAD as App
import FreeCADGui as Gui

class Prism:

    def __init__(self, name):
        self.name = name
        self.obj = None

    def create(self, Polygon, Circumradius, Height, FirstAngle, SecondAngle):
        Prism = App.ActiveDocument.addObject("Part::Prism",self.name)
        Prism.Label = self.name
        Prism.Polygon = Polygon
        Prism.Circumradius = Circumradius
        Prism.Height = Height
        Prism.FirstAngle = FirstAngle
        Prism.SecondAngle = SecondAngle

        self.obj = Prism

    def placement(self, placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))):
        self.obj.Placement = placement
