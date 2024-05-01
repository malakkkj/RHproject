from django.urls import path
from . import views
urlpatterns=[
    path('', views.index, name="RH"),
    path('addemploye', views.addemploye, name="addemploye"),



]