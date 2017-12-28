import pickle
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QAction
from PyQt5.QtGui import QIcon

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 444)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 701, 401))
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.plainTextEdit)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_2 = QAction(MainWindow)
        self.actionOpen_2.triggered.connect(self.showOpenDialog)
        self.actionOpen_2.setShortcut('Ctrl+O')
        self.actionOpen_2.setObjectName("actionOpen_2")
        self.actionSave_2 = QAction(MainWindow)
        self.actionSave_2.triggered.connect(self.showSaveDialog)
        self.actionSave_2.setShortcut('Ctrl+S')
        self.actionSave_2.setObjectName("actionSave_2")
        self.menuFile.addAction(self.actionOpen_2)
        self.menuFile.addAction(self.actionSave_2)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def showOpenDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open...', '/home')[0]

        f = open(fname, 'r')

        with f:
            data = f.read()
            self.plainTextEdit.setPlainText(data)

    def showSaveDialog(self):

    	fname = QFileDialog.getOpenFileName(self, 'Open...', '/home')[0]

    	text = self.plainTextEdit.toPlainText()

    	with open (fname, "wb") as f:
    		pickle.dump(text, f)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_2.setText(_translate("MainWindow", "Open"))
        self.actionSave_2.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
