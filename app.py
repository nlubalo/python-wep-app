from crypt import methods
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///myapp.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)


class Myapp(db.Model):
    c_id = db.Column(db.Integer, primary_key=True)
    c_name = db.Column(db.String(500))
    

@app.route('/')
def home():
    return 'Hi Nancy'


@app.route('/base')
def home1():
    my_list = Myapp.query.all()
    var="hello this is a variable"
    return render_template("base.html", var = var, my_list=my_list)

@app.route('/insert', methods=["POST","GET"])
def home2():
    c_name=request.form.get('c_name')
    new_c_name = Myapp(c_name=c_name)
    db.session.add(new_c_name)
    db.session.commit()
    return redirect(url_for("home1"))

@app.route('/delete/<int:c_id>')
def home3(c_id):
    c_name=Myapp.query.get_or_404(c_id)
    db.session.delete(c_name)
    db.session.commit()
    return redirect(url_for("home1"))

if __name__ == "__main__":
    app.run()
