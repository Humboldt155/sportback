from allauth.account.forms import SignupForm
from django import forms

from django.contrib.auth import get_user_model
User = get_user_model()


class CustomSignupForm(SignupForm):
    name = forms.CharField(max_length=250, label='Name')
    refused_newsletters = forms.BooleanField(label='Refused_newsletters')

    def signup(self, request, user):

        user.name = self.cleaned_data['name']
        user.refused_newsletters = self.cleaned_data['refused_newsletters']

        user.save()
        return user
