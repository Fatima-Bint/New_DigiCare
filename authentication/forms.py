from django import forms
from django.contrib.auth import authenticate, get_user_model


User = get_user_model()


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(strip=False)


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email", "password", "first_name")

    def save(self):
        data = self.cleaned_data 
        return User.objects.create_user(**data)
