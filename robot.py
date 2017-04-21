from gpiozero import Robot
from gpiozero import Motor
import time
import curses

robot = Robot(left=(22, 27), right=(4, 17))
            
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

try:
	while True:
		print 'loop'   
		char = screen.getch()
		if char == ord('q'):
			break
		elif char == curses.KEY_UP:
			robot.forward(.6)
		elif char == curses.KEY_DOWN:
			robot.backward(.6)
		elif char == curses.KEY_RIGHT:
			robot.right(.5)
			#time.sleep(.5)
		elif char == curses.KEY_LEFT:
			robot.left(.5)
			#time.sleep(.5)
            	elif char == ord('p'):
                	robot.stop()
		             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
   
    

