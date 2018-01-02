#!/usr/bin/env python

import rosbag
from std_msgs.msg import Int32, String


bag = rosbag.Bag('../bagfiles/test.bag', 'w')

try:
	strs = String()
	strs.data = 'foo'

	i = Int32()
	i.data = 42

	bag.write('chatter', strs)
	bag.write('numbers', i)
finally:
	bag.close()


