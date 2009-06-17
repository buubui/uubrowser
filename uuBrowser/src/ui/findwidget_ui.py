# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'findwidget.ui'
#
# Created: Wed Jun 17 23:10:10 2009
#      by: PyQt4 UI code generator 4.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(348, 44)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnFindClose = QtGui.QPushButton(Form)
        self.btnFindClose.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btnFindClose.setFlat(True)
        self.btnFindClose.setObjectName("btnFindClose")
        self.horizontalLayout.addWidget(self.btnFindClose)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.txtFind = QtGui.QLineEdit(Form)
        self.txtFind.setMaximumSize(QtCore.QSize(130, 16777215))
        self.txtFind.setObjectName("txtFind")
        self.horizontalLayout.addWidget(self.txtFind)
        self.lbNotfound = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbNotfound.sizePolicy().hasHeightForWidth())
        self.lbNotfound.setSizePolicy(sizePolicy)
        self.lbNotfound.setObjectName("lbNotfound")
        self.horizontalLayout.addWidget(self.lbNotfound)
        self.lbFound = QtGui.QLabel(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbFound.sizePolicy().hasHeightForWidth())
        self.lbFound.setSizePolicy(sizePolicy)
        self.lbFound.setObjectName("lbFound")
        self.horizontalLayout.addWidget(self.lbFound)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.btnFindClose, QtCore.SIGNAL("clicked()"), Form.hide)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFindClose.setText(QtGui.QApplication.translate("Form", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Find text:", None, QtGui.QApplication.UnicodeUTF8))
        self.lbNotfound.setText(QtGui.QApplication.translate("Form", "Not found", None, QtGui.QApplication.UnicodeUTF8))

