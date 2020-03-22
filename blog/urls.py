from django.urls import path
from .views import *

urlpatterns = [
    path("", hello, name="hello"),
    path('post/<int:pk>/', post_detail, name='post_detail'),
]
