'''
Created on Jun 8, 2009

@author: buubui
'''

from PyQt4 import QtCore,QtGui
from findwidget_ui import Ui_Form
class MyFindTextWidget(QtGui.QWidget,Ui_Form):
    '''
    classdocs
    '''


    def __init__(self,parent=None):
        '''
        Constructor
        '''
        QtGui.QWidget.__init__(self,parent)
        self.setupUi(self)
        
        
import sys
if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    widget = MyFindTextWidget()
    widget.show()
    sys.exit(app.exec_())