#!usr/bin/env python

import rospy
from std_msgs.msg import String


def param_talker():
	rospy.init_node('param_talker')


	global_example = rospy.get_param("/global_example")
	rospy.info("%s is %s", rospy.resolve_name('/global_example'), global_example)

	utterance = rospy.get_param('utterance')
    rospy.loginfo("%s is %s", rospy.resolve_name('utterance'), utterance)

	topic_name = rospy.get_param('~topic_name')
    rospy.loginfo("%s is %s", rospy.resolve_name('~topic_name'), topic_name)

	default_param = rospy.get_param('default_param', 'default_value')
    rospy.loginfo('%s is %s', rospy.resolve_name('default_param'), default_param)
	
	gains = rospy.get_param('gains')
    p, i, d = gains['P'], gains['I'], gains['D']
    rospy.loginfo("gains are %s, %s, %s", p, i, d)

	rospy.loginfo('setting parameters...')
    rospy.set_param('list_of_floats', [1., 2., 3., 4.])
    rospy.set_param('bool_True', True)
    rospy.set_param('~private_bar', 1+2)
    rospy.set_param('to_delete', 'baz')
    rospy.loginfo('...parameters have been set')

	if rospy.has_param('to_delete'):
        rospy.delete_param('to_delete')
        rospy.loginfo("deleted %s parameter"%rospy.resolve_name('to_delete'))
    else:
        rospy.loginfo('parameter %s was already deleted'%rospy.resolve_name('to_delete'))

	param_name = rospy.search_param('global_example')
    rospy.loginfo('found global_example parameter under key: %s'%param_name)

	pub = rospy.Publisher(topic_name, String, queue_size=10)
    while not rospy.is_shutdown():
        pub.publish(utterance)
        rospy.loginfo(utterance)
        rospy.sleep(1)


if __name__ == '__main__':
    try:
        param_talker()
    except rospy.ROSInterruptException: 
		pass

