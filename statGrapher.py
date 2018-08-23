#Graphs statistics with arbitrary values on the x and y axis

import csv
from turtle import Turtle

csvRead = open("data.csv")
csvRead = csv.reader(csvRead)

def initTurtle(name,colour):
    name.penup()
    name.color(colour)
    name.hideturtle()
    name.speed(0)

def goCentre(turt):
    turt.penup()
    turt.goto(-300,-200)
    turt.pendown()

def drawAxis():
    axis = Turtle()
    initTurtle(axis,"black")
    goCentre(axis)
    axis.goto(300,-200)
    goCentre(axis)
    axis.goto(-300,200)

def getRowCount():
    rowCount = 0
    for i in csvRead:
        rowCount += 1
    return rowCount

def initData():
    xAxis = []
    yAxis = []
    for row in csvRead:
        xAxis.append(row[0])
        yAxis.append(row[1])
    return xAxis,yAxis

xAxis = initData()[0]
yAxis = initData()[1]

def determineIntervals(xAxis,yAxis):
    xInterval = 600/len(xAxis)
    yInterval = 600/len(yAxis)
    return(xInterval,yInterval)

xInterval = determineInterval[0]
yInterval = determineInterval[1]

def drawGraph(turt):
    for i in range(len(xAxis)):
        turt.goto(xInterval*i,yInterval*i)

drawAxis()
graph = Turtle()
initTurtle(graph,"red")
goCentre(graph)

