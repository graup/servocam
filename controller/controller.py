#!/usr/bin/env python

import sys
sys.path.append("..")

import puka
from servo import Servo

client = puka.Client("amqp://raspberrypi/")
promise = client.connect()
client.wait(promise)

promise = client.queue_declare(queue='servo')
client.wait(promise)

print "  [*] Waiting for messages. Press CTRL+C to quit."

servo = Servo()

while True:

	consume_promise = client.basic_consume(queue='servo')
	result = client.wait(consume_promise)
	print "  [x] Received message %r" % (result,)

	servo.position = int(result.get('body', ''))
	try:
		servo.update_position()
	except Exception, e:
		print "Couldn't update position. %s" % e

	client.basic_ack(result)

	promise = client.basic_cancel(consume_promise)
	client.wait(promise)

promise = client.close()
client.wait(promise)
