from flask import Flask, render_template
import gunicorn

def app():

    app = Flask('app')

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
    
    return app