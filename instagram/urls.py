"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#apps
from instagram import views as local_views


# for static django files
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # local views
    path('admin/', admin.site.urls),
    path(r'', include('django.contrib.auth.urls')),
    path('test/', local_views.test, name='test'),



    # posts views
    path('', include('posts.urls', namespace='posts')),

    #user views
    path('users/', include('users.urls', namespace='users')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


