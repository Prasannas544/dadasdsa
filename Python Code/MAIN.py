

import os
import pickle
import sys
import os
from subprocess import call
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def click_checkinn(self):
        call(["python", "new.py"])

    def click_host(self):
        call(["python","CHECK.py"])
    
    def click_checkout(self):
        call(["python", "checkout.py"])

    def click_list(self):
        call(["python", "LISTOFALLGUEST.py"])
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(19, 10, 761, 571))
        self.frame.setStyleSheet("QFrame{background-color: #3F9CED\n"
";\n"
"\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.INFO = QtWidgets.QLabel(self.frame)
        self.INFO.setGeometry(QtCore.QRect(120, 0, 611, 51))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.INFO.setFont(font)
        self.INFO.setObjectName("INFO")

        self.HOST = QtWidgets.QPushButton(self.frame)
        self.HOST.setGeometry(QtCore.QRect(170, 40, 431, 91))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.HOST.setFont(font)
        self.HOST.setStyleSheet("QPushButton:active:after{\n"
"\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    opacity: 1;\n"
"    transition: 1s;\n"
"-webkit-transition-duration: 0.4s;\n"
"    transition-duration: 0.4s;\n"
"\n"
"    background-color:#19707D;\n"
"    color: white;\n"
"\n"
"   }\n"
"")
        self.HOST.setObjectName("HOST")
        self.HOST.clicked.connect(self.click_host)

        self.CHECKINN = QtWidgets.QPushButton(self.frame)
        self.CHECKINN.setGeometry(QtCore.QRect(170, 140, 431, 91))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.CHECKINN.setFont(font)
        self.CHECKINN.setStyleSheet("QPushButton:active:after{\n"
"\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    opacity: 1;\n"
"    transition: 1s;\n"
"-webkit-transition-duration: 0.4s;\n"
"    transition-duration: 0.4s;\n"
"\n"
"    background-color:#19707D;\n"
"    color: white;\n"
"\n"
"   }\n"
"")
        self.CHECKINN.setObjectName("CHECKINN")
        self.CHECKINN.clicked.connect(self.click_checkinn)




        self.CHECKOUT = QtWidgets.QPushButton(self.frame)
        self.CHECKOUT.setGeometry(QtCore.QRect(170, 250, 431, 91))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.CHECKOUT.setFont(font)
        self.CHECKOUT.setStyleSheet("QPushButton:active:after{\n"
"\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    opacity: 1;\n"
"    transition: 1s;\n"
"-webkit-transition-duration: 0.4s;\n"
"    transition-duration: 0.4s;\n"
"\n"
"    background-color:#19707D;\n"
"    color: white;\n"
"\n"
"   }\n"
"")
        self.CHECKOUT.setObjectName("CHECKOUT")
        self.CHECKOUT.clicked.connect(self.click_checkout)



        self.LISTOFALLGUEST = QtWidgets.QPushButton(self.frame)
        self.LISTOFALLGUEST.setGeometry(QtCore.QRect(170, 360, 431, 91))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.LISTOFALLGUEST.setFont(font)
        self.LISTOFALLGUEST.setStyleSheet("QPushButton:active:after{\n"
"\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    opacity: 1;\n"
"    transition: 1s;\n"
"-webkit-transition-duration: 0.4s;\n"
"    transition-duration: 0.4s;\n"
"\n"
"    background-color:#19707D;\n"
"    color: white;\n"
"\n"
"   }\n"
"")
        self.LISTOFALLGUEST.setObjectName("LISTOFALLGUEST")
        self.LISTOFALLGUEST.clicked.connect(self.click_list)

        self.EXIT = QtWidgets.QPushButton(self.frame)
        self.EXIT.setGeometry(QtCore.QRect(170, 470, 431, 91))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.EXIT.setFont(font)
        self.EXIT.setStyleSheet("QPushButton:active:after{\n"
"\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    opacity: 1;\n"
"    transition: 1s;\n"
"-webkit-transition-duration: 0.4s;\n"
"    transition-duration: 0.4s;\n"
"\n"
"    background-color:#19707D;\n"
"    color: white;\n"
"\n"
"   }\n"
"")
        self.EXIT.setObjectName("EXIT")
        self.EXIT.clicked.connect( sys.exit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ENTRY MANAGEMENT SOFTWARE"))
        self.INFO.setText(_translate("MainWindow", "ENTRY MANAGEMENT SOFTWARE"))
        self.CHECKINN.setText(_translate("MainWindow", "CHECK IN"))
        self.HOST.setText(_translate("MAINWindow","HOST CHECK IN"))
        self.CHECKOUT.setText(_translate("MainWindow", "CHECK OUT"))
        self.LISTOFALLGUEST.setText(_translate("MainWindow", "LIST OF ALL HOST"))
        self.EXIT.setText(_translate("MainWindow", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()

