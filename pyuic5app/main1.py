from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QFileDialog
import os
from PyQt5 import QtCore, QtGui, QtWidgets
import typer

app = typer.Typer()
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(351, 119)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("background-color: QLinearGradient( x1: 0, y1: 0,\n"
"                             x2: 1, y2: 0, \n"
"                          stop: 0 #0f121c, \n"
"                          stop: 1 #0b0d14);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("background-color: QLinearGradient( x1: 0, y1: 0,\n"
"                             x2: 1, y2: 0, \n"
"                          stop: 0 #0f121c, \n"
"                          stop: 1 #0b0d14);")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setSpacing(4)
        self.formLayout_4.setObjectName("formLayout_4")
        self.uiFile = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.uiFile.setFont(font)
        self.uiFile.setStyleSheet("color: rgb(255, 255, 255);")
        self.uiFile.setObjectName("uiFile")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.uiFile)
        self.uiFilePath = QtWidgets.QLineEdit(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(8)
        self.uiFilePath.setFont(font)
        self.uiFilePath.setStyleSheet("border: 1px solid rgb(170, 85, 255);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"padding-right:10px;")
        self.uiFilePath.setObjectName("uiFilePath")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.uiFilePath)
        self.pythonF1 = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.pythonF1.setFont(font)
        self.pythonF1.setStyleSheet("color: rgb(255, 255, 255);")
        self.pythonF1.setObjectName("pythonF1")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pythonF1)
        self.uiToPy = QtWidgets.QLineEdit(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.uiToPy.setFont(font)
        self.uiToPy.setStyleSheet("border: 1px solid rgb(170, 85, 255);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"padding-right:10px;")
        self.uiToPy.setObjectName("uiToPy")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.uiToPy)
        self.horizontalLayout_2.addLayout(self.formLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.upload0 = QtWidgets.QPushButton(self.tab_1)
        self.upload0.setStyleSheet("background-color: rgb(170, 85, 255);\n"
"border-radius:5px;\n"
"height:30px;\n"
"width:30px;")
        self.upload0.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:\\Users\\andre\\Desktop\\QTdesigner\\../MangaTranslator/Icons/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.upload0.setIcon(icon)
        self.upload0.setObjectName("upload0")
        self.verticalLayout_2.addWidget(self.upload0)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.convert1 = QtWidgets.QPushButton(self.tab_1)
        self.convert1.setMaximumSize(QtCore.QSize(300, 16777215))
        self.convert1.setStyleSheet("background-color: rgb(170, 85, 255);\n"
"border-radius:5px;\n"
"height:40px;\n"
"width:150px;")
        self.convert1.setObjectName("convert1")
        self.verticalLayout_3.addWidget(self.convert1, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSpacing(4)
        self.formLayout.setObjectName("formLayout")
        self.qrcFile = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.qrcFile.setFont(font)
        self.qrcFile.setStyleSheet("color: rgb(255, 255, 255);")
        self.qrcFile.setObjectName("qrcFile")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.qrcFile)
        self.qrcFilePath = QtWidgets.QLineEdit(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.qrcFilePath.setFont(font)
        self.qrcFilePath.setStyleSheet("border: 1px solid rgb(170, 85, 255);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"padding-right:10px;")
        self.qrcFilePath.setObjectName("qrcFilePath")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.qrcFilePath)
        self.pythonF2 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.pythonF2.setFont(font)
        self.pythonF2.setStyleSheet("color: rgb(255, 255, 255);")
        self.pythonF2.setObjectName("pythonF2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pythonF2)
        self.qrcToPy = QtWidgets.QLineEdit(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.qrcToPy.setFont(font)
        self.qrcToPy.setStyleSheet("border: 1px solid rgb(170, 85, 255);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"padding-left: 10px;\n"
"padding-right:10px;")
        self.qrcToPy.setObjectName("qrcToPy")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.qrcToPy)
        self.horizontalLayout_3.addLayout(self.formLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.upload = QtWidgets.QPushButton(self.tab_2)
        self.upload.setStyleSheet("background-color: rgb(170, 85, 255);\n"
"border-radius:5px;\n"
"height:30px;\n"
"width:30px;")
        self.upload.setText("")
        self.upload.setIcon(icon)
        self.upload.setObjectName("upload")
        self.verticalLayout.addWidget(self.upload)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.convert2 = QtWidgets.QPushButton(self.tab_2)
        self.convert2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.convert2.setStyleSheet("background-color: rgb(170, 85, 255);\n"
"border-radius:5px;\n"
"height:40px;\n"
"width:150px;")
        self.convert2.setObjectName("convert2")
        self.verticalLayout_4.addWidget(self.convert2, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.uiFile.setText(_translate("MainWindow", "Ui file:"))
        self.uiFilePath.setPlaceholderText(_translate("MainWindow", "Upload .ui file"))
        self.pythonF1.setText(_translate("MainWindow", "PythonFile:"))
        self.uiToPy.setPlaceholderText(_translate("MainWindow", "Type python file name"))
        self.convert1.setText(_translate("MainWindow", "Convert"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", ".ui to .py"))
        self.qrcFile.setText(_translate("MainWindow", "QRC file:"))
        self.qrcFilePath.setPlaceholderText(_translate("MainWindow", "Upload resource file"))
        self.pythonF2.setText(_translate("MainWindow", "PythonFile:"))
        self.qrcToPy.setPlaceholderText(_translate("MainWindow", "Type python file name"))
        self.convert2.setText(_translate("MainWindow", "Convert"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", ".qrc to .py"))

class Main(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.setMinimumSize(700, 200)
        self.setMaximumSize(800, 200)
        self.setWindowTitle("Pyuic5")
        self.qrcFile.setText("QRC File")
        self.uiFile.setText("UI File")
        self.convert1.clicked.connect(self.ui_to_py)
        self.convert2.clicked.connect(self.qrc_to_py)
        self.upload0.clicked.connect(self.getFilePath)
        self.upload.clicked.connect(self.getFilePath)

    def getFilePath(self):
        filename, _ =  QFileDialog.getOpenFileName(
            None,
            "QFileDialog.getOpenFileNames()",
            "",
            "All files (*)"
        )
        if self.tabWidget.currentIndex() == 0:
            self.uiFilePath.setText(filename)
        else:
            self.qrcFilePath.setText(filename)

    def ui_to_py(self):
        uiPath = self.uiFilePath.text()
        pyThon = self.uiToPy.text()
        self.uiFilePath.clear()
        self.uiToPy.clear()
        os.system(f"pyuic5 -x {uiPath} -o {pyThon}")

    def qrc_to_py(self):
        qrcPath = self.qrcFilePath.text()
        pyThon = self.qrcToPy.text()
        self.qrcFilePath.clear()
        self.qrcToPy.clear()
        os.system(f"pyrcc5 -o {pyThon} {qrcPath}")

@app.command()
def run():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = Main()
    w.show()
    sys.exit(app.exec())
