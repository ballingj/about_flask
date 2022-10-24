# pip install flask-wtf
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    '''
    The first value/argument inside parenthesis is the label.  validators is one of the key advantages
    of using the WTForms in Flask. 
    '''
    usermode = SelectField('User Mode', choices=[('user', 'User'), ('adm', 'Admin'), ('maint', 'Maintenance')])
    username = StringField('Username', validators=[DataRequired()])  
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
