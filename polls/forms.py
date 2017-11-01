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
