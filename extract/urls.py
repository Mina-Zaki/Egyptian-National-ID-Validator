from django.urls import path
from . import views

app_name="extract"
urlpatterns = [
    path('', views.index, name='index'),
    path("validition/",views.validition,name="validition"),
]