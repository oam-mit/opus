from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name="game"

urlpatterns=[
    path("",views.index,name="index"),
    path("check/<int:option>/",views.check_story,name="check_story"),
    path("aptitude",views.aptitude,name="aptitude"),
    path("check_aptitude",views.check_aptitude,name="check_aptitude"),
    path("end/day<int:day>/",views.day_ending,name="day_ending"),
    path('profile/',views.profile,name="profile"),
    path("end/",views.game_end,name="game_end"),

    #Checking for staff
    path("check_staff/",views.check_staff,name="check_staff"),

    
]