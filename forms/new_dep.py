from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import SubmitField, StringField, IntegerField, EmailField


class NewDepartForm(FlaskForm):
    title = StringField('Department Title', validators=[DataRequired()])
    chief = IntegerField('Chief ID', validators=[DataRequired()])
    members = StringField('Members', validators=[DataRequired()])
    email = EmailField('Department Email', validators=[DataRequired()])
    submit = SubmitField('Submit')
