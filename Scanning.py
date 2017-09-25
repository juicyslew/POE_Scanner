#!/usr/local/bin/python

from serial import Serial, SerialException
import pickle as pk
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import cos, sin, pi
import numpy as np

#plt.ion()
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
cxn = Serial('/dev/ttyACM0', baudrate=9600)

fname = 'LastSessionData.pkl'
IR_Data = []
IR_Pos = []
"""with open(fname, 'rb') as f:
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
        IR_Pos = []"""

#plt.show()
count = 0;
while(count < 2500):
    try:
        cxn.write([1])
        while cxn.inWaiting() < 1:
            pass
        result = str(cxn.readline());

        result = result.split("|");

        volt = int(result[0])
        if (volt < 90 or volt > 700):
            print("filtered out value")
            continue
        h_pos = int(result[1])
        v_pos = int(result[2])
        h_ang = float((h_pos-90)*pi/180);
        v_ang = float((v_pos-90)*pi/180);
        dist = float(a/(volt-b))
        x = dist*cos(h_ang)*cos(v_ang);
        y = dist*sin(h_ang)*cos(v_ang);
        z = dist*sin(v_ang);
        color = 'blue'
    	if x < 50 and z > -8:
            ax.scatter([x], [y], [z], color=color)

            if (count % 50):
                plt.draw()

            IR_Data.append(dist)
            IR_Pos.append((h_pos, v_pos))
            #print "IR Reads: %i which is %i at angle %i" %(volt, dist, pos)
            print "(x,y,z): (%f, %f, %f)" %(x, y, z)



        else:
            print("filtered out value")
        count += 1
        if count % 20 == 0:
            with open(fname, 'wb') as f:
                pk.dump([IR_Data, IR_Pos], f);
    except ValueError:
        print "The Arduino Returned an Incorrect Value: %s" % cxn.readline()

plt.show()
#heatmap, xedges, yedges = np.histogram2d([x[0] for x in IR_Pos], [x[1] for x in IR_Pos], bins=50)
#extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

#plt.clf()
#plt.imshow(heatmap.T, extent=extent, origin='lower')
#plt.show()
