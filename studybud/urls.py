"""studybud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from base import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('home/', views.index, name='home'),
    path('create-room/', views.createRoom, name='create-room'),
    path('user-profile/<str:pk>', views.userProfile, name='user-profile'),
    path('update_user/', views.updateUser, name="update-user"),
    path('detail/<str:pk>/', views.detail, name='detail'),
    path('update-room/<str:pk>/', views.updateRoom, name='update-room'),
    path('delete-room/<str:pk>/', views.deleteRoom, name='delete-room'),
    path('delete-message/<str:pk>/', views.deleteMessage, name='delete-message'),
    path('login/', views.loginUser, name='login'),
    path('register/', views.registerUser, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('api/', include('api.urls'))
]
urlpatterns+= static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

