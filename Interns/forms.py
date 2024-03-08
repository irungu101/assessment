from Interns.models import Workers
from django import forms

class WorkersForm(forms.ModelForm):
    class Meta:
        model = Workers
        fields = ['firstname', 'lastname', 'phone_number', 'password']