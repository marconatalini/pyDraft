'''
Created on 31 ott 2018

@author: marco
'''
import array

class Structure(object):
    '''
    Classe di definizione della lamiera su struttura
    '''


    def __init__(self, drawing, larghezza, altezza, larghezza_profilo = 51.0, model = "Ambra 1"):
        '''
        Constructor
        '''
        self.drawing = drawing #doc obj
        self.l = larghezza
        self.h = altezza
        self.lp = larghezza_profilo
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.model = model
        
    def baseStructure(self):
        lp = self.lp
        x = self.x
        y = self.y
        z = self.z
        l = self.l
        h = self.h
        
        LayerStruttura = self.drawing.dsLayerManager.GetLayer("AK5110F")
        LayerStruttura.Activate()
        
        Coordinates1 = array.array('d',(x,h,x,y,l,y,l,h))
        plineExt = self.drawing.dsSketchManager.InsertPolyline2D(Coordinates1, True )
        
        Coordinates2 = array.array('d',(x+lp,h-lp,x+lp,y+lp,l-lp,y+lp,l-lp,h-lp))
        plineInt = self.drawing.dsSketchManager.InsertPolyline2D(Coordinates2, True )
        
        line1 = self.drawing.dsSketchManager.InsertLine( x, y, z, x+lp, y+lp, z)
        line2 = self.drawing.dsSketchManager.InsertLine( x, h, z, x+lp, h-lp, z)
        line3 = self.drawing.dsSketchManager.InsertLine( l, y, z, l-lp, y+lp, z)
        line4 = self.drawing.dsSketchManager.InsertLine( l, h, z, l-lp, h-lp, z)
            
        codice = 'AK5110F'
        htext = int(lp*0.8)        
        note1 = self.drawing.dsSketchManager.InsertSimpleNote(l/2, lp/2, z, htext, 0.0 , codice)
        note2 = self.drawing.dsSketchManager.InsertSimpleNote(lp/2, h/2, z, htext, 1.57079632679490 , codice)
        note3 = self.drawing.dsSketchManager.InsertSimpleNote(l/2, h-lp/2, z, htext, 0.0 , codice)
        note4 = self.drawing.dsSketchManager.InsertSimpleNote(l-lp/2, h/2, z, htext, 1.57079632679490 , codice)
    
        for t in [note1, note2, note3, note4]:
            t.Justify = 11 #dsTextJustification_MiddleCenter
            t.TextStyle = "CodiciProfili"
            #t.Layer = "AK5110F" 
            
        
    def verticalBaseStruct(self):
        lp = self.lp

        z = self.z
        l = self.l
        h = self.h
        
        LayerStruttura = self.drawing.dsLayerManager.GetLayer("AK5110F")
        LayerStruttura.Activate()
        
        codice = 'AK5110F'
        htext = int(lp*0.8)
        
        nSupporti = int(round((l-lp*2)/350.0,0))
        ls = ((l-2*lp)-(lp*nSupporti))/(nSupporti + 1) #Luce tra i supporti
        print nSupporti, ls, l-2*lp 
    
        for s in range(nSupporti):
            lss = lp + ls * (s+1) + lp *s
            Coordinates1 = array.array('d',(lss,h-lp,lss,lp,lss+lp,lp,lss+lp,h-lp))
            plineSupp = self.drawing.dsSketchManager.InsertPolyline2D(Coordinates1, True )
            note2 = self.drawing.dsSketchManager.InsertSimpleNote(lss+lp/2, h/2, z, htext, 1.57079632679490 , codice)
            note2.Justify = 11 #dsTextJustification_MiddleCenter
            note2.TextStyle = "CodiciProfili"
    
    def horizontalBaseStruct(self):
        lp = self.lp

        z = self.z
        l = self.l
        h = self.h
        
        LayerStruttura = self.drawing.dsLayerManager.GetLayer("AK5110F")
        LayerStruttura.Activate()
        
        codice = 'AK5110F'
        htext = int(lp*0.8)
        
        nSupporti = int(round((h-lp*2)/350.0,0))
        hs = ((h-2*lp)-(lp*nSupporti))/(nSupporti + 1) #Luce tra i supporti
        print nSupporti, hs, h-2*lp 
        
        for s in range(nSupporti):
            hss = lp + hs * (s+1) + lp *s
            Coordinates1 = array.array('d',(lp,hss+lp,l-lp,hss+lp,l-lp,hss+2*lp,lp,hss+2*lp))
            plineSupp = self.drawing.dsSketchManager.InsertPolyline2D(Coordinates1, True )
            note2 = self.drawing.dsSketchManager.InsertSimpleNote(l/2, lp+hss+lp/2, z, htext, 0.0 , codice)
            note2.Justify = 11 #dsTextJustification_MiddleCenter
            note2.TextStyle = "CodiciProfili"
            