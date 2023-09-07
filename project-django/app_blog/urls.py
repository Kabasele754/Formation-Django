from django.urls import path
#from app_blog.views import indexView
from .views import indexView, contactView, aboutView

urlpatterns = [
    path('', indexView, name='index'),
    path('contact/', contactView, name="contact"),
    path('about/', aboutView, name='about')
]