from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
class CustomerRegistrationForm(UserCreationForm):
    password1=forms.forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.forms.CharField(label=' Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email=forms.forms.CharField(label='Email',required=True,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}