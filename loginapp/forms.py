from django import forms


class LoginForm(forms.Form):
    """THE LOGIN FORM"""
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, min_length=8,
    widget = forms.PasswordInput()
    )