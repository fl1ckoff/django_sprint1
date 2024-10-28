from django.urls import path
from .views import *

app_name = 'pages'
urlpatterns = [
    path("about/", about, name='about'),
    path("rules/", rules, name='rules'),
]