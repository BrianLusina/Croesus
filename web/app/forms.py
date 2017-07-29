from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    """
    Form will have name, company, email, project description
    """
    name = StringField(label="Name", )
    company = StringField(label="Company")
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    projectDesc = TextAreaField(label="Project Description", validators=[DataRequired()])
