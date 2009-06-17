'''
Created on Jun 1, 2009

@author: buubui
'''
from __init__ import *
import sys
import platform
sys.path.append(BASEDIR+'/..')
from PyQt4 import QtCore,QtGui,QtWebKit, QtNetwork
from ui.browser_ui import Ui_MainWindow
from functools import partial
from tabinfo import TabInfo
from mycookiejar import MyCookieJar
from mynetworkaccessmanager import MyNetworkAccessManager
from mywebview import MyWebView,MyWebPage
from ui.myfindtextwidget import MyFindTextWidget
#from gg_translate.gg_translate import GGTranslate
#from FeedReader.feedapp import FeedReader

PROTOCOL=['http://','https://','ftp://']
#URLSLIST=[]
__metaclass__=type
class WebBrowser(QtGui.QMainWindow,Ui_MainWindow):
    '''
    classdocs
    '''
    def changeIcon(self,widget,iconPath):
        icon =QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(iconPath), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        if issubclass(widget.__class__, QtGui.QPushButton): 
            widget.setIcon(icon)
            return 
        if issubclass(widget.__class__, QtGui.QMainWindow) or issubclass(widget.__class__, QtGui.QDialog):
            widget.setWindowIcon(icon)
            return 
        
    def __init__(self):
        '''
        Constructor
        '''
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        #Setup...
        self.findWidget=MyFindTextWidget(self.centralwidget)
        self.layMain.addWidget(self.findWidget)
        self.gg=None
        self.freader=None
#        gg =GGTranslate()
#        self.layMain.addWidget(gg)
#        fd =FeedReader(self)
#        self.layMain.addWidget(fd)
#        self.centralwidget.ins
        self.browserName='uuBrowser'
        self.setWindowTitle(self.browserName)
        self.txtAddress.setText(PROTOCOL[0])
        self.txtAddress.setFocus()
        self.changeIcon(self, pathFromBase('/icons/logo.png'))
        self.changeIcon(self.btnBack, pathFromBase('/icons/go-back.png'))
        self.changeIcon(self.btnForward, pathFromBase('/icons/go-next.png'))
        self.changeIcon(self.btnGo, pathFromBase('/icons/refresh.png'))
        self.btnBack.setDisabled(True)
        self.btnForward.setDisabled(True)
        webbsetting=self.wvDisplay.page().settings()
        webbsetting.setAttribute(QtWebKit.QWebSettings.PluginsEnabled,True)
#        self.networkAccessManager=self.wvDisplay.page().networkAccessManager()
        self.networkAccessManager= MyNetworkAccessManager(self)
        self.wvDisplay.page().setNetworkAccessManager(self.networkAccessManager)
        self.lst =[]
        print QtGui.QDesktopServices.storageLocation(QtGui.QDesktopServices.DataLocation)
#        self.cookieJar =QtNetwork.QNetworkCookieJar()
        self.cookieJar = MyCookieJar(self)
#        self.cookieJar.setAllCookies(self.lst)
        self.networkAccessManager.setCookieJar(self.cookieJar)
#        print 'plugin',a
#        self.proxy = QtNetwork.QNetworkProxy(QtNetwork.QNetworkProxy.HttpProxy,"172.29.2.9",8080)
#        QtNetwork.QNetworkProxy.setApplicationProxy(self.proxy)
#        self.proxy.setType(QtNetwork.QNetworkProxy.NoProxy)
#        QtNetwork.QNetworkProxy.setApplicationProxy(self.proxy)

#        self.wvDisplay.page().networkAccessManager().setProxy(self.proxy)
#===============================================================================
#        networkAccessManager=self.wvDisplay.page().networkAccessManager()
#        manager->get(QNetworkRequest(QUrl("http://qtsoftware.com")));
#===============================================================================
#        self.url =''
        self.wvDisplay.page().setLinkDelegationPolicy(QtWebKit.QWebPage.DelegateAllLinks)
        
#        self.shortHistory=[[]]
#        self.pointer=[0]
        self.tabWidget.setProperty('tabsClosable',QtCore.QVariant(1))
        self.tabWidget.setProperty('movable',QtCore.QVariant(1))
#        self.tabWidget.setProperty('documentMode',QtCore.QVariant(1))
#        self.webViews=[] # list of WebViews
#        self.webViews.append(self.wvDisplay)
        self.tabsList={}
        self.tabsList[self.tab1]= TabInfo(self.wvDisplay)
        self.currTab=0
        
        self.hideFind()
