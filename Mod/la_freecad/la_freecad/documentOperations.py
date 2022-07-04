# -*- coding: utf-8 -*-
import FreeCAD as App
import FreeCADGui as Gui

class DocumentOperations:

    def refresh():
        App.ActiveDocument.recompute()
        Gui.activeDocument().activeView().viewIsometric()
        Gui.SendMsgToActiveView("ViewFit")
