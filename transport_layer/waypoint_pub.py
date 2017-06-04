#!/usr/bin/env python

import rospy
from geographic_msgs.msg import GeoPoseStamped


if __name__ == '__main__':

	rospy.init_node('waypoint_pub')

	way_pub = rospy.Publisher('/waypoints', GeoPoseStamped, queue_size = 1)

	waypoint_lat = 44.566881
	waypoint_lon = -123.275972

	while not rospy.is_shutdown():

		pose = GeoPoseStamped()
				
		pose.header.stamp = rospy.get_rostime()
		pose.header.frame_id = 'world'

		pose.pose.position.latitude = waypoint_lat
		pose.pose.position.longitude = waypoint_lon
		pose.pose.position.altitude = float('NaN')

		way_pub.publish(pose)

		waypoint_lat += 0.0001
		waypoint_lon += 0.0001

		rospy.sleep(0.5)