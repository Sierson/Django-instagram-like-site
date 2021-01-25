from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    full_name = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=200, blank=True)

    gender_choices = [
        ('M', "Male"),
        ('F', "Female"),
    ]

    gender = models.CharField(max_length=10, blank=True, choices=gender_choices)
    date_of_birth = models.DateField(blank=True, null=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)

    def __str__(self):
        return f"{self.user}"

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')

    def __str__(self):
        return f"{self.follower : self.following}"