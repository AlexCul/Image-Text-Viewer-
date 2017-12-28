from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QCoreApplication
from textEdit import Ui_MainWindow
from styleOfImageViewer import Ui_ImageViewerMainWindow

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(401, 381)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, -1, 401, 241))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TextViewer = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.TextViewer.clicked.connect(self.textViewer)
        self.TextViewer.setObjectName("TextViewer")
        self.verticalLayout.addWidget(self.TextViewer)
        self.ImageViewer = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.ImageViewer.clicked.connect(self.imageViewer)
        self.ImageViewer.setObjectName("ImageViewer")
        self.verticalLayout.addWidget(self.ImageViewer)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 240, 401, 141))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.English = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.English.clicked.connect(self.englishTranslate)
        self.English.setObjectName("English")
        self.verticalLayout_2.addWidget(self.English)
        self.Russian = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Russian.clicked.connect(self.russianTranslate)
        self.Russian.setObjectName("Russian")
        self.verticalLayout_2.addWidget(self.Russian)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def imageViewer(self):
        self.window = QMainWindow()
        self.ui = Ui_ImageViewerMainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def textViewer(self):
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def englishTranslate(self):
        _translate = QCoreApplication.translate
        self.TextViewer.setText(_translate("Form", "Text Viewer"))
        self.ImageViewer.setText(_translate("Form", "Image Viewer"))
        self.English.setText(_translate("Form", "English"))
        self.Russian.setText(_translate("Form", "Russian"))

    def russianTranslate(self):
        _translate = QCoreApplication.translate
        self.TextViewer.setText(_translate("Form", "Просмотр Текста"))
        self.ImageViewer.setText(_translate("Form", "Просмотр Изображений"))
        self.English.setText(_translate("Form", "Английский"))
        self.Russian.setText(_translate("Form", "Русский"))

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.TextViewer.setText(_translate("Form", "Text Viewer"))
        self.ImageViewer.setText(_translate("Form", "Image Viewer"))
        self.English.setText(_translate("Form", "English"))
        self.Russian.setText(_translate("Form", "Russian"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    Form.setFixedSize(401, 381)
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())