#        self.tabsList[self.tabWidget.currentWidget()].insertUrl("added")
        #Connect signals- slots
        self.connectGlobal()
        self.connectTab()
        
    def connectGlobal(self):
#        self.createAction=QtGui.QAction(self.tr('New &Tab'), self)
#        self.createAction.setObjectName("createAction")
#        self.createAction.setShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL+QtCore.Qt.Key_T))
#        self.actionNew_Tab.setShortcut(QtGui.QKeySequence(QtCore.Qt.CTRL+QtCore.Qt.Key_T))
        self.connect(self.txtAddress,QtCore.SIGNAL('returnPressed()'),self.btnGo.click)
#        self.connect(self.txtAddress,QtCore.SIGNAL('mouseDoubleClickEvent()'),self.mousePress)
#        self.connect(self.txtAddress,QtCore.SIGNAL('doubleClick'),self.mousePress)
        self.connect(self.tabWidget,QtCore.SIGNAL('currentChanged(int)'),self.changedTab)
#        self.connect(self.actionNew_Tab,QtCore.SIGNAL('activated()'),self.createNewTab)
        self.connect(self.actionNew_Tab,QtCore.SIGNAL('triggered()'),self.createNewTab)
#        self.connect(self.createAction,QtCore.SIGNAL('activated()'),self.createNewTab)
        self.connect(self.actionOpen,QtCore.SIGNAL('activated()'),self.info)
        self.connect(self.tabWidget,QtCore.SIGNAL('tabCloseRequested(int)'),self.closeTab)
#        self.connect(self.tabWidget.tabBar(),QtCore.SIGNAL('mouseDoubleClickEvent ( QMouseEvent * )'),self.doubleClickTab)
        self.connect(self.tabWidget,QtCore.SIGNAL('doubleClick'),self.createNewTab)
#        self.connect(self.btnSearch,QtCore.SIGNAL('clicked()'),self.search)
        self.connect(self.txtSearch,QtCore.SIGNAL('returnPressed()'),self.search)
        self.connect(self.networkAccessManager,QtCore.SIGNAL('sslErrors(QNetworkReply*, constQList<QSslError>&)'),self.sslErrors)
        self.connect(self.action_Find,QtCore.SIGNAL('triggered()'),self.showFind)
        self.connect(self.btnCloseFind,QtCore.SIGNAL('clicked()'),self.hideFind)
        self.connect(self.action_Google_Translator,QtCore.SIGNAL('triggered(bool)'),self.tool_ggTranslator)
        self.connect(self.action_Feed_Reader,QtCore.SIGNAL('triggered(bool)'),self.tool_feedReader)
        self.connect(self.actionAbout,QtCore.SIGNAL('triggered()'),self.aboutBrowser)
        self.connect(self.actionAbout_Qt,QtCore.SIGNAL('triggered()'),partial(QtGui.QMessageBox.aboutQt,self))
    def connectTab(self,tab=None):
        if not tab:
            tab= self.tabWidget.currentWidget()
            
        
        self.connect(self.btnBack,QtCore.SIGNAL('clicked()'),partial(self.navigateButton,tab,-1))
        self.connect(self.btnForward,QtCore.SIGNAL('clicked()'),partial(self.navigateButton,tab,1))
        self.connect(self.tabsList[tab].webView(),QtCore.SIGNAL('urlChanged(QUrl)'),partial(self.urlChanged,tab))
        self.connect(self.tabsList[tab].webView(),QtCore.SIGNAL('loadStarted()'),partial(self.loadStarted,tab))
        self.connect(self.tabsList[tab].webView(),QtCore.SIGNAL('loadFinished(bool)'),partial(self.loadFinished,tab))
        self.connect(self.tabsList[tab].webView(),QtCore.SIGNAL('loadProgress(int)'),partial(self.loadProgress,tab))
        self.connect(self.btnGo,QtCore.SIGNAL('clicked()'),partial(self.loadUrl,tab))
        self.connect(self.tabsList[tab].webView(),QtCore.SIGNAL('linkClicked(const QUrl&)'),partial(self.loadUrl,tab))
