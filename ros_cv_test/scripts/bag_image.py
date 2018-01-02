#!/usr/bin/env python

import rospy
import rosbag
import cv2

from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image


class image_creator:
	
	def __init__(self):
		self.image_pub = rospy.Publisher("/camera/image_raw", Image,queue_size=10)
		self.bridge = CvBridge()
		self.cv_image = cv2.imread('/home/zyq507/catkin_ws/src/ros_cv_test/image/test.jpeg')
		
	
	def write_bag(self):
		with rosbag.Bag('../bagfiles/imagetest.bag', 'w') as bag:
			bag.write('imagetest', self.imgmsg)


	def pub(self):
			try:
				imgmsg = self.bridge.cv2_to_imgmsg(self.cv_image, "bgr8")
			except CvBridgeError as e:
				print(e)
			self.image_pub.publish(imgmsg)


if __name__ == '__main__':

	ic = image_creator()

	try:
		rospy.init_node('image_creator', anonymous=True)
		rate = rospy.Rate(1)

		while not rospy.is_shutdown():
			ic.pub()
			rate.sleep()

	except rospy.ROSInterruptException:
		pass


		

