"""
todo:
        higlighting intervals
        make GUI
        save name and date in log file
        make table with meteor count for every interval and for every sohwer in an interval
        make table with magnitude distribution for the whole observation 
"""

import sys
import os

session = open("example.txt", "r").read().splitlines()

table_rows = []

for i in range(0, len(session)):
        meteor = session[i].split()
        print(meteor)
        row = "<tr>\n" + "<td>" + str(i+1) + "</td>\n" + "<td>" + meteor[2] + "</td>\n" + "<td>" + meteor[1] + "</td>\n" + "<td>" + meteor[0] + "</td>\n" + "</tr>\n"
        table_rows.append(row)

begin = open("templates/first.txt").read()
table = begin

for i in range(0, len(table_rows)):
        table += str(table_rows[i])

end = open("templates/last.txt").read()
table += end 

f = open("table.html", "w")
f.write(table)
f.close()

