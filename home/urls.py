from django.urls import path
from . import views

urlpatterns = [
    path('api/get-quiz/', views.get_quiz, name ='get_quiz'),
    path('',views.quiz, name='quiz')
]