'''
Created on Jun 17, 2009

@author: buubui
'''
from PyQt4 import QtCore,QtGui,QtWebKit, QtNetwork
class MyCookieJar(QtNetwork.QNetworkCookieJar):
    '''
    classdocs
    '''


    def __init__(self,parent=None):
        '''
        Constructor
        '''
        QtNetwork.QNetworkCookieJar.__init__(self,None)