from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# URLConf
urlpatterns = [
    path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('classifier/', views.classification, name='classifier'),
    path('WordClouds/', views.cloud, name='WordClouds')
]
