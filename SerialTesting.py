from time import sleep
from serial import Serial, SerialException
cxn = Serial('/dev/ttyACM0', baudrate=9600)
while(True):
    try:
        cmd_id = raw_input("Press Enter to Record Data")
        #cxn.write([1])
        #while cxn.inWaiting() < 1:
        #    pass
        while cxn.readline() == "_":
            pass
        result = int(cxn.readline());
        print(result)
    except ValueError:
        print "The Arduino Returned an Incorrect Value: %s" %cxn.readline()
    #sleep(.05)
