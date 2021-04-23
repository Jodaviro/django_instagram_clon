"""Users Urls"""
from users import views
from django.urls import path
from .views import UserDetailView

app_name= 'users'
urlpatterns = [
path('login/', views.login_view, name= 'login'),
path('logout/', views.logout_view, name= 'logout'),
path('signup/', views.signup_view, name= 'signup'),
path('me/profile/', views.update_profile, name= 'update_profile'),
path('<str:username>/', UserDetailView.as_view() , name= 'detail'),

]