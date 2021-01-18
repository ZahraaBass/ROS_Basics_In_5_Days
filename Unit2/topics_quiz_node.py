#! /usr/bin/env python

'''
This code will check if the robot has nothing in front of it (ie the reading of the laser at 360 (directly in front of robot) is >1.6, the the robot will move straight. else, the robot will turn.
'''

import rospy 
import time
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


read = LaserScan()
move = Twist()

def read_values(read):
	 Value_Straight = read.ranges[360]
	 if Value_Straight > 1.6:
	  	print("Range greater than 1.6, move straight")
	  	move.linear.x = 0.5
		move.angular.z = 0


	 else: 
	  	print("Range smaller than 1.6, turn")
		move.linear.x = 0 # Reset the value to 0. If you don't reset it, x will still be assigned to 0.5 and the robot will turn while moving.
		move.angular.z = -0.5
	 pub.publish(move)
			
	 


rospy.init_node("node")

sub = rospy.Subscriber("/scan", LaserScan, read_values)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rospy.spin()
