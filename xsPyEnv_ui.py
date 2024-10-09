# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xsPyEnv.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(529, 494)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 1, 520, 451))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.searchBox = QtWidgets.QLineEdit(self.widget)
        self.searchBox.setObjectName("searchBox")
        self.gridLayout.addWidget(self.searchBox, 0, 0, 1, 1)
        self.searchButton = QtWidgets.QPushButton(self.widget)
        self.searchButton.setObjectName("searchButton")
        self.gridLayout.addWidget(self.searchButton, 0, 1, 1, 1)
        self.pyVersionBox = QtWidgets.QComboBox(self.widget)
        self.pyVersionBox.setObjectName("pyVersionBox")
        self.gridLayout.addWidget(self.pyVersionBox, 1, 0, 1, 1)
        self.createVenvButton = QtWidgets.QPushButton(self.widget)
        self.createVenvButton.setObjectName("createVenvButton")
        self.gridLayout.addWidget(self.createVenvButton, 1, 1, 1, 1)
        self.installedLabel = QtWidgets.QLabel(self.widget)
        self.installedLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.installedLabel.setObjectName("installedLabel")
        self.gridLayout.addWidget(self.installedLabel, 2, 0, 1, 1)
        self.installedView = QtWidgets.QListView(self.widget)
        self.installedView.setObjectName("installedView")
        self.gridLayout.addWidget(self.installedView, 3, 0, 1, 1)
        self.installView = QtWidgets.QListView(self.widget)
        self.installView.setObjectName("installView")
        self.gridLayout.addWidget(self.installView, 3, 1, 1, 1)
        self.statusView = QtWidgets.QTextBrowser(self.widget)
        self.statusView.setMaximumSize(QtCore.QSize(16777215, 100))
        self.statusView.setObjectName("statusView")
        self.gridLayout.addWidget(self.statusView, 4, 0, 1, 2)
        self.installButton = QtWidgets.QPushButton(self.widget)
        self.installButton.setObjectName("installButton")
        self.gridLayout.addWidget(self.installButton, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 529, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuExit = QtWidgets.QMenu(self.menubar)
        self.menuExit.setObjectName("menuExit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionpyenv_win = QtWidgets.QAction(MainWindow)
        self.actionpyenv_win.setObjectName("actionpyenv_win")
        self.actionpyenv_virtualenv = QtWidgets.QAction(MainWindow)
        self.actionpyenv_virtualenv.setObjectName("actionpyenv_virtualenv")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionpyenv_win)
        self.menuEdit.addAction(self.actionpyenv_virtualenv)
        self.menuExit.addSeparator()
        self.menuExit.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuExit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.searchButton.setText(_translate("MainWindow", "SEARCH"))
        self.createVenvButton.setText(_translate("MainWindow", "CREATE VENV"))
        self.installedLabel.setText(_translate("MainWindow", "INSTALLED"))
        self.installButton.setText(_translate("MainWindow", "INSTALL"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Download"))
        self.menuExit.setTitle(_translate("MainWindow", "Exit"))
        self.actionpyenv_win.setText(_translate("MainWindow", "pyenv-win"))
        self.actionpyenv_virtualenv.setText(_translate("MainWindow", "pyenv-virtualenv"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))