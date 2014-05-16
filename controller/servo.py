#!/usr/bin/env python

from __future__ import division

class Servo:
	position = 0

	def angle_to_time(self, angle):
		""" Returns pulse width in us """
		time = 20000 * (angle/360)
		time = int(time/10) * 10 # Precision of PWM is only 10us
		return time

	def update_position(self):
		# only import RPIO here because it might not be
		# installable on the platform the API is tested on
		from RPIO import PWM

		servo = PWM.Servo()
		time = self.angle_to_time(self.position)
		print "Setting PWM to %d..." % time 
		servo.set_servo(18, time)
