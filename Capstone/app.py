from flask import Flask, render_template, request, Response, redirect, url_for
import time
# import RPi.GPIO as GPIO

app = Flask(__name__, template_folder= "templates")


@app.route('/')
def hello_world():
    return render_template("login.html")
 
database1 = {'Jay': '123',
            'Arjun': 'xyz'}

database2 = {'Kerins': 'best', 'Edison': 'school'}

 
@app.route('/form_login', methods=['POST', 'GET'])
def login():
    name1 = request.form['username']
    pwd = request.form['password']
    if name1 in database1 and database1[name1] == pwd:
        return render_template('Doctor.html', name=name1)
    elif name1 in database2 and database2[name1] == pwd:
        return render_template('Patient.html', name=name1)
    else:
        return render_template('login.html', info='Invalid credentials')

@app.route('/logout')
def logout():
     return render_template("login.html")
     
@app.route('/newuser')
def newuser():
     return render_template("newuser.html")

@app.route('/', methods = ['GET', 'POST'])
def getTime():
	
	input_time = int(request.form['seconds'])
	
	print(input_time)
	# LED = 22

	# GPIO.setmode(GPIO.BOARD)
	# GPIO.setup(LED, GPIO.OUT)
	# GPIO.output(LED, GPIO.LOW)

	# #if let == "12":
	# GPIO.output(LED, GPIO.HIGH)
	# time.sleep(input_time)
	# GPIO.output(LED, GPIO.LOW)
	# GPIO.cleanup()

	return render_template('Doctor.html')
	


if __name__== '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5001)