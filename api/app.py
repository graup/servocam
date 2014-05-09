#!/usr/bin/env python

import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from flask import Flask, jsonify, request
from controller.servo import Servo
import puka
app = Flask(__name__)

def update_position():
    promise = message_queue.basic_publish(exchange='', routing_key='servo',
                              body=str(servo.position))
    message_queue.wait(promise)
    print " [*] Message sent"

@app.route("/api")
def api():
    f = {"description": "The awesome API"}
    return jsonify(**f)

@app.route("/api/servo", methods=['GET', 'POST'])
def servo():
    response = {'version': '0.1'}
    if request.method == 'GET':
        response['description'] = 'Welcome to the awesome API'
    if request.method == 'POST':
        pos = int(request.form['position'])
        if pos:
            response['description'] = 'Servo position set to ' + str(pos)
            servo.position = pos
            update_position()

    response["position"] = servo.position
    return jsonify(**response)

if __name__ == "__main__":

    message_queue = puka.Client("amqp://localhost/")
    promise = message_queue.connect()
    print "Waiting for AMQP client to connect ..."
    message_queue.wait(promise)
    promise = message_queue.queue_declare(queue='servo')
    message_queue.wait(promise)

    servo = Servo()

    app.debug = True
    app.run()