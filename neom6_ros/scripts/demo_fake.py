#!/bin/env python3

import rospy
from neom6_ros.msg import neom6_msg

class neom6:

    def __init__(self, topic='/neom6', publish_rate=1):

        try:
            self.lat = rospy.get_param('lat')
            self.long = rospy.get_param('long')

        except:
            print('Set lat and long in param server')

        period = rospy.Duration(publish_rate)
        self.pub = rospy.Publisher(topic, neom6_msg, queue_size=10)
        
        self.timer = rospy.Timer(period, self.timerCallback)
        self.counter = 0


        self.msg = neom6_msg()

        self.msg.lat = self.lat
        self.msg.long = self.long

    def timerCallback(self, event):

        self.counter += 1
        print('publishing ', self.counter)

        self.pub.publish(self.msg)

if __name__ == '__main__':
    
    rospy.init_node('fake_gps')
    neo = neom6()
    rospy.spin()

