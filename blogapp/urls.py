from operator import imod
from django.urls import path
from .views import HomeView,ArticleDetailView,AddpostView,UpdatePostViwe,DeletePost,LikeView
from . import views

urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(),name='article-detail'),
    path('add_post', AddpostView.as_view(),name='add_post'),
    path('article/edit/<int:pk>', UpdatePostViwe.as_view(),name='update_post'),
    path('article/<int:pk>/delete',DeletePost.as_view(),name='delete_post'),
    path('like/<int:pk>',LikeView,name='like_post'),
]