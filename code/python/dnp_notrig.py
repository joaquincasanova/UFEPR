import math
import sys
import numpy as np
import time
import synthesizer
import attenuator
import RPi.GPIO as GPIO

resolution=500000      

freq = float(sys.argv[1])
attn = float(sys.argv[2])

GPIO.setmode(GPIO.BOARD)
synthesizer.yig_set_freq(freq, resolution)
print " I just set the yig."
attenuator.digatt_set(attn)
print " I just set the attenuator."
print " Warming up."
time.sleep(10)
GPIO.cleanup()
quit()
        

      
