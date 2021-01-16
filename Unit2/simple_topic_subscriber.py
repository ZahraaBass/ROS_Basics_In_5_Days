#! /usr/bin/env python

import rospy 
from nav_msgs.msg import Odometry

# Create a function that will print the data in "msg"
def listener(msg):
	# To print the Whole msg on the topic:
	  print msg
	# To print specific parts of the msg use:
	# print msg.header
	# print msg.pose
	# print msg.orientation

# Create a node called "topic_subscriber"       
rospy.init_node("topic_subscriber")

# IF using husky_playpen world, then Subscribe to the topic: /husky_velocity_controller/odom , which has messages of type: Odometry flowing into it, and call the function listener, which prints out these msgs. 
sub = rospy.Subscriber('/husky_velocity_controller/odom', Odometry, listener)
# IF exactly following the tutporials (using turtlebot2), then change "/husky_velocity_controller/odom" to "/odom"

# Keep doing this till infinity:
rospy.spin()

# rospy. spin() will effectively go into an infinite loop until it receives a shutdown signal (e.g. ctrl-c ). During that loop it will process any events that occur, such as data received on a topic or a timer triggering, when they occur but otherwise it will sleep..
