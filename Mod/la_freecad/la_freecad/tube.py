# -*- coding: utf-8 -*-
import FreeCAD as App
import FreeCADGui as Gui
import Arch

class Tube:

    def __init__(self, name):
        self.name = name
        self.obj = None

    def create(self, Diameter, Length, WallThickness):
        tube = Arch.makePipe(diameter=Diameter, length=Length,name=self.name)
        tube.WallThickness = WallThickness
        self.obj = tube

    def placement(self, placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))):
        self.obj.Placement = placement
