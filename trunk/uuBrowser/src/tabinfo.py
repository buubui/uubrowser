'''
Created on Jun 17, 2009

@author: buubui
'''
from PyQt4 import QtCore
class TabInfo(QtCore.QObject):
    def __init__(self,webview,parent=None):
        QtCore.QObject.__init__(self,parent)
        self._webview=webview
        self._pointer=0
        self._history=[]
        self._titled=False
        self._msg=''
    def webView(self):
        return self._webview
    def history(self):
        return self._history
    def getSize(self):
        return len(self._history)
    def getTop(self):
        return self._history[self._pointer-1]
    def stop(self):
        self._webview.stop()
    def move(self,step):
        nxt= self._pointer-1+step
        if nxt<0 or nxt>=len(self.shortHistory[self.currTab]):
            print 'out of range.'
            return 
        self._pointer=nxt+1
#        print self.shortHistory[self.currTab][nxt].toString()
    def insertUrl(self,url=None):
        if not url:
            url=self.webView().url()
        self._history.append(url)
    def load(self,url):
        self._webview.load(url)
    def titled(self):
        return self._titled
    def setTitle(self,value):
        self._titled=value
    def setMessage(self,msg):
        if msg:
            self._msg=msg