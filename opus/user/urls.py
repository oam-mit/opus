from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as user_views
from . import views
from .forms import CustomLoginView

from . import views

app_name="user"


urlpatterns=[
    path("",views.index,name="index"),
    path("sign-in/",CustomLoginView.as_view(template_name='user/login.html',redirect_authenticated_user=True),name="login"),
    path("sign-up/",views.signup,name="signup"),
    path("logout",user_views.LogoutView.as_view(template_name='user/index.html'),name="logout"),
    path("password-reset/",user_views.PasswordResetView.as_view(template_name="user/reset.html"),name="reset"),
    path("bot_reply",views.bot_reply,name="reply"),
    
]