#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Copyright (c) 2011, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the Willow Garage, Inc. nor the names of its
#      contributors may be used to endorse or promote products derived from
#       this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
import os
import rospy
import time
from geometry_msgs.msg import Twist,Pose, PoseWithCovarianceStamped, Point, Quaternion
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from actionlib_msgs.msg import *
import sys, select, termios, tty
import  xml.dom.minidom
import rospy
from std_msgs.msg import String

import sys, select, termios, tty

msg = """
Control Your Turtlebot!
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%
space key, k : force stop
anything else : stop smoothly

CTRL-C to quit
"""

moveBindings = {
    'i': (1, 0),
    'o': (1, -1),
    'j': (0, 1),
    'l': (0, -1),
    'u': (1, 1),
    ',': (-1, 0),
    '.': (-1, 1),
    'm': (-1, -1),
    u'往前走':(1,0),
    u'往后走':(-1,0),
    u'往右转':(0,-1),
    u'往左转':(0,1),
}

speedBindings = {
    'q': (1.1, 1.1),
    'z': (.9, .9),
    'w': (1.1, 1),
    'x': (.9, 1),
    'e': (1, 1.1),
    'c': (1, .9),
}

global coutrol_time


# def getKey():
#     tty.setraw(sys.stdin.fileno())
#     rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
#     if rlist:
#         key = sys.stdin.read(1)
#     else:
#         key = ''
#
#     termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
#     return key
def getKey():
    #coutrol_time = coutrol_time -1
    if os.path.exists('/home/admini/file.xml'):
        dom = xml.dom.minidom.parse('/home/admini/file.xml')
        root = dom.documentElement
        cc = dom.getElementsByTagName('rawtext')
        c1 = cc[0]
        #os.remove('/home/admini/file.xml')
        #print "aaaaaaa%s"%c1.firstChild.data.strip()

        if not c1.firstChild.data.strip()=='':
    		return c1.firstChild.data.strip("'")
    else:
        return ""


speed = .2
turn = 1


def vels(speed, turn):
    return "currently:\tspeed %s\tturn %s " % (speed, turn)


if __name__ == "__main__":
    settings = termios.tcgetattr(sys.stdin)

    rospy.init_node('turtlebot_teleop')
    pub = rospy.Publisher('~cmd_vel', Twist, queue_size=5)

    x = 0
    th = 0
    status = 0
    count = 0
    acc = 0.1
    target_speed = 0
    target_turn = 0
    control_speed = 0
    control_turn = 0
    coutrol_time = 0

    try:
        print msg
        print vels(speed, turn)
        while (1):
            key = getKey()
            time.sleep(0.2)
            print key
            print coutrol_time
            if key in moveBindings.keys():
                x = moveBindings[key][0]
                coutrol_time = coutrol_time + 1
                x = 1
                print "xxxxx%d"%x
                th = moveBindings[key][1]
                count = 0
            elif key in speedBindings.keys():
                speed = speed * speedBindings[key][0]
                turn = turn * speedBindings[key][1]
                count = 0

                print vels(speed, turn)
                if (status == 14):
                    print msg
                status = (status + 1) % 15
            elif key == ' ' or key == 'k':
                x = 0
                th = 0
                control_speed = 0
                control_turn = 0
            else:
                count = count + 1
                if count > 4:
                    x = 0
                    th = 0
                if (key == '\x03'):
                    break
            if coutrol_time > 0:
                target_speed = speed * x
                target_turn = turn * th
                print target_speed
                print control_speed
                if target_speed > control_speed:
                    if coutrol_time < 20:
                        target_speed = 0.2  ##control runspeed
                        control_speed = min(target_speed, control_speed)  ##control forward
                    else:
                        control_speed = min(target_speed, control_speed + 0.02)
                        os.remove('/home/admini/file.xml')
                        coutrol_time = 0
                    # control_speed = min(target_speed, control_speed + 0.02)
                elif target_speed <= control_speed:
                    print "CurTime__%s"%coutrol_time
                    if coutrol_time < 20:
                        target_speed = 0.2  ##control runspeed
                        control_speed = max(target_speed, control_speed)  ##control forward
                    else:
                        control_speed = max(target_speed, control_speed - 0.02)
                        os.remove('/home/admini/file.xml')
                        coutrol_time = 0

                else:
                    control_speed = target_speed

                if target_turn > control_turn:
                    control_turn = min(target_turn, control_turn + 0.1)
                elif target_turn < control_turn:
                    control_turn = max(target_turn, control_turn - 0.1)
                else:
                    control_turn = target_turn
            else:
                control_speed = 0
                control_turn = 0
                twist = Twist()
                twist.linear.x = 0;
                twist.linear.y = 0;
                twist.linear.z = 0
                twist.angular.x = 0;
                twist.angular.y = 0;
                twist.angular.z = 0
                pub.publish(twist)

            twist = Twist()
            twist.linear.x = control_speed;
            twist.linear.y = 0;
            twist.linear.z = 0
            twist.angular.x = 0;
            twist.angular.y = 0;
            twist.angular.z = control_turn
            pub.publish(twist)
            # print("loop: {0}".format(count))
            # print("target: vx: {0}, wz: {1}".format(target_speed, target_turn))
            # print("publihsed: vx: {0}, wz: {1}".format(twist.linear.x, twist.angular.z))

    except:
        print ""

    finally:
        twist = Twist()
        twist.linear.x = 0;
        twist.linear.y = 0;
        twist.linear.z = 0
        twist.angular.x = 0;
        twist.angular.y = 0;
        twist.angular.z = 0
        pub.publish(twist)


    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
