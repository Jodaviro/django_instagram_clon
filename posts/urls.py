"""Posts urls"""
from django.urls import path
from posts import views


app_name = 'posts'
urlpatterns = [
path('', views.PostsFeedView.as_view(), name='feed'),
path('post/<int:pk>/', views.PostDetailView.as_view(), name='detail' ),
path('post/create/', views.CreatePostView.as_view(), name='create_post' ),
]