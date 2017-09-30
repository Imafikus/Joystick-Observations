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
        browse_width = 450
        browse_height = 200

        lbl0_x = (browse_width/100)*11.11
        lbl0_y = (browse_height/100)*10

        lbl1_x = (browse_width/100)*35.56
        lbl1_y = (browse_height/100)*35

        self.setGeometry(300, 300, browse_width, browse_height)
        self.setWindowTitle('Browse')
        self.setFixedSize(self.size())
        self.path = str(QFileDialog.getOpenFileName())
        
        self.lbl0 = QLabel("Current Path: "+ self.path, self)
        self.lbl0.move(lbl0_x, lbl0_y)   


        self.lbl1 = QLabel("Save current path?", self)
        self.lbl1.move(lbl1_x, lbl1_y)


        

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
        sliced_part = self.path[2:len(self.path)-19]       
        f = open("config/browse.txt", "w")
        f.write(sliced_part)
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
        self.main_width = 300
        self.main_height = 300

        self.table_width = (self.main_width/100)*44
        self.table_height = (self.main_height/100)*16.67    
        self.table_x = (self.main_width/100)*28
        self.table_y = (self.main_height-100)

        self.interval_width = (self.main_width/100)*23.33
        self.interval_height =(self.main_height/100)*10
        self.interval_x = (self.main_width/100)*48.33
        self.interval_y = (self.main_width/100)*33.33

        self.lbl_interval_x = (self.main_width/100)*28.33
        self.lbl_interval_y = (self.main_width/100)*33.33

        self.lbl_mins_x = (self.main_width/100)*53.33
        self.lbl_mins_y = (self.main_width/100)*25

        self.setGeometry(300, 300, self.main_width, self.main_height)
        #self.setFixedSize(self.size())
        self.setWindowTitle('Joystick Observation') 
        self.center()  
                
        #interval init
        self.lbl_interval = QLabel("Interval", self)
        self.lbl_interval.move(self.lbl_interval_x, self.lbl_interval_y)
        self.lbl_mins = QLabel("Mins.", self)
        self.lbl_mins.move(self.lbl_mins_x, self.lbl_mins_y)
        self.interval = QLineEdit(self)
        self.interval.resize(self.interval_width, self.interval_height)
        self.interval.move(self.interval_x, self.interval_y)
        
        #Button init

        make_table = QPushButton('Make Table', self)
        make_table.resize(self.table_width, self.table_height)
        make_table.move(self.table_x, self.table_y)
        make_table.clicked.connect(self.tableButton)
        
        self.show()

    def browse(self):
        self.B = BrowseWindow()
        self.B.show()
        

    def tableButton(self):
        
        self.get_log()
        self.get_table()
        
    
    def get_log(self):
        path = open('config/browse.txt', 'r').read()
        print (path)
        open('config/browse.txt', 'w').close()

    def get_table(self):
       
        QMessageBox.information(self, "Success!", "Table successfully made!", QMessageBox.Ok)

       
                        
    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
