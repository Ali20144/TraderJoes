from flask import Flask, render_template, request
import sqlite3 as sql
import os
app = Flask(__name__)

import sqlite3
from flask import g

DATABASE = 'database.db'



#http://flask.pocoo.org/docs/0.10/patterns/sqlite3/
def get_db():
    def connect_to_database():
        db = sqlite3.connect(DATABASE)
        
        db.execute('create table if not exists testimonials (id integer primary key, fname text, lname text, email text, phone text, messagebox text)')
        
        return db
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = connect_to_database()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


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
    
    db = get_db()
    
    cursor = db.cursor()
    rows = cursor.execute('select fname,lname,messagebox from testimonials')
    
    return render_template('testimonials.html', rows=rows)

@app.route('/testimonial-submit')
def testimonialsubmit():
    
    fname = request.args.get('fname')
    lname = request.args.get('lname')
    email = request.args.get('email')
    phone = request.args.get('phone')
    messagebox = request.args.get('messagebox')
    
    db = get_db()
    
    cursor = db.cursor()
    
    cursor.execute('insert into testimonials (fname,lname,email,phone,messagebox) values (?,?,?,?,?)', [fname,lname,email,phone,messagebox])
    
    db.commit()
    
    return render_template('testimonials-submit.html')

@app.route('/contactus')
def contactus():
    return render_template('contactus.html')

   
if __name__ == '__main__':
    app.run(port=int(os.getenv('PORT', 8080)), host=os.getenv('IP','0.0.0.0'), debug=True)