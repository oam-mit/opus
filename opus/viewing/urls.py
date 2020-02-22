from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as user_views
from . import views

app_name="profiles"

urlpatterns=[
    path("<int:reg_number>/",views.index,name="index"),
    #searh for players
    path("search/",views.search,name="search"),

]