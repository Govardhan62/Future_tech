from django.urls import path, include
from.views import about,index

urlpatterns = [
    path('about', about, name='about'),
    path('',index,name='index'),
]