#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
from geographic_msgs.msg import GeoPoseStamped

def waypoint_callback(msg, args):

	lat = Float32()
	lon = Float32()

	lat.data = msg.pose.position.latitude
	lon.data = msg.pose.position.longitude

	args[0].publish(lat)
	args[1].publish(lon)

if __name__ == '__main__':

	rospy.init_node('moos_waypoint_pub')

	lat_pub = rospy.Publisher('/waypoints_lat', Float32, queue_size = 1)
	lon_pub = rospy.Publisher('/waypoints_lon', Float32, queue_size = 1)

	way_sub = rospy.Subscriber('/waypoints', GeoPoseStamped, waypoint_callback, [lat_pub, lon_pub])

	rospy.spin()