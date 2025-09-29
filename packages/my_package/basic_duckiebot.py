#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def move_duckiebot():
    rospy.init_node("basic_duckiebot_controller", anonymous=True)
    pub = rospy.Publisher("/duckiebot1/car_cmd", Twist, queue_size=10)

    rate = rospy.Rate(10)  # 10 Hz
    vel_msg = Twist()
    vel_msg.linear.x = 0.2   # forward speed
    vel_msg.angular.z = 0.0  # no rotation

    rospy.loginfo("Duckiebot moving forward...")

    while not rospy.is_shutdown():
        pub.publish(vel_msg)
        rate.sleep()

if __name__ == "__main__":
    try:
        move_duckiebot()
    except rospy.ROSInterruptException:
        pass
