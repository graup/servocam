#!/usr/bin/env python

from __future__ import division

class Servo:
	position = 0

	def angle_to_time(self, angle):D
		if angle > 180:
			angle = 180
		if angle < 0:
			angle = 0
		return 600 + 1800 * (angle/180)

	def update_position(self):
		# only import RPIO here because it might not be
		# installable on the platform the API is tested on
		from RPIO import PWM

		servo = PWM.Servo()
		time = self.angle_to_time(self.position)
		print "Setting PWM to %d..." % time 
		servo.set_servo(18, time)
