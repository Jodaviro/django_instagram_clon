"""Users Urls"""
from users import views
from django.urls import path


app_name= 'users'
urlpatterns = [
path('login/', views.LoginView.as_view(), name= 'login'),
path('logout/', views.logout_view, name= 'logout'),
path('signup/', views.SignUpView.as_view(), name= 'signup'),
path('me/profile/', views.ProfileUpdateView.as_view(), name= 'update_profile'),
path('<str:username>/', views.UserDetailView.as_view() , name= 'detail'),
path('<str:username>/following/', views.FollowingView.as_view() , name= 'following'),
path('<int:profile>/<str:instruction>/followorunfollow/', views.follow_or_unfollow, name= 'followorunfollow'),

]