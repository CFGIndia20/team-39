from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField, TextAreaField, IntegerField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
# from flaskblog.models import User
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class AddQuestionForm(FlaskForm):
    id = IntegerField('ID', validators=[DataRequired()])
    question = TextAreaField('Question', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    submit = SubmitField('Add Question')
