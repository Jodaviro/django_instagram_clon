"""Posts urls"""
from django.urls import path
from posts import views


app_name = 'posts'
urlpatterns = [
path('', views.PostsFeedView.as_view(), name='feed'),
path('post/<int:pk>/', views.PostDetailView.as_view(), name='detail' ),
path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='update' ),
path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete' ),
path('post/create/', views.CreatePostView.as_view(), name='create_post' ),
]