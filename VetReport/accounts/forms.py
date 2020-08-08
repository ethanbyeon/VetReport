from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ('date_of_case', 'role', 'clinician',
                    'veterinary_clinic', 'key_words', 'diagnosis', 'name_of_animal',
                    'signalment', 'complaint', 'description', 'summary',
                    'resources', 'files', 'pictures')