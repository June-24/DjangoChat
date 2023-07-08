from . import views # Add this line
from django.contrib import admin
from django.urls import path, include # Add include to the import statement

urlpatterns = [
    path('',views.index,name='index'),
    path('<slug:slug>/',views.chatroom,name='chatroom'),
]