from gpiozero import Robot
from gpiozero import Motor
from time import sleep

print 'start'
robot = Robot(left=(22, 27), right=(4, 17))
sleep(.5)
robot.backward(.5)
sleep(.5)
#for i in range(4):
#    robot.forward(.5)
#    sleep(1)
#    robot.right(.5)
#    sleep(.3)


#motor = Motor(forward=4, backward=17)

#while True:
#    motor.forward()
#    sleep(5)
#    motor.backward()
#    sleep(5)


print 'end'
