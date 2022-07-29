from logging import PlaceHolder
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form  

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=250) 
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='FIRST NAME', max_length=150, widget=forms.TextInput(attrs={'placeholder':'Enter your First Name'}))
    last_name = forms.CharField(label='LAST NAME', max_length=150, widget=forms.TextInput(attrs={'placeholder':'Enter your LAST NAME'}))
    # mobilenub = forms.CharField(label='MOBILE NUMBER',min_length=5, max_length=15, widget=forms.TextInput(attrs={'placeholder':'Enter your MOBILE NUMBER'}))
    username = forms.CharField(label='USERNAME', min_length=5, max_length=150,  widget=forms.TextInput(attrs={'placeholder':'Enter your Username'}))  
    email = forms.EmailField(label='EMAIL ADDRESS', max_length=250, widget= forms.EmailInput
                           (attrs={'placeholder':'Enter your valid email'}))  
    password1 = forms.CharField(label='PASSWORD', widget=forms.PasswordInput(attrs={'placeholder':'Enter your password'}))  
    password2 = forms.CharField(label='CONFIRM PASSWORD', widget=forms.PasswordInput(attrs={'placeholder':'Confirm your password'}))  
  
    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']

        return last_name
    
    # def clean_mobilenub(self):
    #     mobilenub = self.cleaned_data['mobilenub']

    #     return mobilenub
  
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError("Email Already Exist")  
        return email  
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2  
  
    def save(self, commit = True):  
        user = User.objects.create_user(
        self.cleaned_data['username'],
        first_name=self.cleaned_data['first_name'],
        last_name=self.cleaned_data['last_name'],
        email=self.cleaned_data['email'],
        password=self.cleaned_data['password1']
        # mobilenub = self.cleaned_data['mobilenub']
        )
            # self.cleaned_data['mobilenub']
         
        return user  

        