from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    if not (phone.isdigit() and len(phone) == 10):
        return render_template('index.html', message="Phone number must be 10 digits")
    user = User(name=name, email=email, phone=phone)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))