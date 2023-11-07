# forms.py
from django import forms
from .models import UserProfile,Login

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields="__all__"
        widgets={

        }

class Loginform(forms.ModelForm):
    class Meta:
        model=Login
        fields="__all__"
        widgets={

        }