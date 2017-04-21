import RPi.GPIO as GPIO
import time
import curses


#added motor enable to pi
#pin 16 ->enable
#pin 18 ->enable
class NiksRobot:
	def __init__(self):
		#setup
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(7,GPIO.OUT)
		GPIO.setup(11,GPIO.OUT)
		GPIO.setup(13,GPIO.OUT)
		GPIO.setup(15,GPIO.OUT)

		#GPIO.setup(16,GPIO.OUT)
		#GPIO.setup(18,GPIO.OUT)
		#pwm0=GPIO.PWM(16,100)
		#pwm1=GPIO.PWM(18,100)
		print 'setup complete'
	def forward(self):#, dutyCycle):
		GPIO.output(7,True)
		GPIO.output(11,False)
		GPIO.output(15,True)
		GPIO.output(13,False)
		#pwm0.start(dutyCycle)
		#pwm1.start(dutyCycle)
		#GPIO.output(16,True)
                #GPIO.output(18,True)
	def backward(self):
		GPIO.output(7,False)
		GPIO.output(11,True)
		GPIO.output(15,False)
		GPIO.output(13,True)
        def right(self):
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(15,True)
                GPIO.output(13,False)
        def left(self):
                GPIO.output(7,True)
                GPIO.output(11,False)
                GPIO.output(15,False)
                GPIO.output(13,True)
        def stop(self):
                GPIO.output(7,False)
                GPIO.output(11,False)
                GPIO.output(15,False)
                GPIO.output(13,False)
               	#GPIO.output(16,False)
                #GPIO.output(18,False)
                #pwm0.stop()
                #pwm1.stop()
	def cleanup(self):
		GPIO.cleanup()
		#pwm0.stop()
		#pwm1.stop()

nr = NiksRobot()
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

try:
        while True:   
            char = screen.getch()
            if char == ord('q'):
                break
            elif char == curses.KEY_UP:
		nr.forward()
            elif char == curses.KEY_DOWN:
                nr.backward()
            elif char == curses.KEY_RIGHT:
                nr.right()
            elif char == curses.KEY_LEFT:
                nr.left()
            elif char == ord('p'):
                nr.stop()
             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    nr.cleanup()
    

