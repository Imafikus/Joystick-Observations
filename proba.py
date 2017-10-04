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
        self.table_y = (self.main_height/100)*68.67

        self.interval_width = (self.main_width/100)*23.33
        self.interval_height =(self.main_height/100)*10
        self.interval_x = (self.main_width/100)*48.33
        self.interval_y = (self.main_width/100)*28.33

        self.lbl_interval_x = (self.main_width/100)*28.33
        self.lbl_interval_y = (self.main_width/100)*28.33

        self.lbl_mins_x = (self.main_width/100)*53.33
        self.lbl_mins_y = (self.main_width/100)*19

       
        self.start_lbl_x = (self.main_width/100)*28.33
        self.start_lbl_y = (self.main_height/100)*48.33

        

        self.start_h_lbl_x = (self.main_width/100)*41.67
        self.start_h_lbl_y = (self.main_height/100)*40.67
        self.start_h_x = (self.main_width/100)*40
        self.start_h_y = (self.main_height/100)*48.63        
       
       
        self.start_m_lbl_x = (self.main_width/100)*53.33
        self.start_m_lbl_y = (self.main_height/100)*40.67      
        self.start_m_x = (self.main_width/100)*51.67
        self.start_m_y = (self.main_height/100)*48.63


        
        self.start_s_lbl_x = (self.main_width/100)*65
        self.start_s_lbl_y = (self.main_height/100)*40.67      
        self.start_s_x = (self.main_width/100)*63.33
        self.start_s_y = (self.main_height/100)*48.63


       
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
                
        #start_time init
        self.start_lbl = QLabel("Start: ", self)
        self.start_lbl.move(self.start_lbl_x, self.start_lbl_y)
        
        self.start_h_lbl = QLabel("H", self)
        self.start_h_lbl.move(self.start_h_lbl_x, self.start_h_lbl_y)
        self.start_h = QLineEdit(self)
        self.start_h.setText("0")
        self.start_h.resize(25, 30)
        self.start_h.move(self.start_h_x, self.start_h_y)

        self.start_m_lbl = QLabel("M", self)
        self.start_m_lbl.move(self.start_m_lbl_x, self.start_m_lbl_y)
        self.start_m = QLineEdit(self)
        self.start_m.setText("0")
        self.start_m.resize(25, 30)
        self.start_m.move(self.start_m_x, self.start_m_y)        

        self.start_s_lbl = QLabel("S", self)
        self.start_s_lbl.move(195, 122)
        self.start_s = QLineEdit(self)
        self.start_s.setText("0")
        self.start_s.resize(25, 30)
        self.start_s.move(190, 145) 

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
                
        hrs = self.start_h.text()
        mins = self.start_m.text()
        secs = self.start_s.text()

        report = self.check_start(hrs, mins, secs)

        if report[1] == False:
            QMessageBox.warning(self, "Error", report[0], QMessageBox.Ok)
        else:
            
            if self.check_browse_path()== False:
                QMessageBox.warning(self, "No browse path!", "Choose browse path.", QMessageBox.Ok)
            else:
                start_date = self.make_start_date(hrs, mins, secs)
                check_start_date2
                log = self.get_log()
                interval = self.interval.text()        
                if self.check_interval_input(interval)== False:
                    QMessageBox.warning(self, "Bad Input!", "Interval must be an integer number.", QMessageBox.Ok)
                else:
                    interval = int(interval)
                    browse = open('config/browse.txt', 'r').read()
                    stuff = self.get_dates(log, interval)
                    rows = self.get_rows(log, stuff)
                    table  = self.make_HTML(rows)           
                    f = open("table.html", "w")
                    f.write(table)
                    f.close()
                    QMessageBox.information(self, "Success!", "Table successfully made!", QMessageBox.Ok)

    def make_start_date(self, hrs, mins, secs):
        if len(hrs) == 1: hrs = "0" + hrs
        if len(mins) == 1: mins = "0" + mins
        if len(secs) == 1: secs = "0" + secs

        string_date = hrs + mins + secs
        date = datetime.strptime(string_date, "%H%M%S")
        return date 
                    
    
    def get_log(self):
        path = open('config/browse.txt', 'r').read()
        open('config/browse.txt', 'w').close() 
        log = open(path, "r").read().splitlines()
        return log

    def get_rows(self, log, stuff):
            dates = stuff[0]
            bools = stuff[1]
            rows = []            
            k = 0
            for i in range(0, len(dates)):
                if bools[i] == False:
                    interval = dates[i].strftime('%H:%M:%S')
                    row = self.get_interval_row(interval)
                    rows.append(row)
                else:
                    meteor = log[k].split()
                    row = self.get_meteor_row(meteor, k)
                    rows.append(row)
                    k += 1
            return rows 
            
                   
    def get_meteor_row(self, meteor, i):
            row = "<tr>\n" + "<td>" + str(i+1) + "</td>\n" + "<td>" + meteor[2] + "</td>\n" + "<td>" + meteor[1] + "</td>\n" + "<td>" + meteor[0] + "</td>\n" + "</tr>\n"
            return row        

    def get_interval_row(self, interval):
            row = "<tr>\n" + "<td>" + "Interval" + "</td>\n" + "<td>" + interval + "</td>\n" + "<td>" + "/" + "</td>\n" + "<td>" + "/" + "</td>\n" + "</tr>\n"                
            return row
            
            
    def make_HTML(self, rows):
        table = open("config/begin.txt").read()
        for i in range (0, len(rows)):
            table += rows[i]
        end = open("config/end.txt").read()
        table += end
        return table
                
                   
        
        

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
                
            else:
                first_date = second_date
                second_date = self.add_interval(second_date, interval)
                
                dates.append(first_date)
                bools.append(False)
                dates.append(date)
                bools.append(True)
            i += 1
        dates.append(second_date)
        bools.append(False)
        stuff = (dates, bools)
        return stuff
 

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

    def check_start(self, hrs, mins, secs):
        check = True
        hrs_check = []
        mins_check = []
        secs_check = []

        msg = ""
        
        for i in range (0, 24): 
            hrs_check.append(str(i))

        for i in range (0, 59): 
            mins_check.append(str(i))

        for i in range (0, 59): 
            secs_check.append(str(i))

        if hrs not in hrs_check:
            msg += "Hours must be in range 0-23\n"
            check = False

        if mins not in mins_check:
            msg += "Minutes must be in range 0-59\n"
            check = False

        if secs not in secs_check:
            msg += "Seconds must be in range 0-59\n"
            check = False
        
        report = (msg, check)
        return report
           
                        
    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
