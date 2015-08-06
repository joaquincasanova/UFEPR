import math
import sys
import numpy as np
import time
import synthesizer
import attenuator
import RPi.GPIO as GPIO

global attn
global dur

def attn_loop(channel):
    global attn
    print "Attenuation: ", attn
    if attn > 0:
        attenuator.digatt_set(attn)
        print " I just set the attenuator."
        print " Warming up."
        time.sleep(10)
        print " Running experiment..."
        time.sleep(dur)
        print " Experiment complete."
        attn=attn-delta
    else:
        print " All attenuation steps complete."

attn=32
trig=24
resolution=500000      

freq = float(sys.argv[1])
dur = float(sys.argv[2])
delta =  float(sys.argv[3])

GPIO.setmode(GPIO.BOARD)
GPIO.setup(trig, GPIO.IN)
GPIO.add_event_detect(trig, GPIO.RISING, callback=attn_loop)

synthesizer.yig_set_freq(freq, resolution)
print " I just set the yig."
print " Warming up."
time.sleep(10)

while attn>0:
    pass

attn=32
attenuator.digatt_set(attn)
GPIO.cleanup()
quit()
        

      