#        self.connect(self.tabsList[tab].webView(),QtCore.SIGNAL('linkClicked(const QUrl&)'),partial(self.urlChanged, tab))
        self.connect(self.tabsList[tab].webView(),QtCore.SIGNAL('linkClicked(const QUrl&)'),self.changeAdressBar)
        self.connect(self.tabsList[tab].webView().page(),QtCore.SIGNAL('linkHovered(QString,QString,QString)'),self.hoverLink)
        self.connect(self.tabsList[tab],QtCore.SIGNAL('pointerChanged'),partial(self.controlNavigator,tab))
        self.connect(self.txtFind,QtCore.SIGNAL('returnPressed()'),partial(self.findText,tab))
#        self.connect(self.btnBack,QtCore.SIGNAL('clicked()'),partial(self.navigateButton,self.tabWidget.currentWidget(),-1))
#        self.connect(self.btnForward,QtCore.SIGNAL('clicked()'),partial(self.navigateButton,self.tabWidget.currentWidget(),1))
#        self.connect(self.tabsList[self.tabWidget.currentWidget()].webView(),QtCore.SIGNAL('urlChanged(QUrl)'),partial(self.urlChanged,self.tabWidget.currentWidget()))
#        self.connect(self.tabsList[self.tabWidget.currentWidget()].webView(),QtCore.SIGNAL('loadStarted()'),partial(self.loadStarted,self.tabWidget.currentWidget()))
#        self.connect(self.tabsList[self.tabWidget.currentWidget()].webView(),QtCore.SIGNAL('loadFinished(bool)'),partial(self.loadFinished,self.tabWidget.currentWidget()))
#        self.connect(self.tabsList[self.tabWidget.currentWidget()].webView(),QtCore.SIGNAL('loadProgress(int)'),partial(self.loadProgress,self.tabWidget.currentWidget()))
#        self.connect(self.tabsList[self.tabWidget.currentWidget()].webView(),QtCore.SIGNAL('linkClicked(const QUrl&)'),self.loadUrl)
##        self.connect(self.tabsList[self.tabWidget.currentWidget()].webView(),QtCore.SIGNAL('linkClicked(const QUrl&)'),partial(self.urlChanged, self.tabWidget.currentWidget()))
#        self.connect(self.tabsList[self.tabWidget.currentWidget()].webView(),QtCore.SIGNAL('linkClicked(const QUrl&)'),self.changeAdressBar)
#        self.connect(self.tabsList[self.tabWidget.currentWidget()].webView().page(),QtCore.SIGNAL('linkHovered(QString,QString,QString)'),self.hoverLink)
#        self.connect(self.tabsList[self.tabWidget.currentWidget()],QtCore.SIGNAL('pointerChanged'),partial(self.controlNavigator,self.tabWidget.currentWidget()))
    def tool_ggTranslator(self,checked):
        print 'check=',checked
#        if not self.gg:
#            self.gg =GGTranslate()
#            self.layMain.addWidget(self.gg)
#        if self.gg.isHidden():
#            self.gg.show()
#        else:
#            self.gg.hide()
    def tool_feedReader(self):
        print 'feedreader'
#        if not self.freader:
#            self.freader = FeedReader(self.centralwidget)
#            self.layMain.addWidget(self.freader)
#        if self.freader.isHidden():
#            self.freader.show()
#        else:
#            self.freader.hide()
    
    def hideFind(self):
        self.lbFind.hide()
        self.txtFind.hide()
        self.btnCloseFind.hide()
        self.lbNotFound.hide()
        self.lbFound.hide()
    def showFind(self):
        if not self.btnCloseFind.isHidden():
            return self.hideFind()
        self.txtFind.show()
        self.lbFind.show()
        self.btnCloseFind.show()
        self.txtFind.selectAll()
        self.txtFind.setFocus()
        self.lbFound.show()
    def findText(self,tab,text=None,flags=None):
        self.lbNotFound.hide()
        if not text:
            
            text=self.txtFind.text()
            if flags:
                flags= QtWebKit.QWebPage.FindWrapsAroundDocument|flags
            else:
                    flags= QtWebKit.QWebPage.FindWrapsAroundDocument
        found=self.tabsList[tab].webView().page().findText(text, flags)
