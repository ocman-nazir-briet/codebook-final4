from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']
        labels = {'host' :'host', 'topic': 'topic', 'name':'name', 
        'description': 'description', 'participants': 'participants', 'files': 'Files', 'images':'Images', 'video':'Video'}

class userForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']