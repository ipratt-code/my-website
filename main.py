from flask import Flask, render_template
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

app.run(host='0.0.0.0', port=8080, debug=True)