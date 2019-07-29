from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db import models

# Create your models here.
class Profile(models.Model):
    photo = models.ImageField(default = 'default.jpg',upload_to='images/')
    bio = models.CharField(max_length=150)
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)   
    
    def __str__(self):
        return f'{self.user.username} Profile'
  
        
    def save_profile(self):
        self.save()

    @classmethod
    def delete_profile(id):
       Profile.objects.filter(id=id).delete()

    @classmethod
    def update_profile(id):
       Profile.objects.filter(id = id).update()
    
class Image(models.Model):
    image = models.ImageField(default = 'default.jpg', upload_to='images/')
    name = models.CharField(max_length=60)
    caption = models.CharField(max_length=150)
    profile = models.ForeignKey(Profile) 
    likes = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.name
    def save_image(self):
        self.save()

    @classmethod
    def delete_image(id):
        self.delete()

    @classmethod
    def update_caption(cls,caption):
       cls.objects.filter(caption).update()
    
    @classmethod
    def get_images(cls):
        posts = cls.objects.all()
        return posts
    
    @classmethod
    def search_posts(cls, items):
        posts = cls.objects.filter(category__name__icontains=items)
        return posts