#        print text,self.txtFind.text()
#        print 'findText:',found
#        self.txtFind.hide()
        if not found:
            self.lbNotFound.show()
            self.lbFound.hide()
        else:
            self.lbNotFound.hide()
            self.lbFound.show()
        return found
    def sslErrors(self,rely, errors):
        print 'sslErrors',rely,errors
    
    def controlNavigator(self,tab, value):
        print 'value=', value
        if value>1:
            self.btnBack.setDisabled(False)
        else:self.btnBack.setDisabled(True)
        if value<self.tabsList[tab].getSize():
            self.btnForward.setDisabled(False)
        else: self.btnForward.setDisabled(True)
    def doubleClickTab(self,event):
        print event
    
    def info(self):
        print self.tabsList[self.tabWidget.currentWidget()].getTop()
    def closeTab(self,index):
        if self.tabWidget.count()==1:
            return 
        tab = self.tabWidget.widget(index)
        self.tabsList[tab].webView().stop()
        del self.tabsList[tab]
        self.tabWidget.removeTab(index)

    def changedTab(self,index):
#        print index
#        self.currTab = index
        print 'tabChanged'
        print self.tabWidget.currentIndex()
        currTab=self.tabsList[self.tabWidget.currentWidget()]
        title=addr=''
        if len(currTab.history())>0:
            addr= str(currTab.getTop().toString())
            title=currTab.webView().title()
        else:
            title=addr= 'about:blank'
        self.txtAddress.setText(addr)
        self.setWindowTitle(title+' - '+self.browserName)
        self.txtAddress.selectAll()
        currTab.changePointer()
        print 'pointer=',currTab.pointer()
    def createNewTab(self,mouseEvent=None):
        if mouseEvent:
            pos =mouseEvent.pos()
            y=pos.y()
            h= self.tabWidget.tabBar().height()
            if y>h: return  
        ''' create new tab'''
#        self.tabWidget.addTab()
#        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
#        self.tabWidget.setObjectName("tabWidget")
        print 'new tab'
        newtab = QtGui.QWidget()
        newtab.setObjectName("tab"+str(self.tabWidget.count()+1))
        verticalLayout = QtGui.QVBoxLayout(newtab)
        verticalLayout.setSpacing(0)
        verticalLayout.setMargin(0)
        verticalLayout.setObjectName("verticalLayout")
        wvDisplay = MyWebView(newtab)
        wvDisplay.setUrl(QtCore.QUrl("about:blank"))
        wvDisplay.setObjectName("wvDisplay"+str(self.tabWidget.count()+1))
        wvDisplay.page().setLinkDelegationPolicy(QtWebKit.QWebPage.DelegateAllLinks)
#==================================Enable plugins===============================
        webbsetting=wvDisplay.page().settings()
        webbsetting.setAttribute(QtWebKit.QWebSettings.PluginsEnabled,True)
#===============================================================================
        verticalLayout.addWidget(wvDisplay)
        self.tabWidget.addTab(newtab, "about:blank")
        self.tabsList[newtab]=TabInfo(wvDisplay)
        
        self.connectTab(newtab)
        self.tabWidget.setCurrentWidget(newtab)

    def navigateButton(self,tab, step):
        if tab != self.tabWidget.currentWidget():
            return
        print step
#        nxt= self.pointer[self.currTab]-1+step
#        if nxt<0 or nxt>=len(self.shortHistory[self.currTab]):
#            print 'out of range.'
#            return 
#        self.pointer[self.currTab]=nxt+1
#        print self.shortHistory[self.currTab][nxt].toString()
        if not self.tabsList[tab].move(step):
            print 'out'
            return 
#        if self.tabsList[tab].pointer()==0:
#            self.btnBack.setDisabled(True)
        self.txtAddress.setText(self.tabsList[tab].getTop().toString())
        self.tabsList[tab].stop()
        self.tabsList[tab].reloadTop()
#        self.webViews[self.currTab].load(self.shortHistory[self.currTab][nxt])
    
    def changeAdressBar(self):
#        self.txtAddress.setText(self.url)
        self.txtAddress.setFocus()
        self.txtAddress.selectAll()
    def getUrl(self):
        txt = self.txtAddress.text()
        if(txt):
            urlcorrect=False
            for x in PROTOCOL:
                if x in txt:
                    urlcorrect=True
                    break
            if not urlcorrect:
                txt= PROTOCOL[0]+txt
            self.url=txt
            return QtCore.QUrl(txt)
        else:
            return None
    def loadUrl(self,tab, url=None):
        if not url:
            url = self.getUrl()
        else:
            print url
            url=QtCore.QUrl(url)
            if tab == self.tabWidget.currentWidget():
                self.txtAddress.setText(url.toString())
        print 'self.lst',self.lst
        self.tabsList[self.tabWidget.currentWidget()].insertUrl(url)
