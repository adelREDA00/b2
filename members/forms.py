from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from blogapp.models import Profile


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username" , "password1","password2"]

class ProfilePage(forms.ModelForm):
    class Meta:
        model = Profile
        fields=('bio',)