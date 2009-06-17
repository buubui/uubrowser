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
    def pointer(self):
        return self._pointer
    def getSize(self):
        return len(self._history)
    def getTop(self):
        return self._history[self._pointer-1]
    def stop(self):
        self._webview.stop()
    def move(self,step):
        nxt= self._pointer-1+step
        if nxt<0 or nxt>=len(self._history):
            print 'out of range.'
            return False
        self._pointer=nxt+1
        self.changePointer()
        return True
#        print self.shortHistory[self.currTab][nxt].toString()
    def insertUrl(self,url=None):
        if not url:
            url=self.webView().url()
        del self._history[self._pointer:]
        self._history.append(url)
        self._pointer+=1
        self.changePointer()
    def load(self,url):
        self._webview.load(url)
    def reloadTop(self):
        self.load(self.getTop())
    def titled(self):
        return self._titled
    def setTitle(self,value):
        self._titled=value
    def setMessage(self,msg):
        if msg:
            self._msg=msg
    def changePointer(self):
        print 'changed pointer'
        self.emit(QtCore.SIGNAL('pointerChanged'),self._pointer)