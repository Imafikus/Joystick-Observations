import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from datetime import *



class BrowseWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 450, 200)
        self.setWindowTitle('Browse')
        self.setFixedSize(self.size())
        self.path = str(QFileDialog.getExistingDirectory())
        
        self.lbl0 = QLabel("Current Path: "+ self.path, self)
        self.lbl0.move(50, 20)   


        self.lbl1 = QLabel("Save current path?", self)
        self.lbl1.move(160, 70)


        

        OK = QPushButton('OK', self)
        OK.resize(150, 50)
        OK.move(50, 110)
        OK.clicked.connect(self.okButton)

        Cancel = QPushButton('Cancel', self)
        Cancel.resize(150, 50)
        Cancel.move (250, 110)
        Cancel.clicked.connect(self.cancelButton)
        
    def cancelButton(self):
        self.close()
        
    def okButton(self):
        f = open("config/browse.txt", "w")
        f.write(self.path)
        f.close()
        self.close()     


class MainWindow(QMainWindow):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):

        
        #toolbar init
        
        BrowseAct = QAction(QIcon('icons/browse.png'), 'Browse for folder', self)
        BrowseAct.setShortcut('Ctrl+B')
        BrowseAct.triggered.connect(self.browse)
        
        self.toolbar = self.addToolBar('Browse')
        self.toolbar.addAction(BrowseAct)

        #window init
        self.width = 340
        self.height = 300     
        self.setGeometry(300, 300, self.width, self.height)
        self.setFixedSize(self.size())
        self.setWindowTitle('Joystick Observation') 
        self.center()  
       
        
        #Button init

        make_table = QPushButton('Make Table', self)
        make_table.resize(150, 50)
        make_table.move(95, self.height-100)
        make_table.clicked.connect(self.tableButton)
        
        self.show()

    def browse(self):
        self.B = BrowseWindow()
        self.B.show()
        

    def tableButton(self):
        #def MakingHTML() 
        path = "example.txt"
        self.session = open(path, "r").read().splitlines()
        self.getRows()
        self.getTable()
        self.writeTable()

    def getRows(self):
        self.table_rows = []

        for i in range(0, len(self.session)):
                meteor = self.session[i].split()
                row = "<tr>\n" + "<td>" + str(i+1) + "</td>\n" + "<td>" + meteor[2] + "</td>\n" + "<td>" + meteor[1] + "</td>\n" + "<td>" + meteor[0] + "</td>\n" + "</tr>\n"
                self.table_rows.append(row)
            
    def getTable(self):
        begin = open("config/begin.txt", "r").read()
        self.table = ""

        for i in range(0, len(self.table_rows)):
                self.table += str(self.table_rows[i])
                    
        end = open("config/end.txt", "r").read()
        
        self.table = begin + self.table + end

        QMessageBox.information(self, "Success!", "Table successfully made!", QMessageBox.Ok)

    def writeTable(self):
        self.code = "table.html"
        table = open(self.code, "w")
        table.write(self.table)   
                        
    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
