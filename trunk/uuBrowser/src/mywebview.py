'''
Created on Jun 17, 2009

@author: buubui
'''
from PyQt4 import QtCore,QtGui,QtWebKit, QtNetwork
class MyWebPage(QtWebKit.QWebPage):
    '''
    classdocs
    '''
    def __init__(self,parent=None):
        QtWebKit.QWebPage.__init__(self,parent)
class MyWebView(QtWebKit.QWebView):
    '''
    classdocs
    '''


    def __init__(self,parent):
        '''
        Constructor
        '''
        QtWebKit.QWebView.__init__(self,parent)