from flask import Flask, render_template, request, Response
from gpiozero import Robot
from gpiozero import Motor
from functools import wraps
from time import sleep
from mpu6050 import mpu6050

app = Flask(__name__)
app.run(debug=True)

robot = Robot(left=(22, 27), right=(4, 17))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/robot_left', methods=['POST'])
def robot_left():
    print 'robot_left'
    robot.left(.5)
    sleep(.2)
    robot.stop()
    return 'L'

@app.route('/robot_right', methods=['POST'])
def robot_right():
    print 'robot_right'
    robot.right(.5)
    sleep(.2)
    robot.stop()
    return 'R'

@app.route('/robot_forward', methods=['POST'])
def robot_forward():
    print 'robot_forward'
    #check_course
    #robot.forward(.6)
    #sleep(.5)
    #robot.stop()  	
    #return 'F'

@app.route('/robot_backward', methods=['POST'])
def robot_backward():
    print 'robot_backward'
    robot.backward(.6)
    sleep(.5)
    robot.stop()
    return 'B'


#request.args.get('username')
#def check_auth(username, password):
#    """This function is called to check if a username /
#    password combination is valid.
#    """
#    return username == 'admin' and password == 'secret'
#def authenticate():
#    """Sends a 401 response that enables basic auth"""
#    return Response(
#    'Could not verify your access level for that URL.\n'
#    'You have to login with proper credentials', 401,
#    {'WWW-Authenticate': 'Basic realm="Login Required"'})
#def requires_auth(f):
#    @wraps(f)
#    def decorated(*args, **kwargs):
#        auth = request.authorization
#        if not auth or not check_auth(auth.username, auth.password):
#            return authenticate()
#        return f(*args, **kwargs)
#    return decorated
#@app.route('/secret-page')
#@requires_auth
#def secret_page():
#    return render_template('secret_page.html')

@app.route('/robot_controller')
#@requires_auth
def robot_controller():
    return render_template('robot_controller.html')

def course_correct():
    robot.forward(.6)
    sleep(.2)
    veer = check_veer()
    if veer == -1
        robot.left(.5)
        sleep(.15)
    elsif veer == 1
        robot.right(.5)
        sleep(.15) 
    end
    robot.forward(.6)
    sleep(.2)
    robot.stop()
    return 'F'
    
def gyro_orientation():
        sensor = mpu6050(0x68)
        gyro_data = sensor.get_gyro_data()
        return gyro_data
def check_x_rotation():
        gyro_data = gyro_orientation()
        return gyro_data['x']
def check_veer():
    x_rot = check_x_rotation()
    if x_rot < 5 && x_rot > -5
        return 0
    elsif x_rot > 5
        return 1
    elsif x_rot < -5
        return -1
    end
