from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    photo = models.ImageField(default = 'default.jpg',upload_to='images/')
    bio = models.CharField(max_length=150)
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)   
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
class Image(models.Model):
    image = models.ImageField(default = 'default.jpg', upload_to='images/')
    name = models.CharField(max_length=60)
    caption = models.CharField(max_length=150)
    profile = models.ForeignKey(Profile) 
    likes = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.name
    @classmethod
    def get_images(cls):
        posts = cls.objects.all()
        return posts