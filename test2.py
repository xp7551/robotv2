import time
import pigpio

print 'start'
pi1 = pigpio.pi()       # pi1 accesses the local Pi's GPIO

pi1.write(4, 0) # set local Pi's GPIO 4 low
pi1.read(4)     # get level of dick's GPIO 4
print 'finish'
