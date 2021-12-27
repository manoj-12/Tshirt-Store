from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.forms import User


class CustometCreationForm(UserCreationForm):
    username = forms.EmailField(required=True , label="Email")
    first_name = forms.CharField(required=True , label='First Name')
    last_name = forms.CharField(required=True , label='Last Name')

    def clean_first_name(self):
        FirstName = self.cleaned_data.get('first_name')
        if len(FirstName.strip()) < 4:
            raise ValidationError('First Name must have 4 char long')
        return FirstName.strip()
    class Meta:
        model = User
        fields = ['username','first_name' , 'last_name']



class CustomerLoginForm(AuthenticationForm):

    username = forms.EmailField(required=True , label='Email')