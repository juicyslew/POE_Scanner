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

x = 1/data[:,0]
y = data[:,1]
features = np.polyfit(x, y, 1)
t = np.arange(0,.1, 0.001)
yt = t*features[0] + features[1]

print data
print features

plt.plot(x, y, 'b*')
plt.plot(t, yt, 'r-')

plt.xlabel('1/Distance (1/cm)')
plt.ylabel('Voltage (0-1024)')
plt.title('1/Distance vs Voltage')
plt.grid(True)
plt.savefig("test.png")
plt.show()
