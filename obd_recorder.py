#!/usr/bin/env python

import obd_io
import serial
import platform
import obd_sensors
from datetime import datetime
import time

class OBD_Recorder():
    def __init__(self, path, log_items):
        self.port = None
        self.sensorlist = []
        localtime = time.localtime(time.time())
        filename = path+"bike-"+str(localtime[0])+"-"+str(localtime[1])+"-"+str(localtime[2])+"-"+str(localtime[3])+"-"+str(localtime[4])+"-"+str(localtime[5])+".log"
        self.log_file = open(filename, "w", 128)
        self.log_file.write("Time,RPM,MPH,Throttle,Load,Gear\n");

        for item in log_items:
            self.add_log_item(item)

    def connect(self):
        portnames = ['/dev/ttyUSB0']
        print portnames
        for port in portnames:
            self.port = obd_io.OBDPort(port, None, 2, 2)
            if(self.port.State == 0):
                self.port.close()
                self.port = None
            else:
                break

        if(self.port):
            print "Connected to "+self.port.port.name
            
    def is_connected(self):
        return self.port
        
    def add_log_item(self, item):
        for index, e in enumerate(obd_sensors.SENSORS):
            if(item == e.shortname):
                self.sensorlist.append(index)
                print "Logging item: "+e.name
                break
            
            
    def record_data(self):
        if(self.port is None):
            return None
        
        print "Logging started"
        
        while 1:
            log_string = int(time.time() * 1000)
            results = {}
            for index in self.sensorlist:
                (name, value, unit) = self.port.sensor(index)
                log_string = log_string + ","+str(value)
                results[obd_sensors.SENSORS[index].shortname] = value;

            self.log_file.write(log_string+"\n")
                 
logitems = ["rpm", "speed", "throttle_pos", "load"]
o = OBD_Recorder('/home/pi/logs/', logitems)
o.connect()
if not o.is_connected():
    print "Not connected"
o.record_data()
