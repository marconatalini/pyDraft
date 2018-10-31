'''
Created on 31 ott 2018

@author: marco
'''
import array

class Panel(object):
    '''
    class for draw panels
    '''

    def __init__(self, drawing, larghezza, altezza, model, struct = None):
        '''
        Constructor
        '''
        self.drawing = drawing #doc obj
        self.l = larghezza
        self.h = altezza
        self.model = model
        
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        
        if struct:
            self.setOnStruct(struct)
        
    def setOnStruct(self, struct):
        self.l = struct.l
        self.h = struct.h
        self.model = struct.model
        
    def basePanel(self):
        x = self.x
        y = self.y
    
        l = self.l
        h = self.h
        
        LayerStruttura = self.drawing.dsLayerManager.GetLayer("lamiera")
        LayerStruttura.Activate()
        
        Coordinates1 = array.array('d',(x,h,x,y,l,y,l,h))
        plineExt = self.drawing.dsSketchManager.InsertPolyline2D(Coordinates1, True )
        
    def quoteBasePanel(self):
        x = self.x
        y = self.y
        z = self.z
    
        l = self.l
        h = self.h
        
        LayerQuote = self.drawing.dsLayerManager.GetLayer("quote_lamiera")
        LayerQuote.Activate()
        
        pql1 = array.array('d',(x,y,z))
        pql2 = array.array('d',(l,y,z))
        pqlq = array.array('d',(l/2,y-200,z))
        ql = self.drawing.dsSketchManager.InsertAlignedDimension(pql1, pql2, pqlq, "")