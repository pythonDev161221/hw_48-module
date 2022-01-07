from django.contrib import admin
from django.urls import path

from .views import index_view, detail_view

urlpatterns = [
    path('', index_view, name='index'),
    path('detail/<int:id>', detail_view, name='detail_view')
]
