'''

This node will publish to the topic: /cmd_vel in order to move the robot.
First launch any gazebo simulation that subscribes to the cmd_vel topic (In my case I launched Husky using: roslaunch husky_gazebo husky_playpen.launch
Run this node using: rosrun <package name> simple_topic_publisher

'''


# ---------------------------------------------------Start Code Here------------------------------------------------------------------------------------------------------
#! /usr/bin/env python  #(This line will make sure that your scripts run inside the virtual environment, just copy and paste it at the beginining of each node using python.)


# Import the necessary libraries, here we need:
# rospy: a python library used to quickly interface with ROS Topics, Services, and Parameters.
# Twist from geometry_msgs: This allows to provide messages for common geometric primitives such as points, vectors, and poses.
import rospy 
from geometry_msgs.msg import Twist

# Initialize the node called: topic_publisher
rospy.init_node('topic_publisher')

# Create a Publisher that will publish (Send Messages) to a topic called "/cmd_vel". The Messages published are of type "Twist". 
# queue_size is the size of the outgoing message queue used for asynchronous publishing (1 is good for this case, read here for more http://wiki.ros.org/rospy/Overview/Publishers%20and%20Subscribers)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

# Create a Rate Object, meaning we set a publish rate to 2 Hz. i.e. when rate.sleep() is called, the msg will be sent 2 times per second.
rate = rospy.Rate(2)

# Create an instant of the Msg Twist called move (or just anything), so we can use it later:
move = Twist()

# Send Command velocity messages through the instant move we just made.
move.linear.x = 0.5
move.angular.z = 0.5

# As longs as the Control+C is not pressed:
while not rospy.is_shutdown():  
    # Publish the message:
    pub.publish(move) 
    # the msg will be published at a rate of 2x per second.
    rate.sleep()

