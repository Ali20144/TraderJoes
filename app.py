from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('homepage.html')
    
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/traderjoes')
def traderjoes():
    return render_template('traderjoes.html')
    
@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')
    
@app.route('/usedcars')
def usedcars():
    return render_template('usedcars.html')
    
@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

   
if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0', debug=True)