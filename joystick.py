import sys
import os
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from datetime import *

"""
TODO
-napraviti nacin da se biraju rojevi
-napraviti da se na osnovu izabranih rojeva prebroji koliko kojih meteora ima i da se na osnovu toga posle napravi tabela.
-napraviti mogunost stampanja meteora po intervalu?
-napraviti da generise granice intervala tako sto se unutar while petlje proverava da li je dati time_stamp unutar trenutnog intervala
-napraviti textBox za interval
-napraviti jos jedan table koji samo stampa raspodelu po magnitudama
"""
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
        OK.clicked.connect(self.ok_button)

        Cancel = QPushButton('Cancel', self)
        Cancel.resize(150, 50)
        Cancel.move (250, 110)
        Cancel.clicked.connect(self.cancel_button)
        
    def cancel_button(self):
        self.close()
        
    def ok_button(self):
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
        make_table.clicked.connect(self.table_button)
        
        self.show()

    def browse(self):
        self.B = BrowseWindow()
        self.B.show()
        

    def table_button(self):
        path = "example.txt"
        self.session = open(path, "r").read().splitlines()
        #self.get_start_date()        
        self.get_rows()
        self.get_table()
        self.write_table()
        
        

    def get_rows(self):
        self.table_rows = []
        self.time_stamps = []
        help_rows = []
        i = 0
        while i < len(self.session):
                self.meteor = self.session[i].split()
                row = self.make_row(i)
                string_date = self.meteor[2]
                date = datetime.strptime(string_date, "%H:%M:%S")
                self.time_stamps.append(date)   
                self.table_rows.append(row)
                i += 1
        start_row = self.make_start_row()
        self.table_rows.insert(0, start_row)

    def make_start_row(self):
        self.get_start_date()
        start_date = self.get_start_date()
        start_row = "<tr>\n" + "<td>" + "START" + "</td>\n" + "<td>" + start_date + "</td>\n" + "<td>" + "/" + "</td>\n" + "<td>" + "/" + "</td>\n" + "</tr>\n"
        return start_row
   
    def make_row(self, i):
        row = "<tr>\n" + "<td>" + str(i+1) + "</td>\n" + "<td>" + self.meteor[2] + "</td>\n" + "<td>" + self.meteor[1] + "</td>\n" + "<td>" + self.meteor[0] + "</td>\n" + "</tr>\n"
        return row        

    def get_table(self):
        begin = open("config/begin.txt", "r").read()
        self.table = ""

        for i in range(0, len(self.table_rows)):
                self.table += str(self.table_rows[i])
                    
        end = open("config/end.txt", "r").read()

        self.table = begin + self.table + end

        QMessageBox.information(self, "Success!", "Table successfully made!", QMessageBox.Ok)

    def get_start_date(self):
        self.start_date = self.time_stamps[0]
        self.start_date = self.start_date.replace(second = 0)
        string_date = self.start_date.strftime('%H:%M:%S') 
        return string_date
           
    def add_interval(tm, mins):
        fulldate = datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
        secs = mins*60
        fulldate = fulldate + timedelta(seconds=secs)
        return fulldate.time()   

    def write_table(self):
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
