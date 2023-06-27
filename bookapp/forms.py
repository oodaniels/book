from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField,PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from flask_wtf.file import FileField, FileAllowed, FileRequired


class SignupForm(FlaskForm):
    fullname = StringField("Fullname",validators=[DataRequired(message="Your Full Name Is Required")])
    email = StringField("Email",validators=[Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password = PasswordField("Confirm Password", validators=[EqualTo('password',message="Confirm Password Must Be Equal To Pasword")])
    
    btn = SubmitField("Sign Up!")
 
  
class ContactForm(FlaskForm):
    fullname = StringField("Fullname",validators=[DataRequired(message="hello, you should supply all your names")])
    confirm_name = StringField("Confirm Fullname",validators=[DataRequired(message="Haba!"),EqualTo('fullname',message="Input Email Here")])
    email = StringField("Your Email",validators=[Email()])
    message = TextAreaField("Message", validators=[Length(1,3)])
    
    btn = SubmitField("Send Message")
    

class ProfileForm(FlaskForm):
    fullname = StringField('Fullname',validators=[DataRequired(message="Your Full Name Is Required")])
    pix = FileField('Display Picture',validators=[FileRequired(), FileAllowed(['jpg','jpeg','png'], 'Images Only!')])
    btn = SubmitField("Update Profile")
    
    
     
    