#            print self.tabsList[self.tabWidget.currentWidget()].getTop()
#            self.webViews[self.currTab].load(url)
        self.tabsList[self.tabWidget.currentWidget()].load(url)
        
#        self.btnBack.setDisabled(False)
#        self.btnForward.setDisabled(True)
#            print 'zzz', self.tabsList[self.tabWidget.currentWidget()].getTop()
#            self.setWindowTitle(str(url.toString())+' - '+self.browserName)
        self.txtAddress.selectAll()
#        del self.shortHistory[self.currTab][self.pointer[self.currTab]:]
#        self.pointer[self.currTab]+=1
#        self.shortHistory[self.currTab].append(url)
        
#        print 'aaaaaaaaaaaa',self.tabsList[self.tabWidget.currentWidget()].history(), self.tabsList[self.tabWidget.currentWidget()].pointer()
    def urlChanged(self, tab, url):
        if not tab:
            return 
#        print self.lst
#        self.tabsList[tab].setTop(url)
#        strUrl= str(url.toString())
#        print strUrl
#        self.url=strUrl
#        self.statusbar.showMessage(self.currentStatusMsg()+strUrl)
    def loadStarted(self,tab):
#        self.setTitled=False
        self.tabsList[tab].setTitle(False)
    def loadFinished(self,tab,ok):
        
#        print self.tabsList[self.tab1].getTop()
        
        msg=''
        if not ok:
            msg='Error!'
#            self.tabsList[tab].setMessage('Error!')
#            self.statusbar.showMessage('Error!')
        else:
            msg='Finished.'
#            self.tabsList[tab].setMessage('Finished')
#            self.statusbar.showMessage('Finished.',300)
        self.tabsList[tab].setMessage(msg)
        
        if not self.tabsList[tab].titled():
            self.setTitle(tab)
            self.tabsList[tab].setTitle(True)
            
        ls=self.cookieJar.allCookies()
#        for x in ls:
#            if x.isSessionCookie ():
#            print x.name(),x.domain(),x.isSecure(),x.isSessionCookie(),x.value(), x.expirationDate()

    def loadProgress(self,tab,process):
#        print 'loading'
#        print process, unicode(self.tabsList[tab].webView().title())
#        print  self.url
        if not self.tabsList[tab].titled() and process>10 :
#            print process,self.tabsList[tab].webView().title()
            self.setTitle(tab)
#            self.setTitled=True
        if tab == self.tabWidget.currentWidget():
            strProcess = str(process)
    #        print  strProcess
            self.statusbar.showMessage('Loading'+' ('+strProcess+'%)...'+str(self.tabsList[tab].getTop().toString()))
    def currentStatusMsg(self):
        return str(self.statusbar.currentMessage())
#        self.statusbar.showMessage(self.statusBar())
    def hoverLink(self, link,title,textContent ):
#        print 'link=',link, 'title=',title, 'textContent=',textContent
        self.statusbar.showMessage(link)
    def setTitle(self,tab):
        title= unicode(self.tabsList[tab].webView().title())
#        print self.tabWidget.currentIndex()
#        self.tabWidget.setTabText(self.tabWidget.currentIndex(),title)
        self.tabWidget.setTabText(self.tabWidget.indexOf(tab),title[:20])
        if tab == self.tabWidget.currentWidget():
            self.setWindowTitle(title+' - '+self.browserName)
        self.tabsList[tab].setTitle(True)
    def search(self):
        q= u'http://www.google.com/search?q='+unicode(self.txtSearch.text())
        url= QtCore.QUrl(q)
        self.txtAddress.setText(q)
        self.loadUrl(url)
    def aboutBrowser(self):
        author=''
        for x in __author__:
            author+='<p>'+x+'<br>('+__author__[x]+')'
        QtGui.QMessageBox.about(self, "About uuBrowser",
                '''<center><b>A simple web browser based on QtWebkit</b> 
                <p>Version: {0}
                <p>Copyright &copy; 2009 . 
                All rights reserved.
                {5}
                <p>Python {1} - Qt {2} - PyQt {3} on {4}
                </center>'''.format(
                __version__, platform.python_version(),
                QtCore.QT_VERSION_STR, QtCore.PYQT_VERSION_STR,
                platform.system(),author))
if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    window= WebBrowser()
    window.show()
    sys.exit(app.exec_())