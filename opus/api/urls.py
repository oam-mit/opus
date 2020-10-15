from django.urls import path
from . import views

app_name="api"

urlpatterns=[
    path("get_rank/<int:registration_number>",views.get_rank,name="get_rank"),
]