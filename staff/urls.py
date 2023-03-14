from django.urls import path
from staff.views import inicio 

urlpatterns = [
    path('', inicio),
]
