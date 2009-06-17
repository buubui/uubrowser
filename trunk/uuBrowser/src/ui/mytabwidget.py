'''
Created on Jun 17, 2009

@author: buubui
'''
from PyQt4 import QtCore,QtGui

class MyTabWidget(QtGui.QTabWidget):
    '''
    classdocs
    '''


    def __init__(self,parent):
        '''
        Constructor
        '''
        QtGui.QTableWidget.__init__(self,parent)