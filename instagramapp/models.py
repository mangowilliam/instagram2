from django.db import models

# Create your models here.
class Profile(models.Model):
    photo = models.ImageField(upload_to='images/',)
    bio = models.CharField(max_length=150)
    
    
    def __str__(self):
        return self.bio
    
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=60)
    caption = models.CharField(max_length=150)
    profile = models.ForeignKey(Profile)
    likes = models.IntegerField()
    comments = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.name
    @classmethod
    def get_images(cls):
        posts = cls.objects.all()
        return posts