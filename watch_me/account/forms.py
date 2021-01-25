from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import UserProfile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': "E-mail", 'style': 'margin-top:20px;'}))
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': "Username", 'style': 'margin-top:20px;'}))
    password1 = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={'placeholder': "Password", 'style': 'margin-top:20px;'}))
    password2 = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={'placeholder': "Confirm password", 'style': 'margin-top:20px;'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder': "Username", 'style': 'margin-top:20px;'}))
    password = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={'placeholder': "Password", 'style': 'margin-top:20px;'}))

    class Meta:
        model = User
        fields = '__all__'

class UserDetailsForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), required=False)
    class Meta:
        model = UserProfile
        exclude = ('user',)