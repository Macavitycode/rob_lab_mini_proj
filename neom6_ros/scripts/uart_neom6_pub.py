#!/bin/env python3

import serial
import time
import string
import pynmea2

import rospy
from neom6_ros.msg import neom6_msg

class neom6:


    def __init__(self, topic='/neom6', publish_rate=10):

        self.port = "/dev/ttyS0"
        self.ser = serial.Serial(port, baudrate=9600, timeout=0.5)
        self.dataout = pynmea2.NMEAStreamReader()
        self.newdata = ser.readline()

        period = rospy.Duration(publish_rate)
        self.pub = rospy.Publisher(topic, neom6_msg, queue_size=10)
        
        self.timer = rospy.Timer(period, self.timerCallback)
        self.counter = 0

    def timerCallback(self, event):

        msg = neom6_msg

        if newdata[0:6] == "$GPRMC":
            newmsg = pynmea2.parse(self.newdata)
            lat = newmsg.latitude
            long = newmsg.longitude
        
        try:
            msg.lat = lat
            msg.long = long

        except:
            msg.lat = 0
            msg.long = 0

        self.counter += 1

        print('publishing ', self.counter)
        self.pub.publish(msg)
