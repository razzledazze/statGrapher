#Graphs statistics with arbitrary values on the x and y axis

import csv
from turtle import Turtle

csvRead = open("data.csv")
csvRead = csv.reader(csvRead)

def getRowCount():
    rowCount = 0
    for i in csvRead:
        rowCount += 1
    return rowCount

print(getRowCount())