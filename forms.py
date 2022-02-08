#this is the flask's form module where the customers can fill out a form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddTaskForm(FlaskForm):
    title = StringField('Tell the coon something you want her to know', validators = [DataRequired()])
    submit = SubmitField("Post")
