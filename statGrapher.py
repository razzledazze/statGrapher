#Graphs statistics with arbitrary values on the x and y axis

import csv
from turtle import Turtle
import turtle
import time

screen = turtle.Screen()
screen.tracer(0,0)

csvRead = open("data.csv")
csvRead = csv.reader(csvRead)

def populateIndex(index):
    write = open("data.csv","w")
    write = csv.writer(write)
    def multiplyIndex(i,index):
        for j in range(index-1):
            i *= i
        return i
    for i in range(100):
        write.writerow([i,multiplyIndex(i,index)])

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

def initData(csvRead):
    xAxis = []
    yAxis = []
    for row in csvRead:
        xAxis.append(int(row[0]))
        yAxis.append(int(row[1]))
    return xAxis,yAxis

def greatestValue(array):
    value = array[0]
    for i in array:
        if i > value:
            value = i
    return value

populateIndex(2)
bothAxis = initData(csvRead)
xAxis = bothAxis[0]
yAxis = bothAxis[1]

xInterval = 600/len(xAxis)
yMultiplier = 400 / greatestValue(yAxis)

def drawGraph(turt):
    for i in range(len(xAxis)):
        turt.goto((xInterval*(i))-300,(yAxis[i]*yMultiplier)-200)

drawAxis()
graph = Turtle()
initTurtle(graph,"red")
goCentre(graph)
drawGraph(graph)

screen.update()
time.sleep(5)
screen.update()
