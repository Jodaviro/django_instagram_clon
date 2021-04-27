"""Users Urls"""
from users import views
from django.urls import path
from .views import UserDetailView, ProfileUpdateView

app_name= 'users'
urlpatterns = [
path('login/', views.login_view, name= 'login'),
path('logout/', views.logout_view, name= 'logout'),
path('signup/', views.signup_view, name= 'signup'),
path('me/profile/', ProfileUpdateView.as_view(), name= 'update_profile'),
path('<str:username>/', UserDetailView.as_view() , name= 'detail'),

]