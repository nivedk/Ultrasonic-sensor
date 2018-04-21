import serial
import numpy
import math as m
import matplotlib.pyplot as plt
import matplotlib as mpl
from drawnow import *
mpl.style.use('default')
i=0
p=(m.pi)/180
#create object that reads data from arduino
arduinoData=serial.Serial('com11',9600) #put port and baud rate
r=[]
theta=[]
plt.ion() #tell matplotlib that this is live data

def graph():
    axl=plt.subplot(111,polar=True)
    axl.scatter(theta,r)

while True:         #forever running loop
    while (arduinoData.inWaiting()==0): #wait here until there is data i.e. if no data
        pass #do nothing
    arduinoString = arduinoData.readline().strip().decode() #read the first line of the serial port
    dataArray = arduinoString.split(',')
    while i<20:
    	arduinoString = arduinoData.readline().strip().decode() #read the first line of the serial port
    	dataArray = arduinoString.split(',')
    	print(dataArray,'i is',i)
    	i=i+1
    if i==20:
    	angle=float(dataArray[0])*p          #store it as float
    	dis=float(dataArray[1])
    	theta.append(angle)                  #store it in radius array
    	r.append(dis)
    	print(angle,dis)
    	if angle>0:
    		drawnow(graph)
    	if angle==0:
    		theta = [0]
    		r = [0]
    	