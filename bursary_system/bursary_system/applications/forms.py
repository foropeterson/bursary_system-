# applications/forms.py
from django import forms
from .models import BursaryApplication  # Correct import of the model

class BursaryApplicationForm(forms.ModelForm):
    class Meta:
        model = BursaryApplication
        fields = [
            'first_name', 'last_name', 'email', 'phone_number',
            'address', 'date_of_birth', 'bursary_details', 'institution'  # Include institution
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth', 'type': 'date'}),
            'bursary_details': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Bursary Details'}),
            'institution': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Institution'})  # Add this line
        }
class InstitutionForm(forms.Form):
    institution = forms.CharField(label='Institution', max_length=100)