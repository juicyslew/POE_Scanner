import pickle as pk
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import cos, sin, pi
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
plt.xlabel("Y")
plt.ylabel("Z")

a = 11120.68
b = 32.8364

fname = 'DankW.pkl'
IR_Data = []
IR_Pos = []
skip = False
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
        print("No data to plot.")
        skip = True

if not skip:
    for i in range(len(IR_Data)):
        dist = IR_Data[i]
        h_pos, v_pos = IR_Pos[i]
        h_ang = (h_pos-90)*pi/180;
        v_ang = (v_pos-90)*pi/180;
        x = dist*cos(h_ang)*cos(v_ang);
        if x > 42:
            continue
        y = dist*sin(h_ang)*cos(v_ang);
        z = dist*sin(v_ang);
        plt.scatter(y, z, color = 'blue')
plt.axis([-25, 25,-8,25])
plt.show()
