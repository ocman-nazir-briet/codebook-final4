from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']
        labels = {'host' :'host', 'topic': 'Topic', 'name':'Name', 
        'description': 'Description', 'participants': 'Participants', 'files': 'Files', 'images':'Images', 'video':'Video'}

class userForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'password1', 'password2']
        
class updateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'gender', 'dob', 'bio', 'phone', 'address']
