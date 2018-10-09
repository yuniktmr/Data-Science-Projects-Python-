#Spirit Animal: ChocolateGecko
#Last edited: 04/19/2018
#Challenge 5
#Source: Lecture, Stack Overeflow
import numpy as np
import matplotlib.pyplot as mplot
import csv
#-----------------------variable instantiation------------------------
dataset = []
time = []
frequency = []
intensity = []
with open(r'C:\Users\yunik\Documents\CSCI 343\Challenge 5\ChocolateGecko.csv') as csvfile:
    datareader=csv.reader(csvfile)
    for row in datareader:
        dataset.append(row)
#----------------------fill the lists-------------------------
Flist=[]
f1t1=[]
f1s1=[]
f2t2=[]
f2s2=[]
f3t3=[]
f3s3=[]
f4t4=[]
f4s4=[]
f5t5=[]
f5s5=[]
#------------list of frequencies---------------------------------------------------------
for line in dataset:
    if line[1] not in Flist:
        Flist.append(line[1])
    else:
        continue
#print(Flist)
#--------------populate lists for signal intensity and time for each frequency-------------
for freq in dataset :
    if(float(freq[1])==float(Flist[0])):
        f1t1.append(float(freq[0]))
        f1s1.append(float(freq[2]))
    elif(float(freq[1])==float(Flist[1])):
        f2t2.append(float(freq[0]))
        f2s2.append(float(freq[2]))
    elif(float(freq[1])==float(Flist[2])):
        f3t3.append(float(freq[0]))
        f3s3.append(float(freq[2]))
    elif(float(freq[1])==float(Flist[3])):
        f4t4.append(float(freq[0]))
        f4s4.append(float(freq[2]))
    elif(float(freq[1])==float(Flist[4])):
        f5t5.append(float(freq[0]))
        f5s5.append(float(freq[2]))
#----------------find correlationcoeff for all frequency------------------------
a=np.corrcoef(f1t1,f1s1).flatten()
b=np.corrcoef(f2t2,f2s2).flatten()
c=np.corrcoef(f3t3,f3s3).flatten()
d=np.corrcoef(f4t4,f4s4).flatten()
e=np.corrcoef(f5t5,f5s5).flatten()
#-----------------------------------------------------
dict={}
timedict={a[1]:f1t1,b[1]:f2t2,c[1]:f3t3,d[1]:f4t4,e[1]:f5t5}
signaldict={a[1]:f1s1,b[1]:f2s2,c[1]:f3s3,d[1]:f4s4,e[1]:f5s5}
#-------------------------------------------------------
def Maxtime(a):
    for x in timedict.keys():
        if (a==x):
            return timedict.get(a)
def Mintime(a):
    for x in timedict.keys():
        if (a==x):
            return timedict.get(a)
def MaxSig(a):
    for x in signaldict.keys():
        if (a==x):
            return signaldict.get(a)
def MinSig(a):
    for x in signaldict.keys():
        if (a==x):
            return signaldict.get(a)
#---------------------------------------------------
print(timedict)
List=[]
#----------------list for all correlation values for the signals------------------------
List.append(a[1])
List.append((b[1]))
List.append(c[1])
List.append(d[1])
List.append(e[1])
#----------------find the required signals by analyzing the correlation coefficient-----------------
Max=max(List)#---Max correlation coeff
Min=min(List)#---Min correlation coeff
Maxtime=(Maxtime(Max))#---returns the time and signal for first signal
Mintime=(Mintime(Min))
MaxSignal=MaxSig(Max)#----returns time and signal for second signal
MinSignal=MinSig(Min)
#----------------standard deviation--------------------------------------
def dev(a):
    sum=0
    sd=0
    squared_distance=0
    for x in a:
        sum=sum+x
    avg=sum/len(a)
    for y in a:
        squared_distance+=(y-avg)**2
    sd=np.sqrt(squared_distance/len(a))
    return sd
#-----------------------Slope and y-intercept for linear regression----------------------
Slope1=Max*(dev(MaxSignal)/dev(Maxtime))
Slope2=Min*(dev(MinSignal)/dev(Mintime))
Yint1=np.mean(MaxSignal)-(Slope1*np.mean(Maxtime))
Yint2=np.mean(MinSignal)-(Slope2*np.mean(Mintime))
#-------compute y values for linear regression------------------------
ylist1=[((Slope1*x)+Yint1) for x in Maxtime]
ylist2=[((Slope2*x)+Yint2) for x in Mintime]
#-----------for polynomial regression-------------------
param1=np.polyfit((Maxtime),(MaxSignal),2)
required1=np.polyval(param1,(sorted(Maxtime)))
param2=np.polyfit((Mintime),(MinSignal),2)
required2=np.polyval(param2,sorted(Mintime))
#-----plot for linear regression-----------------------------
mplot.plot((Maxtime),ylist1,color='red')
mplot.plot((Mintime),ylist2,color='red')
#---------plot for polynomial regression-------------------------------
mplot.plot(sorted(Maxtime),required1,color='blue')
mplot.plot(sorted(Mintime),required2,color='blue')
#-----------plot for signal data--------------------------------
mplot.xlabel("Time")
mplot.ylabel("intensity")
mplot.scatter(f1t1,f1s1,s=75,color='green')
mplot.scatter(f2t2,f2s2,s=75,color='yellow')
mplot.scatter(f3t3,f3s3,s=75,color='orange')
mplot.scatter((f4t4),(f4s4),s=75,color='blue')
mplot.scatter((f5t5),(f5s5),s=75,color='red')
mplot.show()
