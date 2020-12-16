from flask import Flask, render_template, send_from_directory
import os

def app():

	app = Flask('app')

	@app.route('/favicon.ico')
	def favicon():
		return send_from_directory(os.path.join(app.root_path, 'static'),'favicon/favicon.ico', mimetype='image/vnd.microsoft.icon')

	@app.route('/')
	def home():
		return render_template('index.html')

	@app.route('/aboutme')
	def aboutme():
		return render_template('aboutme.html')

	@app.route('/otherwebsites')
	def otherwebsites():
		return render_template('otherwebsites.html')

	@app.route('/github')
	def github():
		return render_template('github.html')

	@app.route('/howididthis')
	def howididthis():
		return render_template('howididthis.html')

	@app.route('/projects')
	def projects():
		return render_template('projects.html')

	@app.route('/projects/webdevchallenges')
	def webdevchallenges():
		return render_template('projects/webdevchallenges.html')

	@app.route('/projects/ltscifair2020')
	def ltscifair2020():
		return render_template('projects/ltscifair2020.html')

	@app.route('/projects/imagefilters')
	def imagefilters():
		return render_template('projects/imagefilters.html')

	return app