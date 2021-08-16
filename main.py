from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pickle
from norm import *

pipe = pickle.load(open("pipe.pkl","rb"))
main = Flask(__name__)
main.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///proiect.db'
main.config['SQLALCHEMY TRACK_Modifications'] = False
db = SQLAlchemy(main)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title =  db.Column(db.String(100), nullable=False)
    intro =  db.Column(db.String(300), nullable=False)
    text =  db.Column(db.Text, nullable=False)
    date =  db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Note %r>' % self.id

@main.route('/about')
def about():
    return render_template("about.html")

@main.route('/', methods=['POST', 'GET'])
def create_note():
    if request.method == "POST":
        text = request.form['text']
        nota = pipe.predict([text])[0]
        if nota>1:
            nota = 1
        return redirect(url_for("create_note",nota=int (nota*10)))
    else:
        return render_template("index.html")

if __name__=="__main__":
    main.run(debug=True)
