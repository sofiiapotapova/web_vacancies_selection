from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control'}))
    city = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'city'
        )


class UserSignForm(ModelForm):
    class Meta:
        pass