from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import ShopUser

class ShopUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)

    class Meta:
        model = ShopUser
        fields = ('username', 'email', 'phone', 'password1', 'password2')

class ShopUserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин или Email')