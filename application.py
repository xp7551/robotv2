from flask import Flask, render_template, request, Response
from gpiozero import Robot
from gpiozero import Motor
from functools import wraps
app = Flask(__name__)

#robot = Robot(left=(22, 27), right=(4, 17))
#robot.forward
#robot.backward
#robot.left
#robot.right

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/robot_left', methods=['POST'])
def robot_left():
    print 'robot_left'
    #robot.left
    return 'L'

@app.route('/robot_right', methods=['POST'])
def robot_right():
    print 'robot_right'
    return 'R'

@app.route('/robot_forward', methods=['POST'])
def robot_forward():
    print 'robot_forward'
    return 'F'

@app.route('/robot_backward', methods=['POST'])
def robot_backward():
    print 'robot_backward'
    return 'B'
#request.args.get('username')

#
#
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
#
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
