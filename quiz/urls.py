from quiz.views import *
from django.urls import path, include

app_name = 'quiz'
urlpatterns = [
    path('',test_view,name='index')
]