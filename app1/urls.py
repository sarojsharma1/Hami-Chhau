from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.Home),
    path('blog', views.Blog),
    path('yog-guru', views.Yog_Guru),
    path('psychologist', views.Psychologist),
    path('psychiatrist', views.Psychiatrist),
    
    path('profile', views.Profile),
    path('signup', views.SignUp),
    path('login', views.Login),
    
]