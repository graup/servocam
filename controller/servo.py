#!/usr/bin/env python

from __future__ import division

import math

class Servo:
	position = 0

	def angle_to_time(self, angle):
		if angle > 180:
			angle = 180
		if angle < 0:
			angle = 0
		return 600 + 1800 * (angle/180)

	def update_position(self):
		from RPIO import PWM
		servo = PWM.Servo()
		time = int(self.angle_to_time(self.position))
		time = math.floor(time / 10) * 10
		print "Setting PWM to %d" % time 
		servo.set_servo(18, time)
