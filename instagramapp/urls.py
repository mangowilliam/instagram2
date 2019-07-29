from django.conf.urls import url
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$',views.register,name='register'),
    url(r'instagram',views.instagram,name= 'index'),
    url(r'profile',views.profile,name= 'profile'),
    url(r'^search/', views.search_profile, name='search_profile'),
    url(r'^new/post$', views.new_post, name='new-post')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)