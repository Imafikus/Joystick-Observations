import sys
import os
from datetime import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class BrowseWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):
        browse_width = 550
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
        self.main_height = 350
        #table vals
        self.table_width = (self.main_width/100)*44
        self.table_height = (self.main_height/100)*16.67    
        self.table_x = (self.main_width/100)*28
        self.table_y = (self.main_height/100)*70
        #inteval vals
        self.interval_width = (self.main_width/100)*23.33
        self.interval_height =(self.main_height/100)*7.5
        self.interval_x = (self.main_width/100)*48.33
        self.interval_y = (self.main_width/100)*25.33

        self.lbl_interval_x = (self.main_width/100)*28.33
        self.lbl_interval_y = (self.main_width/100)*25.33

        self.lbl_mins_x = (self.main_width/100)*53.33
        self.lbl_mins_y = (self.main_width/100)*16
        #start_time vals
        self.start_lbl_x = (self.main_width/100)*28.33
        self.start_lbl_y = (self.main_height/100)*38.33

        self.start_h_lbl_x = (self.main_width/100)*41.67
        self.start_h_lbl_y = (self.main_height/100)*31.67
        self.start_h_x = (self.main_width/100)*40
        self.start_h_y = (self.main_height/100)*38.63               
       
        self.start_m_lbl_x = (self.main_width/100)*53.33
        self.start_m_lbl_y = (self.main_height/100)*31.67      
        self.start_m_x = (self.main_width/100)*51.67
        self.start_m_y = (self.main_height/100)*38.63
        
        self.start_s_lbl_x = (self.main_width/100)*65
        self.start_s_lbl_y = (self.main_height/100)*31.67      
        self.start_s_x = (self.main_width/100)*63.33
        self.start_s_y = (self.main_height/100)*38.63

        #end_time vals
        self.end_lbl_x = (self.main_width/100)*28.33
        self.end_lbl_y = (self.main_height/100)*54.33

        self.end_h_lbl_x = (self.main_width/100)*41.67
        self.end_h_lbl_y = (self.main_height/100)*47.67
        self.end_h_x = (self.main_width/100)*40
        self.end_h_y = (self.main_height/100)*54.63               
       
        self.end_m_lbl_x = (self.main_width/100)*53.33
        self.end_m_lbl_y = (self.main_height/100)*47.67      
        self.end_m_x = (self.main_width/100)*51.67
        self.end_m_y = (self.main_height/100)*54.63
        
        self.end_s_lbl_x = (self.main_width/100)*65
        self.end_s_lbl_y = (self.main_height/100)*47.67      
        self.end_s_x = (self.main_width/100)*63.33
        self.end_s_y = (self.main_height/100)*54.63

        #main window
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
        self.start_s_lbl.move(self.start_s_lbl_x, self.start_s_lbl_y)
        self.start_s = QLineEdit(self)
        self.start_s.setText("0")
        self.start_s.resize(25, 30)
        self.start_s.move(self.start_s_x, self.start_s_y)

        #end_time init        

        self.end_lbl = QLabel("End: ", self)
        self.end_lbl.move(self.end_lbl_x, self.end_lbl_y)
        
        self.end_h_lbl = QLabel("H", self)
        self.end_h_lbl.move(self.end_h_lbl_x, self.end_h_lbl_y)
        self.end_h = QLineEdit(self)
        self.end_h.setText("0")
        self.end_h.resize(25, 30)
        self.end_h.move(self.end_h_x, self.end_h_y)

        self.end_m_lbl = QLabel("M", self)
        self.end_m_lbl.move(self.end_m_lbl_x, self.end_m_lbl_y)
        self.end_m = QLineEdit(self)
        self.end_m.setText("0")
        self.end_m.resize(25, 30)
        self.end_m.move(self.end_m_x, self.end_m_y)        

        self.end_s_lbl = QLabel("S", self)
        self.end_s_lbl.move(self.end_s_lbl_x, self.end_s_lbl_y)
        self.end_s = QLineEdit(self)
        self.end_s.setText("0")
        self.end_s.resize(25, 30)
        self.end_s.move(self.end_s_x, self.end_s_y) 
 
 

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
        start_hrs = self.start_h.text()
        start_mins = self.start_m.text()
        start_secs = self.start_s.text()

        end_hrs = self.end_h.text()
        end_mins = self.end_m.text()
        end_secs = self.end_s.text()
        
        report = self.check_input(start_hrs, start_mins, start_secs, end_hrs, end_mins, end_secs)

        if report[1] == False:
            QMessageBox.warning(self, "Error", report[0], QMessageBox.Ok)
        else:
            
            if self.check_browse_path()== False:
                QMessageBox.warning(self, "No browse path!", "Choose browse path.", QMessageBox.Ok)
            else:
                start_time = self.make_start_time(start_hrs, start_mins, start_secs)

                end_time = self.make_end_time(end_hrs, end_mins, end_secs)
                log = self.get_log()

                if self.check_start_time2(start_time, log) == False:
                    QMessageBox.warning(self, "Bad Input!", "Start time must be smaller than first time stamp in session.", QMessageBox.Ok) 
                if self.check_end_time2(end_time, log) == False:
                    QMessageBox.warning(self, "Bad Input!", "End time must be greater than last time stamp in session.", QMessageBox.Ok)                
                else:
                    interval = self.interval.text()        
                    if self.check_interval_input(interval)== False:
                        QMessageBox.warning(self, "Bad Input!", "Interval must be positive integer number.", QMessageBox.Ok)
                    else:
                        interval = int(interval)
                        browse = open('config/browse.txt', 'r').read()
                        stuff = self.get_dates(log, interval, start_time, end_time)   
                        rows = self.get_rows(log, stuff)
                        table  = self.make_HTML(rows)           
                        f = open("table.html", "w")
                        f.write(table)
                        f.close()
                        QMessageBox.information(self, "Success!", "Table successfully made!", QMessageBox.Ok)

    def make_start_time(self, hrs, mins, secs):
        if len(hrs) == 1: hrs = "0" + hrs
        if len(mins) == 1: mins = "0" + mins
        if len(secs) == 1: secs = "0" + secs

        string_date = hrs + mins + secs
        date = datetime.strptime(string_date, "%H%M%S")
        return date 
    
    def make_end_time(self, hrs, mins, secs):
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
            row = "<tr>\n" + "<td>" + "Interval" + "</td>\n" + "<td>" + interval + "</td>\n" + "<td>" + "-" + "</td>\n" + "<td>" + "-" + "</td>\n" + "</tr>\n"                
            return row
            
    def make_HTML(self, rows):
        table = open("config/begin.txt").read()
        for i in range (0, len(rows)):
            table += rows[i]
        end = open("config/end.txt").read()
        table += end
        return table

    def get_dates(self, log, interval, start_date, end_date):   
        dates = []
        bools = []
        i = 0
        
        for i in range(0, len(log)):
            meteor = log[i].split()
            string_date = meteor[2]          
            date = datetime.strptime(string_date, "%H:%M:%S")
            dates.append(date)
            bools.append(True)
        while start_date <= end_date:
            dates.append(start_date)
            bools.append(False)
            start_date = self.add_interval(start_date, interval)
                          
        self.sort_date_tupple(dates, bools) 
        if dates[len(dates)-1] < end_date:
            dates.append(end_date)
            bools.append(False)
             
        stuff = (dates, bools)
        return stuff

    def add_interval(self, tm, mins):
        fulldate = datetime(1900, 1, 1, tm.hour, tm.minute, tm.second)
        secs = mins*60
        fulldate = fulldate + timedelta(seconds=secs)
        return fulldate 
    
    def sort_date_tupple(self, dates, bools):
        check = False  
        while not check:
            check = True  
            for i in range(0, len(dates)-1):
                if dates[i] > dates[i + 1]:
                    check = False
                    hold = dates[i + 1]
                    dates[i + 1] = dates[i]
                    dates[i] = hold

                    hold_b = bools[i + 1]
                    bools[i + 1] = bools[i]
                    bools[i] = hold_b        
    
    def check_interval_input(self,s):
        try:
            int(s)
            if int(s) > 0:
                return True
            else:
                return False
        except ValueError:
            return False

    def check_browse_path(self):
        path = open('config/browse.txt', 'r').read()        
        if len(path) == 0: return False
        else: return True    
              
        QMessageBox.information(self, "Success!", "Table successfully made!", QMessageBox.Ok)

    def check_input(self, start_hrs, start_mins, start_secs, end_hrs, end_mins, end_secs):
        check = True

        hrs_check = []
        mins_check = []
        secs_check = []
        
        hrs_check = []
        mins_check = []
        secs_check = []

        msg = ""
        
        for i in range (0, 24): 
            hrs_check.append(str(i))
            if i < 9: hrs_check.append("0" + str(i))

        for i in range (0, 59): 
            mins_check.append(str(i))
            if i < 9: mins_check.append("0" + str(i))
        
        for i in range (0, 59): 
            secs_check.append(str(i))
            if i < 9: secs_check.append("0" + str(i))

        if (start_hrs not in hrs_check) or (end_hrs not in hrs_check):
            msg += "Hours must be in range 0-23\n"
            check = False

        if (start_mins not in mins_check) or (end_mins not in mins_check):
            msg += "Minutes must be in range 0-59\n"
            check = False

        if (start_secs not in secs_check) or (end_secs not in secs_check):
            msg += "Seconds must be in range 0-59\n"
            check = False
        
        report = (msg, check)
        return report
    
    def check_start_time2(self, start_date, log):
        check = True
        meteor = log[0].split()
        string_date = meteor[2]
        date = datetime.strptime(string_date, "%H:%M:%S")
        if start_date > date: check = False
        return check

    def check_end_time2(self, end_date, log):
        check = True
        meteor = log[len(log)-1].split()
        string_date = meteor[2]
        date = datetime.strptime(string_date, "%H:%M:%S")
        if end_date < date: check = False
        return check
        	          
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
