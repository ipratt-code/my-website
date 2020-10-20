from flask import Flask, render_template
app = Flask('app')

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/aboutme/')
def aboutme():
    return render_template('aboutme.html')

app.run(host='0.0.0.0', port=8080)