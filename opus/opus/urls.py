"""opus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from django.contrib import admin

from django.contrib.auth.models import User

admin.site.site_header = "Hopeless Opus Admin"
admin.site.site_title = "Hopeless Opus Admin Portal"
admin.site.index_title = "Hopeless Opus Portal"

from . import settings

from django.conf.urls.static import static

from django.contrib.auth import views as user_views

urlpatterns = [
    #Admin
    path('admin/', admin.site.urls),

    #Index
    path("",include("user.urls")),

    #Game
    path("game/",include("game.urls")),

    #Password-ResetS
    path("password-reset/confirm/<uidb64>/<token>/",user_views.PasswordResetConfirmView.as_view(template_name="user/reset_confirm.html"),name="password_reset_confirm"),
    path("password-reset/sent/",user_views.PasswordResetDoneView.as_view(template_name="user/reset_sent.html"),name="password_reset_done"),
    path("password-reset/complete/",user_views.PasswordResetCompleteView.as_view(template_name="user/reset_complete.html"),
        name="password_reset_complete"),

    #Profiles

    path("profile/",include("viewing.urls")),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)