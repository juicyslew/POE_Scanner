import numpy as np
import matplotlib.pyplot as plt
import pickle as pk

fname = "CalibrationData.pkl"

IR_Data = []
with open(fname, 'rb') as f:
    IR_Data = pk.load(f)

#distance = np.array([i[0] for i in IR_Data])
#voltage = np.array([i[1] for i in IR_Data])

#print distance
#print voltage
data = np.array(IR_Data)

x = data[:,1]
y = data[:,0]
a = 11120.68
b = 32.8364
t = np.arange(100, 1024, 1)
yt = a/(t-b)

print data

plt.plot(x, y, 'b*')
plt.plot(t, yt, 'r-')

plt.xlabel('Voltage (0-1024)')
plt.ylabel('Distance (cm)')
plt.title('Voltage vs Distance')
plt.grid(True)
plt.savefig("test.png")
plt.show()
