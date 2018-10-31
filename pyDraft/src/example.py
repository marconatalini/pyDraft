'''
Created on 31 ott 2018

@author: marco
'''

from Drawing import Drawing
from Structure import Structure

dwg = Drawing("panel.dwg")

l = 900
h = 1500

bplst = Structure(dwg,900,2100)

bplst.baseStructure()
bplst.basePanel()

dwg.save()

if __name__ == '__main__':
    pass