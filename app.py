from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return \
	'''
	<h1>Hello and welcome</h1>
	<p><a href="/HW"> HW today </a></p>
	<p><a href="/resources"> Resources </a></p>

	'''
@app.route('/HW')
def HW():
	return \
	'''
	<h1>K #<strong>04</strong>: Fill Up Yer Flask</h1>
	<h2>Due <strong>M 2017-09-25</strong>, 8:00am, EST.</h2>
	<p>Your job (solo):
	<br>
	Write a Flask app with 3 routes.
	<br>
	File this under 04_lemme_flask_u_sumpn in the workshop, with your local submodule name in this format: Last-First.</p>
	'''

@app.route('/resources')
def resources():
	return \
	'''
	<h1>Resources</h1>
	<p><a href="https://sites.google.com/a/stuycs.org/home/courses/software-development/resources"> >>><u>CLICK HERE</u><<<</a></p>

	'''

if __name__ == '__main__':
	app.debug = True
	app.run()
