
import os
import pickle
import sys
import os
from subprocess import call
from PyQt5 import QtCore, QtGui, QtWidgets
import MySQLdb as mdb

l2=[]
G=[]
from PyQt5 import QtCore, QtGui, QtWidgets



class save:
    def __init__(self,NAME_PRO,ADDRESS_PRO,MOBILE_NO_PRO,EMAIL_PRO):
        self.name=NAME_PRO
        self.address=ADDRESS_PRO
        self.mobile_no=MOBILE_NO_PRO
        self.email=EMAIL_PRO


class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(432, 813)
        MainWindow.setMinimumSize(QtCore.QSize(432, 813))
        MainWindow.setMaximumSize(QtCore.QSize(432, 813))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 781, 821))
        self.frame.setStyleSheet("QFrame{background-color: #3F9CED\n"
";\n"
"\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.LISTOFALLGUEST = QtWidgets.QLabel(self.frame)
        self.LISTOFALLGUEST.setGeometry(QtCore.QRect(10, 20, 391, 61))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.LISTOFALLGUEST.setFont(font)
        self.LISTOFALLGUEST.setStyleSheet("QWidget{\n"
" background-color:white;\n"
" padding: 10px;\n"
"    border-radius: 25px;\n"
"}")
        self.LISTOFALLGUEST.setObjectName("LISTOFALLGUEST")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(0, 100, 431, 731))
        self.tableWidget.setStyleSheet("QWidget{\n"
"\n"
"    border-radius: 50px;\n"
"}")
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        
        self.tableWidget.horizontalHeader().setDefaultSectionSize(185)
        self.tableWidget.verticalHeader().setMinimumSectionSize(50)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.db = mdb.connect('localhost', 'root', '', 'entry_manage')
        
        self.c1=self.db.cursor()
        
        self.c1.execute("select name from host" )
        self.data=self.c1.fetchall()
        
        for row_number, row_data in enumerate(self.data):
             for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(0,row_number,QtWidgets.QTableWidgetItem(data))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "List of All Hosts"))
        self.LISTOFALLGUEST.setText(_translate("MainWindow", "LIST OF ALL HOST"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "NAME"))
        


if __name__ == "__main__":
    
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

