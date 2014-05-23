servocam
========

This is work-in-progress. Looking at the code won't hurt, but running it is not recommended at this point.

What is this?
-------------

This is some code to remotely control a servo connected to a RaspberryPi. On the servo a webcam is mounted, whose image will also be displayed via a website served by Flask.

- **Flask API** <- RabbitMQ -> **Servo controller**
- **Flask frontend** <- HTTP -> **Flask API**

All running on the RaspberryPi at the moment. It might make sense to not run the controller on the same machine (the Raspberry Pi) as the API in the future.

Setup
-----

Unfortunately, some packages have to be installed globally at the moment as RPIO needs sudo to control the PWM, but running in sudo defeats virtualenv. So, install `puka` and `RPIO` via pip globally. Afterwards you can `pip install` the rest of the requirments in a virtualenv if you want to.

Also install rabbitmq-server. The packaged version works, so a `sudo apt-get update && sudo apt-get install rabbitmq-server` suffices.

How to run
----------

- Start rabbitmq-server
- Start the controller loop: `python controller/controller.py`
- Start the Flask app: `python api/app.py`

The API accepts POST request at /api/servo like

    curl raspberrypi:5000/api/servo -d position=100
    
Better documentation is coming up.