from .models import Profile, Reading
from django.forms import ModelForm
from django.forms.models import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class ProfileForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProfileInfoForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('date_of_birth', 'phone_number', 'location', 'designation')
        widgets = {
            'date_of_birth': DateInput()
        }


class ReadingForm(forms.ModelForm):

    class Meta:
        model = Reading
        fields = ('Date', 'major', 'front', 'rear_sill', 'vent', 'opening',  'remarks')
        widgets = {
            'Date': DateInput()

        }



