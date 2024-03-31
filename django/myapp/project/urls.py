from django.urls import path

from .views import *

urlpatterns = [
    
    path("",home),
    path("home/",home),
    path("addstd/",addstd),
    path("delete/<int:roll>/",delete),
    path("update/<int:roll>/",update),
    path("doupdate/<int:roll>",doupdate),
]