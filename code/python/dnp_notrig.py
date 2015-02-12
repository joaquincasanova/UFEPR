import math
import sys
import numpy as np
import time
import synthesizer
import attenuator
import RPi.GPIO as GPIO


attn = float(sys.argv[1])
   
if len(sys.argv)>2:
    freq = float(sys.argv[2])
    resolution=500000      
    freq = freq*1e9
    
    try:
        attenuator.digatt_set(attn)
        print " I just set the digatt."
        time.sleep(1e-3)
        synthesizer.yig_set_freq(freq, resolution)
        print " I just set the yig."
    except KeyboardInterrupt:
        print "STOP"
    finally:
        GPIO.cleanup()
else:
    
    try:
        attenuator.digatt_set(attn)
        print " I just set the digatt."
        time.sleep(1e-3)
    except KeyboardInterrupt:
        print "STOP"
    finally:
        GPIO.cleanup()
        

      
