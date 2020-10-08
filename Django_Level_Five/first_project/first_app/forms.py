from django import forms
from django.contrib.auth.models import User
from first_app.model import UserInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserInfoForm(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = ('portfolio','picture')
