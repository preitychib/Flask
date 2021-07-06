from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hello.db'
db = SQLAlchemy(app)

class Item(db.Model):
	id = db.Column(db.Integer(),primary_key=True)
	name = db.Column(db.String(length=30),nullable=False,unique=True)
	price = db.Column(db.Integer(),nullable=False)
	barcode = db.Column(db.String(length=12),nullable=False,unique=True)
	description =db.Column(db.String(length=1024),nullable=False,unique=False)

def __repr__(self):
    	return f'Item{self.name}'

@app.route('/')
@app.route('/home')
def index ():
	return render_template('hello.html')
@app.route('/market')
def about_page ():
	items = Item
	return render_template('about.html', context=items)
