from django import forms

class UserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'required' : 'true'}))
    email = forms.EmailField(required=False, widget=forms.EmailInput(attrs={'class' : 'form-control', 'required' : 'true'}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class' : 'form-control', 'required' : 'true'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class' : 'form-control', 'required' : 'true'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control', 'required' : 'true'}))

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Username', 'required' : 'true'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : 'Password', 'required' : 'true'}))