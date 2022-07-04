# -*- coding: utf-8 -*-
import FreeCAD as App
import FreeCADGui as Gui


class Cube:

    def __init__(self, name):
        self.name = name
        self.obj = None

    def create(self, length,  width, height):
        cube = App.ActiveDocument.addObject("Part::Box", self.name)
        cube.Label = self.name        
        cube.Length = length
        cube.Width = width
        box.Height = height
        self.obj = cube

    def placement(self, placement=App.Placement(App.Vector(0,0,0), App.Rotation(App.Vector(0,0,1),0), App.Vector(0,0,0))):
        self.obj.Placement = placement
