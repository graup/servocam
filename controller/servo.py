#!/usr/bin/env python

from __future__ import division

import math

class Servo:
	position = 0

	def angle_to_time(self, angle):
		return 20000 * (angle/360)

	def update_position(self):
		from RPIO import PWM
		servo = PWM.Servo()
		time = int(self.angle_to_time(self.position))
		time = math.floor(time / 10) * 10
		print "Setting PWM to %d" % time 
		servo.set_servo(18, time)
