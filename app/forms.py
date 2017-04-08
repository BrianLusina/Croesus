from flask_wtf import FlaskForm



class ContactForm(FlaskForm):
    """
    Form will have name, company, email, project description
    """
    name = forms.CharField(label="Name", required=True)
    company = forms.CharField(label="Company", required=False)
    email = forms.EmailField(label="Email", widget=forms.EmailInput, required=True, validators=[validate_email])
    projectDesc = forms.CharField(label="Project Description", widget=forms.Textarea, required=True)
