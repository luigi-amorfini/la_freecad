import FreeCADGui
import FreeCAD
from FreeCAD import Base
import Part
import math

class Bolt:
    def __init__(self, obj, name):
        self.name = name
        # Add some custom properties to the feature
        obj.addProperty("App::PropertyString","name","Bolt","Nome").name=name
        obj.addProperty("App::PropertyLength","d","Bolt","Nominal diameter").d=10.0
        obj.addProperty("App::PropertyLength","L","Bolt","Length of the bolt").L=50.0
        obj.addProperty("App::PropertyLength","K","Bolt","Height of the head of the bolt").K=6.4
        obj.addProperty("App::PropertyLength","S","Bolt","Width of the head of the nut").S=17.0
        obj.addProperty("App::PropertyLength","m","Bolt","Height of the nut").m=8.0
        obj.addProperty("App::PropertyLength","DistanceNutFromHead","Bolt","Distance of the nut from the head").DistanceNutFromHead=30.0
        obj.addProperty("App::PropertyLength","WasherDiameterExternal","Bolt","External diameter of washer").WasherDiameterExternal=22.0
        obj.addProperty("App::PropertyLength","WasherDiameterInternal","Bolt","External diameter of washer").WasherDiameterInternal=11.0
        obj.addProperty("App::PropertyLength","WasherThickness","Bolt","Thickness of the washer").WasherThickness=2.0
        obj.addProperty("App::PropertyBool","WasherUp","Bolt","Washer up").WasherUp=True
        obj.addProperty("App::PropertyBool","WasherDown","Bolt","Washer down").WasherDown=True
        obj.addProperty("App::PropertyBool","Accuracy","Bolt","Accuracy").Accuracy=False
        obj.Proxy = self

    def execute(self, fp):
        r = (fp.S/2) / math.cos( math.pi/6 )

        Solid = Part.makeCylinder( fp.d/2, fp.L )
        DT = fp.L
        if fp.WasherUp:
            DT -= fp.WasherThickness
        Solid.translate( Base.Vector(0,0,-DT) )

        if fp.K!=0:
            vertexes = []
            for i in range(0,7):
                vertexes.append(Base.Vector( r * math.cos(math.pi/6+i*math.pi/3), r * math.sin(math.pi/6+i*math.pi/3),0))
            Shape=Part.makePolygon(vertexes)
            Wire = Part.Wire(Shape.Edges)
            Face = Part.Face(Wire)
            NutSolid = Face.extrude(Base.Vector(0,0,fp.K))

            if fp.Accuracy:
                vertexes = []
                vertexes.append(Base.Vector(fp.S/2,0,fp.K))
                xTop = r * 1.1
                zTop = fp.K * 1.1
                vertexes.append(Base.Vector(fp.S/2,0,zTop))
                vertexes.append(Base.Vector(xTop,0,zTop))
                vertexes.append(Base.Vector(xTop,0, fp.K-(r-fp.S/2)*math.tan(math.pi/6.0)))
                vertexes.append(Base.Vector(r,0, fp.K-(r-fp.S/2)*math.tan(math.pi/6.0)))
                vertexes.append(Base.Vector(fp.S/2,0,fp.K))
                CutShape = Part.makePolygon(vertexes)
                CutWire = Part.Wire(CutShape.Edges)
                CutFace = Part.Face(CutWire)
                CutSolid = CutFace.revolve(Base.Vector(0,0,0), Base.Vector(0,0,1),360 )
                NutSolid = NutSolid.cut(CutSolid)
                vertexes = []
                vertexes.append(Base.Vector(fp.S/2,0,0))
                vertexes.append(Base.Vector(r,0,0))
                vertexes.append(Base.Vector(r,0, (r-fp.S/2)*math.tan(math.pi/6.0)))
                vertexes.append(Base.Vector(fp.S/2,0,0))
                CutShape=Part.makePolygon(vertexes)
                CutWire = Part.Wire(CutShape.Edges)
                CutFace = Part.Face(CutWire)
                CutSolid = CutFace.revolve(Base.Vector(0,0,0), Base.Vector(0,0,1),360 )
                NutSolid = NutSolid.cut(CutSolid)
            if fp.WasherUp:
                NutSolid.translate( Base.Vector(0,0,fp.WasherThickness) )
            Solid = Solid.fuse(NutSolid)

        if fp.WasherUp:
            Washer = Part.makeCylinder( fp.WasherDiameterExternal/2, fp.WasherThickness )
            Washer.cut( Part.makeCylinder( fp.WasherDiameterInternal/2, fp.WasherThickness ) )
            Solid = Solid.fuse(Washer)

        if fp.WasherDown:
            Washer = Part.makeCylinder( fp.WasherDiameterExternal/2, fp.WasherThickness )
            Washer.cut( Part.makeCylinder( fp.WasherDiameterInternal/2, fp.WasherThickness ) )
            Washer.translate( Base.Vector(0,0,-(fp.DistanceNutFromHead+fp.WasherThickness) ) )
            Solid = Solid.fuse(Washer)

        if fp.m!=0:
            vertexes = []
            for i in range(0,7):
                vertexes.append(Base.Vector( r * math.cos(math.pi/6+i*math.pi/3), r * math.sin(math.pi/6+i*math.pi/3),0))
            Shape=Part.makePolygon(vertexes)
            Wire = Part.Wire(Shape.Edges)
            Face = Part.Face(Wire)
            NutSolid = Face.extrude(Base.Vector(0,0,fp.m))

            if fp.Accuracy:
                vertexes = []
                vertexes.append(Base.Vector(fp.S/2,0,fp.m))
                vertexes.append(Base.Vector(r,0,fp.m))
                vertexes.append(Base.Vector(r,0, fp.m-(r-fp.S/2)*math.tan(math.pi/6.0)))
                vertexes.append(Base.Vector(fp.S/2,0,fp.m))
                CutShape=Part.makePolygon(vertexes)
                CutWire = Part.Wire(CutShape.Edges)
                CutFace = Part.Face(CutWire)
                CutSolid = CutFace.revolve(Base.Vector(0,0,0), Base.Vector(0,0,1),360 )
                NutSolid = NutSolid.cut(CutSolid)
                vertexes = []
                vertexes.append(Base.Vector(fp.S/2,0,0))
                vertexes.append(Base.Vector(r,0,0))
                vertexes.append(Base.Vector(r,0, (r-fp.S/2)*math.tan(math.pi/6.0)))
                vertexes.append(Base.Vector(fp.S/2,0,0))
                CutShape=Part.makePolygon(vertexes)
                CutWire = Part.Wire(CutShape.Edges)
                CutFace = Part.Face(CutWire)
                CutSolid = CutFace.revolve(Base.Vector(0,0,0), Base.Vector(0,0,1),360 )
                NutSolid = NutSolid.cut(CutSolid)
            DT = fp.DistanceNutFromHead+fp.m
            if fp.WasherDown:
                DT += fp.WasherThickness
            NutSolid.translate( Base.Vector(0,0,-DT ) )
            Solid = Solid.fuse(NutSolid)

        fp.Shape = Solid

class ViewProviderBolt:
    def __init__(self, obj):
        # Set this object to the proxy object of the actual view provider
        obj.Proxy = self

    def getDefaultDisplayMode(self):
        # Return the name of the default display mode. It must be defined in getDisplayModes.
        return "Flat Lines"

def makeBolt(name):
    a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython", name)
    Bolt(a, name)
    ViewProviderBolt(a.ViewObject)
    FreeCAD.ActiveDocument.recompute()
