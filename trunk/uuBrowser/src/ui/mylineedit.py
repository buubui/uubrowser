'''
Created on Jun 17, 2009

@author: buubui
'''
from PyQt4 import QtCore,QtGui

class MyLineEdit(QtGui.QLineEdit):
    '''
    classdocs
    '''


    def __init__(self,parent):
        '''
        Constructor
        '''
        QtGui.QLineEdit.__init__(self,parent)