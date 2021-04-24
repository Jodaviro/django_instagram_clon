"""Posts urls"""
from django.urls import path
from posts import views
from .views import PostsFeedView
from .views import PostDetailView

app_name = 'posts'
urlpatterns = [
# path('', views.list_posts, name='feed'),
path('new/', views.create_post, name='create_post'),
path('', PostsFeedView.as_view(), name='feed'),
path('post/<int:id>/', PostDetailView.as_view(), name='detail' )
]