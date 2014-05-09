#!/usr/bin/env python

class Servo:
	position = 0

	def angle_to_time(self, angle):
		return 20000 * (angle/360)

	def update_position(self):
		from RPIO import PWM
		servo = PWM.Servo()
		servo.set_servo(18, angle_to_time(self.position) )