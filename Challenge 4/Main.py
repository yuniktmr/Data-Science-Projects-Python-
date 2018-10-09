#ChocolateGecko
#Challenge 4
#Last edited: March 28th 2018
#Source: Lectures, TA, Stack overflow
import csv
import numpy as np
import math
import matplotlib.pyplot as mplot
import sys
#populate the US border outline data
file=sys.argv[0]
borderdata=[]
k=int(input("Enter the value of k"))
with open(r'C:\Users\yunik\Documents\CSCI 343\Challenge 4\us_outline.csv') as csvfile:
    datareader=csv.reader(csvfile)
    for row in datareader:
        borderdata.append(row)
us_x = []
us_y = []
for i in range(0,len(borderdata)):
    for j in range(0,len(borderdata[i])):
        if (j % 2 == 0):
            us_x.append(np.float32(borderdata[i][j]))
        else:
            us_y.append(np.float32(borderdata[i][j]))
#-------------------------------------------------------------------
#populate the data from the data csv
x = []
y = []
population = []
pointdata = []
with open(r'C:\Users\yunik\Documents\CSCI 343\Challenge 4\data.csv') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        pointdata.append(row)
for m in range(0,len(pointdata)):
    for n in range(0,len(pointdata[m])):
        if (n % 3 == 0):
            x.append(np.float32(pointdata[m][n]))
        elif (n % 3 == 1):
            y.append(np.float32(pointdata[m][n]))
        else:
            population.append(np.float32(pointdata[m][n]))
# ----------------------------------------------------------------------
distance=[]
netpop=[]
final=[]
x_grid=[]
y_grid=[]
#approximation
for row in range(194):
    for col in range (120):
        for i in range(len(x)):
            xdist=math.pow((x[i]-row),2)
            ydist=math.pow((y[i]-col),2)
            dist = math.sqrt(xdist+ydist)
            distance.append([dist,population[i]])
        distance = sorted(distance, key=lambda val:val[0])
        final= distance[0:k]
        dis ,pop = zip(*final)
        netpop.append(np.mean(pop))
        #if(row>=min(x_us_outline) and row<=max(x_us_outline) and col>=min(y_us_outline) and col<=max(y_us_outline)):
        x_grid.append(row)
        y_grid.append(col)
        distance=[]
mplot.plot(us_x,us_y,c='#000000')
mplot.scatter(x_grid,y_grid,marker='s',c=netpop, cmap='viridis')
mplot.show()
