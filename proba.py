import sys
import os
from datetime import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


#uporedjiati sa stringom, ako je trenutni 


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

        ok_width = (browse_width/100)*33.33
        ok_height = (browse_height/100)*25
        ok_x = (browse_width/100)*11.11
        ok_y = (browse_height/100)*55

        cancel_width = (browse_width/100)*33.33
        cancel_height = (browse_height/100)*25
        cancel_x = (browse_width/100)*55.56
        cancel_y = (browse_height/100)*55

        self.setGeometry(300, 300, browse_width, browse_height)
        self.setWindowTitle('Browse')
        self.setFixedSize(self.size())
        self.path = str(QFileDialog.getOpenFileName())
        self.path = self.path[2:len(self.path)-19] 
        
        
        self.lbl0 = QLabel("Current Path: "+ self.path, self)
        self.lbl0.move(lbl0_x, lbl0_y)   


        self.lbl1 = QLabel("Save current path?", self)
        self.lbl1.move(lbl1_x, lbl1_y)


        

        OK = QPushButton('OK', self)
        OK.resize(ok_width, ok_height)
        OK.move(ok_x, ok_y)
        OK.clicked.connect(self.okButton)

        Cancel = QPushButton('Cancel', self)
        Cancel.resize(cancel_width, cancel_height)
        Cancel.move (cancel_x, cancel_y)
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
        self.main_width = 300
        self.main_height = 300

        self.table_width = (self.main_width/100)*44
        self.table_height = (self.main_height/100)*16.67    
        self.table_x = (self.main_width/100)*28
        self.table_y = (self.main_height/100)*66.67

        self.interval_width = (self.main_width/100)*23.33
        self.interval_height =(self.main_height/100)*10
        self.interval_x = (self.main_width/100)*48.33
        self.interval_y = (self.main_width/100)*33.33

        self.lbl_interval_x = (self.main_width/100)*28.33
        self.lbl_interval_y = (self.main_width/100)*33.33

        self.lbl_mins_x = (self.main_width/100)*53.33
        self.lbl_mins_y = (self.main_width/100)*25

        self.setGeometry(300, 300, self.main_width, self.main_height)
        self.setFixedSize(self.size())
        self.setWindowTitle('Joystick Observation') 
        self.center()  
                
        #interval init
        self.lbl_interval = QLabel("Interval:", self)
        self.lbl_interval.move(self.lbl_interval_x, self.lbl_interval_y)
        self.lbl_mins = QLabel("Mins.", self)
        self.lbl_mins.move(self.lbl_mins_x, self.lbl_mins_y)
        self.interval = QLineEdit(self)
        self.interval.setText("5")
        self.interval.resize(self.interval_width, self.interval_height)
        self.interval.move(self.interval_x, self.interval_y)
        
        #Button init

        make_table = QPushButton('Make Table', self)
        make_table.resize(self.table_width, self.table_height)
        make_table.move(self.table_x, self.table_y)
        make_table.clicked.connect(self.table_button)
        
        self.show()

    def browse(self):
        self.B = BrowseWindow()
        self.B.show()
        

    def table_button(self):
        if self.check_browse_path()== False:
            QMessageBox.warning(self, "No browse path!", "Choose browse path.", QMessageBox.Ok)
        else:
  
            interval = self.interval.text()        
            if self.check_interval_input(interval)== False:
                QMessageBox.warning(self, "Bad Input!", "Interval must be an integer number.", QMessageBox.Ok)
            else:
                interval = int(interval)
                browse = open('config/browse.txt', 'r').read()
                log = self.get_log()
                stuff = self.get_dates(log, interval)
                #dates = self.get_dates(log, interval)
                self.try_shit(log, stuff)
                table  = self.get_table(log)           
                #print("DATUMI")
                #self.print_dates(dates)
                #return
                f = open("table.html", "w")
                f.write(table)
                f.close()
                QMessageBox.information(self, "Success!", "Table successfully made!", QMessageBox.Ok)

    def print_dates(self, dates):
        for date in dates:
            print (date)            
    
    def get_log(self):
        path = open('config/browse.txt', 'r').read()
        open('config/browse.txt', 'w').close() 
        log = open(path, "r").read().splitlines()
        return log

    def try_shit(self, log, stuff):
        dates = stuff[0]
        bools = stuff[1]

        print(len(bools))
        print("brm")
        print(len(dates))       
        
            
        
        
    #def get_meteor_row(meteor)
        
        
            
            
            
                   
        
        

    def get_dates(self, log, interval):  
        dates = []
        bools = []
        i = 0
        start_date = datetime.strptime("13:48:00", "%H:%M:%S")
        dates.append(start_date)
        bools.append(False)
        first_date = start_date
        second_date = self.add_interval(start_date, interval)
        while i < len(log):
            meteor = log[i].split()
            string_date = meteor[2]
            date = datetime.strptime(string_date, "%H:%M:%S")
            if (date >= start_date) and (date <= second_date):
                dates.append(date)
                bools.append(True) 
                #dates.append((date, True))
            else:
                first_date = second_date
                second_date = self.add_interval(second_date, interval)
                
                dates.append(first_date)
                bools.append(False)
                dates.append(date)
                bools.append(True)
                                
               #dates.append((first_date, False))
               #dates.append((date, True)) 
            i += 1
        #dates.append((second_date, False))
        dates.append(second_date)
        bools.append(False)
        stuff = (dates, bools)

        return stuff
    
    def get_table(self, log):
        table = open("config/begin.txt").read()
        for i in range(0, len(log)): 
            meteor = log[i].split()
            row = "<tr>\n" + "<td>" + str(i+1) + "</td>\n" + "<td>" + meteor[2] + "</td>\n" + "<td>" + meteor[1] + "</td>\n" + "<td>" + meteor[0] + "</td>\n" + "</tr>\n"
            table += row
        end = open("config/end.txt").read()
        table += end
        return table

    def add_interval(self, tm, mins):
        fulldate = datetime(1900, 1, 1, tm.hour, tm.minute, tm.second)
        secs = mins*60
        fulldate = fulldate + timedelta(seconds=secs)
        return fulldate 

    def check_interval_input(self,s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def check_browse_path(self):
        path = open('config/browse.txt', 'r').read()        
        if len(path) == 0: return False
        else: return True    
              
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
