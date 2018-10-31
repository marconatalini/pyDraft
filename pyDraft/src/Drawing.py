'''
Created on 29 ott 2018

@author: marco
'''
import comtypes.client

class Drawing(object):
    '''
    Class of the general drawing
    '''

    def __init__(self, filepath):
        '''
        
        '''
        self.filepath = filepath
        self.dsApp = comtypes.client.CreateObject('DraftSight.Application', dynamic = True)
        self.dsApp.AbortRunningCommand()
        self.dsDoc = self.dsApp.NewDocument(r"C:\Users\marco\AppData\Roaming\DraftSight\18.2.3072\Template\Europrofili.dwt")
        self.dsModel = self.dsDoc.GetModel()
        self.dsLayerManager = self.dsDoc.GetLayerManager()
        self.dsSketchManager = self.dsModel.GetSketchManager()
        
    def save(self, newpath = None):
        
        if newpath: self.filepath = newpath
        saveErr = comtypes.c_int()
        
        self.dsDoc.SaveAs2(self.filepath, 4, True, comtypes.byref(saveErr))