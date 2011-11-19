# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created: Sat Nov 19 23:16:38 2011
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.ui_exec_btn = QtGui.QToolButton(self.centralwidget)
        self.ui_exec_btn.setText(QtGui.QApplication.translate("MainWindow", "Exec Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.ui_exec_btn.setObjectName(_fromUtf8("ui_exec_btn"))
        self.horizontalLayout_2.addWidget(self.ui_exec_btn)
        self.ui_show_btn = QtGui.QToolButton(self.centralwidget)
        self.ui_show_btn.setText(QtGui.QApplication.translate("MainWindow", "Show Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.ui_show_btn.setObjectName(_fromUtf8("ui_show_btn"))
        self.horizontalLayout_2.addWidget(self.ui_show_btn)
        self.ui_count_btn = QtGui.QToolButton(self.centralwidget)
        self.ui_count_btn.setText(QtGui.QApplication.translate("MainWindow", "Show Count", None, QtGui.QApplication.UnicodeUTF8))
        self.ui_count_btn.setObjectName(_fromUtf8("ui_count_btn"))
        self.horizontalLayout_2.addWidget(self.ui_count_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.ui_test_menu = QtGui.QMenu(self.menubar)
        self.ui_test_menu.setTitle(QtGui.QApplication.translate("MainWindow", "Test", None, QtGui.QApplication.UnicodeUTF8))
        self.ui_test_menu.setObjectName(_fromUtf8("ui_test_menu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.ui_exec_act = QtGui.QAction(MainWindow)
        self.ui_exec_act.setText(QtGui.QApplication.translate("MainWindow", "Exec Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.ui_exec_act.setObjectName(_fromUtf8("ui_exec_act"))
        self.ui_show_act = QtGui.QAction(MainWindow)
        self.ui_show_act.setText(QtGui.QApplication.translate("MainWindow", "Show Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.ui_show_act.setObjectName(_fromUtf8("ui_show_act"))
        self.ui_count_act = QtGui.QAction(MainWindow)
        self.ui_count_act.setText(QtGui.QApplication.translate("MainWindow", "Show Count", None, QtGui.QApplication.UnicodeUTF8))
        self.ui_count_act.setObjectName(_fromUtf8("ui_count_act"))
        self.ui_test_menu.addAction(self.ui_exec_act)
        self.ui_test_menu.addAction(self.ui_show_act)
        self.ui_test_menu.addAction(self.ui_count_act)
        self.menubar.addAction(self.ui_test_menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

