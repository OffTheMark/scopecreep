from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password"
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        try:
            user = User.objects.get(username=username)
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password.")
        except User.DoesNotExist:
            raise forms.ValidationError("Username does not exist.")


class SignupForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email address",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
            }
        )
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm password",
            }
        )
    )

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("A user with this username already exists.")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        if password != confirm_password:
            raise forms.ValidationError("Passwords don't match.")