from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import *

class User(AbstractUser):
    genderChoice=(
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),
    )
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    gender = models.CharField(max_length=25, choices=genderChoice)
    dob = models.DateField(null=True)
    phone = models.CharField(max_length=15)
    address = models.TextField(max_length=125)
    bio = models.TextField(max_length=500)
    avatar = models.ImageField(upload_to='avatars', default='nopic.jpg')
    status = models.BooleanField(default=True)
    email_otp = models.CharField(max_length=12, default="000000")
    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    
    

    def __str__(self):
        return self.username

class Topic(models.Model):
    name = models.CharField(max_length=200)
    count = models.IntegerField(default=1)
    def __str__(self):
        return self.name[:20]
    class Meta:
        ordering=['name']

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=532)
    name = models.CharField(max_length=200)
    description = models.TextField()
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    files = models.FileField(upload_to="Room-files", blank=True)
    images = models.ImageField(upload_to="Room-images", blank=True)
    video = models.FileField(upload_to="Room-videos", blank=True, max_length=10000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        ordering=['-updated', '-created']

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=5000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body[0:30]

    class Meta:
        ordering=['-updated', '-created']