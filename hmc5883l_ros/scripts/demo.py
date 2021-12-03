#!/bin/env python3

import rospy
from i2c_hmc5883l_pub import i2c_hmc5883l

if __name__ == "__main__":

    rospy.init_node()
    hmc = i2c_hmc5883l(1)

    hmc.setContinuousMode()

    rospy.spin()
