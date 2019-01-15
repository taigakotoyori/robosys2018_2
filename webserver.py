#!/usr/bin/env python
# _*_ coding: utf-8 _*_
import rospy , os
import SimpleHTTPServer

def kill():
 os.system("kill -KILL " + str(os.getpid()))

os.chdir(os.path.dirname(__file__))
rospy.init_node("webserver")
rospy.on_shutdown(kill)
SimpleHTTPServer.test()
