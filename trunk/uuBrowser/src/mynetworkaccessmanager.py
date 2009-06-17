'''
Created on Jun 17, 2009

@author: buubui
'''
from PyQt4 import QtCore,QtGui,QtWebKit, QtNetwork
class MyNetworkAccessManager(QtNetwork.QNetworkAccessManager):
    '''
    classdocs
    '''


    def __init__(self,parent=None):
        '''
        Constructor
        '''
        QtNetwork.QNetworkAccessManager.__init__(self,parent)