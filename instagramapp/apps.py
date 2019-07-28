from django.apps import AppConfig


class InstagramappConfig(AppConfig):
    name = 'instagramapp'

    
    
    
    def read(self):
        import users.signals