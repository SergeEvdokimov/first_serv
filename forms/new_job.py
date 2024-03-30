from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, IntegerField, BooleanField, SubmitField


class NewJobForm(FlaskForm):
    job = StringField('Job (name)', validators=[DataRequired()])
    team_leader = IntegerField('Team leader id', validators=[DataRequired()])
    work_size = IntegerField('Work size', validators=[DataRequired()])
    collaborators = StringField('Collaborators', validators=[DataRequired()])
    is_finished = BooleanField('If job is finished?')
    category = IntegerField('Job Category', default=1)
    submit = SubmitField('Submit')
