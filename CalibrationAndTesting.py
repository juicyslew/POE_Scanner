#!/usr/local/bin/python

from serial import Serial, SerialException
import pickle as pk

# The Serial constructor will take a different first argument on
# Windows. The first argument on Windows will likely be of the form
# 'COMX' where 'X' is a number like 3,4,5 etc.
# Eg.cxn = Serial('COM5', baudrate=9600
#
# NOTE: You won't be able to program your Arduino or run the Serial
# Monitor while the Python script is running.
cxn = Serial('/dev/ttyACM0', baudrate=9600)

fname = 'CalibrationData.pkl'
IR_Data = []
with open(fname, 'rb') as f:
    try:
        IR_Data = pk.load(f)
        if type(IR_Data) != list:
            IR_Data = []
    except EOFError:
        IR_Data = []

while(True):
    try:
        cmd_id = raw_input("Press Enter to Record Data")
        cxn.write([1])
        while cxn.inWaiting() < 1:
            pass
        result = int(cxn.readline());
        continuing = False
        while(True):
            try:
                distance = float(raw_input("What distance was that in centemeters?"));
                if distance == 0:
                    continuing = True
                    break
            except ValueError:
                print "You must enter a float for distance"
                continue
            break
        if continuing:
            continue;
        IR_Data.append((distance, result))
        print "IR Reads: %i" %result
        with open(fname, 'wb') as f:
            pk.dump(IR_Data, f);
    except ValueError:
        print "The Arduino Returned an Incorrect Value"
