from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.messages),
    path('get/', views.get_message)
]