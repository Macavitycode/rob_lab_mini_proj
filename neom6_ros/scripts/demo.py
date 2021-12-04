#!/bin/env python3

import rospy
from uart_neom6_pub import neom6

if __name__ == '__main__':

    neo = neom6()
    rospy.spin()
