from django.test import TestCase
from.models import Image,Profile

# Create your tests here.
class ProfileTestClass(TestCase):
         
     def setUp(self):
        self.mango = Profile(username='mango')

    def test_instance(self):
        self.assertTrue(isinstance(self.mango, Profile))

    def tearDown(self):
        Profile.objects.all().delete()
        
     def test_save(self):
        self.food.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete(self):
        self.mango.save()
        self.mango.delete()
        self.assertTrue(len(Profile.objects.all()) == 0)

    def test_update(self):
        self.mango.save()
        self.mango.username = 'william'
        self.assertTrue(self.mango.username == 'william')


class ImageTestClass(TestCase):
         
     def setUp(self):
        self.machakura = Image(name='machakura')

    def test_instance(self):
        self.assertTrue(isinstance(self.macakura, Image))

    def tearDown(self):
        Image.objects.all().delete()
        
     def test_save(self):
        self.machakura.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete(self):
        self.machakura.save()
        self.machakura.delete()
        self.assertTrue(len(Image.objects.all()) == 0)

    def test_update(self):
        self.mango.save()
        self.machakura.name = 'city'
        self.assertTrue(self.machakura.name == 'city')