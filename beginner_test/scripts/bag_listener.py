#!/usr/bin/env python


import rosbag

bag =rosbag.Bag('../bagfiles/test.bag')

for topic, msg, t in bag.read_messages(topics=['chatter', 'numbers']):
	print topic, msg, t

bag.close()

