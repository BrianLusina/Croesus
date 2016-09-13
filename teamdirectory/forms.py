from django import forms
from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', "last_name", 'email', 'title', 'linkedin', 'github', 'twitter', 'image',
                  'responsibilities', 'bio', 'birthday']

