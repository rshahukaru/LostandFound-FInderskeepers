from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    phone = StringField('Phone Number (Optional)', validators=[Length(max=20)])
    submit = SubmitField('Register')


# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, DateField
from wtforms.validators import DataRequired

class LostItemForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    category = SelectField('Category', choices=[
        ('electronics', 'Electronics'),
        ('clothing', 'Clothing'),
        ('documents', 'Documents'),
        ('accessories', 'Accessories'),
        ('other', 'Other')
    ])
    description = TextAreaField('Description', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    date_lost = DateField('Date Lost', validators=[DataRequired()])

# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, DateField
from wtforms.validators import DataRequired

class LostItemForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    category = SelectField('Category', choices=[
        ('electronics', 'Electronics'),
        ('clothing', 'Clothing'),
        ('documents', 'Documents'),
        ('accessories', 'Accessories'),
        ('other', 'Other')
    ])
    description = TextAreaField('Description', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    date_lost = DateField('Date Lost', validators=[DataRequired()])

class FoundItemForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    category = SelectField('Category', choices=[
        ('electronics', 'Electronics'),
        ('clothing', 'Clothing'),
        ('documents', 'Documents'),
        ('accessories', 'Accessories'),
        ('other', 'Other')
    ])
    description = TextAreaField('Description', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    date_found = DateField('Date Found', validators=[DataRequired()])