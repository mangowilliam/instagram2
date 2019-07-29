from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    class Meta:
        db_table = 'profile'
    photo = models.ImageField(default = 'default.jpg',upload_to='images/')
    bio = models.CharField(max_length=150)
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True, related_name='profile')   
    
    def __str__(self):
        return self.user.username
  
        
    def save_profile(self):
        self.save()

    @classmethod
    def delete_profile(self):
       self.delete()

    @classmethod
    def update_profile(id):
       Profile.objects.filter(id = id).update()
    
    @classmethod
    def search_profile(cls, items):
        posts = cls.objects.filter(user__username__icontains=items)
        return posts
    
class Image(models.Model):
    image = models.ImageField(default = 'default.jpg', upload_to='images/')
    name = models.CharField(max_length=60)
    caption = models.CharField(max_length=150)
    profile = models.ForeignKey(User, on_delete=models.CASCADE) 
    likes = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.name
    def save_image(self):
        self.save()

    @classmethod
    def delete_image(self):
        self.delete()

    @classmethod
    def update_caption(cls,caption):
       cls.objects.filter(caption).update()
    
    @classmethod
    def get_images(cls):
        posts = cls.objects.all()
        return posts
    
   