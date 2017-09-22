#!/usr/local/bin/python

from serial import Serial, SerialException
import pickle as pk
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import cos, sin, pi


plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.xlabel("X")
plt.ylabel("Y")
# The Serial constructor will take a different first argument on
# Windows. The first argument on Windows will likely be of the form
# 'COMX' where 'X' is a number like 3,4,5 etc.
# Eg.cxn = Serial('COM5', baudrate=9600
#
# NOTE: You won't be able to program your Arduino or run the Serial
# Monitor while the Python script is running.

a = 11120.68
b = 32.8364
cxn = Serial('/dev/ttyACM1', baudrate=9600)

fname = 'LastSessionData.pkl'
IR_Data = []
IR_Pos = []
with open(fname, 'rb') as f:
    try:
        Data = pk.load(f)
        if type(Data) != list:
            IR_Data = []
            IR_Pos = []
        else:
            IR_Data = Data[0]
            IR_Pos = Data[1]
    except EOFError:
        IR_Data = []
        IR_Pos = []

plt.show()
count = 0;
while(True):
    try:
        cxn.write([1])
        while cxn.inWaiting() < 1:
            pass
        result = str(cxn.readline());

        result = result.split("|");

        volt = int(result[0])
        if (volt < 90 or volt > 700):
            continue
        h_pos = int(result[1])
        v_pos = int(result[2])
        h_ang = (h_pos-90)*pi/180;
        v_ang = (v_pos-90)*pi/180;
        dist = a/(volt-b)
        x = -dist*cos(h_ang)*sin(v_ang);
        y = dist*sin(h_ang)*sin(v_ang);
        z = dist*cos(v_ang);
        color = 'blue'
        if dist > 100:
            color = 'red'
        ax.scatter([x], [y], [z], color=color)

        plt.draw()
        plt.pause(.01)
        IR_Data.append(dist)
        IR_Pos.append((h_pos, v_pos))
        #print "IR Reads: %i which is %i at angle %i" %(volt, dist, pos)
        print "(x,y,z): (%i, %i, %i)" %(x, y, z)

        if count % 150 == 0:
            with open(fname, 'wb') as f:
                pk.dump([IR_Data, IR_Pos], f);
        count += 1
    except ValueError:
        print "The Arduino Returned an Incorrect Value"
