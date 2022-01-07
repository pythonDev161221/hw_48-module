from django.contrib import admin
from django.urls import path

from .views import index_view, detail_view, create_view, update_view

urlpatterns = [
    path('', index_view, name='index'),
    path('detail/<int:id>', detail_view, name='detail_view'),
    path('create/', create_view, name='create_view'),
    path('update/<int:id>', update_view, name='update_view'),
]
