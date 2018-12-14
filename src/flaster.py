from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm
from wtforms import Form
from wtforms import StringField,SubmitField,FileField
from wtforms.validators import DataRequired
import os
from judgeCore import judgeCpp
import random, string

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ACLARRR'
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

class formming(FlaskForm):
    idd=StringField("\nID: ",validators=[DataRequired(message="Can't be empty")])
    q=StringField("\nQuestion: ",validators=[DataRequired(message="Can't be empty")])
    file = FileField('\nCPP file',validators=[DataRequired(message="Can't be empty")])
    submit=SubmitField("送出")

@app.route("/")
def index():
    return "<h1>AC or WA ?</h1>"

@app.route('/submit',methods=['GET','POST'])
def submit():
    form=formming()
    if form.validate_on_submit():
        idd=form.idd.data
        q=form.q.data
        cppFile=form.file.data
        filename = secure_filename(idd+"_"+q+"_"+randomword(7)) 
        cppFile.save('./submitted/'+filename+".cpp")
        result=judgeCpp(q,filename)
        return 'Success Submit: '+filename+"<br>Result: "+result
    return render_template('form.html',form=form)

if __name__ == "__main__":
    app.run(debug=True)