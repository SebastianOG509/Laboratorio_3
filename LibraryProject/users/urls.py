from django.urls import path

from . import views

urlpatterns = [
    path('',views.Users, name="Users"),
]
##to implemen more views
