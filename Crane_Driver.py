#!/usr/bin/env python3

import RPi.GPIO as gpio
import time
import sys


try:
  direction=sys.argv[1]
  steps = int(float(sys.argv[2]))
except:
  steps = 0

print("You told me to turn %s %s steps.") % (direction, steps)

delay = 0.0055
StepCounter = 0

gpio.setup(1, gpio.OUT)
gpio.setup(2, gpio.OUT)

if direction == 'left':
  gpio.output(2, True)
elif direction == 'right':
  gpio.output(2, False)

while StepCounter < steps:
  gpio.output(1, True)
  gpio.output(1, False)
  StepCounter += 1
  time.sleep(delay)

  gpio.cleanup()
