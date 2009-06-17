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
        QtGui.QTabWidget.__init__(self,parent)
    def mouseDoubleClickEvent(self,event):
        if event:
            print event
            if event.y() < self.tabBar().height ():
                self.emit(QtCore.SIGNAL('doubleClick'),event)