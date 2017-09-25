import numpy as np
import matplotlib.pyplot as plt
import pickle as pk

fname = "FinCalibrationData2.pkl"
fname2 = "TestingData.pkl"

IR_Data = []
IR_Test = []
with open(fname, 'rb') as f:
    IR_Data = pk.load(f)
with open(fname2, 'rb') as f:
    IR_Test = pk.load(f)

#distance = np.array([i[0] for i in IR_Data])
#voltage = np.array([i[1] for i in IR_Data])

#print distance
#print voltage
data = np.array(IR_Data)
test = np.asarray([[x for x in np.arange(22.5, 120, 5)],[497, 435, 371, 325, 286, 256, 232, 209, 193, 174, 165, 153, 145, 137, 129, 121, 118, 109, 105, 101]])

x = data[:,1]
y = data[:,0]
a = 11120.68
b = 29.39476351
t = np.arange(100, 1024, 1)
yt = a/(t-b)

print data

#plt.plot(x, y, 'b*')
plt.plot(t, yt, 'b-')
print(test)
plt.plot(test[1,:], test[0,:], 'r*')


plt.legend(['Calibration Data', 'Prediction Model', 'Testing Data'])
plt.xlabel('Voltage (0-1024)')
plt.ylabel('Distance (cm)')
plt.title('Voltage vs Distance')
plt.grid(True)
plt.savefig("Error.png")
plt.show()
