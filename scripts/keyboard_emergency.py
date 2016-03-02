#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
02/03/2016
@author: Sam Pfeiffer
"""

import rospy
from std_msgs.msg import Bool
import sys
import os
import termios


# From http://stackoverflow.com/questions/983354/how-do-i-make-python-to-wait-for-a-pressed-key
def wait_key():
    ''' Wait for a key press on the console and return it. '''
    result = None
    fd = sys.stdin.fileno()

    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)

    try:
        result = sys.stdin.read(1)
    except IOError:
        pass
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

    return result


if __name__ == '__main__':
    rospy.init_node('keyboard_emergency_button')
    # Publish in the topic /external_stop_trigger of type std_msgs/Bool
    # a message with value True to trigger an emergency stop via software
    # this will unload all current running controllers that control some joint.
    # 
    # A message with value False should be published to enable future
    # triggers by resetting the trigger node.
    pub = rospy.Publisher('/external_stop_trigger', Bool, queue_size=5)
    rospy.loginfo("\n\n\nPress ANY KEY to trigger emergency stop.\n\n\nStop with Control+C+Enter.")
    while not rospy.is_shutdown():
        key_pressed = wait_key()
        rospy.logwarn("Publishing emergency stop trigger! (pressed '" + str(key_pressed) + "')")
        pub.publish(Bool(True))
        rospy.sleep(0.5)
        # Reset the trigger or we won't stop controllers again
        # with the next keypress
        pub.publish(Bool(False))
