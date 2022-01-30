from operator import imod
from django.urls import path
from . import views
from .views import ShowProfilePageView , CreatProfilePage

urlpatterns = [
  path('register/',views.creatuser,name='register'),
  path('<int:pk>/profile',ShowProfilePageView.as_view(),name='show_profile_viwe'),
  path('CreatProfilePage/',CreatProfilePage.as_view(),name='CreatProfilePage'),
]